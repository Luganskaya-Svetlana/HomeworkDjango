from django.urls import path, re_path

from . import views

app_name = 'catalog'
urlpatterns = [
    path('', views.ItemsView.as_view(), name='list'),
    re_path(r'^(?P<pk>[1-9]\d*)/$', views.ItemView.as_view(), name='detail'),
    path('category/<str:slug>/', views.ItemCategoryView.as_view(),
         name='category'),
    path('category/', views.CategoriesView.as_view(), name='categories')
]
