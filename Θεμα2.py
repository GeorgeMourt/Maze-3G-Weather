import math
p1b=2
p2b=2
p1m=2
p2m=2
p1s=2
p2s=2

Board=[[['.' for i in range(3)]for i in range(3)]for i in range(4)]
pointer=[[0 for i in range(3)]for i in range(3)]
victory="neither"
for i in range(3):
	print Board[0][i][pointer[0][i]],Board[1][i][pointer[1][i]],Board[2][i][pointer[2][i]]
while victory=="neither":
	print "Player 1's turn"
	while True:
		Pawnfrom=raw_input("Do you want to take a pawn from the BOARD or HAND?")
		if Pawnfrom=="HAND":
			if p1b>0 or p1m>0 or p1s>0:
				Size=raw_input("Do you want a BIG, MEDIUM or SMALL pawn?")
				if Size=="BIG":
					p1b-=1
					break
				elif Size=="MEDIUM":
					p1m-=1
					break
				elif Size=="SMALL":
					p1s-=1
					break
				else:
					print "You did not give a valid input"
			else:
				print "You do not have any pawns in hand.So you will have to take a pawn from the Board"
		if Pawnfrom=="BOARD":
			if p1b==2 and p1m==2 and p1s==2:
				print "You have no pawns on the Board.So you will have to take a pawn from the Board"
			else:
				i=input("Give the horizontal potision:")
				j=input("Give the vertical potision:")
				if i<4 and j<4 and i>0 and j>0 and isinstance(i,int) and isinstance(j,int):
					if pointer[i-1][j-1]>0:
						if Board[i-1][j-1][pointer[i-1][j-1]]=="P1B":
							Board[i-1][j-1][pointer[i-1][j-1]]="."
							pointer[i-1][j-1]-=1
							Size="BIG"
							break
						elif Board[i-1][j-1][pointer[i-1][j-1]]=="P1M":
							Board[i-1][j-1][pointer[i-1][j-1]]="."
							pointer[i-1][j-1]-=1
							Size="MEDIUM"
							break
						elif Board[i-1][j-1][pointer[i-1][j-1]]=="P1S":
							Board[i-1][j-1][pointer[i-1][j-1]]="."
							pointer[i-1][j-1]-=1
							Size="SMALL"
							break
						else:
							print "You have no pawn there"
					else:
						print "You did not give a valid input"
				else:
					print "You did not give a valid input"
	for i in range(3):	
		if Board[0][i][pointer[0][i]]=="P2B" or Board[0][i][pointer[0][i]]=="P2M" or Board[0][i][pointer[0][i]]=="P2S":
			if Board[1][i][pointer[1][i]]=="P2B" or Board[1][i][pointer[1][i]]=="P2M" or Board[1][i][pointer[1][i]]=="P2S":
				if Board[2][i][pointer[2][i]]=="P2B" or Board[2][i][pointer[2][i]]=="P2M" or Board[2][i][pointer[2][i]]=="P2S":
					victory="Player 2"
		elif Board[i][0][pointer[i][0]]=="P2B" or Board[i][0][pointer[i][0]]=="P2M" or Board[i][0][pointer[i][0]]=="P2S":
			if Board[i][1][pointer[i][1]]=="P2B" or Board[i][1][pointer[i][1]]=="P2M" or Board[i][1][pointer[i][1]]=="P2S":
				if Board[i][2][pointer[i][2]]=="P2B" or Board[i][2][pointer[i][2]]=="P2M" or Board[i][2][pointer[i][2]]=="P2S":
					victory="Player 2"
	if Board[0][0][pointer[0][0]]=="P2B" or Board[0][0][pointer[0][0]]=="P2M" or Board[0][0][pointer[0][0]]=="P2S":
		if Board[1][1][pointer[1][1]]=="P2B" or Board[1][1][pointer[1][1]]=="P2M" or Board[1][1][pointer[1][1]]=="P2S":
			if Board[2][2][pointer[2][2]]=="P2B" or Board[2][2][pointer[2][2]]=="P2M" or Board[2][2][pointer[2][2]]=="P2S":
				victory="Player 2"
	if Board[2][0][pointer[2][0]]=="P2B" or Board[2][0][pointer[2][0]]=="P2M" or Board[2][0][pointer[2][0]]=="P2S":
		if Board[1][1][pointer[1][1]]=="P2B" or Board[1][1][pointer[1][1]]=="P2M" or Board[1][1][pointer[1][1]]=="P2S":
			if Board[0][2][pointer[0][2]]=="P2B" or Board[0][2][pointer[0][2]]=="P2M" or Board[0][2][pointer[0][2]]=="P2S":
				victory="Player 2"
	for i in range(3):
		print Board[0][i][pointer[0][i]],Board[1][i][pointer[1][i]],Board[2][i][pointer[2][i]]
	
	if victory=="neither":
		while True:
			print "Player 1 where do you want to put your pawn?"
			i=input("Horizontal:")
			j=input("Vertical:")
			if i<4 and j<4 and i>0 and j>0 and isinstance(i,int) and isinstance(j,int):
				if Size=="BIG" and Board[i-1][j-1][pointer[i-1][j-1]]!="P1B" and Board[i-1][j-1][pointer[i-1][j-1]]!="P2B":
					pointer[i-1][j-1]+=1
					Board[i-1][j-1][pointer[i-1][j-1]]="P1B"
					break
				if Size=="MEDIUM" and Board[i-1][j-1][pointer[i-1][j-1]]!="P1M" and Board[i-1][j-1][pointer[i-1][j-1]]!="P2M" and Board[i-1][j-1][pointer[i-1][j-1]]!="P1B" and Board[i-1][j-1][pointer[i-1][j-1]]!="P2B":
					pointer[i-1][j-1]+=1
					Board[i-1][j-1][pointer[i-1][j-1]]="P1M"
					break
				if Size=="SMALL" and Board[i-1][j-1][pointer[i-1][j-1]]==".":
					pointer[i-1][j-1]+=1
					Board[i-1][j-1][pointer[i-1][j-1]]="P1S"
					break
			else:
				print "You did not give a valid input"
	for i in range(3):
		print Board[0][i][pointer[0][i]],Board[1][i][pointer[1][i]],Board[2][i][pointer[2][i]]
	for i in range(3):	
		if Board[0][i][pointer[0][i]]=="P1B" or Board[0][i][pointer[0][i]]=="P1M" or Board[0][i][pointer[0][i]]=="P1S":
			if Board[1][i][pointer[1][i]]=="P1B" or Board[1][i][pointer[1][i]]=="P1M" or Board[1][i][pointer[1][i]]=="P1S":
				if Board[2][i][pointer[2][i]]=="P1B" or Board[2][i][pointer[2][i]]=="P1M" or Board[2][i][pointer[2][i]]=="P1S":
					victory="Player 1"
		elif Board[i][0][pointer[i][0]]=="P1B" or Board[i][0][pointer[i][0]]=="P1M" or Board[i][0][pointer[i][0]]=="P1S":
			if Board[i][1][pointer[i][1]]=="P1B" or Board[i][1][pointer[i][1]]=="P1M" or Board[i][1][pointer[i][1]]=="P1S":
				if Board[i][2][pointer[i][2]]=="P1B" or Board[i][2][pointer[i][2]]=="P1M" or Board[i][2][pointer[i][2]]=="P1S":
					victory="Player 1"
	if Board[0][0][pointer[0][0]]=="P1B" or Board[0][0][pointer[0][0]]=="P1M" or Board[0][0][pointer[0][0]]=="P1S":
		if Board[1][1][pointer[1][1]]=="P1B" or Board[1][1][pointer[1][1]]=="P1M" or Board[1][1][pointer[1][1]]=="P1S":
			if Board[2][2][pointer[2][2]]=="P1B" or Board[2][2][pointer[2][2]]=="P1M" or Board[2][2][pointer[2][2]]=="P1S":
				victory="Player 1"
	if Board[2][0][pointer[2][0]]=="P1B" or Board[2][0][pointer[2][0]]=="P1M" or Board[2][0][pointer[2][0]]=="P1S":
		if Board[1][1][pointer[1][1]]=="P1B" or Board[1][1][pointer[1][1]]=="P1M" or Board[1][1][pointer[1][1]]=="P1S":
			if Board[0][2][pointer[0][2]]=="P1B" or Board[0][2][pointer[0][2]]=="P1M" or Board[0][2][pointer[0][2]]=="P1S":
				victory="Player 1"

				
	if victory=="neither":
		print "Player 2's turn"
		while True:
			Pawnfrom=raw_input("Do you want to take a pawn from the BOARD or HAND?")
			if Pawnfrom=="HAND":
				if p2b>0 or p2m>0 or p2s>0:
					Size=raw_input("Do you want a BIG, MEDIUM or SMALL pawn?")
					if Size=="BIG":
						p2b-=1
						break
					elif Size=="MEDIUM":
						p2m-=1
						break
					elif Size=="SMALL":
						p2s-=1
						break
					else:
						print "You did not give a valid input"
				else:
					print "You do not have any pawns in hand.So you will have to take a pawn from the Board"
			if Pawnfrom=="BOARD":
				if p2b==2 and p2m==2 and p2s==2:
					print "You have no pawns on the Board.So you will have to take a pawn from the Board"
				else:
					i=input("Give the horizontal potision:")
					j=input("Give the vertical potision:")
					if i<4 and j<4 and i>0 and j>0 and isinstance(i,int) and isinstance(j,int):
						if pointer[i-1][j-1]>0:
							if Board[i-1][j-1][pointer[i-1][j-1]]=="P2B":
								Board[i-1][j-1][pointer[i-1][j-1]]="."
								pointer[i-1][j-1]-=1
								Size="BIG"
								break
							elif Board[i-1][j-1][pointer[i-1][j-1]]=="P2M":
								Board[i-1][j-1][pointer[i-1][j-1]]="."
								pointer[i-1][j-1]-=1
								Size="MEDIUM"
								break
							elif Board[i-1][j-1][pointer[i-1][j-1]]=="P2S":
								Board[i-1][j-1][pointer[i-1][j-1]]="."
								pointer[i-1][j-1]-=1
								Size="SMALL"
								break
							else:
								print "You have no pawn there"
						else:
							print "You did not give a valid input"
					else:
						print "You did not give a valid input"
		for i in range(3):	
			if Board[0][i][pointer[0][i]]=="P1B" or Board[0][i][pointer[0][i]]=="P1M" or Board[0][i][pointer[0][i]]=="P1S":
				if Board[1][i][pointer[1][i]]=="P1B" or Board[1][i][pointer[1][i]]=="P1M" or Board[1][i][pointer[1][i]]=="P1S":
					if Board[2][i][pointer[2][i]]=="P1B" or Board[2][i][pointer[2][i]]=="P1M" or Board[2][i][pointer[2][i]]=="P1S":
						victory="Player 1"
			elif Board[i][0][pointer[i][0]]=="P1B" or Board[i][0][pointer[i][0]]=="P1M" or Board[i][0][pointer[i][0]]=="P1S":
				if Board[i][1][pointer[i][1]]=="P1B" or Board[i][1][pointer[i][1]]=="P1M" or Board[i][1][pointer[i][1]]=="P1S":
					if Board[i][2][pointer[i][2]]=="P1B" or Board[i][2][pointer[i][2]]=="P1M" or Board[i][2][pointer[i][2]]=="P1S":
						victory="Player 1"
		if Board[0][0][pointer[0][0]]=="P1B" or Board[0][0][pointer[0][0]]=="P1M" or Board[0][0][pointer[0][0]]=="P1S":
			if Board[1][1][pointer[1][1]]=="P1B" or Board[1][1][pointer[1][1]]=="P1M" or Board[1][1][pointer[1][1]]=="P1S":
				if Board[2][2][pointer[2][2]]=="P1B" or Board[2][2][pointer[2][2]]=="P1M" or Board[2][2][pointer[2][2]]=="P1S":
					victory="Player 1"
		if Board[2][0][pointer[2][0]]=="P1B" or Board[2][0][pointer[2][0]]=="P1M" or Board[2][0][pointer[2][0]]=="P1S":
			if Board[1][1][pointer[1][1]]=="P1B" or Board[1][1][pointer[1][1]]=="P1M" or Board[1][1][pointer[1][1]]=="P1S":
				if Board[0][2][pointer[0][2]]=="P1B" or Board[0][2][pointer[0][2]]=="P1M" or Board[0][2][pointer[0][2]]=="P1S":
					victory="Player 1"
		for i in range(3):
			print Board[0][i][pointer[0][i]],Board[1][i][pointer[1][i]],Board[2][i][pointer[2][i]]
		
		if victory=="neither":
			while True:
				print "Player 2 where do you want to put your pawn?"
				i=input("Horizontal:")
				j=input("Vertical:")
				if i<4 and j<4 and i>0 and j>0 and isinstance(i,int) and isinstance(j,int):
					if Size=="BIG" and Board[i-1][j-1][pointer[i-1][j-1]]!="P1B" and Board[i-1][j-1][pointer[i-1][j-1]]!="P2B":
						pointer[i-1][j-1]+=1
						Board[i-1][j-1][pointer[i-1][j-1]]="P2B"
						break
					if Size=="MEDIUM" and Board[i-1][j-1][pointer[i-1][j-1]]!="P1M" and Board[i-1][j-1][pointer[i-1][j-1]]!="P2M" and Board[i-1][j-1][pointer[i-1][j-1]]!="P1B" and Board[i-1][j-1][pointer[i-1][j-1]]!="P2B":
						pointer[i-1][j-1]+=1
						Board[i-1][j-1][pointer[i-1][j-1]]="P2M"
						break
					if Size=="SMALL" and Board[i-1][j-1][pointer[i-1][j-1]]==".":
						pointer[i-1][j-1]+=1
						Board[i-1][j-1][pointer[i-1][j-1]]="P2S"
						break
				else:
					print "You did not give a valid input"
		for i in range(3):
			print Board[0][i][pointer[0][i]],Board[1][i][pointer[1][i]],Board[2][i][pointer[2][i]]
		for i in range(3):	
			if Board[0][i][pointer[0][i]]=="P2B" or Board[0][i][pointer[0][i]]=="P2M" or Board[0][i][pointer[0][i]]=="P2S":
				if Board[1][i][pointer[1][i]]=="P2B" or Board[1][i][pointer[1][i]]=="P2M" or Board[1][i][pointer[1][i]]=="P2S":
					if Board[2][i][pointer[2][i]]=="P2B" or Board[2][i][pointer[2][i]]=="P2M" or Board[2][i][pointer[2][i]]=="P2S":
						victory="Player 2"
			elif Board[i][0][pointer[i][0]]=="P2B" or Board[i][0][pointer[i][0]]=="P2M" or Board[i][0][pointer[i][0]]=="P2S":
				if Board[i][1][pointer[i][1]]=="P2B" or Board[i][1][pointer[i][1]]=="P2M" or Board[i][1][pointer[i][1]]=="P2S":
					if Board[i][2][pointer[i][2]]=="P2B" or Board[i][2][pointer[i][2]]=="P2M" or Board[i][2][pointer[i][2]]=="P2S":
						victory="Player 2"
		if Board[0][0][pointer[0][0]]=="P2B" or Board[0][0][pointer[0][0]]=="P2M" or Board[0][0][pointer[0][0]]=="P2S":
			if Board[1][1][pointer[1][1]]=="P2B" or Board[1][1][pointer[1][1]]=="P2M" or Board[1][1][pointer[1][1]]=="P2S":
				if Board[2][2][pointer[2][2]]=="P2B" or Board[2][2][pointer[2][2]]=="P2M" or Board[2][2][pointer[2][2]]=="P2S":
					victory="Player 2"
		if Board[2][0][pointer[2][0]]=="P2B" or Board[2][0][pointer[2][0]]=="P2M" or Board[2][0][pointer[2][0]]=="P2S":
			if Board[1][1][pointer[1][1]]=="P2B" or Board[1][1][pointer[1][1]]=="P2M" or Board[1][1][pointer[1][1]]=="P2S":
				if Board[0][2][pointer[0][2]]=="P2B" or Board[0][2][pointer[0][2]]=="P2M" or Board[0][2][pointer[0][2]]=="P2S":
					victory="Player 2"

print victory," has won"