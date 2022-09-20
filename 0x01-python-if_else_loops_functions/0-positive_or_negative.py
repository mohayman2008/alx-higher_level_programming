#!/usr/bin/python3
import random
number = random.randint(-10, 10)
msgs = {'-ve': 'is negative', 'zero': 'is zero', '+ve': 'is positive'}
if number < 0:
    message = msgs['-ve']
elif number == 0:
    message = msgs['zero']
else:
    message = msgs['+ve']

print(f'{number:d} {message}')
