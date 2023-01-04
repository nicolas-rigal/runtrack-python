def calcule(num1,operateur,num2):
    if operateur == "+":
        result = num1 + num2
    if operateur == "-":
        result = num1 - num2
    if operateur == "*":
        result = num1 * num2    
    if operateur == "/":
        result = num1 / num2
    if operateur == "%":
        result = num1 % num2
    return result

print(calcule(5,"+",5))
print(calcule(5,"-",5))
print(calcule(5,"*",5))
print(calcule(5,"/",5))
print(calcule(5,"%",5))
