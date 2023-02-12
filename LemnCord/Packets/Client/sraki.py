import time, colorama, random

def sraki():
	text = "sparki dai mne 3 rublya"

	for i in range(2000):
		colors = list(vars(colorama.Fore).values())
		colored_lines = [random.choice(colors) + line for line in text.split('\n')]



		print(''.join(colored_lines))
		time.sleep(0.5)