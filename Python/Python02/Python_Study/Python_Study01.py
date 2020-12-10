
# def all_check(lst):
#     eturn len(lst) == len(set(lst))


# x = [1,2,3,4]
# y = [1,2,3,3]


# all_check(x)

# print (all_check(x))

# test_str = "D!@#$%^"
# test_str[0:1]

#문자열 첫글자 대문자로 만들기 
# def Make_Upper(str):
#     eturn  str[0:1].upper() +  str[1:]

# def Make_Upper2(str):
#     eturn str.title()


# print(Make_Upper("test String")) 
# print(Make_Upper2("test String")) 


#섭씨온도 화씨온도로 변경 
# def celsius_to_fahrenheit(celsius):
#     eturn ((celsius * 1.8 ) +32 )

# convert_value = celsius_to_fahrenheit(100)

# print (str(convert_value))

#remove Falsey Value  from list 

# def compact(lst): 
#     eturn list(filter(None,lst))


# test= [0,1,2,3,4,'',False]

# result = compact(test)

# print(result)


def first_word(text: str):
    """
        returns the first word in a given text.
    """
    # your code here
    return text[0:1]

print(first_word("vim 너무 어렵다 " ))






















