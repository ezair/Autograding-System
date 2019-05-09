import codecs
import shutil
import os
import webbrowser

os.chdir("compiler/autograderexamples/Cards")
os.system("gradle build")
os.chdir("build/reports/tests/test")
os.system("ls")
webbrowser.open('file://' + os.path.realpath('index.html'))
print(os.path.realpath('index.html'))
os.chdir('/codecs')
os.system('ls')