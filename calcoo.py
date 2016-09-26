#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Made by Felipe Sandoval Sibada

import sys


class Calculadora:
    def __init__(self, op1, op2):
        self.var1 = op1
        self.var2 = op2

    def add(self):
        return (self.var1 + self.var2)

    def minus(self):
        return (self.var1 - self.var2)


if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")
    except IndexError:
        sys.exit("Error: You need to give me numbers on the Command Line")

    variables = Calculadora(operando1, operando2)  # making the object

    if sys.argv[2] == "suma":
        result = Calculadora.add(variables)
    elif sys.argv[2] == "resta":
        result = Calculadora.minus(variables)
    else:
        sys.exit('You can only add or subtract.')

    print(result)
