from PIL import Image
import os

size_300 = (300, 300)
size_700 = (700, 700)

#Saving in a dif format
#for f in os.listdir('.'):
#    if f.endswith('.JPG'):
#        image = Image.open(f)
#        fn, fext = os.path.splitext(f)
#        image.save('pngs/{}.png'.format(fn))

#Changing the size
#for f in os.listdir('.'):
#    if f.endswith('.JPG'):
#        i = Image.open(f)
#        fn, fext = os.path.splitext(f)
#        
#        i.thumbnail(size_300)
#        i.save('300/{}_300{}'.format(fn, fext))
#        
#        i.thumbnail(size_700)
#        i.save('700/{}_700{}'.format(fn, fext))


image1 = Image.open('i1.JPG')
image1.rotate(-90).save('i1_mod.jpg')

image1.convert(mode='L').save('i1_mod2.jpg')