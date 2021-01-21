# Install the Project

1. Download the zip project or clone the git project
```
git clone https://github.com/rmontesleo/basic_dao_layer.git
```

1. Go the basic_dao_layer
```
cd basic_dao_layer
```

1. Create or activate your virtual environment with pipenv
```
pipenv shell
```

1. After create/activate the virtual environment you must see in the at the beginin of the prompt (basic_dao_layer). That means the virtual environment is activated.

1. With your environment activated, next step is install the project dependencies. In this case we have a Pipfile.lock file, it contains the dependencies. Only run the install command. Without more parameters pipenv takes the Pipfile.lock file to install the required dependencies.
```
pipenv install
```

1. In case you need to install an additional dependency  use pipen install and the name of your required dependency.
```
pipenv install <depencenciy_name>
```
exmple

```
pipenv install python-dotenv
```

1. Run python in the virtual environment, check the version. **IMPORTANT** in your virtual environment use python not python3
```
python --version
```

1. Run the hello world program in the main.py file in the root of the project
```
python main.py
```
