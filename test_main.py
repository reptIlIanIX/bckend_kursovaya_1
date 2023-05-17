from main import executed_json
import json

with open("operations.json.", encoding='utf-8') as my_json:
    json_load = json.load(my_json)
    new_json = []
    for item in json_load:
        if item != {}:
            new_json.append(item)


def test_executed_json():
    assert executed_json()[1]['id'] == 41428829
    assert executed_json()[7]['date'] == "2019-07-12T20:41:47.882230"

