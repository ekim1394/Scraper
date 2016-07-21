'''
This program is meant to help scrape data off of .txt files
by reading from the work folder
and writing new files into the done folder

It will separate data files into lists and organize them accordingly

glob is used to find specific file types
shelve is used to save variables to copy onto final txts
pyperclip is used to copy/paste
shutil is used to move/modify files from folder to folder
'''
import sys, os, glob, shelve, pyperclip, shutil

# variables needed
directory = 'C:\Users\e.a.kim\Documents\TXT Scraper'
work = '\work'
done = '\done'
wpShelf = shelve.open('wp')
labels = []
# sets working directory to work directory
os.chdir(directory+work)

#read manifest files
for filename in glob.glob('*.manifest'):
   workFile = directory+work+'\\'+filename
   openFile = open(workFile, 'r') #opens file for editing
   readFile = openFile.readlines() #opens file line by line in list

# lists each line of file skipping line breaks
for line in readFile:
   if line == '\\n':
       continue
   else:
       label_id = line.split('|')[1]
       print label_id
       labels.append(label_id)

print labels



# sets working directory to done
os.chdir(directory+done)

# close shelf
wpShelf.close()
