import re

class LenghtRule:

	def __init__(self, length, errorMessage):
		self.length = length
		self.errorMessage = errorMessage

	def valide(self, data):
		return len(data) >= self.length 

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
			problems.append(rule.errorMessage)
			strongPassword = False

	return (strongPassword, problems)	

def outputResult(result):
	successfulMessage = "Strong Password"
	if result[0]:
		print(successfulMessage)
		return True
	for i in result[1]:
		print(i)
	return False	
	

password = input()	
outputResult(checkPassword(password))
