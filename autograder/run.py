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
					Run build, down, and migrate:
						python3 run.py down migrate (will always run down first) even if
													 you do "python3 run.py migrate down")
Last edited by:	Eric Zair
Last edited on:	03/02/2019
'''
import socket
import time
import os
import sys
from os import system


'''
	Purpose:	This method is here to ensure that our db service (postgres server)
				runs before our web service (django server), because the web service
				relies on the db service.

	Why this is important:	If the web service were to run first, it would not be able
							to connect to the db service, and as a result, it will throw
							an exception and not allow us to connect to the postgres server.
							NOTE:
								This function makes sure this issue does NOT happen.
'''
def wait_for_db():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Keep trying to connect to the postgres database, until
	# we are finally able to connect.
	# After that, we can just close our connection.
	while True:
		# Connect to the postgres server, so that we can see if it is
		# currently running.
		# 		IMPORTANT NOTE:
		#			The port MUST match the one in "settings.py" file.
		#			...basically, we should never change it, or it will be an issue.
		try:
			s.connect(('127.0.0.1', 5432))
			s.close()
			break
		# Server is not yet running, so we re-loop and try again.
		except socket.error as ex:
			print("Attemping to connect to postgres server")
			time.sleep(0.1)

#_______________________________________________________________________
def main():
	# postgres server must be running before the django server,
	wait_for_db()
	
	# Allows us to run a docker-compose down.
	if 'down'.strip() in sys.argv:
		system("sudo docker-compose down")

	# ALWAYS run a build before doing anything, no matter what.
	system("sudo docker-compose build")

	# Allows us to run a docker-compose down
	if 'migrate'.strip() in sys.argv:
		system("sudo docker-compose run web python3 manage.py migrate")

	# Run after script, no matter what.
	# We are simply starting the server here.
	system("sudo docker-compose up")

# end program	
if __name__=="__main__":
	main()