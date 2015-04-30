from django.forms import widgets
from rest_framework import serializers
from co_op.models import posting

class posting_serializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    number_of_semesters = serializers.IntegerField(read_only=True)
    description = serializers.CharField()

    def create(self, validated_data):
        return posting.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        insatnce.number_of_semesters = validated_data.get('number_of_semesters', instance.number_of_semesters)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
