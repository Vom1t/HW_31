from rest_framework import serializers

from ads.serializers import AdSerializerCompressed
from selection.models import Selection


class SelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ('id', 'name',)


class SelectionPostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Selection
        fields = '__all__'


class SelectionDetailSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field='username',  read_only=True)
    items = AdSerializerCompressed(many=True)

    class Meta:
        model = Selection
        fields = ('id', 'name', 'owner', 'items',)


class SelectionUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Selection
        fields = ('name', 'items')


class SelectionDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Selection
        fields = ('id',)