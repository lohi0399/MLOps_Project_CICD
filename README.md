# MLOps_Project_CICD

Step 1:

1. Set up the github repository
 
 (a) New environment (venv) -- use python -m venv .venv in the cmd and activate it using .\.venv\Scripts\activate (in windows) -- This helps us in freezing all the libraries which I will be using for this particular project
 --Add a gitingore file manually or from the repo itself in the browser

 (b) Setup.py -- This is important if you want to make you code into a package which can be install using pip, and can be hosted or deployed on python pypi. We can use this package in other projects.

 -- For setup.py to identify packages in my project,we need to create a folder called src within which a file names __init__.py needs to be made. Now whenever the find_packages() function is running (within setup.py) then it automatically checks to see if how many __init__.py files are there anywhere within my project and will try to build it. It basically consideres thwe src fodler as a package and hence we can run src (__init__.py) as a package and use it (if hosted on pypi).

 (c) requirements.txt -- As 100's of dependencies are needed and it is not feasible to mention everything within the setup.py file. Here it is important to note that to tie setup.py to requirements we need to write "-e ." in this file, so that the setup file can directly be run when we call 'pip install requirement.txt'. (Also handle removing this -e . in the setup files while this reads all libraries) -- run this using pip install -r requirements.txt ( You can see that mlproject.egg-info is created meaning setup.py is run, You can now everything in the package would be run from __init__.py)

 NOTE: All this process file making and defining process can be automated by make a simple template.py script, but the point of making it from scracth is for beginner to understanf what each file does

 2. Logging and Exception Handling
 
 (a) Create a folder called component in src and create a __init__.py under. This means compoent can also be exported as a package and hence can also be imported to someother file location. (This component may be handling extracting data from other databases and using it or ingesting it in our project) So within this I create:
 
 -- data ingestion.py : for reading data , making train and test etc..
 -- data transformation.py : hot one encoding, converting numerical to categoirical etc..
 -- model_trainer.py : training the model and checking accuracy (r2 etc..)
 -- model_pusher.py: pushing the model.pkl file into the cloud

 (b) Create a folder called pipeline within src. This is need so that we have a defined training and prediction pipeline. 

 -- train_pipeline.py : From the training pipeline I will try to call the data ingestion, transfomation etc..
 -- prediction_pipeline.py : for new data

 (c) Adding three files logger.py,utils.py and exception.py for handling my project bugs, dependencies and errors.

 -- exception.py
 -- logger.py

 So whenver I get an excpetion I will get the error from exception.py and then log it using logger.py

