

class Laba:
	def __init__(self):
		self.titles = {"dice": "Дайс", "start_prob_dice": "Початкова ймов., P(Вi)", "probability_falling_num_k": "Ймовірністьвипадання числа k, P(A|Bi)", "multiplication_probility": "P(Вi)*P(A|Bi)", "main_probility": "P(Bi|A)"}
		
		self.start_probability_dice = {"d4": "1/3", "d6": "1/3", "d8": "1/3"}
		self.probability_falling_num_k = {"d4": "1/4", "d6": "1/6", "d8": "1/8"}
		self.multiplication_probility = {"d4": "1/12", "d6": "1/18", "d8": "1/24"}
		self.main_probility = {"d4": "6/13", "d6": "4/13", "d8": "3/13"}
		self.total_probability = "13/72"

	def handler(self):
		pass

	def table(self):
		indicator = 0

		for o in range(6):
			for i in range(106):
				print("-", end = '')

			if indicator == 0:
				print(f"\n|\t\t\t  |\t\t\t\t\t\t   |\t\t\t\t\t\t\t\t\t   |\t\t\t   |\t\t |\n|    {self.titles['dice']}\t  |\t{self.titles['start_prob_dice']} | {self.titles['probability_falling_num_k']} | {self.titles['multiplication_probility']} | {self.titles['main_probility']} |\n|\t\t\t  |\t\t\t\t\t\t   |\t\t\t\t\t\t\t\t\t   |\t\t\t   |\t\t |")
				indicator = indicator + 1
			
			elif indicator == 1:
				print(f"\n|     4d      |\t\t\t  {self.start_probability_dice['d4']}\t\t   |\t\t\t\t   {self.probability_falling_num_k['d4']}\t\t\t\t   |\t {self.multiplication_probility['d4']}\t   |   {self.main_probility['d4']}  |")
				indicator = indicator + 1

			elif indicator == 2:
				print(f"\n|     6d      |\t\t\t  {self.start_probability_dice['d6']}\t\t   |\t\t\t\t   {self.probability_falling_num_k['d6']}\t\t\t\t   |\t {self.multiplication_probility['d6']}\t   |   {self.main_probility['d6']}  |")
				indicator = indicator + 1

			elif indicator == 3:
				print(f"\n|     8d      |\t\t\t  {self.start_probability_dice['d8']}\t\t   |\t\t\t\t   {self.probability_falling_num_k['d8']}\t\t\t\t   |\t {self.multiplication_probility['d8']}\t   |   {self.main_probility['d8']}  |")
				indicator = indicator + 1

			elif indicator == 4:
				print(f"\n|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   |\t\t\t   |\n|     Сумарна ймовірність, P(A)\t\t\t\t\t\t\t\t\t\t\t\t   |\t {self.total_probability}\t   |")
				indicator = indicator + 1





Laba().table()