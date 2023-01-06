from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
    path('finches/create/', views.FinchCreate.as_view(), name='finch_create'),
    path('finches/<int:pk>/update/', views.FinchUpdate.as_view(), name='finch_update'),
    path('finches/<int:pk>/delete/', views.FinchDelete.as_view(), name='finch_delete'),
    path('finch/<int:finch_id>/add_food/', views.add_food, name='add_food'),
    path('twigs/', views.TwigList.as_view(), name='twigs_index'),
    path('twigs/<int:pk>/', views.TwigDetail.as_view(), name='twig_details'),
    path('twigs/create/', views.TwigCreate.as_view(), name='twigs_create'),
    path('twigs/<int:pk>/update/', views.TwigUpdate.as_view(), name='twig_update'),
    path('twigs/<int:pk>/delete/', views.TwigDelete.as_view(), name='twig_delete'),
    path('twigs/<int:finch_id>/assoc_twig/<int:twig_id>/', views.assoc_twig, name='assoc_twig'),
    path('twigs/<int:finch_id>/unassoc_twig/<int:twig_id>/', views.unassoc_twig, name='unassoc_twig')
]