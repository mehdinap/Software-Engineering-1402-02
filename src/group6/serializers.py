from rest_framework import serializers
from .models import FAQ


class FAQSerializer(serializers.ModelSerializer):
    is_leaf = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ['id', 'text', 'parent', 'is_leaf']

    def get_is_leaf(self, obj):
        return obj.get_children() == []
