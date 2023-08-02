# CivilBot-WebScraping-Excel
"This repository contains Python scripts for the CivilBot project. The bot performs web scraping on a civil engineering website, extracts relevant data, and compiles the data into Excel files. It also includes a script to combine multiple Excel files into one."


# Installation
To install and run this project, you will need Python and several dependencies. After cloning the repository, you can install these dependencies with:

pip install -r requirements.txt
OR for anaconda users
conda activate myenv

# **NOTE**
Please note that while pip and conda are both package managers, they have some differences. pip is a package manager for Python and can install packages from the Python Package Index (PyPI). conda is a package manager for any software (not limited to Python) and can install packages from the Anaconda distribution and from the Conda package manager itself.

If you have a requirements.txt file and want to install it in a Conda environment, you can do so using pip within your Conda environment:
conda create --name myenv
conda activate myenv
pip install -r requirements.txt
This will create a new Conda environment, activate it, and then use pip to install the dependencies listed in your requirements.txt file.
# *REMINDER*
However, there are a few things to keep in mind:

1.Package Conflicts: If there are packages in your requirements.txt file that conflict with each other or with other packages already installed in the environment, you may encounter issues. This is true for any package management system, not just Conda.

2.Mixed Use of Conda and Pip: While Conda and Pip can be used together, it's generally recommended to use Conda when you're in a Conda environment if possible, as Conda is aware of and can manage dependencies between all the packages in the environment. Pip is not aware of Conda's packages. This can potentially lead to inconsistencies or conflicts.

3.Isolation of Environments: One of the main benefits of using environments (like with Conda) is that they're isolated. If something goes wrong in one environment, it shouldn't affect your other environments. You can simply delete the problematic environment and start again.

If you're concerned about potential issues, you might consider exporting your Conda environment's packages to a environment.yml file (using conda env export > environment.yml), which can be used to recreate the environment later if needed.


# Usage
To run the main script, use the following command:


-----Copy code-----
python workslaves.py

This will start the bot, which will begin scraping data and creating Excel files.

# Contributing
Contributions are welcome! Please fork this repository and open a pull request to add enhancements.

# License
This project is licensed under the MIT License.

Remember to replace the commands and instructions with what's applicable to your project.
