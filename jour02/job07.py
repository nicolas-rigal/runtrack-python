def switch(lang):
    if lang == "JavaScript":
        return "Vous pouvez devenir web developer."
    elif lang == "PHP":
        return "Vous pouvez devenir backend developer."
    elif lang == "Python":
        return "Vous pouvez devenir Data Scientist"
    elif lang == "Solidity":
        return "Vous pouvez devenir Blockchain developer."
    elif lang == "Java":
        return "Vous pouvez devenir mobile app developer"
    else:
        return "je serais le meuilleur développeur"

#print de toutes les possibilité
print(switch("JavaScript"))   
print(switch("PHP"))   
print(switch("Java"))

#input test
lang=(input('JavaScript, PHP, Python, Solidity, Java?'))
print(switch(lang))