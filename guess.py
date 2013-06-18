from random import randint


print "What's your name?"
name = raw_input(">")
print "%s, I'm thinking of a number between 1 and 100. Try to guess my number!!!" %(name)

answer = 50 #randint(1,100)
counter = 0

while True:
	
	print "What's your guess?"
	guess = int(raw_input(">"))
		
	if answer > guess:
		print "Your guess is too low, try again."
		counter += 1
		
	if answer < guess:
		print "Your guess is too high, try again."
		counter += 1
			
	if guess==answer:
		counter += 1
		print "Well done, %s! You found my number in %r tries!" %(name, counter)
		break


