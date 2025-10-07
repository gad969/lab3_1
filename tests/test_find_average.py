from src import my_lib
import pytest

# Тест функции находящей среднее значение списка чисел
class TestFindAverage:

    def test_on_correct(self): # Тест на корректных значениях
        assert my_lib.find_average([1, 2, 3, 4, 5]) == 3.0

    def test_on_str(self): # Тест на некорректных значения, где вместо чисел функции передается масси букв
        with pytest.raises(TypeError):
            assert my_lib.find_average(['a', 'b', 'c'])
