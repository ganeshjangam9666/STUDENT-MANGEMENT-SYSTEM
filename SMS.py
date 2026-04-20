# 1. Write a statement(WAS) to print “Hello World” by using shell
# Open python shell and simply type 'Hello World' and hit enter it displays the output as 'Hello World'

# 2. WAS to print “Hello world” by using python print function
print("Hello World")

# 3. WAS to initialize variable and value as 50.
a=50

# 4. WAS to initialize multivariable value are 150,120,250(take your own variable names )
a=150
b=120
c=250
# or
a,b,c=150,120,250

# 5. WAS to print the type of the data in the given value.
print(type(5))
print(type('hello'))

# 6. WAS to print the address of the memory block in given value.
a=123
print(id(a))
l1=[1,2,3]
print(id(l1))
l2=l1
print(id(l2))
l2[2]=4
print(l1)
print(id(l1))

# s1=[1,2,3]
# s2=[1,2,3]
# print(id(s1))
# print(id(s2))

# 7. WAS to print your details, first store your details, extract the values and display it.
Fname='Ganesh'
Lname='Jangam'
Age=21
education='B.Tech'
percentage=74.0
print(Fname,Lname,Age,education,percentage)

# 8. WAS to swap the two values. With a temp variable.
a=10
b=20
temp=a
a=b
b=temp
print(a,b)

# 9. WAS to swap the two values without temp variable
a=50
b=100
a=a+b
b=a-b
a=a-b
print(a,b)

a=200
b=500
a=a^b
b=a^b
a=a^b
print(a,b)

# 10. WAS to initialize a value and print the value, after print then reinitialize the new value to the existing variable and display the value.

a=1000
print(a)
b=200
a=b
print(a)

# 11. WAS to convert single to multi value data type
# I/p ⇒ a=10
# o/p ⇒ [‘1’,’0’]
a=10
s=str(a)
l=list(s)
print(l)

# 12. WAS to concat the two multi value data types(str , list, tuple, dict).

# String concatination
s1="Hello"
s2="World"
print(s1+s2)
# list cocatination
l1=[1,3,4]
l2=[5,6,8]
print(l1+l2)
# tuple concatination
t1=(1,2.4,'raja')
print(t1+('rani',123))
# dictionary concatination
d={1:[1,2,6],2:('raj','vikram','aditya')}
d[1]=d[1]+['rani']
# d+{3:'raju'} # Error  unsupported operand type + for dict and dict
print(d)


# 13. WAC to perform  the length of the collection.
l1=[1,2,4,5,6.9,'raj','rani']
print(l1,len(l1))

# 14. WAC to find out the middle value of the given collection.

l=[1,2,3,4,5]
n=len(l)
if(n%2!=0):
    print(l[n//2])
else:
    print(l[(n//2)-1],l[(n//2)])

# 15. WAS to concat the new string into the starting of the given string.
s='Jangam'
newstr='Ganesh'
print(newstr+s)

# 16. WAS to concat the new string into the ending of the given string.
s='Jangam'
newstr='Ganesh'
print(s+newstr)

# 17. WAS to concat the new string into the middle of the given string.
s='HelloGanesh'
n=len(s)//2
newstr=s[:n]+"Mr."+s[n:]
print(newstr)

# 18. WAS to replace the old character into a new character of the given string.
name='Ganesh jangam'
# method 1
print(name.replace('j','J'))
# method 2
print(name)
l=list(name)
print(l)
l[7]='J'
print(l)
res=""
for i in l:
    res+=i
print(res)

# 19. WAS to delete the specific character in the given string
s='Hello, World!'
print(s.replace('W',''))
#print(s)

# 20. WAS to concat the new string into the specific position of the given string.
p=6
s="Hello, World!"
newstr='My'
print(s[:p]+newstr+s[p:])

# 21. WAS to concat the new value into the starting of the given list.
l=[1,2,3,4]
l.insert(0,0)
print(l)
# or
print([0]+l)

# 22. WAS to concat the new value into the ending of the given list.
l=[3,4,5,6]
# method1
print(l+[10])
# method 2
l.append(10)
print(l)

# 23. WAS to concat the new value into the middle of the given list.
l=[1,2.5,"raja","rani"]
n=(len(l)//2)
l.insert(n,'Jack')
print(l)

# 24. WAS to modify the new value into the specific position of the given list.
p=3
l=[2,1,3,5,6]
l[3]=10
print(l)


# 25. WAS to modify the new value into the starting of the given list.
lst=[12,2,3]
lst[0]=1
print(lst)

# 26. WAS to modify the new value into the ending of the given list.
l=[1,2.5,'Rose']
l[len(l)-1]='Jack'
print(l)

# 27. WAS to modify the new value into the middle of the given  list.
l=[1,2,4.5,'stop','start']
l[(len(l)//2)]='Jack'
print(l)

# 28. WAS to modify the first 4 positions values into a given list.
l=[10,20,30,40,5]
l[0],l[1],l[2],l[3]=1,2,3,4
print(l)

# 29. WAS to delete the value in the specific position of the given list.
l=[10,20,30,40,5]
# print(l.pop())
# print(l)
p=2
l.remove(l[p])
print(l)

# 30. WAS to delete the new value into the ending of the list.
l=[20,10,15,30,40]
print(l)
print(l.pop())
print(l)

# 31. WAS to delete the new value into the middle of the list.
l=[20,10,15,30,40]
print(l)
l.remove(l[len(l)//2])
print(l)

# 32. WAS to concat the new value into starting of the tuple.
t=(10,20,30,40)
print((200,)+(t))

# 33. WAS to concat the new value into the middle of the tuple.
t=(10,20,30,40,50,60)
# we can't add the element at the middle of the tuple as tuple is immutable
# this we can achieve by using slicing by creating new tuple object
n=len(t)//2
print(t[:n]+(35,)+t[n:])

# 34. WAS to concat the new value into the ending of the tuple.
t=(10,20,30,40,50,60)
# we can't add the element at the end of the tuple as tuple is immutable
# this we can achieve by using slicing by creating new tuple object
print(t+(70,))

# 35. WAS to concat the new value into the set.
s={1,2,3}
# print(s+{5,6})
# print(s)
# Concatination is not possible, but we can add the element into the set
s.add(4)
print(s)

# 36. WAS to concat the new key and value into the dict.
d={1:'jack',2:'sparrow'}
# d+{3:'bgm'} #TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
d[3]='bgm'
print(d)

# 37. WAS to delete the specific key and value in the given dict.
d={1:'jack',2:'sparrow',3:'bgm'}
d.pop(1)
print(d)

# 38. WAS to delete the set value.
s={1,2,4,5,7}
print(s)
s.remove(2)
print(s)
s.discard(7)
print(s)

# 39. WAS to modify the specific value in the given dict.
d={1:'jack',2:'sparrow',3:'bgm'}
d[3]='movie'
print(d)

# 40. WAS to concat the list value and tuple value by using type casting.
l=[1,2,4,5,6]
t=(7,8,9,10)
print(l+list(t))

# 41.WAS to concat the list value and tuple value without using type casting.
l=[1,2,3]
t=(4,5)
# without type casting it is cannot be possible
print(l+[t[0],t[1]])

# 42. WAC to the given number is divisible by 3.
n=27
print(n%3==0)

# 43. WAC to the given number is divisible by 2 and 6.
n=18
print(n%2==0 and n%6==0)

# 44. WAC to the given number, the last digit is divisible by 3. (don't use typecasting)
n=123
ld=n%10
print(ld%3==0)

# 45. WAC to the last digit of a given number is divisible by 3.(use typecasting)
n=154
s=str(n)
print(s[-1])
print((int(s[-1]))%3==0)

# 46. WAC to the given number is greater than 150.
n=155
print(n>150)

# 47. WAC to the given number is greater than or equal to 100.
n=100
print(n>=100)

# 48. WAC to check the given number is less than 150, print the result.
n=122
print(n<=150)

# 49. WAC to the given number is less than or equal to 100.
n=123
print(n<=100)


# 50. WAC to the given number is greater than 15 & less than 24
n=21
print(n>15 and n<24)

# 51. WAC to the given number is even.
n=122
print(n%2==0)

# 52. WAC to the given number is odd.
n=122
print(n%2!=0)


# 53. WAC to perform the replication of a given string with 6.
s='Ganesh'
print(s*6)

# 54. WAC to the given number is divisible by 3 and also the number should be greater than 22.
n=123
print(n%3==0 and n>22)

# 55. WAC to perform the length of the collection is even or not.
l=[1,6,2,5,3,9,0,4]
print(len(l)%2==0)


# 56. WAC to perform  the length of the collection is less than 55 and greater than 16.
l=[1,2,3,4,5,5,6,6,6,6,3,2,2,5,6,7,6,8,9,5,7,8,9,0,3,2,1]
print(n>16 and n<55)

# 57. WAC to perform  the length of the collection is divisible by 5 and odd.
l=[1,2,3,4,5]
n=len(l)
print(n%5==0 and n%2!=0)

# 58. WAC to extract the middle position of a given collection.(str, lis, tuple)
l=[1,2,3,4,5]
print(len(l)//2)
t=(1,2,3,4,5)
print(len(t)//2)
s='Hello!'
print(len(s)//2)


# 59. WAC to the given number is greater than 20 and less than 30 and it should be even.
n=25
print(n>20 and n<30 and n%2==0)


# 60. WAC to the given number is even and it should be less than 120.
n=66
print(n%2==0 and n<120)


# 61.WAC to the given number is even and present from 40 to 70
n=45
print(n%2==0 and n>=40 and n<=70)


# 62. WAC to the given number is odd and it should be greater than 97.
n=145
print(n%2!=0 and n>97)


# 63. WAC to the given number is less than 122 and greater than 48 and the number should be divisible by 4.
n=99
print(n<122 and n>48 and n%4==0)


# 64. WAC to the given number is divisible by 3 or 5, displaying the value.
n=25
print(n%3==0 or n%5==0)


# 65. WAC to the given number is between 100 to 200 including the limit.
n=200
print(n>=100 and n<=200)


# 66. WAC to the given number is in between 100 to 200.
n=200
print(n>100 and n<200)


# 67. WAC to the given string's last character ASCII value should be divisible by 5.
s='Hello'
n=ord(s[-1])
print(n%5==0)


# 68. WAC to the given number is present between 60 to 130 and the number should be divisible by 3 and 4
# and the last digit should be  9.

n=129
print(n>60 and n<130 and  n%3==0 and n%4==0 and (n%10)==9)

# 69. WAC to the given number is even or less than 25.
n=34
print(n%2==0 or n<25)


# 70. WAC to the given number is even or greater than 25.
n=34
print(n%2==0 or n>25)


# 71. WAC to the given number is divisible by either 3 or 5.
n=155
print(n%3==0 or n%5==0)



# 72. WAC to the given number is not an even number.
n=123
print(not(n%2==0))


# 73. WAC to the given number is not a odd number
n=123
print(not(n%2!=0))
print(n%2!=0)


# 74. WAC to the given number is not a divisible by 3
n=123
print(not(n%3==0))
print(n%3!=0)


# 75. WAC to the given number is not a divisible by 3 and  5
n=225
print(not(n%3==0 and n%5==0))


# 76. WAC to the given number is not a divisible by 3 or  5
n=225
print(not(n%3==0 or n%5==0))


# 77. WAC to the given character ascii value is not divisible by 5.
ch='h'
print(not(ord(ch)%5==0))


# 78. WAC to find out the ascii character in a given number.
ch=67
print(chr(ch))


# 79. WAC to find out the ascii value in a given character.
ch='r'
print(ord(ch))


# 80. WAC to the given character is uppercase or not.
ch='S'
print(ch>='A' and ch>='Z')

# 81. WAC to the given character is the alphabet.
ch='q'
print((ch>='A' and ch>='Z') or (ch>='a' and ch<='z'))


# 82. WAC to the given character is lowercase.
ch='q'
print(ch>='a' and ch<='z')



# 83. WAC to the given character is the ascii number.
ch='$'
print(len(ch)==1 and ord(ch)<128)


# 84. WAC to the given character is the special character.
ch='$'
print(not((ch>='A' and ch<='Z') or (ch>='a' and ch<='z') or (ch>='0' and ch<='9')))


# 85. WAC to the given character should not be uppercase.
ch='C'
print(not(ch>='A' and ch<='Z'))

# 86. WAC to the given character should not be lowercase.
ch='C'
print(not(ch>='a' and ch<='z'))


# 87. WAC to the given character should not be the alphabet.
ch='$'
print(not(ch>='A' and ch<='Z' and ch>='a' and ch<='z'))


# 88. WAC to the given character should not be an ascii number.
ch='$'
print(not(len(ch)==1 and ord(ch)<128))


# 89. WAC to the given character is the special character.
ch='$'
print(not((ch>='A' and ch<='Z') or (ch>='a' and ch<='z') or (ch>='0' and ch<='9')))


# 90. WAC to the given character is a vowel.
ch='u'
s='AEIOUaeiou'
print('u' in s)
print('S' in s)



# 91. WAC to the given character is  a consonant.
ch='u'
s='AEIOUaeiou'
print('u' not in s)
print('S' not in s)

# 92. WAS to convert uppercase to lowercase in a given character.
ch='C'
print(chr(ord(ch)+32))
r=ch.lower()
print(r)
print(ch.lower())


# 93. WAS to convert lowercase to uppercase in a given character.
ch='g'
print(chr(ord(ch)-32))
r=ch.upper()
print(r)
print(ch.upper())


# 94. WAS to extract the previous character in the given character.
ch='D'
n=ord(ch)
print(chr(n-1))



# 95. WAS to extract the next character in the given character.
ch='D'
n=ord(ch)
print(chr(n+1))



# 96. WAC to the given number character is a special symbol.
n=125
print(not((n>=65 and n<=90) or(n>=97 and n<=122) or (n>=48 and n<=57)))



# 97. WAC to the given character is converted to ASCII value and the value is even as well as the character should be lowercase.
ch='t'
a=ord(ch)
print(a%2==0 and (a>=97 and a<=122))


# 98. WAC to the given character is converted to ASCII value and the value is odd as well as the character should be uppercase.
ch='t'
a=ord(ch)
print(a%2!=0 and (a>=65 and a<=90))


# 99. WAC to which the given number is converted to character is not a special symbol or not.
n=122
ch=chr(n)
print((ch>='A' and ch<='Z') or (ch>='a' and ch<='z') or (ch>='0' and ch<='9'))



# 100. WAC to the given number of the ascii character is a vowel.
n=69
ch=chr(n)
s='AEIOUaeiou'
print(ch in s)



# 101. WAC to check if the first and second characters are sequence or not in a given string.
s='efafdh'
a1=ord(s[0])
a2=ord(s[1])
print((a1+1)==a2)


# 102. WAC to the given  character ASCII value should be either greater than 50 or greater than 25 or less than 112.
ch='D'
n=ord(ch)
print((n>50) or (n>25 or n<112))


# 103. WAC to the given number is increased by 1.
n=200
n+=1
print(n)


# 104. WAC to the given number is increased by 2.
n=123
n+=2
print(n)


# 105. WAC to the given number is decreased by 1.
n=123
n-=1
print(n)



# 106. WAC to the given number is decreased by 3.
n=123
n-=3
print(n)


# 107. WAC to the given integer number is present in the collection.
l=[1,3,2,8,6,5,77]
print(2 in l)
print(10 in l)



# 108. WAC to perform the addition operation on A value and B value and final result should be updated to A.
a=100
b=200
a=a+b
print(a)


# 109. WAC to the given value is present in the collection.
s={4,1,2,3,7,8,9}
print(2 in s)
print(10 in s)



# 110. WAC to the given list is present in the list.
l=[1,2,3,[4],[5,6],7]
print([4] in l)
print([1] in l)



# 111. WAC to the given dict value is present in tuple.
d={1:'ganesh',2:5,3:2.5}
t=(1,5,'ganesh')
print(d[1] in t)
print(d[3] in t)


# 112. WAC to the check given value is integer value or not.
a=12
print(type(a)==int)
print(type(12.4)==int)


# 113. WAC to the check given value is string value or not.
a='123'
print(type(a)==str)
print(type('gdgcdud')==str)
print(type(12.6)==str)


# 114. WAC to the check given value is single value or not.
a=[1,2,3]
print(type(a)==int or type(a)==float or type(a)==complex or type(a)==bool)


# 115. WAC to the check given value should not be a single value.
a=[1,2,3]
print(not(type(a)==int or type(a)==float or type(a)==complex or type(a)==bool))


# 116. WAC to the check given value is multi value or not.
a=['raja',1,2,3,'rani']
print(not(type(a)==int or type(a)==float or type(a)==complex or type(a)==bool))



# 117. WAC to the check given value is a mutable value or not.
a=('raja',1,2,3,'rani')
print(type(a)==list or type(a)==set or type(a)==dict)



# 118. WAC to the check given value is an immutable value or not.
a=('raja',1,2,3,'rani')
#a=[1,2,3]
print(not(type(a)==list or type(a)==set or type(a)==dict))

l=[1,2,3,4]
print(not(type(l)==list or type(l)==set or type(l)==dict))


# 119. WAC to the check given value should be an immutable value.
a='string'
print(not(type(a)==list or type(a)==set or type(a)==dict))

l=[1,2,3,4]
print(not(type(l)==list or type(l)==set or type(l)==dict))



# 120. WAC to check if a given value is divisible by 6 as well as that value present in the collection or not.
l=[12,45,33,66,77,88,99]
e=66
print(e%6==0 and (e in l))


# 121. WAC to perform the bitwise or operation given values are 115 and 79.
print(115 | 79)


# 122. WAC to perform the bitwise xor operation given values are 56 and 22.
print(56^22)


# 123. WAC to perform the bitwise not operation given values are 15.
print(~(15))


# # 124. WAC  to perform the bitwise left shift with 32  and  skipping value is 3.
print(32<<3)



# 125. WAC  to perform the bitwise right shift with 25  and  skipping value is 2.

print(25>>2)


# 126. To find out the output of a given condition.
# (10+20*60 and 10**3) or ({10,20} or not ([15-16]))
print((10+20*60 and 10**3) or ({10,20} or (not([15-16]))))


# 127. WAC to check if the first and last characters are the same or not in the given list.
l=[1,3,5,'raj','vikram',4,6,1]
print(l[0]==l[-1])

l=[1,3,5,'raj','vikram',4,6]
print(l[0]==l[-1])



# 128. WAC to check if a given key is present in a dict.
d={1:'hello',2:10.4,3:60,4:'jack'}
print(2 in d.keys())
print(7 in d.keys())



# 129. WAC to check if value is present in the dict.
d={1:'hello',2:10.4,3:60,4:'jack'}
print(2 in d.values())
print(7 in d.values())


# 130. WAC to check if the key is not present in a dict.
d={1:'hello',2:10.4,3:60,4:'jack'}
print(8 not in d.keys())
print(1 not in d.keys())



# 131. WAC to check if two values are pointing to the same address or not
a=[20,30,40]
b=[20,30,40]
print(id(a)==id(b))

a=[20,30,40]
b=a
print(id(a)==id(b))

a=12.5
b=a
print(id(a)==id(b))

a=12.5
b=12
print(id(a)==id(b))



# 132. WAC to check both the values should be integer and both the values are pointing to the same address.
a=12
b=12
print(id(a)==id(b))

a=12
b=124
print(id(a)==id(b))


