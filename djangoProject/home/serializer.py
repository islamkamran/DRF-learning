from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):

    class Meta:  # Learn about the concepts of Meta class in python and inheritance
        model = Todo
        field = '__all__'  # you can select seperate fields too