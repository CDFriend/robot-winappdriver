*** Settings ***

Library     CalculatorLibrary.py

*** Test Cases ***

Two plus two should equal four
    Press   2
    Press   +
    Press   2
    Press   =
    Result should be    4
