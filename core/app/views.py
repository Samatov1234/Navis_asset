from rest_framework import generics
from .models import Partner, FAQ, News, Feedback, Application
from .serializers import PartnerSerializer, FAQSerializer, NewsSerializer, FeedbackSerializer, ApplicationSerializer


class PartnerList(generics.ListAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

class PartnerDetail(generics.RetrieveAPIView):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


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

class FeedbackList(generics.ListAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class FeedbackDetail(generics.RetrieveAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class ApplicationList(generics.ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class ApplicationDetail(generics.RetrieveAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class ApplicationCreate(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer