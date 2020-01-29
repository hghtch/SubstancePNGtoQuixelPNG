from PIL import Image
import os

srcDir = input("Enter Source Directoy.\n")+"\\"
def save_img(name):
	global img
	global ipath
	img= img.convert("RGB")#convert 32b RGBA to 24b RGB
	img.save(os.path.join(ipath,"24b_"+name), compress_level=0)#save img with 24b_ prefix
	print("File: "+os.path.join(ipath,"24b_"+name)+" saved."
for d in os.listdir(srcDir): ## for every dir in source dir
	ipath=os.path.join(srcDir, d+"\\") #join source dir with dir into one path
	for i in os.listdir(ipath): #for every file in ipath
		with Image.open(ipath+i) as img: #open file as "img"
			if img.mode == 'I': #if mode of img is 'I'
				table = [i/256 for i in range(65536)]; img = img.point(table, 'L')#manually convert 16b greyscale to 8b due to bug in Pillow https://stackoverflow.com/questions/19892919/pil-converting-an-image-with-mode-i-to-rgb-results-in-a-fully-white-image
				save_img(i)
			elif img.mode == 'RGBA': #if mode is RGBA
				save_img(i)
			else:
				print("PNGs are in wrong Image Mode. This script takes 16 bit greyscale and 32bit RGBA PNGs")
