import random
import itertools
import collections
class Node():
	"""docstring for ClassName"""
	def __init__(self, puzzle,parent=None,action=None):
		self.puzzle=puzzle
		self.parent=parent
		self.action=action
		if (self.parent !=None):
			self.g= parent.g +1	
		else:
			self.g = 0
	def score(self):
		return(self.g+self.h)
	def state(self):
		return str(self)
	def path(self):
		node . p =self,[]
		while node:
			p.append(node)
			node=node.parent
		yield from reversed(p)
	def solve(self):
		return self.puzzle.solved
	def action(self):
		return self.puzzle.action
	def h(self):
		return self.puzzle.manhattan
	def f(self):
		return	self.h + self.g
	def __str__(self):
		return	str(self.puzzle)
class Solver:

	def __init__(self,start):
		self.start=start
	def solve(self):
		queue = collections.deque([Node(self.start)])
		seen =set()
		seen.add(queue[0].state)
		while queue:
			queue = collections.deque(sorted(List(queue),key=lambda node:node.f))
			node = queue.popleft()
			if node.sloved:
				return node.path
			for move, action in node.actions:
				child= Node(move(),node,action)
				if child.state not in seen:
					queue.appendleft(child)
					seen.add(child.state)
class Puzzle:
	def __init__(self,board):
		self.width=len(board[0])
		self.board = board
	def sloved(self):
		N=self.width*self.width
		return str(self) ==''.join(map(str,range(1,N)))+'0'
	def actions(self):
		def create_move(at,to):
			return lambda:self._move(at,to)
			moves =[]
		for i,j in itertools.product(range(self.width),range(self.width)):
			direcs ={'R':(i,j-1),
					'L':(i,j+1),
					'U':(i+1,j),
					'D':(i-1,j)}
			for action, (r,c) in direcs.items():
				if r>=0 and c>=0 and r<self.width and c<self.width and \
				self.board[r][c]==0:
					move = create_move((i,j),(r,c),action)
					move.append(move)

		return moves
	def manhattan(self):
		distance = 0
		for i in range(3):
			for j in range(3):
				if self.board[i][j]!=0:
					x,y - divmod(self.board[i][j]-1,3)
					distance+=abs(x-i)+abs(y-j)
			return distance	
	def shuffle(self):
		puzzle = self
		for _ in range(1000):
			puzzle=random.choice(puzzle.actions)[0]()
		return puzzle
	def copy(self):
		board=[]
		for row in self.board:
			board.append([x for x in row])
		return Puzzle(board)
	def move(self,at,to):
		copy = self.copy()
		i,j =at
		r,c=to
		copy.board[i][j],copy.board[r][c]=copy.board[r][c],copy.board[i][j]
		return copy
	def pprint(self):
		for row in self.board:
			print(row)
		print()
	def __str__(self):
		return ''.join(map(str,self))
	def __iter__(self):
		for row in self.board:
			yield from row
#board
board=[[7,3,4],[6,0,5],[2,1,8]]
puzzle =Puzzle(board)
s=Solver(puzzle)
p=s.solve()
step=0
for node in p:
	print(node.action)
	noode.puzzle.pprint()
	step=step+1;

print('total step:',str(steps))