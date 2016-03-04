from push_notifications.models import Device, GCMDevice, APNSDevice
from push_notifications.ser import DeviceSer, GCMDeviceSer, APNSDeviceSer

def get_ser(device_type):
	device_type = device_type.lower()

	if device_type == "android":
		return GCMDeviceSer
	elif device_type == "ios":
		return  APNSDeviceSer

	return None

def get_model(device_type):
	device_type = device_type.lower()
	
	if device_type == "android":
		return GCMDevice
	elif device_type == "ios":
		return  APNSDevice

	return None

def get_ser_and_model(device_type):
	return (get_ser(device_type), get_model(device_type))

