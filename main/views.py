from rest_framework import viewsets, permissions
from .models import Student, LibraryHistory, FeesHistory
from .serializers import StudentSerializer, LibraryHistorySerializer, FeesHistorySerializer

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'

class IsOfficeStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['admin', 'office']

class IsLibrarian(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['admin', 'librarian']

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOfficeStaff]

class LibraryHistoryViewSet(viewsets.ModelViewSet):
    queryset = LibraryHistory.objects.all()
    serializer_class = LibraryHistorySerializer
    permission_classes = [permissions.IsAuthenticated, IsLibrarian]

class FeesHistoryViewSet(viewsets.ModelViewSet):
    queryset = FeesHistory.objects.all()
    serializer_class = FeesHistorySerializer
    permission_classes = [permissions.IsAuthenticated, IsOfficeStaff]
