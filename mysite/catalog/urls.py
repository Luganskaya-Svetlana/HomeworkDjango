from django.urls import path, re_path


from . import views


urlpatterns = [
    path('', views.item_list),
    re_path(r'(?P<pk>^[1-9]\d*)/$', views.item_detail)
]
