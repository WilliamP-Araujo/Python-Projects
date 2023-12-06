# Logical operators (Operadores logicos)
"""Nesse teste de operadores logicos utilizem em base um sistema de aprovação para credito imediato, onde dedependendo
do valor será aprovado ou negado."""

income_above_5k = input("Is your income above 5k? (yes/no) ") == "yes"
clean_name = input("Is your name clean? (yes/no) ") == "yes"

if income_above_5k and clean_name:
    print("Financing approved")
else:
    print("Financing denied, we are sorry")
