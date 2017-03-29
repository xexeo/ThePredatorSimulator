#This class is designed to handle the case-based reasoning algorithm

## Properties:
##  - Take in Prey Count
##  - Take in Predator Count
##  - (Pos)Take in weather

class Case_Based_Reasoning(object):
	def __init__(self):
		self.cases = []
		self.add_case(3, 2, 1, True)
		self.add_case(2, 5, 2, True)
		self.add_case(1, 1, 1, False)
		self.add_case(1, 2, 1, False)
		self.add_case(2, 3, 3, False)
		self.add_case(6, 1, 1, True)
	
	class Case(object):
		def __init__(self, behaviour, preyCount, predCount, result):
			self.behaviour = behaviour
			self.preyCount = preyCount
			self.predCount = predCount
			self.result = result
		
		def get_result(self):
			return self.result
			
		def get_behaviour(self):
			return self.behaviour
			
		def get_prey_count(self):
			return self.preyCount	
		
		def get_pred_count(self):
			return self.predCount
	
	def add_case(self, behaviour, preyCount, predCount, result):
		self.cases.append(self.Case(behaviour, preyCount, predCount, result))

	def get_case(self, match_percentage, behaviour, preyCount, predCount):
		tempList = []
		for case in self.cases:
			# Need an algorithm to get match percentage
			match = self.check_match(behaviour, case.get_behaviour())
			match += self.check_match(predCount, case.get_pred_count())
			match += self.check_match(preyCount, case.get_prey_count())
			match = round(match/3, 0)
			if (match >= match_percentage): # Only select closests matches
				tempList.append((match, case))
		# Order list and return best match
		if (len(tempList) > 0):
			print(tempList)
			tempList.sort(reverse = True) # Sort Descending
			for case in tempList:
				if(case[1].get_result()):
					return case[1] # Pass across test where success was correct
		return False
	
	def check_match(self, new_val, comp_val):
		if (new_val >= comp_val):
			return calc_percentage_diff(new_val, comp_val)
		return calc_percentage_diff(comp_val, new_val)
	
def calc_percentage_diff(new_val, comp_val):
	# https://www.skillsyouneed.com/num/percent-change.html
	return 100 - (((new_val - comp_val) / new_val) * 100)
	