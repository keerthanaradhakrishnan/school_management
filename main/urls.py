from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, LibraryHistoryViewSet, FeesHistoryViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')
router.register(r'library', LibraryHistoryViewSet, basename='library')
router.register(r'fees', FeesHistoryViewSet, basename='fees')

urlpatterns = router.urls

