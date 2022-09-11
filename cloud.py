# TODO: Cloud class

class Cloud(object):
    def __init__(self, xpos, ypos, _size, display):
        self.xpos = xpos
        self.ypos = ypos
        self._size = _size
        self.display = display
    def display(self):
        cloud = createShape()
        cloud.beginShape()
        cloud.noStroke()
        


        cloud.endShape(CLOSE)
        shape(cloud, self.xpos, self.ypos)
        
