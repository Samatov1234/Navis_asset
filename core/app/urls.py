from django.urls import path
from . import views
from .views import ApplicationCreate

urlpatterns = [
    path('news-list/', views.NewsList.as_view()),
    path('news-detail/<int:pk>/', views.NewsDetail.as_view()),

    path('faq-list/', views.FAQList.as_view()),
    path('faq-detail/<int:pk>/', views.FAQDetail.as_view()),

    path('partner-list/', views.PartnerList.as_view()),
    path('partner-detail/<int:pk>/', views.PartnerDetail.as_view()),

    path('feedback-list/', views.FeedbackList.as_view()),
    path('feedback-detail/<int:pk>/', views.FeedbackDetail.as_view()),

    path('application-list/', views.ApplicationList.as_view()),
    path('application-detail/<int:pk>/', views.ApplicationDetail.as_view()),
    path('application-create/', ApplicationCreate.as_view()),

]