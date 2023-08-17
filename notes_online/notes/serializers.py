from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from .models import Note, Theme

class ThemeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    theme_name = serializers.CharField(help_text="Note theme", max_length=30)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Theme.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.theme_name = validated_data.get("theme_name", instance.theme_name)
        instance.save()
        return instance

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

