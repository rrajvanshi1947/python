from PIL import Image

img = Image.open('795.jpeg')
print(img.size)
print(img.format)

# img.show()

area = (100,100,800,800)
cropped_img = img.crop(area)

print(cropped_img.size)
print(cropped_img.format)
# cropped_img.show()

partypic = Image.open('IMG_20171119_213726.jpg')
print(partypic.size)
area2 = (150,150,1110,1110)
partypic.paste(img, area2)
partypic.show()
