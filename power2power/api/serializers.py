from .models import Node, User
from rest_framework import serializers

class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = '__all__'

    def update(self, instance, validated_data):
        power_in = validated_data.pop('power_in', None)
        power_out = validated_data.pop('power_in', None)

        if power_in:
            instance.power_in = power_in
            instance.save()
        if power_out:
            instance.power_out = power_out
            instance.save()
        return instance

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return Node.objects.create(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
