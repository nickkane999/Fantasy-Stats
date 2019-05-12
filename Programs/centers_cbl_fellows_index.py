import os
import sys

# Set Parameters
content_filename = "content.txt" # Content for CMS page
file_path = "C:/Users/Nick Kane/Dropbox/Work/Projects/Personal Projects/CMS Uploading/Functions" # File path holding Upload CMS program
sys.path.insert(0, file_path)
from Upload_CMS import *

# Get .py name, to pass as relative path into the program
path = os.path.basename(sys.argv[0])[:-3]
uploadCMS(path, content_filename)
