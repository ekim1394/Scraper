import sys, os, glob

#variables needed
directory = 'C:\Users\e.a.kim\Documents\TXT Scraper'
work = '\work'
done = '\done'

#sets working directory to work directory
os.chdir(directory+work)

#manifest files
for filename in glob.glob('*.manifest'):
   print filename #returns all files in work folder with

#med files
for filename in glob.glob('*.med'):
   print filename #returns all files in work folder with

#
for filename in glob.glob('CDAS_POS_ACP*'):
   print filename #returns all files in work folder with


#sets working directory to done
os.chdir(directory+done)
