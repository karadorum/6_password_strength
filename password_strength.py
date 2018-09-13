
def get_password_strength(password):
    symbols = '~`!@#$%^&*()_-+={}[]:>;\',</?"/\\'
    num = len([int(i) for i in password if i.isdigit()])
    up = len([str(i) for i in password if i.isupper()])
    lower = len([str(i) for i in password if i.islower()])
    symbol = len([str(i) for i in password if i in symbols])
    password_lenght = len(password)
    num_list = [num, up, lower, symbol]
    return num_list

def password_rating(num_list, password_lenght):
    rating = 0
    for n in num_list:
        if n == 1:
            rating += 1
        elif n >= 2:
            rating += 2
    
    if password_lenght >= 10:
        rating += 2
    return rating
        
    

if __name__ == '__main__':
    password = input('type your password: ')
    rating = password_rating(get_password_strength(password), len(password))
    print('your password rating is {}'.format(rating))
    
