import random, os, time, datetime

# Constants used in the program
starttime = time.time()
heads = 0
tails = 0
flipped = 0
i = 0

print("\nThis is a program that simulates a coin flip a certain number of times, and displays the results.".upper())
print("\n")
print("*" * 40, "COIN FLIP GENERATOR", "*" * 40)
print("\n")
# Input number of times to flip the coin
rep = int(input("Number of times you would like the coin to be flipped? "))
# Input filename (without .txt extension)
log_file_name = input("Log file filename- ")

while i < rep:
	flip = random.randrange(2)		# 0/1 randomly generated
	flipped = flipped + 1
	i = i + 1

	if flip == 0:					# 0 represents Heads
		heads = heads + 1
	else:							# 1 represents Tails
		tails = tails + 1
	print(flip, end = " ")			# To sepearate output by a space " "

# Calculting percentage of tails and heads in number of flips
tails_percent = (100 / rep) * tails
heads_percent = (100 / rep) * heads

# Calculating difference between number of heads and number of tails
if tails > heads:
	difference = tails - heads
elif heads > tails:
	difference = heads - tails
else:
	difference = 0

# Calculating Time lapsed
time_elapsed = str(datetime.timedelta(seconds=round(time.time()-starttime,2)))
time_elapsed = time_elapsed[:-4]

# Displaying result
print("\n")
print("Flipped a coin", rep, "times.")
print("Total execution time:", time_elapsed)
print("Tails was flipped", tails, "times, or", tails_percent, "% of the time.")
print("Heads was flipped", heads, "times, or", heads_percent, "% of the time.")
print("The difference between the two was", difference, ".")

logfile = open(os.getcwd() + "/" + log_file_name, "w")
logfile.write("Flipped a coin " + str(rep) + " times.\n")
logfile.write("Total execution time: " + str(time_elapsed) + "\n")
logfile.write("Tails was flipped " + str(tails) + " times, or " + str(tails_percent) + "% of the time.\n")
logfile.write("Heads was flipped " + str(heads) + " times, or " + str(heads_percent) + "% of the time.\n")
logfile.write("The difference between the two was " + str(difference) + ".\n")
logfile.close()
