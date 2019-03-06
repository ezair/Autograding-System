'''
Created by:	Eric Zair
File: run.py
Description:	This file is just a quick script to allow people
				to quickly run their docker project instead of typing
				in LONG manual commands.
				NOTE:
					This file is python3 NOT python2
					Thus, it should be run as "python3 run.py arg"

				List of things you can do from this file:					
					Run with just build and up:
						python3 run.py

					Run migrations with:
						python3 run.py migrate
					
					Run with docker down (will run docker down before anything else):
						python3 run.py down
					
					Run ALL tests with:
						python3 run.py test
					
					Run build, down, and migrate:
						python3 run.py down migrate (will always run down first) even if
													 you do "python3 run.py migrate down")
Last edited by:	Eric Zair
Last edited on:	03/05/2019
'''
import os
import sys
from os import system


#_______________________________________________________________________
def main():
	
	# Allows us to run a docker-compose down.
	if 'down'.strip() in sys.argv:
		system("sudo docker-compose down")

	# ALWAYS run a build before doing anything, no matter what.
	system("sudo docker-compose build")

	# Allows us to run a docker-compose down
	if 'migrate'.strip() in sys.argv:
		system("sudo docker-compose run web python3 manage.py migrate")

	# Allows us to run ALL tests.
	if 'test'.strip() in sys.argv:
		system("sudo docker-compose run web python3 manage.py test")

	# Run after script, no matter what.
	# We are simply starting the server here.
	system("sudo docker-compose up")

# end program	
if __name__=="__main__":
	main()