from django.db.models import fields
from rest_framework import serializers
from api.models import (User)

from django.core.exceptions import ValidationError
from main.settings import TIME12HRSFORMAT, DATEFORMAT
from api.serializers.uploadMedia import UploadMediaDetailsSerializer

class UserLoginDetailSerializer(serializers.ModelSerializer):
	"""
	Return the details of Login User.
	"""
	image = UploadMediaDetailsSerializer()
	class Meta(object):
		model = User
		fields = (
		'id', 'email', 'first_name', 'last_name', 'phone_no', 'is_active', 'is_deleted', "profile_status", "country_code", "image")


class UserCreateUpdateSerializer(serializers.ModelSerializer):
	"""
	create/update user .
	"""
	id = serializers.IntegerField(required=False)
	class Meta:
		model = User
		fields = ('id', 'first_name', 'phone_no', 'email', 'country_code', 'role', 'gender', 'address', 'longitude', 'latitude', 'image')       

	def update(self, instance, validated_data):
		instance.first_name = validated_data['first_name']
		instance.email = validated_data['email']
		instance.country_code = validated_data['country_code']
		instance.phone_no = validated_data['phone_no']
		instance.address = validated_data['address']
		if 'longitude' in validated_data:
			instance.longitude = validated_data['longitude']
		if 'latitude' in validated_data:
			instance.latitude = validated_data['latitude']
		instance.gender = validated_data['gender']
		instance.role = validated_data['role']
		instance.image = validated_data['image']
		instance.encoded_id = None
		instance.is_active = True
		instance.profile_status = 4
		instance.save()

		return instance


class UserUpdateDetialsSerializer(serializers.ModelSerializer):
	"""
	create/update user.
	"""
	id = serializers.IntegerField(required=False)
	class Meta:
		model = User
		fields = ('id', 'first_name', 'phone_no', 'email', 'country_code', 'role', 'gender', 'address', 'longitude', 'latitude', 'image')       

	# def update(self, instance, validated_data):
	# 	instance.first_name = validated_data['first_name']
	# 	instance.email = validated_data['email']
	# 	instance.country_code = validated_data['country_code']
	# 	instance.phone_no = validated_data['phone_no']
	# 	instance.address = validated_data['address']
	# 	if 'longitude' in validated_data:
	# 		instance.longitude = validated_data['longitude']
	# 	if 'latitude' in validated_data:
	# 		instance.latitude = validated_data['latitude']
	# 	instance.gender = validated_data['gender']
	# 	instance.role = validated_data['role']
	# 	instance.image = validated_data['image']
	# 	instance.encoded_id = None
	# 	instance.is_active = True
	# 	instance.profile_status = 4
	# 	instance.save()



		# return instance
	
	