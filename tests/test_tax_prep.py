from ada_tax_prep.income_tax import (
    calculate_tax_2020
)

def test_no_income():
    income = 0

    taxes = calculate_tax_2020(income)

    assert taxes == 0

def test_max_bracket_one():
    income = 9875

    taxes = calculate_tax_2020(income)

    assert taxes == 988

def test_min_bracket_two():
    income = 9876

    taxes = calculate_tax_2020(income)

    assert taxes == 988 + 0

def test_max_bracket_two():
    income = 40125

    taxes = calculate_tax_2020(income)

    assert taxes == 988 + 3630

def test_min_bracket_three():
    income = 40126

    taxes = calculate_tax_2020(income)

    assert taxes == 988 + 3630 + 0

def test_max_bracket_three():
    income = 85525

    taxes = calculate_tax_2020(income)

    assert taxes == 988 + 3630 + 9988

def test_min_bracket_four():
    income = 85526

    taxes = calculate_tax_2020(income)

    assert taxes == 988 + 3630 + 9988 + 0

def test_max_bracket_four():
    income = 163300

    taxes = calculate_tax_2020(income)

    assert taxes == 988 + 3630 + 9988 + 18666


def test_min_bracket_five():
    income = 163301

    taxes = calculate_tax_2020(income)

    assert taxes == 988 + 3630 + 9988 + 18666 + 0

def test_max_bracket_five():
    income = 207350

    taxes = calculate_tax_2020(income)

    assert taxes == 988 + 3630 + 9988 + 18666 + 14096

def test_min_bracket_six():
    income = 207351

    taxes = calculate_tax_2020(income)

    assert taxes == 988 + 3630 + 9988 + 18666 + 14096 + 0

def test_max_bracket_six():
    income = 518400

    taxes = calculate_tax_2020(income)

    assert taxes == 988 + 3630 + 9988 + 18666 + 14096 + 108868

def test_min_bracket_last():
    income = 518401

    taxes = calculate_tax_2020(income)

    assert taxes == 988 + 3630 + 9988 + 18666 + 14096 + 108868 + 0

def test_big_bracket_last():
    income = 1000000

    taxes = calculate_tax_2020(income)

    assert taxes == 988 + 3630 + 9988 + 18666 + 14096 + 108868 + 178192
