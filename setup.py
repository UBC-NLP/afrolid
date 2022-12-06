from afrolid.copyright import *
from setuptools import setup, find_packages

with open("README.rst", "r") as readme_file:
    readme = readme_file.read()

from setuptools import setup

setup(name='afrolid',
      version=version,
      description=description,
      long_description=readme,
      url='https://github.com/UBC-NLP/afrolid',
      author=author,
      author_email=email,
      license=license,
      packages=find_packages(),
      install_requires=[
          'tensorboardX==2.5.1',
          'regex',
          'torch==1.11.0',
          # 'protobuf',
          'sentencepiece==0.1.96',
          'fairseq==0.12.2',
          # 'pandas',
          'tqdm==4.63.0',
        ],
      entry_points={
            "console_scripts": [
                "afrolid_cli = afrolid.cli:afrolid_cli",
                # "turjuman_score = turjuman_cli.score:score_cli",
                # "afrolid_interactive = afrolid_cli.interactive:interactive_cli",
            ],
        },
      
      )
