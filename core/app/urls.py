from django.urls import path
from . import views

urlpatterns = [
    path('news-list/', views.NewsList.as_view()),
    path('news-detail/<int:pk>/', views.NewsDetail.as_view()),

    path('faq-list/', views.FAQList.as_view()),
    path('faq-detail/<int:pk>/', views.FAQDetail.as_view()),

    path('partner-list/', views.PartnersList.as_view()),
    path('partner-detail/<int:pk>/', views.PartnersDetail.as_view()),

    path('feedback-list/', views.ReviewList.as_view()),
    path('feedback-detail/<int:pk>/', views.ReviewDetail.as_view()),

]