from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:Id>/', views.detail, name = 'detail'),
    # path('<int:Id>/results/', views.results, name = 'results'),
    path('<int:Id>/validate', views.validate, name = 'validate')
]