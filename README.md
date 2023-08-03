# Software Architecture

## Model-View-Controller

MVC archtecture seperates the application into 3 logical units, Model, View, Controller.
User of the application interact with View and trigger events.
Controller respond to the event created by the View.
Model is the logical component which directly manages and manipulates the data and handles the application logic.

### How to run the application

Run the controller.py in `pattern_name/MVC/server` in a terminal. Open another terminal and run the App.py in `pattern_name/MVC/client`

Working alternative repository: https://github.com/KabilanMA/Model-View-Controller.git

-------------

dependencies:
- flask<br>
- flask-sqlalchemy<br>
- sqlalchemy<br>
- requests<br>
- pytest : For testing coverage report <br>
