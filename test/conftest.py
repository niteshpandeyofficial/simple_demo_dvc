from msilib import schema
import yaml
import os
import json
import pytest


@pytest.fixture
def config(config_path='params.yaml'):
    with open(config_path) as yaml_file:
        config=config_path.safe_load(yaml_file)
    return config


@pytest.fixture
def schema_in(schema_path="schema_in.json"):
    with open(schema_path) as json_file:
        schema=json.load(json_file)
    return schema


