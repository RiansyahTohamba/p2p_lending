# fizz_buzz.py
# bisa dibagi 3? = fizz
# bisa dibagi 5? = buzz
# bisa dibagi 3 dan 5?  = fizz buzz
n = 35
for x in range(n):
	x=x+1
	if (x%3==0) and (x%5==0):
		x = 'fizz buzz'
	elif (x%3==0):
		x = 'fizz'
	elif (x%5==0):
		x = 'buzz'

	print(x)