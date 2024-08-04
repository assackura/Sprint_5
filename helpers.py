import random

class Help:
    @staticmethod
    def generate_email():
        symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                   'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7',
                   '8', '9', '0', '_']
        email = ""
        for i in range(0, 10):
            email += symbols[random.randint(0, len(symbols) - 1)]

        email += "@ya.ru"
        return email

    @staticmethod
    def generate_password():
        symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                   'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7',
                   '8', '9', '0', '_', '!', '@', '#', '$', '%', '^', '&', '(', ')', '{', '}']
        count_symbols = random.randint(6, 20)
        pwd = ""
        for i in range(0, count_symbols):
            pwd += symbols[random.randint(0, len(symbols) - 1)]
        return pwd
