from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    HYPEN_E_DOT='-e .'
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements] # readline adds "enter" esacpe sequence at last so replacing it
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Abhideep',
    author_email='workingabhideep@gmail.com',
    packages=find_packages(), # will go in folders and check in how many dir you have __init__.py and would execute it and will consider dir as a module
    install_requires=get_requirements('requirement.txt')
)