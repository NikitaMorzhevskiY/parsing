from unittest.mock import patch
from utils.func import split_carver_name_descr

@patch("utils.func.carvers")
def test_with_mock_carvers(mock_carvers):
    mock_carvers.TEST = {
        "шина": {
            "Наименование": "Шаблон для наименования",
            "Описание": "Шаблон для описания"
        }
    }

    column = ["Шинакшинав"]
    result = split_carver_name_descr(column)

    assert result["Наименование"] == ["Шаблон для наименования"]
    assert result["Описание"] == ["Шаблон для описания"]