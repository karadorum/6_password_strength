from getpass import getpass
import string


def get_chars_count_list(password):
    numbers_count = len([char for char in password if char.isdigit()])
    upper_chars_count = len([char for char in password if char.isupper()])
    lower_chars_count = len([char for char in password if char.islower()])
    punctuation_chars_count = len([char for char in password if char in string.punctuation])
    password_lenght = len(password)
    chars_quantity_list = [numbers_count, upper_chars_count, lower_chars_count, punctuation_chars_count]
    return chars_quantity_list


def get_password_rating(chars_quantity_list, password_lenght):
    rating = 0
    medium_lenght_password = 10
    for quantity in chars_quantity_list:
        if quantity == 1:
            rating += 1
        elif quantity >= 2:
            rating += 2

    if password_lenght >= medium_lenght_password:
        rating += 2
    return rating


if __name__ == '__main__':
    password = getpass(prompt='type your password: ')
    rating = get_password_rating(get_chars_count_list(password), len(password))
    print('your password rating is {}'.format(rating))
