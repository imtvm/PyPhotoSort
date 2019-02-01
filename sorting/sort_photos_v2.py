from PIL import Image as img
from PIL.ExifTags import TAGS, GPSTAGS
import os, platform, time

DIR = os.path.dirname(os.path.realpath(__file__))

MONTHS = {'01' : "Jan", '02' : "Feb", '03' : "Mar", '04' : "Apr", '05' : "May", '06' : "June", '07' : "July", '08' : "Aug", '09' : "Sept", '10' : "Oct", '11' : "Nov", '12' : "Dec"}

def split_date_time(d):
    return d.split(" ")[0].split(":")

def split_creation_date(d):
    return d.split(' ')

def get_creation_date(f):
    if platform.system() == 'Window':
        print ("Windows")
    else:
        try:
            return time.ctime(os.stat(f).st_birthtime)
        except AttributeError:
            return time.ctime(os.stat(f).st_mtime)

def get_date_time(i):
    info = i._getexif()
    for tag, val in info.items():
        key = TAGS.get(tag, tag)
        if (key == "DateTime"):
            return str(val)
        
def check_folder_cre(d):
    if not (os.path.exists(DIR + "/{}".format(d[4]))):
        os.mkdir("{}".format(d[4]))
    if not (os.path.exists(DIR + "/{}/{}".format(d[4], d[1]))):
        os.mkdir("{}/{}".format(d[4], d[1]))
        
def check_folder_meta(d):
    if not (os.path.exists(DIR + "/{}".format(d[0]))):
        os.mkdir("{}".format(d[0]))
    if not (os.path.exists(DIR + "/{}/{}".format(d[0], MONTHS[d[1]]))):
        os.mkdir("{}/{}".format(d[0], str(MONTHS[d[1]])))

def move_file(i, d, fn, fext, mode):
    if mode == 1:
        check_folder_cre(d)
        i.save("{}/{}/{}".format(d[4], d[1], fn+fext))
    elif mode == 0:
        check_folder_meta(d)
        i.save("{}/{}/{}".format(d[0], MONTHS[d[1]], fn+fext))

def sort_files():
    for f in os.listdir('.'):
        if f.endswith('.jpeg') or f.endswith('.jpg') or f.endswith('.JPG'):
            i = img.open(f)
            img_path = os.path.realpath(f)
            fn, fext = os.path.splitext(f)
            date = 0
            try:
                print ("0 " + f)
                date = split_date_time(get_date_time(i))
                mode = 0
            except:
                print ("1 " + f)
                date = split_creation_date(get_creation_date(f))
                mode = 1
            finally:
                move_file(i,date,fn,fext,mode)
#            os.remove(f)

sort_files()