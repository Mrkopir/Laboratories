import random
import matplotlib.pyplot as plt

class Laba:
	def __init__(self):
		self.count_num = input("Enter count of numbers >>> ")
		self.user_num_k = input("Enter number (1, 4) >>> ")

	def random_num_generator(self):
		self.generation_list = []
		for i in range(int(self.count_num)):
			self.random_num = random.randint(1, 4)
			self.generation_list.append(self.random_num)
		print(self.generation_list)

	def number_hendler(self):
		self.num_proccent = (self.generation_list.count(int(self.user_num_k)) / int(self.count_num))
		self.selective_math_expectation = (int(self.user_num_k) * int(self.num_proccent))

		print(f"\n\n\n")
		print(f"Proccent of the falling number {self.num_proccent * 100}%")


	def graphics(self):
		plt.bar(int(1), self.generation_list.count(1), label = "1", width = 0.5)
		plt.bar(int(2), self.generation_list.count(2), label = "2", width = 0.5)
		plt.bar(int(3), self.generation_list.count(3), label = "3", width = 0.5)
		plt.bar(int(4), self.generation_list.count(4), label = "4", width = 0.5)
		plt.legend()
		plt.show()

	def run(self):
		self.random_num_generator()
		self.number_hendler()
		self.graphics()


Laba().run()