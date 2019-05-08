#imports are to navigate and use terminal commands
import os.path, subprocess

#tick is the name of the folder to move into 
tic = "TicTacToe"
#move into the directory
os.chdir(tic)
#build gradle 
compileCheck = os.system("gradle build")
#go to the directory with the test file htmls 
os.chdir("build/reports/tests/test/classes/")
#run the ls command and take it's output
getFiles = subprocess.check_output("ls", shell = True)
#split up string into a array that needs refinment
htmlFiles = str(getFiles).split("\\")
#First element is different then the rest so it needs some more cleaning
temp = htmlFiles[0] 
htmlFiles[0] = temp[1:] 
#Could be simplified but it is a loop that goes through every element of htmlFiles
i=0
j = len(htmlFiles) -1
#launch the webpage stored in the first element
os.system("xdg-open " + htmlFiles[0])
while(i < j):
	#repeat the proccess for the remaining elements of the array
	temp = htmlFiles[i] 
	htmlFiles[i] = temp[1:] 
	os.system("xdg-open " + htmlFiles[i])
	i+=1
