from setuptools import setup, find_packages

setup(
    name='mindbank',
    version='0.1',
    description='A tool for recording and transcribing conversations',
    author='Matt Lamsey',  
    author_email='lamsey@gatech.edu',  
    url='http://github.com/mlamsey/mindbank',
    # package_dir={'': 'src'},  # specify the src directory
    packages=find_packages(where='src'),
    entry_points={
        'console_scripts': [
            'mindbank=mindbank.__main__:main',
        ],
    },
)