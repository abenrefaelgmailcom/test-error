import time
import math
import pytest
import calculator

def test_calculator_add_small():
    # Arrange
    a: int = 2
    b: int = 5
    expected: int = 7

    # Act
    actual: int = calculator.add(a, b)

    # Assert
    assert expected == actual, "small numbers add"

# pip install pytest
# option 1- run the tests : play
# option 2- run the tests
#         in the Terminal : pytest .
# add test sub
# add test mul
# add test div


def test_calculator_add_power():
    a: int = 2
    b: int = 4
    expected: int = 16

    # Act
    actual: int = calculator.add(a, b)

    # Assert
    assert expected == actual, "small numbers add"

def test_calculator_add_square():
    a: int = 9
    #b: int = 4
    expected: int = 3

#d
def test_calculator_power():
    # Arrange
    a: int = 2
    b: int = 4
    expected: int = 16

    # Act
    actual: int = calculator.power(a, b)

    # Assert
    assert expected == actual, "Power function failed for small numbers"

#e
'''e. כמו בסעיף הקודם, בדוק בטסט שב - power עבור 3 ו- 2 חזר 9 )assert )
'''

def test_calculator_power():
    # Arrange
    a: int = 3
    b: int = 2
    expected: int = 9

    # Act
    actual: int = calculator.power(a, b)

    # Assert
    assert expected == actual, "Power function failed for 3^2"

#f
'''f. בדוק בטסט שב- sqrt עבור 25 חזר 5 )השתמש ב assert )'''

def test_calculator_sqrt():
    # Arrange
    a: int = 25
    expected: int = 5

    # Act
    actual: int = calculator.sqrt(a)

    # Assert
    assert expected == actual, "sqrt function failed for sqrt(25)"

#g
'''בדוק בטסט שב- sqrt עבור מינוס 5 התרחשה שגיא ה מסוג ValueError
רמז: (ValueError(raises.pytest with( ראה קוד מהשיעור('''

def test_calculator_sqrt_negative():
    # Arrange
    a: int = -5

    # Act & Assert
    with pytest.raises(ValueError):
        calculator.sqrt(a)

#h
'''h. בדוק בטסט שב- factorial עבור 4 חזר 24 )השתמש ב assert )'''

def test_calculator_factorial():
    # Arrange
    a: int = 4
    expected: int = 24

    # Act
    actual: int = calculator.factorial(a)

    # Assert
    assert expected == actual, "factorial function failed for sqrt(4)"

#g
'''i. בדוק בטסט שב- factorial עבור 5 חזר 120 )השתמש ב assert )'''

def test_calculator_factorial():
    # Arrange
    a: int = 5
    expected: int = 120

    # Act
    actual: int = calculator.factorial(a)

    # Assert
    assert expected == actual, "factorial function failed for sqrt(5)"


#h
'''בדוק בטסט שב- factorial עבור מינוס 3 התרחשה שגיאה מסוג ValueError'''


def test_calculator_sqrt_factorial():
    # Arrange
    a: int = -3

    # Act & Assert
    with pytest.raises(ValueError):
        calculator.sqrt(a)
