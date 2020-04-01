"""
i know code is bad but it works ☺
"""

def lefttoright(word,a,space):
	for i in range(len(word)):
		print(space,word[:a],"  ",word[a:])
		a+=1
		space+="  "
def righttoleft(word,a,space):
	for i in range(len(word)):
		b=""
		for i in word[:a]:
			b+=i
		c=""
		for i in word[a:]:
			c+=i
		d=""
		for i in space:
			d+=i
		print(d,c,"  ",b)
		a+=1
		space.pop()
		space.pop()
for i in range(50):
	word="quarantined"
	a=1
	space="  "	

	lefttoright(word,a,space)
	
	word=['q', 'u', 'a', 'r', 'a', 'n', 't', 'i', 'n', 'e', 'd']
	a=1
	space=[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
	righttoleft(word,a,space)
