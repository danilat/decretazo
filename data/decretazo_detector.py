import os
import shutil

for dirname, dirnames, filenames in os.walk('data/html'):
    for filename in filenames:
    	filedir = os.path.join(dirname, filename)
        f = open(filedir, 'r')
        content = f.read()
        #comprobar si es decreto ley
        if True:
        	print filedir
        	shutil.copyfile(filedir, 'data/decreto-ley/'+filename)
        