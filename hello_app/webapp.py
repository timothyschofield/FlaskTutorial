"""
Entry point for the application.

Make sure the Python virtual enviroment is running 
	.venv\Scripts\activate
If .venv is running you should see a green (.venv) to the left of the prompt in the Terminal

To run this app outside of the VS Code debugger, 
    use the following steps in the terminal:

	I am using Powershell as the Terminal so...

	1) $env:FLASK_APP="webapp"
	2) In the terminal, navigate to the hello_app folder and launch the program using
		python -m flask run

"""
from . import app    # For application discovery by the 'flask' command.
from . import views  # For import side-effects of setting up routes.