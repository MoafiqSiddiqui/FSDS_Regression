from setuptools import find_packages, setup
from typing import List

HYPEN_E_Dot='-e .'

def get_req(file_path:str)->List[str]:
    req = []
    with open(file_path) as file_obj:
        req = file_obj.readlines()
        req = [r.replace("\n","") for r in req]

        if HYPEN_E_Dot in req:
            req.remove(HYPEN_E_Dot)

    return req

setup(
    name='RegressorProject',
    version='0.0.1',
    author='Moafiq',
    author_email='moafiqsiddiqui@gmail.com',
    install_requires=get_req('requirements.txt'),
    packages=find_packages()
)
