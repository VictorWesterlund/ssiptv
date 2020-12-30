import urllib.request
from PIL import Image

cwd = "../io/"
outputDir = cwd + "dev_og.jpg"

# Lines (width,height)
sizes = {
	"Martin1": (240,240),
	"Martin2": (240,240),
	"Scottie1": (240,240),
	"Scottie2": (240,240),
	"Robot24": (218,120),
	"Robot36": (320,240),
	"Robot72": (256,240)
}

# CCTV Superclass
class CCTV:

	resample = Image.ANTIALIAS

	def resize(self,mode):
		image = Image.open(outputDir,mode="r")
		image = image.resize(sizes[mode],CCTV.resample)

		image.save(f"{cwd}images/dev_{mode}.jpg")

	def save(self,url):
		urllib.request.urlretrieve(url,outputDir)
