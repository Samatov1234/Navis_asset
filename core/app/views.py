from rest_framework import generics
from .models import Partners, FAQ, News, Review
from .serializers import PartnersSerializer, FAQSerializer, NewsSerializer, ReviewSerializer

class PartnersList(generics.ListAPIView):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer

class PartnersDetail(generics.RetrieveAPIView):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializer


class FAQList(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

class FAQDetail(generics.RetrieveAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class NewsList(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NewsDetail(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class ReviewList(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetail(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer