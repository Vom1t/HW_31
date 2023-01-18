from rest_framework import serializers

from users.models import Locations
from users.models import User


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = '__all__'


class LocationPostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Locations
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        depth = 1
        fields = '__all__'


class UserPostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    location = LocationPostSerializer(allow_null=True, required=False)

    def is_valid(self, raise_exception=False):
        self.location_data = self.initial_data.pop('location', None)
        super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        location, _ = Locations.objects.get_or_create(**self.location_data)
        user = User.objects.create(location=location, **validated_data)
        user.set_password(user.password)
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id',
                  'first_name',
                  'last_name',
                  'username',
                  'password',
                  'role',
                  'age',
                  'location',
                  'birth_date',
                  'email'
                  )


class UserUpdateSerializer(serializers.ModelSerializer):
    location = LocationPostSerializer(required=False)

    def is_valid(self, raise_exception=False):
        self.location_data = self.initial_data.pop('location', None)
        super().is_valid(raise_exception=raise_exception)

    def update(self, instance, validated_data):
        _ = self.validated_data.pop('location', None)
        super().update(instance=instance, validated_data=validated_data)
        if self.location_data:
            location, created = Locations.objects.get_or_create(**self.location_data)
            if created:
                instance.location = location
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'password', 'role', 'age', 'location')


class UserDestroySerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id',)



