### Basic command 

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
