#!/usr/bin/env python3

import os
from PIL import Image


def set_folder(folder):
  if os.path.isdir(folder):
    list_files(os.path.join(os.getcwd(), folder))
  else:
    print("Folder not found")

def list_files(path):
  
  files = os.listdir(path)
  for file in files:
    if os.path.isdir(os.path.join(path, file)):
      print("Found sub-folder")
      list_files(os.path.join(path, file))
    else:
      #print(os.path.join(path, file))
      try:
        with Image.open(os.path.join(path, file)).convert('RGB') as im:
          new_im = im.rotate(90).resize((128,128))
          new_im.save(os.path.join(path, file) + ".jpg")
          #new_im = im.rotate(90).resize((128,128))
          #print(os.path.join(path, file), new_im.format, f"{new_im.size}x{new_im.mode}")
          #print(os.path.join(path , file) + ".jpg")
          #new_im.save(os.path.join(path, file) + ".jpg")
          #new_im.save(file + ".jpg")
      except OSError:

if __name__ == '__main__':
  set_folder(input("Please enter folder location to be processed: \n(This can be either an absolute path or a relative path)\n"))

