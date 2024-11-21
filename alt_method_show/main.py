#install packet
#pip install opencv python
#pip install matplotlib
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"alt_method_show\zumselpainter_cute_capybara_at_the_dance_floor_disco_light_--ar_a80c5a60-40db-4dd3-840c-d0c387d6c418.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
g_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
hsv_img = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
r,g,b = cv2.split(img)  

titles = [" red"," green"," blue","original","gray","hsv",]
images = [r,g,b,img,g_img,hsv_img,]
count = 6
for i in range(count):
    plt.subplot(2,3,i + 1)
    plt.title(titles[i])
    plt.imshow(images[i],"gray")
plt.show()

