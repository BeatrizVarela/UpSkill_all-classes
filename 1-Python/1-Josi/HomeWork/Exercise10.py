# -*- coding: utf-8 -*-

phone_number = input('Please enter a phone number in the format XXX-XXX-5555: ')

credit_str = "xxxx----xxxx----5555---"
new_credit_str = credit_str[credit_str.index('5'):credit_str.index('5') + len('5555')]
print(new_credit_str)
