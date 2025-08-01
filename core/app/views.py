from rest_framework import generics
from . import serializers, models

# Partners
class PartnersListView(generics.ListAPIView):
    queryset = models.Partners.objects.all()
    serializer_class = serializers.PartnersSerializer

class PartnersDetailView(generics.RetrieveAPIView):
    queryset = models.Partners.objects.all()
    serializer_class = serializers.PartnersSerializer

# Questions & Answers
class QuestionsListView(generics.ListAPIView):
    queryset = models.QuestionsAnswers.objects.all()
    serializer_class = serializers.QuestionsAnswersSerializer

class QuestionsDetailView(generics.RetrieveAPIView):
    queryset = models.QuestionsAnswers.objects.all()
    serializer_class = serializers.QuestionsAnswersSerializer

# News
class NewsListView(generics.ListAPIView):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer

class NewsDetailView(generics.RetrieveAPIView):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer

# Reviews
class ReviewsListView(generics.ListAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

class ReviewsDetailView(generics.RetrieveAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

# Applications
class ApplicationsListView(generics.ListAPIView):
    queryset = models.Application.objects.all()
    serializer_class = serializers.ApplicationSerializer

class ApplicationsDetailView(generics.RetrieveAPIView):
    queryset = models.Application.objects.all()
    serializer_class = serializers.ApplicationSerializer