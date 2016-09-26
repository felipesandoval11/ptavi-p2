#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Made by Felipe Sandoval Sibada

import sys
import csv
import calcoo
import calcoohija
import calcplus

if __name__ == "__main__":  # new changes. with and csv applied.
    try:
        with open(str(sys.argv[1]), newline='') as file:
            lineas = csv.reader(file)

            for operaciones in lineas:
                important_only = operaciones[1:]
                list_num = [int(i) for i in important_only]
                op1 = calcplus.itera(operaciones, list_num)
                op2 = list_num[-1]
                variables = calcoo.Calculadora(op1, op2)

                if operaciones[0] == 'suma':
                    print("Adding total: " +
                          str(calcoohija.CalculadoraHija.add(variables)))
                elif operaciones[0] == "resta":
                    print("Subtract total: " +
                          str(calcoohija.CalculadoraHija.minus(variables)))
                elif operaciones[0] == "multiplica":
                    print("Multiplication total: " +
                          str(calcoohija.CalculadoraHija.multiply(variables)))
                elif operaciones[0] == "divide":
                    print("Divition total: " +
                          str(calcoohija.CalculadoraHija.divide(variables)))
                else:
                    print('use suma, resta, multiplica o divide" at the'
                          'beggining')

    except ValueError:
        sys.exit("Error: Non numerical parameters")
    except IndexError:
        sys.exit("Error: You need to give me a file to read")
