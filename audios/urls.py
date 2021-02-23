from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:class_id>/<int:week_id>', views.details, name='details'),
    path('<int:class_id>/<int:week_id>/listen', views.listen, name='listen'),
    path('<int:class_id>/<int:week_id>/upload', views.upload_form, name='upload'),
]