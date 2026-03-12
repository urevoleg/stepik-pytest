import pytest
import sys

from src.calculator import add, divide


@pytest.mark.smoke
def test_add():
    """
    :return: result of testing
    """
    assert add(2, 3) == 5


@pytest.mark.regression
def test_add_raises_type_error_on_string_input():
    with pytest.raises(TypeError):
        add(3, "hello")


@pytest.mark.regression
def test_divide_by_zero_raises_value_error_with_message():
    with pytest.raises(ValueError) as excinfo:
        divide(3, 0)

    assert "Нельзя делить на ноль" in str(excinfo.value)

@pytest.mark.smoke
@pytest.mark.parametrize("a, b, expected", (
    pytest.param(1, 1, 1, id="divide one by one"),
    pytest.param(7, 1, 7, id="divide by one"),
    pytest.param(4, 2, 2, id="even_int2int"),
    pytest.param(7, 2, 3.5, id="noneven_int2int"),
    pytest.param(10.5, 2, 5.25, id="float2int"),
    pytest.param(21.3, 3, 7.1, id="float2float"),
))
def test_divide(a, b, expected):
    assert divide(a, b) == pytest.approx(expected)


@pytest.mark.slow
def test_very_slow_calculation():
    """Гипотетический тест, который работает очень долго."""
    # для примера просто сделаем его успешным
    assert True


@pytest.mark.skip(reason="Эта функциональность будет реализована в версии 2.0")
def test_substraction():
    """Тест для будущей функции вычитания."""
    # assert subtract(10, 5) == 5
    pass

@pytest.mark.skipif(condition=sys.version_info < (3, 17), reason="Для теста требуется Python версии 3.17+")
def test_new_python_feature():
    """Тест, использующий синтаксис, доступный только в новых версиях Python."""
    # Пример использования match-case, который появился в 3.10
    result = 0
    match 1:
        case 1:
            result = 1
    assert result == 1


@pytest.mark.xfail(reason="Известный баг с точностью float, будет исправлен в #TICKET-123")
def test_add_floats_bug():
    # Этот тест будет падать из-за особенностей представления float в Python
    assert add(0.1, 0.2) == 0.3

    # Используем три аргумента: два для входа, один для ожидания


@pytest.mark.parametrize("a, b, expected", [
    # 1. Тест-кейс: Положительные числа
    pytest.param(1, 2, 3, id="positive"),

    # 2. Тест-кейс: Отрицательные числа
    pytest.param(-5, -3, -8, id="negative"),

    # 3. Тест-кейс: Смешанные знаки
    pytest.param(-10, 5, -5, id="complex"),

    # 4. Тест-кейс: Сложение с нулем
    pytest.param(100, 0, 100, id="zero add"),

    # 5. Тест-кейс: Дробные числа (float)
    pytest.param(0.1, 0.2, 0.3, id="float")
])
def test_add_parametrized(a, b, expected):
    """
    Проверяет функцию add на различных наборах данных
    с помощью параметризации.
    """
    # Мы используем approx для сравнения float, чтобы избежать проблем с точностью
    assert add(a, b) == pytest.approx(expected)