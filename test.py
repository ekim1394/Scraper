import os, sys, glob

directory = 'C:\Users\e.a.kim\Documents\TXT Scraper'
work = '\work'
done = '\done'

#sets working directory to work directory
os.chdir(directory+work)

for filename in glob.glob('*.manifest'):
   print filename #returns all files in work folder with
   workDirectory = directory+work+'\'+filename
   print workDirectory
