import json, os
from datetime import datetime

p = os.path.abspath('operations.json')


def get_data():
    with open(p, encoding='utf-8') as my_json:
        json_load = json.load(my_json)
    return json_load


data = get_data()


def get_filtered_data(data, filter_empty_from=False):
    data = [x for x in data if "state" in x and x["state"] == "EXECUTED"]
    if filter_empty_from:
        data = [x for x in data if "from" in x]
    return data


data_sorted = sorted(get_filtered_data(data), key=lambda x: x["date"], reverse=True)


def card_hider():
    for item in get_filtered_data(data):
        if 'from' in item:
            from_item = item.get('from').split()
            removed_numbers = from_item.pop(-1)
            sender = ' '.join(from_item)
        return (f'{sender} {removed_numbers[0:4]} {removed_numbers[4:6]}** **** {removed_numbers[12:16]}')


def last_operations():
    for item in data_sorted[1:5]:
        datetime_str = item["date"][:19]
        datetime_object = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S")
        print(
            f'{datetime_object}: {item["description"]} \n {card_hider()} -> {item.get("to")[0:4]} **{item.get("to")[5:9]}\n {item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]}')


last_operations()
