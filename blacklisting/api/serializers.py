from rest_framework import serializers
from . models import Ipv4


class ipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ipv4
        fields = ["ip"]
