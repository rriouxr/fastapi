from setuptools import setup, find_packages

setup(
    name='fastapi',
    version='0.1.0',
    packages=find_packages(),
    install_requires = [
    'click == 7.1.2',
    'fastapi == 0.63.0',
    'h11 == 0.12.0',
    'pydantic == 1.7.3',
    'starlette == 0.13.6',
    'uvicorn == 0.13.3'
    ]
)