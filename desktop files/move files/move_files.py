import os
import shutil

os.chdir('/Users/username/Desktop/docs')

if not os.path.exists("moved_docs"):
  os.mkdir("moved_docs")

for file in os.listdir():
  if file == "moved_docs":
    continue
  shutil.move(file, "moved_docs")
