from PIL import Image
import math

class graphicsWindow:

    def __init__(self,width=640,height=480):
        self.__mode = 'RGB'
        self.__width = width
        self.__height = height
        self.__canvas = Image.new(self.__mode,(self.__width,self.__height))
        self.__image = self.__canvas.load()

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def drawPixel(self,pixel,color):
        self.__image[pixel[0],pixel[1]] = color

    def saveImage(self,fileName):
        self.__canvas.save(fileName)

    # do we add a self in front? HUH
    def drawLine(self,p1,p2,color):

        def bresenham_odd (x1, y1, dx, dy, inc_x, inc_y):
            self.drawPixel((x1, y1), color)
            p = 2 * dy - dx
            for x in range(abs(dx)):
                if p < 0:
                    p = p + 2 * dy
                else:
                    p = p + 2 * dy - 2 * dx
                    y1 += inc_y
                x1 += inc_x
                self.drawPixel((x1, y1), color)

        def bresenham_even (x1, y1, dx, dy, inc_x, inc_y):
            self.drawPixel((x1, y1), color)
            p = 2 * dx - dy
            for y in range(abs(dy)):
                if p < 0:
                    p = p + 2 * dx
                else:
                    p = p + 2 * dx - 2 * dy
                    x1 += inc_x
                y1 += inc_y
                self.drawPixel((x1, y1), color)

        x1, y1 = p1
        x2, y2 = p2
        dx = x2 - x1
        dy = y2 - y1

        try: slope = dy/dx
        except ZeroDivisionError: slope = None
        
        if slope is None:   # vertical line
            y = min(y1, y2)
            for i in range(abs(dy)): self.drawPixel((x1, y + i), color)
        elif slope == 0:    # horizontal line
            x = min(x1, x2)
            for i in range(abs(dx)): self.drawPixel((x + i, y1), color)
        else:
            if x1 < x2 and y1 < y2 and 0 <= slope and slope <= 1: bresenham_odd (x1, y1, dx, dy, 1, 1)                  # Octant 1
            elif x1 < x2 and y1 < y2 and 1 < slope and slope < math.inf: bresenham_even (x1, y1, dx, dy, 1, 1)          # Octant 2
            elif x1 > x2 and y1 < y2 and -1 > slope and slope > -math.inf: bresenham_even (x1, y1, -dx, dy, -1, 1)      # Octant 3
            elif x1 > x2 and y1 < y2 and 0 >= slope and slope >= -1: bresenham_odd (x1, y1, -dx, dy, -1, 1)             # Octant 4
            elif x1 > x2 and y1 > y2 and 0 <= slope and slope <= 1: bresenham_odd (x1, y1, -dx, -dy, -1, -1)            # Octant 5
            elif x1 > x2 and y1 > y2 and 1 < slope and slope < math.inf: bresenham_even (x1, y1, -dx, -dy, -1, -1)      # Octant 6
            elif x1 < x2 and y1 > y2 and -1 > slope and slope > -math.inf: bresenham_even (x1, y1, dx, -dy, 1, -1)      # Octant 7
            elif x1 < x2 and y1 > y2 and 0 >= slope and slope >= -1: bresenham_odd (x1, y1, dx, -dy, 1, -1)             # Octant 8