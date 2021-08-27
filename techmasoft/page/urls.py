from django.urls import path
from page.views import PageView, MessagesListView, archive, delete

urlpatterns = [
    path('', PageView.as_view(), name='homepage'),
    path('messages/', MessagesListView.as_view(), name='messages'),
    path('archive/<id>', archive, name='archive'),
    path('delete/<id>', delete, name='delete')
]