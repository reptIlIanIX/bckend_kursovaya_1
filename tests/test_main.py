from main import get_filtered_data, data, get_data, card_hider, last_operations


def test_get_json():
    assert type(get_data()) == list


def test_get_filtered_data():
    assert get_filtered_data(data)[1]['id'] == 41428829
    assert get_filtered_data(data)[7]['date'] == "2019-07-12T20:41:47.882230"
    for item in get_filtered_data(data, filter_empty_from=True):
        if "from" in item:
            assert True


def test_card_hider():
    assert card_hider()[18:20] == '**'


def test_last_operations():
    assert type(last_operations()) != str or int or bool
    assert last_operations() == None
