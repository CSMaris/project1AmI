#a variable can contain any kind of data
#Python does not use chars, everything is a string
#NB the print result is ALWAYS a string


print("Hello")
value = "String"  #could use also ' instead of "
value2 = 'I\'m a string'#\ means character after that is just a syntax char
print(value2)
print(type(value))

people=40
cats=40

if people<cats:
    print("Too many cats!!!!!!!!")
elif people>cats:
    print("Too many people!!!!!!")
else:
    print("Same number")

    print(2==1)


for char in "hello":#for any char in hello print that char
    print(char)
#print("\n")
sayH = "hello"
print(sayH[1])

for number in range (0,10):#10 not included,you could also write (0,10,2) which means the same thing but counts by steps of 2
    print(number)

#use + to contatenate two strings

word="Hello"
word3=word*3
print(word3)

print(3, "times",5,"is",3*5)#to concatenate strings and integers
#either way
print(str(3)+"hello")

result="%d times %d is %d" %(2,3,6)#to concatenate strings and integers
print(result)


print("How old are you?")
age=input()#you have to write your age in the window below
print("Your age is "+age)

#or
print("How old are you?")
age=int(input())
print("Your age is "+ str(age))

#see lists and dictionaries on slides




