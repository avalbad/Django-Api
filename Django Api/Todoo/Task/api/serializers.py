from rest_framework import serializers
from Task.models import TodoTask

class TodoTaskserializers(serializers.ModelSerializer):
    class Meta:
        model = TodoTask
        fields = ['category','title','created_at']