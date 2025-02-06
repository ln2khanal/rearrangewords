# Drag and Drop Game
This easy to play puzzle game is for children who has a basic knowledge of things around them.
# Installation and Initialization:
A minimal computer or a PC can be used to run this application as there has not been any significant computations done in this game. Please follow the below steps smoothly run this application in you system.
* Install Python in your machine.
* Create a virtual environment not to conflict with your existing projects if any. To do so run the following command `python3 -m venv .env`. And activate the virtual environment bye executing this `source .env/bin/activate`.
* Install the required python packages. Run `pip install -r requirements`.
* Enter inside the project folder and run the flask server. Run `flask --app main run`. You should notice something similar to `* Running on http://127.0.0.1:5000`.
* Navigate to the link shown while running the flask app in previous step.
* Make sure you have enabled JavaScript in your browser. Now, you should be able to play the puzzle.
* Try dragging an item from the column back to the original place and observe how the progress bar behave.
* Please refer to the screenshots which contains two images of different progress stages.

# Clarification
* UI Design has not been done yet. But in the final product, there will be proper design with possibilities of minimal animations.
* Authentication/Security while fetching data from server has been ignored for now.
* The UI is not responsive because the application has been developed using venilla JavaScript and to make responsive it would take more time without modern JavaScript tools.
* I really thought about having audio feature for dictation that could be helpful for children with vision disabilities but couldn't implement it at the moment.