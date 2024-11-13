from rest_framework.permissions import BasePermission
from rest_framework import permissions
from .models import InvestorProfile
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import InvestorsProfileSerializer


class InvestorProfile(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk, format=None):
        obj = InvestorProfile.objects.get(pk=pk)
        # Check object-level permission using the custom permission
        self.check_object_permissions(request, obj)
        # Continue with your view logic
        serializer = InvestorsProfileSerializer(obj)
        return Response(serializer.data)
    