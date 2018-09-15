
def get_password_strength(password):
    symbols = '~`!@#$%^&*()_-+={}[]:>;\',</?"/\\'
    number = len([int(char) for char in password if char.isdigit()])
    upper = len([str(char) for char in password if char.isupper()])
    lower = len([str(char) for char in password if char.islower()])
    symbol = len([str(char) for char in password if char in symbols])
    password_lenght = len(password)
    quantity_list = [number, upper, lower, symbol]
    return num_list


def password_rating(quantity_list, password_lenght):
    rating = 0
    for quantity in num_list:
        if quantity == 1:
            rating += 1
        elif quantity >= 2:
            rating += 2

    if password_lenght >= 10:
        rating += 2
    return rating


if __name__ == '__main__':
    password = input('type your password: ')
    rating = password_rating(get_password_strength(password), len(password))
    print('your password rating is {}'.format(rating))
