from setuptools import setup, find_packages

from typing import List
def get_requirements(file_path:str)->List[str]:
    '''this function will return the list of requirements
    '''
    with open(file_path) as file_obj:
        requiremants = file_obj.readlines()
        requiremants = [req.replace("\n","") for req in requiremants]

        if "-e ." in requiremants:
            requiremants.remove("-e .")
    return requiremants

setup(
    name="ml_project",
    version="0.0.1",
    author="sairam parasa",
    author_email="parasasairam2@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)