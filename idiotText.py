import random

print("::WELCOME TO IDIOTIC TEXT GENERATOR::")
print("::KEEP ON TYPING OR ENTER . TO EXIT")

def idiotize(str):
	str = str.lower()
	idioticStr = ''
	count = random.randint(1,2)
	for c in str:
		if c == 'a':
			idioticStr += '4'
		elif count % 2 == 0:
			idioticStr += c.upper()
		else:
			idioticStr += c
		count += 1
		
	return idioticStr

while True:
    line = input("Enter non-idiotic text: ")
    print(idiotize(line))
    if line == '.':
        print("Quitting program...")
        break
