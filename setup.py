from setuptools import find_packages, setup

setup(
    description='Polish Case Trainer',
    author='Thomas Busby',
    url='https://github.com/tombusby/PolishCaseTrainer',
    download_url='https://github.com/tombusby/PolishCaseTrainer',
    author_email='tom@busby.ninja',
    version='0.1',
    install_requires=['inquirer'],
    packages=find_packages(exclude=['tests']),
    data_files=[('polish_case_trainer/word-data', [
        'polish_case_trainer/word-data/nouns.json',
        'polish_case_trainer/word-data/adjectives.json'
    ])],
    name='polish_case_trainer',
    entry_points={
        'console_scripts': [
            'polish_case_trainer=polish_case_trainer.polish_case_trainer:main',
        ],
    },
)
