import pyaudio
import pychromecast

def GetChromecasts():
	return pychromecast.get_chromecasts()

def GetAudioDeviceNames():
	p = pyaudio.PyAudio()
	deviceNames = []
	for i in range(p.get_device_count()):
		deviceNames.append(p.get_device_info_by_index(i).get("name"))
	return deviceNames

def GetAudioDevices():
	p = pyaudio.PyAudio()
	deviceNames = []
	for i in range(p.get_device_count()):
		deviceNames.append(p.get_device_info_by_index(i))
	return deviceNames

if __name__ == '__main__':
	print (GetAudioDeviceNames())
	print (GetAudioDevices())
	print (GetChromecasts())
