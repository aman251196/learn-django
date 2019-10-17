import logging

from django.shortcuts import render
from django.utils.translation import gettext as _
from rest_framework import status, viewsets, filters
from rest_framework.response import Response

from .models import Product
from .serializers import ProductListSerializer, ProductCreateSerializer

logger = logging.getLogger(__name__)
# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    model = Product
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    create_serializer_class = ProductCreateSerializer

    def create(self, request):
        try:
            request_data = request.data.copy()
            serializer = self.create_serializer_class(data = request_data)
            if serializer.is_valid():
                obj = serializer.save()
                context = {"success" : True, "message": _("Product created successfully."), "data": self.serializer_class(obj).data}
                logger.info("{} added successfully to product list".format(obj.title))
                return Response(context, status=status.HTTP_200_OK)
            else:
                context = {"success" : False, "message": _("Failed to create Product."), "error":serializer.errors}
                logger.error("Failed to add to product list due to {}".format(serializer.errors))
                return Response(context, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            context = {"success" : False, "message": _("Failed to create Product."), "error":str(error)}
            logger.exception("Failed to add {} to product list")
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def list(self, request):
        try:
            obj = self.get_queryset()
            serializer = self.serializer_class(obj, many=True)
            context = {"success" : True, "message": _("List of Products returned successfully."), "data": serializer.data}
            return Response(context, status=status.HTTP_200_OK)
        except Exception as error:
            context = {"success" : False, "message": _("Failed to get list of Products."), "error":str(error)}
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def retrieve(self, request, pk=None):
        try:
            try:
                obj = self.get_object()
            except Exception as error:
                context = {"success" : False, "message": _("ID not found."), "error": str(error)}
                return Response(context, status=status.HTTP_200_OK)
            serializer = self.serializer_class(data=obj)
            context = {"success" : True, "message": _("Product details returned successfully."), "data": serializer.data}
            return Response(context, status=status.HTTP_200_OK)
        except Exception as error:
            context = {"success" : False, "message": _("Failed to retrieve Product."), "error":str(error)}
            return Response(context, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
