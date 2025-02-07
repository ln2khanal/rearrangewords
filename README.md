# Drag and Drop Game
This easy-to-play puzzle game is for children with basic knowledge of things around them.
# Installation and Initialization:
A minimal computer or a PC can run this application, as no significant computations have been made in this game. Please follow the below steps to smoothly run this application on your system.
* Install Python on your machine.
* Create a virtual environment that does not conflict with your existing projects, if any. To do so, run the command `python3 -m venv .env`. Then, activate the virtual environment by executing `source .env/bin/activate`.
* Install the required Python packages. Run `pip install -r requirements`.
* Enter inside the project folder and run the flask server. Run `flask --app main run`. You should notice something similar to `* Running on http://127.0.0.1:5000`.
* Navigate to the link shown while running the flask app in the previous step.
* Make sure you have enabled JavaScript in your browser. Now, you should be able to play the puzzle.
* Try dragging an item from the column back to the original place and observe how the progress bar behaves.
* Please refer to the screenshots which contain two images of different progress stages.

# Clarification
* UI design has not yet been done.
* Authentication/Security while fetching data from the server has been ignored for now.
* The UI is not responsive because the application has been developed using Vanilla JavaScript and to make responsive it would take more time without modern JavaScript tools.
* I thought about having an audio feature for dictation that could be helpful for children with vision disabilities but couldn't implement it at the moment.
