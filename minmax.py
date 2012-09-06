
class troop:
	def __init__(self,rank,color):
		self.rank=rank
		self.color=color
		self.fighting=True
		self.ontimeability=True
			
	
			
class board:
	def __init__(self):
		self.cell=[[None for i in range(8)] for j in range(8)]
		
		self.boardinit()
		#self.testcase()
		#self.maxforecast=3
		
		
	def boardinit(self):		
		self.cell[1][0]=troop(6,1)
		self.cell[1][1]=troop(6,1)
		self.cell[1][2]=troop(6,1)
		self.cell[1][3]=troop(6,1)
		self.cell[1][4]=troop(6,1)
		self.cell[1][5]=troop(6,1)
		self.cell[1][6]=troop(6,1)
		self.cell[1][7]=troop(6,1)
		self.cell[0][0]=troop(5,1)
		self.cell[0][1]=troop(4,1)
		self.cell[0][2]=troop(3,1)
		self.cell[0][3]=troop(2,1)
		self.cell[0][4]=troop(1,1)
		self.cell[0][5]=troop(3,1)
		self.cell[0][6]=troop(4,1)
		self.cell[0][7]=troop(5,1)
		
		self.cell[6][0]=troop(6,-1)
		self.cell[6][1]=troop(6,-1)
		self.cell[6][2]=troop(6,-1)
		self.cell[6][3]=troop(6,-1)
		self.cell[6][4]=troop(6,-1)
		self.cell[6][5]=troop(6,-1)
		self.cell[6][6]=troop(6,-1)
		self.cell[6][7]=troop(6,-1)
		self.cell[7][0]=troop(5,-1)
		self.cell[7][1]=troop(4,-1)
		self.cell[7][2]=troop(3,-1)
		self.cell[7][4]=troop(2,-1)
		self.cell[7][3]=troop(1,-1)
		self.cell[7][5]=troop(3,-1)
		self.cell[7][6]=troop(4,-1)
		self.cell[7][7]=troop(5,-1)
	def testcase(self):
			
		self.cell[0][0]=troop(1,1)
		self.cell[1][7]=troop(5,-1)
		self.cell[7][6]=troop(2,-1)
		
		
	
	def inside(self,x,y):
		if x>=0 and x<8 and y>=0 and y<8: 
			return True
		return False
	
	
	def copy(self,cell):
		return [[cell[j][i] for i in range(8)] for j in range(8)]
	
	
	
	def safe(self,i,j,cell,color):
		
		for (d1,d2) in ((1,1),(-1,-1),(-1,1),(1,-1)):
			x=i
			y=j
			while True:
				x+=d1
				y+=d2
				
				if not self.inside(x,y):
					break
				elif not cell[x][y]==None:
					if not cell[x][y].color==color and (cell[x][y].rank in (2,3)):
						return False
					break
		for (d1,d2) in ((0,1),(1,0),(0,-1),(-1,0)):
			x=i
			y=j
			while True:
				x+=d1
				y+=d2
				
				if not self.inside(x,y):
					break
				elif not cell[x][y]==None:
					if not cell[x][y].color==color and (cell[x][y].rank in (2,5)):
						return False
					break
		
		for (d1,d2) in ((2,1),(-2,-1),(2,-1),(-2,1),(1,2),(-1,-2),(-1,2),(1,-2)):
			if self.inside(i+d1,j+d2):	
				if not cell[i+d1][j+d2]==None and not cell[i+d1][j+d2].color==color and cell[i+d1][j+d2].rank==4:
					return False
		for (d1,d2) in ((color,1),(color,-1)):
			if self.inside(i+d1,j+d2):	
				if not cell[i+d1][j+d2]==None and not cell[i+d1][j+d2].color==color and cell[i+d1][j+d2].rank==6:
					return False
		for (d1,d2) in ((-1,-1),(1,-1),(-1,1),(1,1),(0,1),(1,0),(0,-1),(-1,0)):
			if self.inside(i+d1,j+d2):	
				if not cell[i+d1][j+d2]==None and not cell[i+d1][j+d2].color==color and cell[i+d1][j+d2].rank==1:
					return False
		return True
					
	def coverage(self,i,j,cell):
	
		color=cell[i][j].color
		rang=[]					
		for (x,y) in self.force(color,cell):
			if cell[x][y].rank==1:
				kx=x
				ky=y
				
				break
					
		#if not self.safe(kx,ky,cell,color) and not cell[i][j].rank==1:
		#	print 'check'
		#	return rang			
				
		
		if cell[i][j].rank==1:
			
			for (d1,d2) in ((-1,-1),(1,-1),(-1,1),(1,1),(0,1),(1,0),(0,-1),(-1,0)):
				if self.inside(i+d1,j+d2):	
					if (cell[i+d1][j+d2]==None or not cell[i+d1][j+d2].color==color) and self.safe(i+d1,j+d2,cell,color):
						rang.append((i+d1,j+d2))
			
								
		elif cell[i][j].rank==2:
			for (d1,d2) in ((0,1),(1,1),(1,0),(0,-1),(-1,-1),(-1,0),(-1,1),(1,-1)):
				
				x=i
				y=j
				while True:
					
					x+=d1
					y+=d2
					if not self.inside(x,y):
						break
					elif cell[x][y]==None:
						rang.append((x,y))
					else:
						if not cell[x][y].color==color:
							rang.append((x,y))
						break
							
						
		
		elif cell[i][j].rank==3:
		
			for (d1,d2) in ((1,1),(-1,-1),(-1,1),(1,-1)):
				
				x=i
				y=j
				while True:
					
					x+=d1
					y+=d2
					if not self.inside(x,y):
						break
					elif cell[x][y]==None:
						rang.append((x,y))
					else:
						if not cell[x][y].color==color:
							rang.append((x,y))
						break
		
		
			
		elif cell[i][j].rank==4:
			for (d1,d2) in ((2,1),(-2,-1),(2,-1),(-2,1),(1,2),(-1,-2),(-1,2),(1,-2)):
				if self.inside(i+d1,j+d2):	
					if cell[i+d1][j+d2]==None:
						rang.append((i+d1,j+d2))
					elif not cell[i+d1][j+d2].color==color:
						rang.append((i+d1,j+d2))

		elif cell[i][j].rank==5:
			for (d1,d2) in ((0,1),(1,0),(0,-1),(-1,0)):
				
				x=i
				y=j
				while True:
					
					x+=d1
					y+=d2
					if not self.inside(x,y):
						break
					elif cell[x][y]==None:
						rang.append((x,y))
					else:
						if not cell[x][y].color==color:
							rang.append((x,y))
						break
		elif cell[i][j].rank==6:
			if self.inside(i+cell[i][j].color,j):
				if cell[i+cell[i][j].color][j]==None:
					rang.append((i+cell[i][j].color,j))
					if cell[i][j].color==-1 and i==6 or cell[i][j].color==1 and i==1:
						if cell[i+cell[i][j].color*2][j]==None:
							rang.append((i+cell[i][j].color*2,j))
				
			if self.inside(i+cell[i][j].color,j+1) and not cell[i+cell[i][j].color][j+1]==None and not cell[i+cell[i][j].color][j+1].color==color:
				rang.append((i+cell[i][j].color,j+1))
			if self.inside(i+cell[i][j].color,j-1) and not cell[i+cell[i][j].color][j-1]==None and not cell[i+cell[i][j].color][j-1].color==color:
				rang.append((i+cell[i][j].color,j-1))
		
		
		frang=[]
		if cell[i][j].rank==1:
			return rang
		else:
			for (x,y) in rang:
			
				if self.safe(kx,ky,self.move(self.copy(cell),i,j,x,y),color):
					frang.append((x,y))
		
		return frang	
	def move(self,cell,i,j,x,y):
		cell[x][y]=cell[i][j]
		cell[i][j]=None
		return cell
	def movable(self,cell,color,i,j,x,y):
		if not cell[x][y]==None and cell[x][y].color==color:
			return False
		
		return((x,y) in self.coverage(i,j,cell))
	def force(self,color,cell):
		l=[]
		for i in range(8):
			for j in range(8):
				if not cell[i][j]== None and cell[i][j].color==color:
					l.append((i,j))
		return l 
	def power(self,color,cell):
		p=0
		for (x,y) in self.force(color,cell):
			p+=7-cell[x][y].rank
		
		return p
	def profit(self,cell,color,pcolor,pforce,oforce,depth):
		npforce=self.power(pcolor,cell)
		noforce=self.power(pcolor*-1,cell)
		checkbenifit=0
		if depth==0:
			
			return (npforce-pforce+oforce-noforce)*100
			

		for (x,y) in self.force(color,cell):
			
			if cell[x][y].rank==1:
				
				if not self.safe(x,y,cell,color):
					
					if len(self.coverage(x,y,cell))==0:
						
						return (color==pcolor and -100 or 100)*depth*100
						
					possible=self.coverage(x,y,cell)
					c=0
					for (p,q) in possible:
						c+=self.profit(self.move(self.copy(cell),x,y,p,q),color*-1,pcolor,npforce,noforce,depth-1)
					
					return c+checkbenifit+(npforce-pforce+oforce-noforce)*100*depth*100
			break
		
		
		
		c=0
		for (x,y) in self.force(color,cell):
			possible=self.coverage(x,y,cell)
			
			for (p,q) in possible:
				c+=self.profit(self.move(self.copy(cell),x,y,p,q),color*-1,pcolor,npforce,noforce,depth-1)
		
				
		return c+(npforce-pforce+oforce-noforce)*100*depth*100
					
					
	def checkmate(self,cell,color):
		possible=0
		for (x,y) in self.force(color,cell):
			
			if cell[x][y].rank==1:
				if self.safe(x,y,cell,color):
					return False
			possible+=len(self.coverage(x,y,cell))
	
		if possible==0:
			return True
		else:
			return False
			
	def bestpos(self,cell,color,pcolor,depth):	
		bestprofit=-999999
		
		best=None
		npforce=self.power(color,cell)
		noforce=self.power(color*-1,cell)
		for (x,y) in self.force(color,cell):
			
			if cell[x][y].rank==1:
				
				if not self.safe(x,y,cell,color):
					
					if self.checkmate(cell,color):
						
						return None
				break
				
		
			
		bestprofit=-99999
		for (x,y) in self.force(color,cell):
			possible=self.coverage(x,y,cell)
		
			
			for (p,q) in possible:
				 
				c=self.profit(self.move(self.copy(cell),x,y,p,q),color*-1,pcolor,npforce,noforce,depth-1)
				print (x,y), (p,q), c
				
				if c>=bestprofit:
					best=self.move(self.copy(cell),x,y,p,q)
					bestprofit=c
					
		return best
	def bestposition(self,cell,color,depth):
		return self.bestpos(cell,color,color,depth)
		
