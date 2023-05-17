import json
from datetime import datetime

with open("operations.json", encoding='utf-8') as my_json:
    json_load = json.load(my_json)
    new_json = []
    for item in json_load:
        if item != {}:
            new_json.append(item)


def executed_json():
    executed = []
    for item in new_json:
        if item["state"] == "EXECUTED":
            executed.append(item)
    return executed

def date_maker():
    for item in executed_json():
        datetime_str = item["date"][:19]
        datetime_object = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S")
        item['date'] = datetime_object
    return executed_json()


def last_operations():
    for item in executed_json()[1:5]:
        datetime_str = item["date"][:19]
        datetime_object = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S")
        print(
            f'{datetime_object}: {item["description"]} \n {item.get("from")} -> {item.get("to")}\n {item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]}')

last_operations()