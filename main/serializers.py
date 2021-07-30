from rest_framework import serializers
from django import forms

from .models import Illness,Drug,Post,Reply

        
class IllnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Illness
        fields = '__all__'
        
class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = '__all__'
        
class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'
        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
