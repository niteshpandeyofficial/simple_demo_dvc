Create new conda environment for this project using below commands.
```bash
conda activate -n <virtual_env_name>
```

Activate the created virtual environment
```bash
conda activate <virtual_env_name>
```

Create requirements file.
```bash
pip freeze >requirements.txt
```
or
```bash
touch requirements.txt
```

add the dependencies and install the dependencies
```bash
pip install -r requirements.txt
```

Git and dvc commands

```bash

git init
dvc init

dvc add data_given/winequality.csv
git commit -m "<msg_name>"

```
