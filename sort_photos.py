from PIL import Image as img
from PIL.ExifTags import TAGS
import os

#DIR = os.path.dirname(os.path.realpath(__file__))

DIR = "testphotos/"

MONTHS = {'01' : "Jan", '02' : "Feb", '03' : "Mar", '04' : "Apr", '05' : "May", '06' : "June", '07' : "July", '08' : "Aug", '09' : "Sept", '10' : "Oct", '11' : "Nov", '12' : "Dec"}

def split_date_time(d):
    return d.split(" ")[0].split(":")

def get_date_time(i):
    info = i._getexif()
    
    for tag, val in info.items():
        key = TAGS.get(tag, tag)
        
        if (key == "DateTime"):
            return str(vale)
        
def sort_files():
#    os.chdir(DIR)
    for f in os.listdir('.'):
        if f.endswith('.jpeg') or f.endswith('.jpg') or f.endswith('.JPG'):
            i = img.open(f)
            print (i._getexif())
            try:
                print (split_date_time(get_date_time(i)))
            except:
                print ("Error")
            
sort_files()