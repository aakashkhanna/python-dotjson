from io import StringIO
import os
from pydantic import BaseModel
from typing import List
from dotjson.main import (
    find_json_path,
    load_dotjson,
    model_dotjson,
    dict_dotjson,
    DotJson,
)

settings_content = '{"apple":1,"mango":5,"fruit":{"units":["kg","pound"]}}'
os.chdir("/project/tests/sample-settings")


def test_find_json_path():
    path = find_json_path()
    assert path is not None


def test_load_dotjson():
    load_dotjson()
    assert os.environ["apple"] == "1"
    assert os.environ["mango"] == "5"
    assert os.environ["fruit__units__0"] == "kg"
    assert os.environ["fruit__units__1"] == "pound"


def test_dict_dotjson():
    dict_output = dict_dotjson()
    assert dict_output["apple"] == 1
    assert dict_output["mango"] == 5
    assert dict_output["fruit"]["units"][0] == "kg"
    assert dict_output["fruit"]["units"][1] == "pound"


def test_model_dotjson():
    class fruit_model(BaseModel):
        units: List[str]

    class settings_model(BaseModel):
        apple: int
        mango: int
        fruit: fruit_model

    model_output = model_dotjson(settings_model)
    assert model_output.apple == 1
    assert model_output.mango == 5
    assert model_output.fruit.units[0] == "kg"
    assert model_output.fruit.units[1] == "pound"


def test_load_dotjson_with_jsonpath():
    load_dotjson(json_path="settings.json")
    assert os.environ["apple"] == "1"
    assert os.environ["mango"] == "5"
    assert os.environ["fruit__units__0"] == "kg"
    assert os.environ["fruit__units__1"] == "pound"


def test_dict_dotjson_with_jsonpath():
    dict_output = dict_dotjson(json_path="settings.json")
    assert dict_output["apple"] == 1
    assert dict_output["mango"] == 5
    assert dict_output["fruit"]["units"][0] == "kg"
    assert dict_output["fruit"]["units"][1] == "pound"


def test_model_dotjson_with_jsonpath():
    class fruit_model(BaseModel):
        units: List[str]

    class settings_model(BaseModel):
        apple: int
        mango: int
        fruit: fruit_model

    model_output = model_dotjson(settings_model, json_path="settings.json")
    assert model_output.apple == 1
    assert model_output.mango == 5
    assert model_output.fruit.units[0] == "kg"
    assert model_output.fruit.units[1] == "pound"


def test_load_dotjson_with_stream():
    load_dotjson(stream=StringIO(settings_content))
    assert os.environ["apple"] == "1"
    assert os.environ["mango"] == "5"
    assert os.environ["fruit__units__0"] == "kg"
    assert os.environ["fruit__units__1"] == "pound"


def test_dict_dotjson_with_stream():
    dict_output = dict_dotjson(stream=StringIO(settings_content))
    assert dict_output["apple"] == 1
    assert dict_output["mango"] == 5
    assert dict_output["fruit"]["units"][0] == "kg"
    assert dict_output["fruit"]["units"][1] == "pound"


def test_model_dotjson_with_stream():
    class fruit_model(BaseModel):
        units: List[str]

    class settings_model(BaseModel):
        apple: int
        mango: int
        fruit: fruit_model

    model_output = model_dotjson(
        settings_model, stream=StringIO(settings_content)
    )
    assert model_output.apple == 1
    assert model_output.mango == 5
    assert model_output.fruit.units[0] == "kg"
    assert model_output.fruit.units[1] == "pound"


def test_load_dotjson_with_pathlist():
    settings_paths = ["settings.json", "settings.dev.json"]
    load_dotjson(json_paths_list=settings_paths)
    assert os.environ["apple"] == "2"
    assert os.environ["mango"] == "5"
    assert os.environ["fruit__units__0"] == "kg"
    assert os.environ["fruit__units__1"] == "pound"
    assert os.environ["fruit__units__2"] == "grams"


def test_dict_dotjson_with_pathlist():
    settings_paths = ["settings.json", "settings.dev.json"]
    dict_output = dict_dotjson(json_paths_list=settings_paths)
    assert dict_output["apple"] == 2
    assert dict_output["mango"] == 5
    assert dict_output["fruit"]["units"][0] == "kg"
    assert dict_output["fruit"]["units"][1] == "pound"
    assert dict_output["fruit"]["units"][2] == "grams"


def test_model_dotjson_with_pathlist():
    class fruit_model(BaseModel):
        units: List[str]

    class settings_model(BaseModel):
        apple: int
        mango: int
        fruit: fruit_model

    settings_paths = ["settings.json", "settings.dev.json"]
    model_output = model_dotjson(settings_model, json_paths_list=settings_paths)
    assert model_output.apple == 2
    assert model_output.mango == 5
    assert model_output.fruit.units[0] == "kg"
    assert model_output.fruit.units[1] == "pound"
    assert model_output.fruit.units[2] == "grams"


def test_to_dict():
    dotjson = DotJson(None, None, None)
    dict_output = dotjson.to_dict()
    assert dict_output["apple"] == 1
    assert dict_output["mango"] == 5
    assert dict_output["fruit"]["units"][0] == "kg"
    assert dict_output["fruit"]["units"][1] == "pound"


def test_flattened_json_dict():
    dotjson = DotJson(None, None, None)
    dict_output = dotjson.to_flattened_json_dict()
    assert dict_output["apple"] == 1
    assert dict_output["mango"] == 5
    assert dict_output["fruit__units__0"] == "kg"
    assert dict_output["fruit__units__1"] == "pound"


def test_to_envvars():
    dotjson = DotJson(None, None, None)
    dotjson.to_envvars()
    assert os.environ["apple"] == "1"
    assert os.environ["mango"] == "5"
    assert os.environ["fruit__units__0"] == "kg"
    assert os.environ["fruit__units__1"] == "pound"


def test_to_model():
    dotjson = DotJson(None, None, None)

    class fruit_model(BaseModel):
        units: List[str]

    class settings_model(BaseModel):
        apple: int
        mango: int
        fruit: fruit_model

    model_output = dotjson.to_model(settings_model)
    assert model_output.apple == 1
    assert model_output.mango == 5
    assert model_output.fruit.units[0] == "kg"
    assert model_output.fruit.units[1] == "pound"


def test_to_dict_with_jsonpath():
    dotjson = DotJson("settings.json", None, None)
    dict_output = dotjson.to_dict()
    assert dict_output["apple"] == 1
    assert dict_output["mango"] == 5
    assert dict_output["fruit"]["units"][0] == "kg"
    assert dict_output["fruit"]["units"][1] == "pound"


def test_flattened_json_dict_with_jsonpath():
    dotjson = DotJson("settings.json", None, None)
    dict_output = dotjson.to_flattened_json_dict()
    assert dict_output["apple"] == 1
    assert dict_output["mango"] == 5
    assert dict_output["fruit__units__0"] == "kg"
    assert dict_output["fruit__units__1"] == "pound"


def test_to_envvars_with_jsonpath():
    dotjson = DotJson("settings.json", None, None)
    dotjson.to_envvars()
    assert os.environ["apple"] == "1"
    assert os.environ["mango"] == "5"
    assert os.environ["fruit__units__0"] == "kg"
    assert os.environ["fruit__units__1"] == "pound"


def test_to_model_with_jsonpath():
    dotjson = DotJson("settings.json", None, None)

    class fruit_model(BaseModel):
        units: List[str]

    class settings_model(BaseModel):
        apple: int
        mango: int
        fruit: fruit_model

    model_output = dotjson.to_model(settings_model)
    assert model_output.apple == 1
    assert model_output.mango == 5
    assert model_output.fruit.units[0] == "kg"
    assert model_output.fruit.units[1] == "pound"


def test_to_dict_with_stream():
    dotjson = DotJson(None, StringIO(settings_content), None)
    dict_output = dotjson.to_dict()
    assert dict_output["apple"] == 1
    assert dict_output["mango"] == 5
    assert dict_output["fruit"]["units"][0] == "kg"
    assert dict_output["fruit"]["units"][1] == "pound"


def test_flattened_json_dict_with_stream():
    dotjson = DotJson(None, StringIO(settings_content), None)
    dict_output = dotjson.to_flattened_json_dict()
    assert dict_output["apple"] == 1
    assert dict_output["mango"] == 5
    assert dict_output["fruit__units__0"] == "kg"
    assert dict_output["fruit__units__1"] == "pound"


def test_to_envvars_with_stream():
    dotjson = DotJson(None, StringIO(settings_content), None)
    dotjson.to_envvars()
    assert os.environ["apple"] == "1"
    assert os.environ["mango"] == "5"
    assert os.environ["fruit__units__0"] == "kg"
    assert os.environ["fruit__units__1"] == "pound"


def test_to_model_with_stream():
    dotjson = DotJson(None, StringIO(settings_content), None)

    class fruit_model(BaseModel):
        units: List[str]

    class settings_model(BaseModel):
        apple: int
        mango: int
        fruit: fruit_model

    model_output = dotjson.to_model(settings_model)
    assert model_output.apple == 1
    assert model_output.mango == 5
    assert model_output.fruit.units[0] == "kg"
    assert model_output.fruit.units[1] == "pound"


def test_to_dict_with_pathlist():
    settings_paths = ["settings.json", "settings.dev.json"]
    dotjson = DotJson(None, None, settings_paths)
    dict_output = dotjson.to_dict()
    assert dict_output["apple"] == 2
    assert dict_output["mango"] == 5
    assert dict_output["fruit"]["units"][0] == "kg"
    assert dict_output["fruit"]["units"][1] == "pound"
    assert dict_output["fruit"]["units"][2] == "grams"


def test_flattened_json_dict_with_pathlist():
    settings_paths = ["settings.json", "settings.dev.json"]
    dotjson = DotJson(None, None, settings_paths)
    dict_output = dotjson.to_flattened_json_dict()
    assert dict_output["apple"] == 2
    assert dict_output["mango"] == 5
    assert dict_output["fruit__units__0"] == "kg"
    assert dict_output["fruit__units__1"] == "pound"
    assert dict_output["fruit__units__2"] == "grams"


def test_to_envvars_with_pathlist():
    settings_paths = ["settings.json", "settings.dev.json"]
    dotjson = DotJson(None, None, settings_paths)
    dotjson.to_envvars()
    assert os.environ["apple"] == "2"
    assert os.environ["mango"] == "5"
    assert os.environ["fruit__units__0"] == "kg"
    assert os.environ["fruit__units__1"] == "pound"
    assert os.environ["fruit__units__2"] == "grams"


def test_to_model_with_pathlist():
    settings_paths = ["settings.json", "settings.dev.json"]
    dotjson = DotJson(None, None, settings_paths)

    class fruit_model(BaseModel):
        units: List[str]

    class settings_model(BaseModel):
        apple: int
        mango: int
        fruit: fruit_model

    model_output = dotjson.to_model(settings_model)
    assert model_output.apple == 2
    assert model_output.mango == 5
    assert model_output.fruit.units[0] == "kg"
    assert model_output.fruit.units[1] == "pound"
    assert model_output.fruit.units[2] == "grams"
