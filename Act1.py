import cv2
import os
from PIL import Image

os.chdir("C:/Users/mbnrs/OneDrive/Documents/Jetlearn/OpenCV-6/Photos")
path = "C:/Users/mbnrs/OneDrive/Documents/Jetlearn/OpenCV-6/Photos"

meanwidth= 0
meanheight= 0
num_img = len(os.listdir("."))
print("Number of images:",num_img)

for file in os.listdir("."):
    img=Image.open(os.path.join(path,file))
    width, height = img.size
    meanwidth= meanwidth+width
    meanheight= meanheight+height

meanwidth= meanwidth//num_img
meanheight= meanheight//num_img

print("Mean Width: ", meanwidth)
print("Mean Height: ", meanheight)

for file in os.listdir("."):
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
        img=Image.open(os.path.join(path,file))
        imgResized=img.resize((meanwidth, meanheight))
        imgResized.save(file, "JPEG", quality = 100)
        print("Image is resized")

def videoGenerator():
    video_name = "MyFirstVideo.avi"
    os.chdir("C:/Users/mbnrs/OneDrive/Documents/Jetlearn/OpenCV-6/Photos")
    images=[]
    for img in os.listdir("."):
        images.append(img)

    
    frame=cv2.imread(os.path.join(".",images[0]))
    height, width, layer = frame.shape
    video=cv2.VideoWriter(video_name, 0, 1, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(".",image)))

    cv2.destroyAllWindows()
    video.release()

videoGenerator()