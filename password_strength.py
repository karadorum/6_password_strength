from getpass import getpass
import string


def get_password_symbols(password):
    '''symbols = '~`!@#$%^&*()_-+={}[]:>;\',</?"/\\'''
    number = len([char for char in password if char.isdigit()])
    upper = len([str(char) for char in password if char.isupper()])
    lower = len([str(char) for char in password if char.islower()])
    punctuation = len([str(char) for char in password if char in string.punctuation])
    password_lenght = len(password)
    symb_quantity_list = [number, upper, lower, punctuation]
    return symb_quantity_list


def get_password_rating(symb_quantity_list, password_lenght):
    rating = 0
    medium_lenght_password = 10
    for quantity in symb_quantity_list:
        if quantity == 1:
            rating += 1
        elif quantity >= 2:
            rating += 2

    if password_lenght >= medium_lenght_password:
        rating += 2
    return rating


if __name__ == '__main__':
    password = getpass(prompt='type your password: ')
    rating = get_password_rating(get_password_symbols(password), len(password))
    print('your password rating is {}'.format(rating))
