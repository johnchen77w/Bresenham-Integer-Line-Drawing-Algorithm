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

        x1, y1 = p1
        x2, y2 = p2

        dx = x2 - x1
        dy = y2 - y1

        try:
            slope = dy/dx
        except ZeroDivisionError:
            slope = None
        
        if slope is None:
            # vertical line
            y = min(y1, y2)
            for i in range(abs(dy)):
                self.drawPixel((x1, y + i), color)
        else:
            # x > 0
            if x1 < x2:
                # Q1
                if y1 < y2:
                    # Octant 1
                    if 0 <= slope and slope <= 1:
                        self.drawPixel((x1, y1), color)
                        pi = 2 * dy - dx
                        for i in range(abs(dx)):
                            if pi < 0:
                                pi = pi + 2 * dy
                            else:
                                pi = pi + 2 * dy - 2 * dx
                                y1 += 1
                            x1 += 1
                            self.drawPixel((x1, y1), color)
                    # Octant 2
                    elif 1 < slope and slope < math.inf:
                        self.drawPixel((x1, y1), color)
                        pi = 2 * dx - dy
                        for i in range(abs(dy)):
                            if pi < 0:
                                pi = pi + 2 * dx
                            else:
                                pi = pi + 2 * dx - 2 * dy
                                x1 += 1
                            y1 += 1
                            self.drawPixel((x1, y1), color)
                # Q4
                else:
                    # Octant 7
                    if -1 > slope and slope > -math.inf:
                        self.drawPixel((x1, y1), color)
                        p = 2 * dx - (-dy)
                        for i in range(abs(-dy)):
                            if p < 0:
                                p = p + 2 * dx
                            else:
                                p = p + 2 * dx - 2 * (-dy)
                                x1 += 1
                            y1 -= 1
                            self.drawPixel((x1, y1), color)
                    # Octant 8
                    elif 0 >= slope and slope >= -1:
                        self.drawPixel((x1, y1), color)
                        p = 2 * (-dy) - dx
                        for i in range(abs(dx)):
                            if p < 0:
                                p = p + 2 * (-dy)
                            else:
                                p = p + 2 * (-dy) - 2 * dx
                                y1 -= 1
                            x1 += 1
                            self.drawPixel((x1, y1), color)
            # x < 0
            elif x1 > x2:
                # Q2
                if y1 < y2:
                    # Octant 3
                    if -1 > slope and slope > -math.inf:
                        self.drawPixel((x1, y1), color)
                        p = 2 * (-dx) - dy
                        for i in range(abs(dy)):
                            if p < 0:
                                p = p + 2 * (-dx)
                            else:
                                p = p + 2 * (-dx) - 2 * dy
                                x1 -= 1
                            y1 += 1
                            self.drawPixel((x1, y1), color)
                    # Octant 4
                    elif 0 >= slope and slope >= -1:
                        self.drawPixel((x1, y1), color)
                        p = 2 * dy - (-dx)
                        for i in range(abs(dx)):
                            if p < 0:
                                p = p + 2 * dy
                            else:
                                p = p + 2 * dy - 2 * (-dx)
                                y1 += 1
                            x1 -= 1
                            self.drawPixel((x1, y1), color)
                # Q3
                else:
                    # Octant 5
                    if 0 <= slope and slope <= 1:
                        self.drawPixel((x1, y1), color)
                        p = 2 * (-dy) - (-dx)
                        for i in range(abs(dx)):
                            if p < 0:
                                p = p + 2 * (-dy)
                            else:
                                p = p + 2 * (-dy) - 2 * (-dx)
                                y1 -= 1
                            x1 -= 1
                            self.drawPixel((x1, y1), color)
                    # Octant 6
                    elif 1 < slope and slope < math.inf:
                        self.drawPixel((x1, y1), color)
                        p = 2 * (-dx) - (-dy)
                        for i in range(abs(-dy)):
                            if p < 0:
                                p = p + 2 * (-dx)
                            else:
                                p = p + 2 * (-dx) - 2 * (-dy)
                                x1 -= 1
                            y1 -= 1
                            self.drawPixel((x1, y1), color)
            