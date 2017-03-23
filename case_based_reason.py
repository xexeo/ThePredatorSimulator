#This class is designed to handle the case-based reasoning algorithm

## Properties:
##  - Take in Prey Count
##  - Take in Predator Count
##  - (Pos)Take in weather

class Case_Based_Reasoning(object):
	def __init__(self):
		self.cases = []
	
	def add_case(self, preyCount, predCount, result):
		self.cases.append(Case(preyCount, predCount, result))

	def get_case(self, preyCount, predCount):
		for case in self.cases:
			# Need an algorithm to get match percentage
			match = check_match(preyCount, case.get_prey_count())
		return self.cases[0]
	
	def check_match(val1, val2):
		return val1 - val2
	
	class Case(object):
		def __init__(self, preyCount, predCount, result):
			self.preyCount = preyCount
			self.predCount = predCount
			self.result = result
		
		def get_result(self):
			return self.result
			
		def get_prey_count(self):
			return self.preyCount	
		
		def get_pred_count(self):
			return self.predCount