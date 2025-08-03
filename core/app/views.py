from rest_framework import viewsets
from .models import Partners, FAQ, News, Review,Application
from .serializers import PartnersSerializer, FAQSerializer, NewsSerializer, ReviewSerializer, ApplicationSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view


@extend_schema_view(
    list=extend_schema(summary="Получить список партнеров"),
    retrieve=extend_schema(summary="Получить одного партнера"),
    create=extend_schema(summary="Создать партнера"),
    update=extend_schema(summary="Обновить партнера"),
    partial_update=extend_schema(summary="Частично обновить партнера"),
    destroy=extend_schema(summary="Удалить партнера"),
)
class PartnersViewSet(viewsets.ModelViewSet):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer


@extend_schema_view(
    list=extend_schema(summary="Получить список FAQ"),
    retrieve=extend_schema(summary="Получить один FAQ"),
    create=extend_schema(summary="Создать FAQ"),
    update=extend_schema(summary="Обновить FAQ"),
    partial_update=extend_schema(summary="Частично обновить FAQ"),
    destroy=extend_schema(summary="Удалить FAQ"),
)
class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


@extend_schema_view(
    list=extend_schema(summary="Получить список новостей"),
    retrieve=extend_schema(summary="Получить одну новость"),
    create=extend_schema(summary="Создать новость"),
    update=extend_schema(summary="Обновить новость"),
    partial_update=extend_schema(summary="Частично обновить новость"),
    destroy=extend_schema(summary="Удалить новость"),
)
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


@extend_schema_view(
    list=extend_schema(summary="Получить все отзывы"),
    retrieve=extend_schema(summary="Получить один отзыв"),
    create=extend_schema(summary="Оставить отзыв"),
    update=extend_schema(summary="Обновить отзыв"),
    partial_update=extend_schema(summary="Частично обновить отзыв"),
    destroy=extend_schema(summary="Удалить отзыв"),
)
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

@extend_schema_view(
    list=extend_schema(summary="Получить список Application"),
    retrieve=extend_schema(summary="Получить один Application"),
    create=extend_schema(summary="Создать Application"),
    update=extend_schema(summary="Обновить Application"),
    partial_update=extend_schema(summary="Частично обновить Application"),
    destroy=extend_schema(summary="Удалить Application"),
)
class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = FAQSerializer