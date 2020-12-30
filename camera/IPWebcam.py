from CCTV import CCTV

# Android app: https://play.google.com/store/apps/details?id=com.pas.webcam
class IPWebcam(CCTV):

	normal = "/photo.jpg"
	focused = "/photoaf.jpg"

	def __init__(self,endpoint = None,focus = False):
		if(endpoint is None):
			raise ValueError("Invalid endpoint")

		self.focus = focus
		self.fetch(endpoint)

	def fetch(self,endpoint):
		if(self.focus):
			# Save a focused photo
			self.save(endpoint + IPWebcam.focused)
			return
		
		# Save a normal photo
		self.save(endpoint + IPWebcam.normal)
