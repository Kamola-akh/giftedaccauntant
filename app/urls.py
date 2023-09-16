from django.urls import path

from app import views

urlpatterns = [
        path("news/<str:news_id>", views.NewsDetailView.as_view()),
        path("news", views.NewsListView.as_view()),
        path("contact", views.ContactViewSet.as_view()),
        path("tarif-product/", views.TarifProductionViews.as_view()),

]