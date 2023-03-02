from django.urls import path

from webapp.views.base import IndexView
from webapp.views.tasks import TaskDetail

urlpatterns = [
    path("", IndexView.as_view(), name="index_page"),
    path("task/", IndexView.as_view()),
    path('task/<int:pk>', TaskDetail.as_view(), name='detail_task'),

]
