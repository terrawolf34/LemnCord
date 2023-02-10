import time
import colorama
import random

text = "sparky dai vam 3 rublei"

for i in range(2000):
	colors = list(vars(colorama.Fore).values())
	colored_lines = [random.choice(colors) + line for line in text.split('\n')]



	print(''.join(colored_lines))
	time.sleep(0.5)