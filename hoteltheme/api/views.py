from rest_framework import viewsets, permissions
# from rest_framework import  DjangoObjectPermissions
from listings.models import Listing
from realtors.models import Realtor
from .serializers import ListingSerializer
from .serializers import RealtorSerializer


class ListingView(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

    # permission_classes = (permissions.IsAuthenticated, permissions.DjangoModelPermissions,)
    # permission_classes = (permissions.IsAdminUser,)


# class DjangoObjectPermissionsOrAnonReadOnly(DjangoObjectPermissions):
#     authenticated_users_only = False


class RealtorView(viewsets.ModelViewSet):
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer
