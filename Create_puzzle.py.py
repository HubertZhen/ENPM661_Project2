import pygame
import pygame.gfxdraw

pygame.init()

MAX_X = 300
MAX_Y = 200

obs1_pts = set()
obs2_pts = set()
obs3_pts = set()
obs4_pts = set()
obs5_pts = set()

startColor = (0, 255, 0)
goalColor = (255, 0, 0)
obstacleColor = (0, 0, 0)
pathColor = (0, 0, 255)

puzzleMap = pygame.display.set_mode((MAX_X, MAX_Y))
puzzleMap.fill((255, 255, 255))

pygame.draw.circle(puzzleMap, obstacleColor, (225,50), 25)

pygame.draw.ellipse(puzzleMap, obstacleColor, (110, 80, 80, 40))

pygame.draw.polygon(puzzleMap, obstacleColor, ((95,170),(100,161),(35,124),(30,133)))
pygame.draw.polygon(puzzleMap, obstacleColor, ((20,80),(50,50),(75,80),(100,50),(75,15),(25,15)))
pygame.draw.polygon(puzzleMap, obstacleColor, ((225,190),(250,175),(225,160),(200,175)))


def updateTheStep(position, color):
	pygame.gfxdraw.pixel(puzzleMap, position[0], position[1], color)
	pygame.display.update()


def showPath(pathList):
	for step in pathList:
		pygame.gfxdraw.pixel(puzzleMap, step[0], step[1], pathColor)
		pygame.display.update()


def isValidStep(position):
	pos = tuple(position)
	if(inObs1(pos) == True) or (inObs2(pos) == True) or (inObs3(pos) == True) or (inObs4(pos) == True) or (inObs5(pos) == True):
		return False
	else:
		return True


def inObs1(pos):
	if pos in obs1_pts:
		return True
	else:
		x, y = pos[0], pos[1]
		if ((8 * x + 5 * y <= 1610) and (-38 * x + 65 * y >= 6730) and (9 * x + 5 * y >= 935) and (37 * x - 65 * y >= -7535)):
			obs1_pts.add(pos)
			return True
		else:
			return False

def inObs2(pos):
	if pos in obs2_pts:
		return True
	else:
		x, y = pos[0], pos[1]
		if ((13 * x + y >= 340) and (x + y <= 100) and (-7 * x + 5 * y >= -100) or (-6 * x + 5 * y <= -50) and (6 * x + 5 * y <= 850) and (7 * x - 5 * y <= 450) and \
		 (y >= 15) and (-7 * x + 5 * y <= -100)):
			obs2_pts.add(pos)
			return True
		else:
			return False

def inObs3(pos):
	if pos in obs3_pts:
		return True
	else:
		x, y = pos[0], pos[1]
		if (((x - 150) ** 2) / 1600 + ((y - 100) ** 2) / 400 <= 1):
			obs3_pts.add(pos)
			return True
		else:
			return False

def inObs4(pos):
	if pos in obs4_pts:
		return True
	else:
		x, y = pos[0], pos[1]
		if ((x - 225) ** 2 + (y - 50) ** 2 <= 225):
			obs4_pts.add(pos)
			return True
		else:
			return False

def inObs5(pos):
	if pos in obs5_pts:
		return True
	else:
		x, y = pos[0], pos[1]
		if ((3 * x + 5 * y <= 1625) and  (5 * y - 3 * x <= 275) and (3 * x + 5 * y >= 1475) and (5 * y - 3 * x >= 125)):
			obs5_pts.add(pos)
			return True
		else:
			return False