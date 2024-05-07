import random, string
	
def rand_pass(size):
	generate_pass = ''.join([random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
							for n in range(size)])
							
	return generate_pass

password = rand_pass(8)
print(password)