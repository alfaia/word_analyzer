from rest_framework import serializers


class VowelCountRequestSerializer(serializers.Serializer):
    words = serializers.ListField(
        child=serializers.CharField()
    )


class SortRequestSerializer(serializers.Serializer):
    words = serializers.ListField(
        child=serializers.CharField()
    )
    order = serializers.ChoiceField(choices=['asc', 'desc'])
