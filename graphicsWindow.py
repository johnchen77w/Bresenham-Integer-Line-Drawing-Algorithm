from PIL import Image

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
        self.__image[p1[0],p1[1]] = color
        self.__image[p2[0],p2[1]] = color
        
        x1 = p1[0]
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)

        while (x1 < x2):
            err = 2*dy - dx
            if err >= 0:
                err = err + 2*dy - 2*dx
                y1 = y1 + 1
            else:
                err = err + 2*dy
            x1 = x1 + 1