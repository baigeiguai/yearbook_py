from django.urls import path

from . import views

urlpatterns = [
    path('echo', views.echo_index, name='echo'),
    path('entity_extract',views.entity_extract_index,name="entity_extract")
]