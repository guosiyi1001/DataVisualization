#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install opencv-python')


# In[2]:


from PIL import Image,ImageDraw

imgpath='Lucky to meet you.jpg'   #图片路径
im = Image.open(imgpath)  #打开图片到im对象
w,h=im.size #读取图片宽、高
print(w,h)
im = im.convert('RGB')#将im对象转换为RGB对象
array = []
for x in range(w):#输出图片对象每个像素点的RBG值到array
    for y in range(h):
        r, g, b = im.getpixel((x,y))#获取当前像素点RGB值
        rgb = (r, g, b)
        array.append(rgb)
image = Image.new('RGB', (w, h), (255, 255, 255)) #创建新图片对象
draw = ImageDraw.Draw(image) #创建Draw对象用于绘制新图
i=0
for x in range(w):  #填充每个像素并对对应像素填上RGB值:
    for y in range(h):
        draw.point((x, y), fill=array[i])
        i=i+1
image.save('new_sample.jpg', 'jpeg')  #写入图片文件


# In[3]:


import matplotlib.pyplot as plt
import numpy as np

imgpath='Lucky to meet you.jpg' #原图片路径
savepath='newplt_example.jpg' #保存图片路径
#读取图片RGB信息到array列表
img_data = plt.imread(imgpath)  #打开图片到im对象
plt.imshow(img_data)  #使用matplotlib模块显示图片
plt.show()
plt.imsave(savepath, img_data)


# In[4]:


#使用Pillow读取和保存图片：读取图片，显示图片，保存为另一个格式
from PIL import Image
import matplotlib.pyplot as plt
img_path = 'Lucky to meet you.jpg'
img = Image.open(img_path)

plt.imshow(img)
plt.axis('off')  # 关闭坐标轴
plt.show()

output_path = 'output_image.png'
img.save(output_path)
print(f"图片已保存为 {output_path}")


# In[5]:


#使用Pillow调整图片大小：读取图片，调整图片大小，保存调整后的图片
from PIL import Image
img = Image.open('Lucky to meet you.jpg')
new_size = (800, 600)
img_resized = img.resize(new_size)
img_resized.save('resized_image.jpg')

plt.imshow(img)
plt.axis('off')  
plt.show()


# In[ ]:


#使用OpenCV读取和保存图片：读取图片，显示图片，保存为另一个格式
import matplotlib.pyplot as plt
import cv2

imgpath='Lucky to meet you.jpg'#图片路径
#读取图片RGB信息到array列表
img_data = cv2.imread(imgpath)  #打开图片到im对象
cv2.imshow('imshow',img_data) #cv2函数imshow(winname, mat)显示图像
cv2.waitKey(0)
cv2.destroyAllWindows() # Jupyter Notebook环境下一定要销毁窗口，否则显示窗口无响应!
plt.imshow(img_data)  #使用matplotlib模块显示图片
plt.show()

cv2.imwrite('output_image.png', img)


# In[ ]:


#使用OpenCV将图片转化为灰度图：读取图片，转化为灰度图，保存灰度图，显示灰度图
import cv2
img = cv2.imread('Lucky to meet you.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_image.jpg', gray_img)
cv2.imshow('Grayscale Image', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.imshow(img)
plt.axis('off')  
plt.show()


# In[ ]:


#使用Pillow在图片上添加文字：读取图片，创建绘图对象，添加文字（设置大小），保存图片
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
img_path = 'Lucky to meet you.jpg'
img = Image.open(img_path)
draw = ImageDraw.Draw(img)
text = "Lucky to meet you too."
position = (50, 50)
font_size = 80

try:
    font = ImageFont.truetype('arial.ttf', font_size)
except IOError:
    font = ImageFont.load_default()

text_color = (0, 0, 0)

draw.text(position, text, font=font, fill=text_color)

output_path = 'image_with_text.jpg'
img.save(output_path)
print(f"图片已保存为 {output_path}")

plt.imshow(img)
plt.axis('off')
plt.show()


# In[ ]:


#使用OpenCV进行图像边缘检测：读取图片，转为灰度图，边缘检测，保存检测结果
import cv2
img = cv2.imread('Lucky to meet you.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray_img, 100, 200)
cv2.imwrite('edges.jpg', edges)
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




