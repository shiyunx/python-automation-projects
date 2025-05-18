import os
import shutil

os.chdir('/Users/username/Desktop/docs')

if not os.path.exists("copied_docs"):
  os.mkdir("copied_docs")

for file in os.listdir():
  if file == "copied_docs":
    continue
  shutil.copy(file, "copied_docs")