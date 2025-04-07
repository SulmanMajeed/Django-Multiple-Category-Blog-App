from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogpost/<str:slug>', views.blogpost, name='blogpost'),
    path('category/<str:slug>', views.blog_category, name='blog_category'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('search', views.search, name='search'),
    path("legal", views.legal, name="legal"),
]
