from rest_framework import serializers

from mainapp.models import(
    Iphone, Macbook, Airpods,
)

class IphoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Iphone
        fields = (
            'id', 'name', 'version', 'gb', 'color', 'year'
        )


class MacbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Macbook
        fields = (
            'id', 'name', 'version', 'gb', 'year'
        )

class AirpodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airpods
        fields = (
            'id', 'name', 'version', 'color', 'year'
        )