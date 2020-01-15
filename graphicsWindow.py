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
        x1 = p1[0]
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]

        dx = x2 - x1
        dy = y2 - y1

        self.drawPixel((x1,y1), color)
        for x in range(x1, x2 + 1): 
            if x == x1:
                p = 2*dy - dx
            else:    
                if p >= 0:
                    p = p + 2*dy - 2*dx
                    y1 = y1 + 1
                else:
                    p = p + 2*dy
                x1 = x1 + 1
                self.drawPixel((x1,y1), color)