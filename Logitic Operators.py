# Logical operators (Operadores logicos)
#Author: William P. Araujo
"""Nesse teste de operadores logicos utilizem em base um sistema de aprovação para credito imediato, onde dedependendo
do valor será aprovado ou negado."""

renda_acima_5mil = input("Sua renda é acima de 5 mil? (sim/não) ") == "sim"
nome_limpo = input("Seu nome está limpo? (sim/não) ") == "sim"

if renda_acima_5mil and nome_limpo:
    print("Financimento aprovado")
else:
    print("Financimento negado, sentimos muito")

#English Ver:

# Logical operators
"""In this test of logical operators, use a system for immediate credit approval as a basis, where depending
on the value it will be approved or denied."""


income_above_5k = input("Is your income above 5k? (yes/no) ") == "yes"
clean_name = input("Is your name clean? (yes/no) ") == "yes"

if income_above_5k and clean_name:
    print("Financing approved")
else:
    print("Financing denied, we are sorry")
