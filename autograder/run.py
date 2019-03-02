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
					Run with docker down (will run docker down before anything else):
						python3 run.py down
Last edited by:	Eric Zair
Last edited on:	03/01/2019
'''
from os import system
import sys


def main():
	# run docker down (if give down as an argument), then close program.
	if 'down'.strip() in sys.argv:
		system("sudo docker-compose down")

	# ALWAYS run a build before doing anything, no matter what.
	system("sudo docker-compose build")

	# migrate command.
	if 'migrate'.strip() in sys.argv:
		system("sudo docker-compose run web python3 manage.py migrate")

	# run after script, no matter what.
	system("sudo docker-compose up")

# end program	
if __name__=="__main__":
	main()