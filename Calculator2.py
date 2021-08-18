from tkinter import *
from PIL import Image, ImageTk, ImageDraw
import time

def main():
   f = open("All IBET Surface Calculations", "w");
   
   for i in range(1,22):
      f.write("IBET Group " + str(i)+": ")
      try:
         percent = calculate("IBETGroup"+str(i)+".jpg")
         f.write(percent + "\n")
      except IOError:
         f.write("***** NO FILE *****" + "\n")
         continue
   
def calculate(filename):

   img = Image.open(filename)
   w,h = img.size
   
   total = w*h
      
   pix_count = 0.0
   imp_count = 0.0
   
   white = (255,255,255)
   cyan = (0, 255,255)
      
   image1 = Image.new("RGB", (w,h), (255,255,255))
   draw = ImageDraw.Draw(image1)
      
   rp,gp,bp = 0,0,0
           
   for x in range(w):
      for y in range(h):
         rp,gp,bp = img.getpixel((x,y))
         if 40 <= (2.03*gp)-rp-bp:
            if not(x+1 == w or y+1 == h):
               draw.line([x,y,x+1,y+1],cyan)
 
         elif gp > rp+2*bp-80:
            if not(x+1 == w or y+1 == h):
               draw.line([x,y,x+1,y+1],cyan)
         else:
            draw.line([x,y,x+1,y+1],(rp,gp,bp))
         
   for x in range(w):
      for y in range(h):        
         if (x-w/2)*(x-w/2) + (y-h/2)*(y-h/2) > (w/2-5)*(w/2-5):
            draw.line([x,y,x,y], white)

   filename = ("image"+filename)
   image1.save(filename)            
   total_changing = total
   for pixel in image1.getdata():
      if pixel == (255,255,255):
         total_changing -= 1
      elif not pixel == (0,255,255):
         imp_count+=1
   pix_count = total_changing
         
   percentage = imp_count*100/pix_count
   return(str(round(percentage,5)) + "%")

if __name__ == "__main__":
   main()