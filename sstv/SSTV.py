import os

cwd = "../io/"
inputDir = cwd + "images/"
outputDir = cwd + "waves/"

class SSTV:

	def __init__(self,mode):
		self.mode = mode or "Robot36"

		self.image = f"{inputDir}dev_{self.mode}.jpg"
		self.wav = f"{outputDir}dev_{self.mode}.wav"
		self.gen()

	def gen(self):
		os.system(f"python3 -m pysstv {self.image} {self.wav} --mode {self.mode} --vox")
