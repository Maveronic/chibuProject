from .models import Message
from rest_framework import serializers

class MessageSerializer(serializers.ModelSerializer):
    """
    This class converts the Message model into JSON format and vice versa.
    """
    text = serializers.CharField(max_length=225)

    class Meta:
        """
        Meta options for the MessageSerializer.
        """
        model = Message
        fields = ('id', 'text',)
