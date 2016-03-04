from rest_framework import serializers
from push_notifications.models import Device, GCMDevice, APNSDevice
from consultant.ser import ConsultantTokenSer

class DeviceSer(serializers.ModelSerializer):
	user = ConsultantTokenSer()
	class Meta:
		model = Device

class GCMDeviceSer(serializers.ModelSerializer):
	user = ConsultantTokenSer()
	
	class Meta:
		model = GCMDevice

class APNSDeviceSer(serializers.ModelSerializer):
	user = ConsultantTokenSer()

	class Meta:
		model = APNSDevice