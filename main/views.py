from rest_framework import viewsets, permissions
from .models import Student, LibraryHistory, FeesHistory
from .serializers import StudentSerializer, LibraryHistorySerializer, FeesHistorySerializer

# Permissions for Admin, Office Staff, and Librarians
class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser

class IsOfficeStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_office_staff

class IsLibrarian(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_librarian

# Admin, Office Staff, and Librarian views
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdmin | IsOfficeStaff]  # Admin and Office Staff

class LibraryHistoryViewSet(viewsets.ModelViewSet):
    queryset = LibraryHistory.objects.all()
    serializer_class = LibraryHistorySerializer
    permission_classes = [IsOfficeStaff | IsLibrarian]  # Office Staff and Librarians

class FeesHistoryViewSet(viewsets.ModelViewSet):
    queryset = FeesHistory.objects.all()
    serializer_class = FeesHistorySerializer
    permission_classes = [IsOfficeStaff]  # Only Office Staff
