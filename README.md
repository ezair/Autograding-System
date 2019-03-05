Some notes on running our docker:
	
	You can run our project by using the run.py script (located in the autograder/ folder next to manage.py).

	NOTE:
		If using run.py, you may have to get rid of the sudo commands (if you are on windows or any machine that you do not have sudo access to).

		If you do have sudo access, then this will not be a problem.

		The script has instructions as to how it works.

Important note:
	All commands stated may need to be run with sudo, varying on your computer and operating system.

Before doing anything, you want to run "docker-compose-build" so that you can make any needed install changes that are required.

Then you can simply type "docker-compose up" to begin running the project's web server.

To make migrations , simply type "docker-compose run web python3 manage.py migrate"

To sign into admin page, Username: "Admin", Password: "Admin"

Varying on your computer, you may have to put sudo in front of the command.


For testinging admin:
	username: admin
	password: testtest