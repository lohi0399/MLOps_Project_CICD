from setuptools import find_packages,setup # This can be used to directly fgind all the packages which are being used in our application
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(file_path) -> List[str]:
    # This function will return a list of requirements which will be needed to be given in install_requires.

    requirements = []
    with open('requirements.txt') as file_obj:
        requirements = file_obj.readlines() # This will also add a new line character at the end of each line and hence needs to be removed
        requirements = [req.replace("\n"," ") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

# This can be thought of the metadata (i.e the data explaining other data) for this project
setup(

name='mlproject',
version= '0.0.1',
author='Lohit',
author_email='lohit0399@gmail.com',
packages=find_packages(),
# install_requires=['pandas','numpy','seaborn'] --> Not feasible
install_requires = get_requirements('requirements.txt')

)