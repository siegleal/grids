import time

class world:

    actors = []
    sizex = 0
    sizey = 0
    grid = [[]]
    
    def __init__(self, x, y):
        self.grid = [[0 for i in xrange(x)] for j in xrange(y)]
        self.sizex = x
        self.sizey = y

    def isInGrid(self, x, y):
        if x < 0 or y < 0:
            return False
        if x > self.sizex - 1 or y > self.sizey - 1:
            return False
        return True

    def addActor(self, actor):
        self.actors.append(actor)

    def removeActor(self, actor):
        self.actors.remove(actor)

    def drawWorld(self):
        self.grid = [[0 for i in xrange(self.sizex)] for j in xrange(self.sizey)]
        for a in self.actors:
            self.grid[a.locy][a.locx] = 1
        for i in xrange(self.sizex):
            for j in xrange(self.sizey):
                print self.grid[i][j],
            print

    def tick(self):
        for a in self.actors:
            a.act()
        

class actor(object):

    locx = 0
    loxy = 0
    direction = 0
    world = 0

    def __init__(self,x,y, d, w):
        self.locx = x
        self.locy = y
        self.direction = d
        self.world = w

    def act(self): pass

class walker(actor):

    def act(self):
        if self.direction == 0: #up
            self.locy -= 1
        elif self.direction == 1: #right
            self.locx += 1
        elif self.direction == 2: #down
            self.locy += 1
        else: #left
            self.locx -= 1

        if not self.world.isInGrid(self.locx, self.locy):
            self.world.removeActor(self)

w = world(5,5)
a = walker(0,1,1,w)
w.addActor(a)

while (True):
    w.drawWorld()
    w.tick()
    print
    time.sleep(1)


