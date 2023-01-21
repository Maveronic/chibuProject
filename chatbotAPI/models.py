from django.db import models

class Message(models.Model):
    """
    This class represents a message in the database.
    """
    text = models.CharField(max_length=225)

    def __str__(self):
        """
        Returns the text of the message as a string representation.
        """
        return self.text
