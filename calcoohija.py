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


class CalculadoraHija(Calculadora):
	def multiply(self):
		return (self.var1 * self.var2)

	def divide(self):
		try:
			return (self.var1 / self.var2)
		except ZeroDivisionError:
			sys.exit("Division by zero is not allowed.")


if __name__ == "__main__":
	try:
		operando1 = int(sys.argv[1])
		operando2 = int(sys.argv[3])
	except ValueError:
		sys.exit("Error: Non numerical parameters")
	except IndexError:
		sys.exit("Error: You need to give me numbers on the Command Line")

# making the object	
	variables = Calculadora(operando1, operando2)

	if sys.argv[2] == "suma":
		result = CalculadoraHija.add(variables)
	elif sys.argv[2] == "resta":
		result = CalculadoraHija.minus(variables)
	elif sys.argv[2] == "multiplica":
		result = CalculadoraHija.multiply(variables)
	elif sys.argv[2] == "divide":
		result = CalculadoraHija.divide(variables)
	else:
		sys.exit('You can only add or subtract.')


	print(result)