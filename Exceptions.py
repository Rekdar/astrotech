# x = 'hello'
# assert x == 'hello'
# assert x == 'abc'
# **************************************************************************
# user_temp = input('Wprowadź temperature w Kelwinach: ')
#
# class ValueToSmall(Exception):
#     pass
#
# def check_temp(u_temp):
#     try:
#         temp = float(u_temp)
#         if temp < 0:
#             raise ValueToSmall('Temperatura jest mniejsza od 0, podaj większą od 0')
#             pass
#     except ValueError:
#         print('Musisz podać wartość liczbową')
#         temp = None
#     return temp
#
# print(check_temp(user_temp))

# **************************************************************************

# user_age = input('Podaj swój wiek: ')
#
# if int(user_age) < 18:
#     raise PermissionError('Adults only')

# **************************************************************************

user_value = input('Wprowadź stopie kąta figury geometrycznej: ')

class CotangentError(Exception):
    pass

def geometria(u_val):
    try:
        degree = float(user_value)
        if degree > 180:
            raise CotangentError('Wartość musi być mniejsza niż 180 stopni')
    except ValueError:
        print('Kąt musi być wartością numeryczną')
    return degree
print(geometria(user_value))