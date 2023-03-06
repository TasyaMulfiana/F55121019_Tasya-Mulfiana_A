from PIL import Image,ImageChops
img1 = Image.open('doraemon1.jpg')
img2 = Image.open('doraemon2.jpg')
diff = ImageChops.difference(img1,img2)
if diff.getbbox():
   diff.show()