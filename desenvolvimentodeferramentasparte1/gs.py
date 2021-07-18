import random, string

size = int(input('type the password size you wish: '))

chars = string.ascii_letters+string.digits+'!@#$%çç!@#$##$%'

rnd = random.SystemRandom() #osurandom

print(''.join(rnd.choice(chars) for i in range(size)))

