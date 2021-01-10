user_temp = input('Wprowadź temperature w Kelwinach: ')


def check_temp(u_temp):
    try:
        temp = int(u_temp)
    except ValueError:
        print('Muszisz podać wartość liczbową')
        temp = None
    return temp


#check_temp(user_temp)

print(check_temp(user_temp))
