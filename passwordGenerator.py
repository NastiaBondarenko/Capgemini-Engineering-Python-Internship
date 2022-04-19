import random
import string
import re

class LenghtRule:

	def __init__(self, length, errorMessage):
		self.length = length
		self.errorMessage = errorMessage

	def valide(self, data):
		return len(data) >= self.lenghh	

class UpperLowerRule:

	def __init__(self, errorMessage):
		self.regularLower = r'[a-z]'
		self.regularUpper = r'[A-Z]'
		self.errorMessage = errorMessage

	def valide(self, data):
		return (re.search(self.regularLower, data)   and  re.search(self.regularUpper, data) )	


class RegexRule:

	def __init__(self, regular, errorMessage):
		self.regular = regular
		self.errorMessage = errorMessage

	def valide(self, data):
		return re.search(self.regular, data)	


def checkPassword(password):

	strongPassword = True 
	problems = []   
 
	rules = [ 
		UpperLowerRule("- Password must contain both lowercase and uppercase characters"),
		RegexRule(r'\d', "- Password must contain at least one digit"), 
		RegexRule(r'\W|_', "- Password must contain at least one punctuation character"), 
		LenghtRule(14, "- Password must be at least 14 characters long")
		]		

	for rule in rules:
		if not rule.valide(password):
			strongPassword = False

	return strongPassword	


def generatPassword ():
	generated = False

	lenght = random.randint(14, 20)

	allСharacters = string.ascii_letters + string.digits + string.punctuation

	while not generated:	

		password = ''

		for i in range(lenght):
			password += password.join(random.choice(allСharacters))

		if(checkPassword(password)):
			generated = True	
			return password	
	

print(generatPassword())