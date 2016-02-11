import random
import math
Maze= [['x' for i in range(10)] for i in range(10)]
itr=random.randrange(0,9)
jtr=random.randrange(0,9)
ipl=random.randrange(0,9)
jpl=random.randrange(0,9)
while ipl==itr and jpl==jtr:
	ipl=random.randrange(0,9)
	jpl=random.randrange(0,9)
Maze[ipl][jpl]='p'
Distance=math.fabs(ipl-itr)+math.fabs(jpl-jtr)
print 'you are at:',ipl+1,jpl+1,'and your distance is:',Distance,'blocks'
for i in range(10):
	print Maze[i]
victory=True if ipl==itr and jpl==jtr else False
while victory==False:
	Direction=raw_input('Do you want to go UP,DOWN,LEFT or RIGHT?')
	if (Direction=='RIGHT'):
		if (jpl+1<10):
			Maze[ipl][jpl]='x'
			jpl=jpl + 1
			Maze[ipl][jpl]='p'
			Distance=math.fabs(ipl-itr)+math.fabs(jpl-jtr)
			print 'You are at:',ipl+1,jpl+1,'and your distance is:',Distance,'blocks'
	elif (Direction=='LEFT'):
		if (jpl-1>-1):
			Maze[ipl][jpl]='x'
			jpl=jpl-1
			Maze[ipl][jpl]='p'
			Distance=math.fabs(ipl-itr)+math.fabs(jpl-jtr)
			print 'You are at:',ipl+1,jpl+1,'and your distance is:',Distance,'blocks'
	elif (Direction=='UP'):
		if (ipl-1>-1):
			Maze[ipl][jpl]='x'
			ipl=ipl-1
			Maze[ipl][jpl]='p'
			Distance=math.fabs(ipl-itr)+math.fabs(jpl-jtr)
			print 'You are at:',ipl+1,jpl+1,'and your distance is:',Distance,'blocks'
	elif (Direction=='DOWN'):
		if (ipl+1<10):
			Maze[ipl][jpl]='x'
			ipl=ipl+1
			Maze[ipl][jpl]='p'
			Distance=math.fabs(ipl-itr)+math.fabs(jpl-jtr)
			print 'You are at:',ipl+1,jpl+1,'and your distance is:',Distance,'blocks'	
	else:
		print 'you did not give a valid input'
	victory=True if ipl==itr and jpl==jtr else False
	for i in range(10):
		print Maze[i]
print 'YOU HAVE FOUND THE TREASURE!!!!'
