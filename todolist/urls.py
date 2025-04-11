from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet, SecureHelloView

router = DefaultRouter()
router.register(r'todos', TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('secure-hello/', SecureHelloView.as_view()),  # Protected route
]
