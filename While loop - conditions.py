# == While loop ==

value = int(input("Insert your product value:"))

while value > 20:
    value = (value * 0.10) + value
    print(f"The final value of your product is R${value}")
    break