from rest_framework import serializers
from .models import Testimonial, Title

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ("photo", "name", "work", "declaration")

class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ("label",)