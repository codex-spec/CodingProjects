"""
This is a python program used to calculate the volume and surface
area of various shapes and size: some of these shapes include
2-D shapes: square, rectangle, circle, hexagon, triangle
3-D shapes: sphere, cube, rectangular prism, hexagonal prism, triangular prism.
"""
import math
import random

name = input("What is your name: ")
#sig = input("Do you want to compute the area/volume of a 2-D or 3-D object: ")
result = 0

#__init__(n):

def getAreaOfSquare(length):
  return length * length

def getAreaOfRectangle(length, width):
  x = int(length)
  y = int(width)
  return x * y

def getAreaOfCircle(radius):
  radius = int(radius)
  return (math.pi) * (radius * radius)

def getAreaOfTriangle(base, height):
  return (base * height)/2

def getAreaOfHexagon(sideLength):
  return ((3/2)*math.sqrt(3))*sideLength

def getAreaOfCube(length):
  return 6*length*length;

def getAreaOfRectanglularPrism(length, width, height):
  return 2*length*width + 2*length*height + 2*width*height

def getAreaOfHexagonalPrism(sideLength, height):
  return (6*sideLength*height) + (3*(math.sqrt(3)))*(sideLength*sideLength)

def getAreaOfTriangularPrism(sideLengthOne, sideLengthTwo, sideLengthThree, height, length):
  return sideLengthOne*height + (sideLengthOne + sideLengthTwo + sideLengthThree * length)

def getAreaOfSphere(radius):
  return 4*math.pi*(radius*radius)

def getVolumeOfCube(sideLength):
    return sideLength*sideLength*sideLength

def getVolumeOfSphere(radius):
    return 4/3*(math.pi*radius*radius*radius)

def getVolumeOfRectangularPrism(width, height, length):
    return width*height*length

def getVolumeOfHexagonalPrism(sideLength, height):
    return 3*((math.sqrt(3)/2)*sideLength*sideLength)*height

def getVolumeOfTriangularPrism(baseLength, sideLength1, sideLength2, height):
    return (1/4)*height* (math.sqrt((-baseLength ** 4) + 2 * ((baseLength*sideLength1) ** 2) + 2*((baseLength*sideLength2) ** 2) - (sideLength1 ** 4) + 2 * ((sideLength1 * sideLength2) ** 2) - (sideLength2 ** 4)))

resultOne = input("Do you want to compute the area/volume of a 2-D or 3-D object: ")
resultTwo = input("Do you want to compute the area or volume: ")
resultThree = input("What shape? ")

#resultFour = input("Input the dimesnsions: ")

def getShapeResult(resultOne, resultTwo, resultThree):
    sig = 0
    result = 0
    if resultOne == "2d" or resultOne == '2D' or resultOne == "two D" or resultOne == "Two D":
        sig = 2
    elif resultOne == "3d" or resultOne == "3D" or resultOne == "three D" or resultOne == "Three D":
        sig  = 3
    else:
        print("invalid response")
        #sig = random.randit(2, 3)

    if sig == 2:
        if resultTwo == "area" or resultTwo == "Area":
            if resultThree == "square" or resultThree == "Square":
                print("Input the dimesnsions")
                inputF = input("Enter square sideLength ")
                result = getAreaOfSquare(inputF)
            elif resultThree == "rectangle" or resultThree == "Rectangle":
                print("Input the dimesnsions")
                inputFI = input("Enter the sideLength")
                inputS = input("Enter the widthLength")
                result = getAreaOfRectangle(inputFI, inputS)
            elif resultThree == "circle" or resultThree == "Circle":
                print("Input the dimesnsions")
                inputR = input("Enter the radius ")
                result = getAreaOfCircle(inputR)
            elif resultThree == "triangle" or resultThree == "Triangle":
                print("Input the dimesnsions")
                inputB = input("Enter the base dimesnsions ")
                inputH = input("Enter the height dimesnsions ")
                result = getAreaOfTriangle(inputB, inputH)
            else:
                inputSL = input("Enter the sideLength ")
                result = getAreaOfHexagon(inputSL)
                print("Input the dimesnsions")
        elif resultTwo == "volume" or resultTwo == "Volume" or resultTwo != "volume" or resultTwo != "Volume" or resultTwo != "area" or resultTwo != "Area":
            print("incorrect response as 2d shapes have no volume or invalid input")
    elif sig == 3:
        if resultTwo == "volume" or resultTwo == "Volume":
            if resultThree == "cube" or resultThree == "Cube":
                print("input the dimesnsions")
                inputCube1 = input("Input the sideLength ")
                result = getVolumeOfCube(inputCube1)
            elif resultThree == "sphere" or resultThree == "Sphere":
                print("input the dimesnsions")
                inputSphere1 = input("input the radius ")
                result = getVolumeOfSphere(inputSphere1)
            elif resultThree == "RectangularPrism" or resultThree == "rectangularprism":
                print("input the dimesnsions")
                inputRectangularPrismW = input("input the width ")
                inputRectangularPrismH = input("input the height ")
                inputRectangularPrismL = input("input the length ")
                result = getVolumeOfRectangularPrism(inputRectangularPrismW, inputRectangularPrismH, inputRectangularPrismL)
            elif resultThree == "HexagonalPrism" or resultThree == "hexagonalprism":
                print("input the dimesnsions")
                inputHexagonalPrismB = input("input the base edge ")
                inputHexagonalPrismH = input("input the height ")
                result = getVolumeOfHexagonalPrism(inputHexagonalPrismB, inputHexagonalPrismH)
            elif resultThree == "TriangularPrism" or resultThree == "triangularprism":
                print("input the dimesnsions")
                inputTriangularPrismBaseLength = input("input the baseLength ")
                inputTriangularPrismSideLength1 = input("input the sideLength1 ")
                inputTriangularPrismSideLength2 = input("input the sideLength2 ")
                inputTriangularPrismHeight = input("input the height of the triangle ")
        elif resultTwo == "area" or resultTwo == "Area":
            if resultThree == "cube" or resultThree == "Cube":
                print("Input the dimesnsions")
                inputCubeD1 = input("input the sideLength ")
                result = getAreaOfCube(inputCubeD1)
            elif resultThree == "sphere" or resultThree == "Sphere":
                printf("input the dimesnsions")
                inputSphereD1 = input("input the radius ")
                result = getAreaOfSphere(inputSphereD1)
            elif resultThree == "RectangularPrism" or resultThree == "rectangularprism":
                print("input the dimesnsions")
                inputRectangularPrismWD1 = input("input the width ")
                inputRectangularPrismHD1 = input("input the height ")
                inputRectangularPrismLD1 = input("input the length ")
                result = getAreaOfRectanglularPrism(inputRectangularPrismWD1, inputRectangularPrismHD1, inputRectangularPrismLD1)
            elif resultThree == "HexagonalPrism" or resultThree == "hexagonalprism":
                print("input the dimesnsions ")
                inputHexagonalPrismSL = input("input the hexagonal prism sideLength ")
                inputHexagonalPrismH1 = input("input the hexagonal prism height ")
                result = getAreaOfHexagonalPrism(inputHexagonalPrismSL, inputHexagonalPrismH1)
            elif resultThree == "TriangularPrism" or resultThree == "triangularprism":
                print("input the dimesnsions ")
                inputTriangularPrismSideLengthOne = input("input the sideLengthOne ")
                inputTriangularPrismSideLengthTwo = input("input the sideLenghtTwo ")
                inputTriangularPrismSidwLengthThree = input("input the sideLengthThree ")
                inputTriangularPrismHeight = input("input the height ")
                inputTriangularPrismLength = input("input the Length ")
                result = getAreaOfTriangularPrism(inputTriangularPrismSideLengthOne, inputTriangularPrismSideLengthTwo, inputTriangularPrismSidwLengthThree, inputTriangularPrismHeight, inputTriangularPrismLength)
    return result

print("The output will be the " + resultTwo + " of a " + resultThree + " and will have the " + resultTwo + " of " + str(getShapeResult(resultOne, resultTwo, resultThree)))
#print(getShapeResult(resultOne, resultTwo, resultThree))
"""
Here will lie the tester code and anything else below it
"""
