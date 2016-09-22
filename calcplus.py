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


def itera(list, num):
	total = num[0]
	counter = 1
	while counter < len(num) - 1:
		if list[0] == "suma":
			total = total + num[counter]
		elif list[0] == "resta":
			total = total - num[counter]
		elif list[0] == "multiplica":
			total = total * num[counter]
		elif list[0] == "divide":
			try:
				total = total / num[counter]
			except ZeroDivisionError:
				sys.exit("Division by zero is not allowed.")
		counter = counter + 1
	return total


if __name__ == "__main__":
	try:
		fich = open(str(sys.argv[1]), "r")
		lineas = fich.readlines()
		fich.close()
		
		for operaciones in lineas:
			
			operaciones = operaciones.split(",")
			important_only = operaciones[1:]
			list_num = [int(i) for i in important_only]
			op1 = itera(operaciones, list_num)
			op2 = list_num[-1]
			variables = Calculadora(op1, op2)
		
			if operaciones[0] == "suma":
				print("Adding total: " + str(CalculadoraHija.add(variables)))
			elif operaciones[0] == "resta":
				print("Subtract total: " + \
				str(CalculadoraHija.minus(variables)))
			elif operaciones[0] == "multiplica":
				print("Multiplication total: " + \
				str(CalculadoraHija.multiply(variables)))
			elif operaciones[0] == "divide":
				print("Divition total: " + \
				str(CalculadoraHija.divide(variables)))
			else:
				print("use 'suma', 'resta, 'multiplica o 'divide' at the beggining ''")
			
	except ValueError:
		sys.exit("Error: Non numerical parameters")
	except IndexError:
		sys.exit("Error: You need to give me a file to read")