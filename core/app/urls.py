from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PartnersViewSet, FAQViewSet, NewsViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'partners', PartnersViewSet)
router.register(r'faqs', FAQViewSet)
router.register(r'news', NewsViewSet)
router.register(r'feedbacks', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]