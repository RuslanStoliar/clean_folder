from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.0.0',
    description='sorting files by appropriate folders',
    author='Stoliar Ruslan',
    author_email='Dozent10123@gmail.com',
    packages=find_namespace_packages(),
    install_requires=['markdown'],
    entry_points={'console_scripts': ['clean_folder= clean_folder.clean:path_function']}
)