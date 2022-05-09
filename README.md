### Basic command 
 Tools used in this project
```
dvc
git
tox
pytest
```

Create new conda environment commands.
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

Add the dependencies and install the dependencies
```bash
pip install -r requirements.txt
```

Git and dvc commands

```bash
git init
git add .
git commit -m "<msg_name>"

dvc init
dvc add data_given/winequality.csv
git push origin main
```

Some DVC commands to check the details
```bash
dvc params diff
dvc metrics show
dvc metrics diff
```

setup commands
```bash
pip install -e .
```

Tox commands
```bash
tox
```
Tox rebuild commands
```bash
tox -r
```
Pytest command
```bash
pytest -v
```
build your own package command
```bash
python setup.py sdist bdist_wheel
```



ML Flow Commands

Create Artifacts
```bash
mkdir artifacts
```

mlflow server command 
```bash
mlflow server \
    --backend-store-uri sqlite:///mlflow.db \
    --default-artifact-root ./artifacts \
    --host 0.0.0.0 -p 1234
```
