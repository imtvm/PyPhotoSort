from PIL import Image as img
from PIL.ExifTags import TAGS, GPSTAGS
import os, platform, time

DIR = os.path.dirname(os.path.realpath('.'))

MONTHS = {'01' : "Jan", '02' : "Feb", '03' : "Mar", '04' : "Apr", '05' : "May", '06' : "June", '07' : "July", '08' : "Aug", '09' : "Sept", '10' : "Oct", '11' : "Nov", '12' : "Dec"}

def split_date_time(d):
    return d.split(" ")[0].split(":")

def get_date_time(i):
    info = i._getexif()
    for tag, val in info.items():
        key = TAGS.get(tag, tag)
        if (key == "DateTime"):
            return str(val)
        
def check_folder(d):
    if not (os.path.exists(DIR + "/{}".format(d[0]))):
        print ('mkdir 1')
        os.mkdir("{}".format(d[0]))
    if not (os.path.exists(DIR + "/{}/{}".format(d[0], d[1]))):
        print ('mkdir 2')
        os.mkdir("{}/{}".format(d[0], d[1]))

def move_file(i, d, fn, fext):
    check_folder(d)
    i.save("{}/{}/{}".format(d[0], MONTHS[d[1]], fn+fext))

def sort_files():
    count = 0
    scount = 0
    for f in os.listdir('.'):
        if f.endswith('.jpeg') or f.endswith('.jpg') or f.endswith('.JPG'):
            i = img.open(f)
            img_path = os.path.realpath(f)
            fn, fext = os.path.splitext(f)
            date = 0
            try:
                print ("Success " + str(scount))
                scount += 1
#                date = split_date_time(get_date_time(i))
#                move_file(i,date,fn,fext)
            except:
                print ("Error " + str(count))
                count += 1
#            finally:
#            os.remove(f)

sort_files()