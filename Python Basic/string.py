str1 = "My name is KDG"
print(len(str1))

# Escape문자, I'm a Boy
print("I'm a Boy")
print('I\'m a Boy')
print("I\\'m a Boy")
print("'I'm a Boy'")

print('a \t b')
print('a \n b')
print('a \"\" b')

multi_str = \
'''
aaaaaaaa
bbbbbbbb
cccccccc
'''

print(multi_str)
                    #\
                        #\





str_o1 = "Apple"
str_o2 = "Banana"
print(str_o1*3)
print(str_o1+str_o2)
print('A' in str_o1)
print('z' not in str_o1)

#문자열 함수()
#(upper, isalnum, startswitch, count, endswithh, isalpha.....)
print("Capitalize: ", str_o1.capitalize())
print("endswith?: ", str_o1.endswith('t'))