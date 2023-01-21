from django.urls import path
from .views import CreateMessageView, DetailMessageView

urlpatterns = [
    path('create', CreateMessageView.as_view(), name='create-message'),
    path('<int:message_id>', DetailMessageView.as_view(), name='detail-message')
]