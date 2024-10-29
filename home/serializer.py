from .models import JOBSLISTING
from rest_framework import serializers

class jobserializer(serializers.ModelSerializer):

    class Meta:
        model =JOBSLISTING
        fields='__all__'