from tkinter import *
from PIL import Image, ImageTk, ImageDraw
import time

def main():
   global canvas, img,w,h
   image_name = "IBETGroup17.jpg"
   img = Image.open(image_name)
   w,h = img.size
   mv = 22
   
   pix_count = 0
   imp_count = 0
   
   white = (255,255,255)
   cyan = (0, 255,255)
   
#    root = Tk()
#    root.title(image_name)
#    canvas = Canvas(root, width = w*2+10, height = h)
#    canvas.pack()

#   display = ImageTk.PhotoImage(img)  
#    canvas.create_image(0, 0, anchor=NW, image=display)
#    canvas.create_image(w+10, 0, anchor=NW, image=display)
   
   image1 = Image.new("RGB", (w,h), (255,255,255))
   draw = ImageDraw.Draw(image1)
      
   rp,gp,bp = 0,0,0
           
   for x in range(w):
      for y in range(h):
         rp,gp,bp = img.getpixel((x,y))
         draw.line([x,y,x,y],(rp,gp,bp))
         if 36 <= (2.02*gp)-rp-bp:
            if not(x+1 == w or y+1 == h):
               draw.line([x,y,x,y],cyan)
#               canvas.create_line(x,y,x+1,y+1, fill = 'cyan')
 
         if gp > rp+2*bp-70:
            if not(x+1 == w or y+1 == h):
               draw.line([x,y,x,y],cyan)
#               canvas.create_line(x,y,x+1,y+1, fill = 'cyan')

   for x in range(w):
      for y in range(h):        
         if (x-w/2)*(x-w/2) + (y-h/2)*(y-h/2) > (w/2-5)*(w/2-5):
            draw.line([x,y,x,y], white)
#            canvas.create_line(x,y,x+1,y+1, fill = 'white')
         else:
            pix_count+=1
   
#    for x in range(w+10,w*2+10):
#       for y in range(h):        
#          if (x-(w/2+w+10))*(x-(w/2+w+10)) + (y-h/2)*(y-h/2) > (w/2-5)*(w/2-5):
#             draw.line([x,y,x,y], white)
# #            canvas.create_line(x,y,x+1,y+1, fill = 'white')
   filename = ("IBETGroup17image.jpg")
   image1.save(filename)            
#    root.bind('<Button-1>', click)
#    root.mainloop()
   clated = Image.open(filename)
   w1,h1 = clated.size
   for x in range(w1):
      for y in range(w1):
         if(clated.getpixel((x,y))==0,255,255):
            imp_count+=1
   print(imp_count)
   print(pix_count)

if __name__ == "__main__":
   main()