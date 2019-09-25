#!/usr/bin/python3
import numpy as np

N = [4,6,8,10]

def attack_block(state,row,col):
	new_state = np.copy(state)
	availBlock = []
	for i in range(n):
		for j in range(n):
			if(i == row or j == col or i+j==row+col or i-j == row-col):
				new_state[i,j] = 1
			elif(state[i,j]==0 and j==col+1):
				availBlock.append(i)
	if(availBlock):
		naive_algorithm(new_state,availBlock,col+1)
	#else:
	#	print("Faluire")


def naive_algorithm(state,availBlock,col):
	global success_count
	for row in availBlock:
		if(col == n-1):
			success_count +=1
			#print("Success")
		else:
			attack_block(state,row,col)
		
if __name__ == '__main__':
	for n in N:
		success_count= 0
		possible = [i for i in range(n)]
		state = np.zeros([n,n])
		naive_algorithm(state,possible,0)
		print('number of solutions for ',n,'queens is: ',success_count)

