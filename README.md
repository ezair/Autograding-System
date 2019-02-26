Important note:
	All commands stated may need to be run with sudo, varying on your computer and operating system.

Before doing anything, you want to run "docker-compose-build" so that you can make any needed install changes that are required.

Then you can simply type "docker-compose up" to begin running the project's web server.

To make migrations , simply type "docker-compose run web python3 manage.py migrate"

To sign into admin page, Username: "Admin", Password: "Admin"

Varying on your computer, you may have to put sudo in front of the command.