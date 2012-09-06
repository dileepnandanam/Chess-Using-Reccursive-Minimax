import minmax
import pygame
import sys

class chessgui:
	def __init__(self):
		pygame.init()
		self.selected=False
		self.bricksize=80
		self.chesscanvas=pygame.display.set_mode((self.bricksize*8,self.bricksize*8))
		
		self.board=minmax.board()
		
		self.black=-1
		self.white=1
		self.pcolor=self.black
		self.opcolor=self.white
		self.highlight=(0,0)
		self.img=[[pygame.image.load("troop/"+i+j+".gif") for j in ("k","q","b","h","f","p")] for i in ("b","w")]
		print self.img
		
		
		
		pygame.display.flip()
		
	def display(self,cell):
		for i in range(8):
			for j in range(8):
				if i%2==0 and j%2==0 or i%2==1 and j%2==1:
					pygame.draw.rect(self.chesscanvas, (225,225,225), ((i*self.bricksize,j*self.bricksize),(self.bricksize,self.bricksize)),0)
				else:
					pygame.draw.rect(self.chesscanvas, (0,100,225), ((i*self.bricksize,j*self.bricksize),(self.bricksize,self.bricksize)),0)
					
		if self.selected:
			pygame.draw.rect(self.chesscanvas, (40,100,15), ((self.highlight[1]*self.bricksize,self.highlight[0]*self.bricksize),(self.bricksize,self.bricksize)),0)
		for i in range(8):
			for j in range(8):
				if not cell[i][j]==None:

					self.chesscanvas.blit(self.img[(cell[i][j].color==self.pcolor and 0 or cell[i][j].color==self.opcolor and 1)][cell[i][j].rank-1], (j*self.bricksize+5,i*self.bricksize+5))		
				
		pygame.display.flip()
			
	def getcell(self,p):
		return (p[1]/self.bricksize,p[0]/self.bricksize)
			
	def main(self):
		self.selected=False
		fr=(0,0)
		to=(0,0)
		cell=self.board.cell
		while True:
			self.display(cell)
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					sys.exit()
				if event.type==pygame.MOUSEBUTTONDOWN:
					if self.selected:
						to=self.getcell(pygame.mouse.get_pos())	
						if not fr==to :
							
							if self.board.movable(cell,self.pcolor,fr[0],fr[1],to[0],to[1]):
								print 'moving to', to								
								self.board.move(cell,fr[0],fr[1],to[0],to[1])
								self.display(cell)
								cell=self.board.bestposition(cell,self.opcolor,3)
								if cell==None or self.board.checkmate(cell,self.pcolor):
									print 'checkmate'
									self.board.boardinit()
								else:
									self.display(cell)
							self.selected=False
					else:
						fr=self.getcell(pygame.mouse.get_pos())
						if not cell[fr[0]][fr[1]]==None and cell[fr[0]][fr[1]].color==self.pcolor:
							self.selected=True
							self.highlight=fr
							print fr, 'self.selected'
	
gui=chessgui()
gui.main()		
