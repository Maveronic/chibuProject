from .models import Message
from .serializers import MessageSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema


# Create your views here.
class CreateMessageView(GenericAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()

    @swagger_auto_schema(operation_summary="Get all messages in the database")
    def get(self, request):
        messages = Message.objects.all()
        serializer = self.serializer_class(instance=messages, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="Add a new message to the database")
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'text': 'Hello'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailMessageView(GenericAPIView):
    serializer_class = MessageSerializer

    @swagger_auto_schema(operation_summary='Get a specific message using its unique identifier')
    def get(self, request, message_id):
        message = get_object_or_404(Message, pk=message_id)
        serializer = self.serializer_class(instance=message)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary='Update a specific message selected using its unique identifier')
    def put(self, request, message_id):
        data = request.data
        message = get_object_or_404(Message, pk=message_id)
        serializer = self.serializer_class(data=data, instance=message)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'text': 'Hello'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_summary='Delete a specific message using its unique identifier')
    def delete(self, request, message_id):
        message = get_object_or_404(Message, pk=message_id)
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
