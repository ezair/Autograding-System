import shutil
import os
import webbrowser
from catalog.models import *
from submission_grader.models import *
import zipfile

# CURRENTLY: This is just a test script to see just how we
# can actually find locations of the testcases and stuff.


# get test case
test_case = TestCase.objects.all()[0]
test_case_location = test_case.get_abs_path()
print(test_case_location)

# get submission
submission = Submission.objects.all()[0]
submission_location = submission.files.path
print(submission_location)

# # create new dir
new_dir_name = "compiler/" + str(submission)
if not os.path.isdir(new_dir_name):
	os.mkdir(new_dir_name)

# # move to new dir && create gradle locations.
os.chdir(new_dir_name)
os.system("gradle init")
# We need to edit the build file, so that it has the correct dependencies.
with open('./build.gradle', 'w') as build_file:
	build_file.write("apply plugin: 'java'\n")
	build_file.write("repositories {\nmavenCentral()\n}\n")
	build_file.write("dependencies {\ntestCompile group: 'junit', name: 'junit', version: '4+'\n}")

os.mkdir("src/")
os.mkdir("src/main/")
os.mkdir("src/test/")
shutil.copy(submission_location, "./src/main/")
shutil.copy(test_case_location, "./src/test/")

# Unzip these bad bois
zip_file = zipfile.ZipFile("./src/main/" + submission.file_name(), 'r')
zip_file.extractall('./src/main/')
zip_file = zipfile.ZipFile("./src/test/" + test_case.file_name(), 'r')
zip_file.extractall('./src/test/')
zip_file.close()

#...let's run this son of a gun.
print(os.listdir('.'))
os.system("gradle build")
os.chdir("/")
os.system("gradle build")		