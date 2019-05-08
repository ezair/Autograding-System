import os.path, subprocess
from subprocess import STDOUT, PIPE, Popen

#file name minus java
testFile = "compiler/testHelloWorld"
studentFile = "\nhelloWorld.java"

#     "javac " + studentFile + ".java"
process = subprocess.Popen(['java ' + studentFile], stdout=subprocess.PIPE,  shell=True)
out, err = process.communicate()
print(out)
print("yeet")




'''
#compiles student to check if worked successfully
compileCheck = "javac " + studentFile + ".java"
compileCheck = os.system(compileCheck)

if compileCheck == 256:	
	print("Failed to compile on student")

#second versa same as the first
compileCheck = "javac " + testFile + ".java"
compileCheck = os.system(compileCheck)

#process = subprocess.Popen(['ls', '-a'], stdout=subprocess.PIPE)






#only difference minus name, mode goes into mode 1
mode = 0
if compileCheck == 256:	
	print("Failed to compile on teacher")

#mode one compils, runs, and gets input and compairs input of test and student
elif mode == 1:	
	#get test files again
	executeStudent = "javac " + studentFile + ".java;java " + studentFile
	executeTest = "javac " + testFile + ".java;java " + testFile

	#get output of the files
	#testOutput = subprocess.check_output(executeTest, shell = True) 
	studentOutput = subprocess.check_output(executeStudent, shell = True) 

	#simple compair print
	print(studentOutput.decode("utf-8") == testOutput.decode("utf-8")) 
	

# docker-compose run web java -cp compiler/ testHelloWorld






#below here is nonsense you don't have to worry about

elif mode == 2:
    #under development, unsure how to finalize this as of now
    #mode 2 is for parameters  java programName arg1 2 3 4....
    parameters = ["jasdkj", "as,jhdfasjhdf", "ajshdfjas"]

    executeTest = "javac " + testFile + ".java;java " + testFile
    


elif mode == 3:
    #currently only works on programs taking 1 input and only 1!
    executeStudent = "javac " + studentFile + ".java;java " + studentFile
    executeTest = "javac " + testFile + ".java;java " + testFile

    protoString = "zib"
    #encode is to turn it into a bytes like object
    protoList = protoString.encode()
    #this isnt used crashes before it could
    protoList += protoString.encode()
    
    
    testOutput = subprocess.check_output(executeTest, shell = True, input = protoList)
    
    
    #prints out the output of the entire program
    print(testOutput.decode("utf-8")) 
'''













