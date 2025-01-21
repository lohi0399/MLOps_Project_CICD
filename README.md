# MLOps_Project_CICD

Step 1:

1. Set up the github repository
 (a) New environment (venv) -- use python -m venv .venv in the cmd and activate it using .\.venv\Scripts\activate (in windows) -- This helps us in freezing all the libraries which I will be using for this particular project
 --Add a gitingore file manually or from the repo itself in the browser
 
 (b) Setup.py -- This is important if you want to make you code into a package which can be install using pip, and can be hosted or deployed on python pypi. We can use this package in other projects.

 -- For setup.py to identify packages in my project,we need to create a folder called src within which a file names __init__.py needs to be made. Now whenever the find_packages() function is running (within setup.py) then it automatically checks to see if how many __init__.py files are there anywhere within my project and will try to build it. It basically consideres thwe src fodler as a package and hence we can run src (__init__.py) as a package and use it (if hosted on pypi).

 (c) requirements.txt -- As 100's of dependencies are needed and it is not feasible to mention everything within the setup.py file. Here it is important to note that to tie setup.py to requirements we need to write "-e ." in this file, so that the setup file can directly be run when we call 'pip install requirement.txt'. (Also handle removing this -e . in the setup files while this reads all libraries) -- run this using pip install -r requirements.txt ( You can see that mlproject.egg-info is created meaning setup.py is run, You can now everything in the package would be run from __init__.py)

 NOTE: All this process file making and defining process can be automated by make a simple template script, but the point of making it from scracth is for beginner to understanf what each file does

 
