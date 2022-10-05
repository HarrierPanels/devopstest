DevOps Essentials Quizz!

There are 2 files that you have to place in the same directory: epamtest.py & questions.toml
 
You can run the script from shell (Python virtual environment activated) as follows: 

    python -m epamtest  

It was tested on Python 3.6.8. Should work on older 3.x versions or above. The script uses the Tomli library and emoji module that you have to install via pip into your virtual environment. Please refer to Roman's tutorial from Python Essentials.

    python -m venv test       # creates a virtual environment test
    source test/bin/activate  # activates it 
    pip install tomli         # installs tomli
    pip install emoji         # installs emoji
