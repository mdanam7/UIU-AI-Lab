c={}#empty dictionary
marks={
    "Anam":100,
    "Raihan":98,
    "Rahat":89
}

print(marks,type(marks))#{'Anam': 100, 'Raihan': 98, 'Rahat': 89} <class 'dict'>
print(marks["Raihan"])
print(marks.items())#dict_items([('Anam', 100), ('Raihan', 98), ('Rahat', 89)])
print(marks.keys())
print(marks.values())
#dict_keys(['Anam', 'Raihan', 'Rahat'])
# dict_values([100, 98, 89])

marks.update({"Anam":88,"Dipu":56})
print(marks)#{'Anam': 88, 'Raihan': 98, 'Rahat': 89, 'Dipu': 56}
print(marks.get("Raihan"))#98








#practice1
words={"piriti":"Love",
       "pagla":"mad",
       "purbo":"east"}
word=input("Enter the word you want meaning of: ")

print(words[word])



#practice 2
d={}
name=input("Enter friends name: ")
lang=input("Enter language name: ")
d.update({name:lang})
name=input("Enter friends name: ")
lang=input("Enter language name: ")
d.update({name:lang})
name=input("Enter friends name: ")
lang=input("Enter language name: ")
d.update({name:lang})
name=input("Enter friends name: ")
lang=input("Enter language name: ")
d.update({name:lang})
name=input("Enter friends name: ")
lang=input("Enter language name: ")
d.update({name:lang})
name=input("Enter friends name: ")
lang=input("Enter language name: ")
d.update({name:lang})#its always unique for key 
print(d)


