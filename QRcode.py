# Put THE LINK OF ANYTHING YOU WISH TO MAKE QR OF IN MAKE FUNCTION YOU JUST NEED TO PASTE IT
# AT SECOND LIE OF CODE WHICH IS IMG.SAVE(" ") . IN THIS YOU NEED TO ENTER THE NAME FOR IMAGE SAVE  AND IT WILL STORE IMAGE IN JPG FORMAT.
#AFTER THAT RUN THE CODE .YOU JUST NEED TO CHECK THE FOLDER IN WHICH .PY YOU HAVE STORED THERE YOU FIND AND IMAGE HAS OCCURED OPEN IT AND SCAN IT


import qrcode

img=qrcode.make("https://github.com/Anshu1802")
img.save("Git-hub.jpg")

img=qrcode.make("https://www.linkedin.com/in/ansh-kevadiya-22623b227")
img.save("Linkedin.jpg")


img=qrcode.make("https://www.instagram.com/__anshu__1802/")
img.save("Instagram.jpg")
