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
					Migrate:	python3 run.py migrate
					Run with just build and up:
						python3 run.py

Last edited by:	Eric Zair
Last edited on:	02/28/2019
'''
from os import system
import sys


def main():
	# Always run a build before doing anything.
	system("sudo docker-compose build")

	# Add the ability to migrate through the run.py file
	# Command:
	#		python3 run.py migrate
	if (sys.argv != 1) and (str(sys.argv[1]) == 'migrate'):
		system("sudo docker-compose run web python3 manage.py migrate")
	
	# run after script in all cases.
	system("sudo docker-compose up")

# end program	
if __name__=="__main__":
	main()