import pytest
import json
import os
from unittest import mock


import src.utils as utils


def test_load_products_success():
    file_content = '[{"name": "Product1", "price": 100}]'
    expected_result = [{"name": "Product1", "price": 100}]
    filename = 'testfile.json'

    with mock.patch('builtins.open', mock.mock_open(read_data=file_content)) as mocked_file:
        result = utils.load_products(filename)
        mocked_file.assert_called_once_with(os.path.join("src/data", filename))

        assert result == expected_result


def test_load_products_file_not_found():
    filename = 'non_existent.json'

    with pytest.raises(FileNotFoundError):
        with mock.patch('builtins.open', side_effect=FileNotFoundError):
            utils.load_products(filename)


def test_load_products_json_decode_error():
    filename = 'bad_json.json'

    file_content = '{"name": "Product1", "price": 100'

    with pytest.raises(json.decoder.JSONDecodeError):
        with mock.patch('builtins.open', mock.mock_open(read_data=file_content)):
            utils.load_products(filename)
