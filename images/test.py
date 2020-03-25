from PIL import Image

im = Image.open("download.jpeg", "r")
val = list(im.getdata())

print(val)
