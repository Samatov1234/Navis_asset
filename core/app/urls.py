from django.urls import path
from . import views

urlpatterns = [
    # Partners
    path('partners/', views.PartnersListView.as_view(), name='partners-list'),
    path('partners/<int:pk>/', views.PartnersDetailView.as_view(), name='partners-detail'),

    # Questions & Answers
    path('questions/', views.QuestionsListView.as_view(), name='questions-list'),
    path('questions/<int:pk>/', views.QuestionsDetailView.as_view(), name='questions-detail'),

    # News
    path('news/', views.NewsListView.as_view(), name='news-list'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='news-detail'),

    # Reviews
    path('reviews/', views.ReviewsListView.as_view(), name='reviews-list'),
    path('reviews/<int:pk>/', views.ReviewsDetailView.as_view(), name='reviews-detail'),

    # Applications
    path('applications/', views.ApplicationsListView.as_view(), name='applications-list'),
    path('applications/<int:pk>/', views.ApplicationsDetailView.as_view(), name='applications-detail'),
]
