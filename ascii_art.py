#Generate ASCII art based on this image of Mike Ehrmantraut from Breaking Bad

import pygame, sys, math

pygame.init()

img = pygame.image.load("finger.png") #picture we will convert to ASCII art

width = img.get_width()
height = img.get_height()

screen = pygame.display.set_mode((width,height))
screen.blit(img, (0,0)) #to display image in window

#first, convert the image to black and white
def convert_grayscale(screen):

    #iterate through each pixel of the image
    for i in range (width):
        for j in range(height):
            color = screen.get_at((i,j)) #get color of pixel
            
            #grayscale is when the r, g, b values of the color are equal
            #to ahieve this, take the average of each r, g, and b component, to make them the same
            r = (color[0]+color[1]+color[2])/3
            g = (color[0]+color[1]+color[2])/3
            b = (color[0]+color[1]+color[2])/3
            color = r,g,b

            pygame.draw.rect(screen, color, pygame.Rect(i,j,1,1)) #redraw the pixel with the new shade of gray by drawing a 1x1 pixel rectangle

le_string= "" #this string will store the ASCII characters
size = math.floor(width/100) #the pixel-size of each grid square (195 characters wide)

#next, "pixelate" the image to make it simpler for conversion into ASCII characters
def simplify_grid(screen):
    global le_string
    r=0
    g=0
    b=0

    #iterate through each grid square
    for q in range(math.floor(height/size)):
        for k in range(math.floor(width/size)):

            #iterate through each pixel in the grid square
            for i in range(k*size, k*size+size):
                for j in range(q*size, q*size+size):
                        color = screen.get_at((i,j)) #get color of pixel
                        r+=color[0]
                        g+=color[1]
                        b+=color[2]

            #set grid-square color to the average color of all the pixels in the square
            r = math.floor(r/(size*size))
            g = math.floor(g/(size*size))
            b = math.floor(b/(size*size))
            pygame.draw.rect(screen, (r,g,b), pygame.Rect(k*size,q*size,size,size)) #draw a rectangle with this average color

            #assign grid squares to ASCII characters based on square's brightness
            #if a square is brighter (more white), assign it a "full/bold" character such as @
            if r > 190: le_string+="@@"
            elif r > 160: le_string+="$$"
            elif r > 110: le_string+="%%"
            elif r > 80: le_string+="::"
            elif r > 60: le_string+=".."
            else: le_string+= " "
        le_string+="\n"

convert_grayscale(screen) #make image black and white
simplify_grid(screen) #make image pixelated

print(le_string) #print ascii string

pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
