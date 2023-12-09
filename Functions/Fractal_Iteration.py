import pygame, math

def fractal(x, y, size, angle, n):
  if n > 1:
  #base
    pygame.draw.line(screen, "black", [x-size*math.cos(angle), y-size*math.sin(angle)], [x+size*math.cos(angle), y+size*math.sin(angle)])
  #left triangle line
    pygame.draw.line(screen, "black", [x-size/3*math.cos(angle), y-size*math.sin(angle)/3], [x+size*1/2*math.cos(angle-math.pi/2), y+size*1/2*math.sin(angle-math.pi/2)])
  #right triangle line
    pygame.draw.line(screen, "black", [x+size/3*math.cos(angle), y+size*math.sin(angle)/3], [x+size*1/2*math.cos(angle-math.pi/2), y+size*1/2*math.sin(angle-math.pi/2)])
  #erase middle
    pygame.draw.line(screen, "white", [x-size/3*math.cos(angle), y-size/3*math.sin(angle)], [x+size/3*math.cos(angle), y+size/3*math.sin(angle)], 2)
  #recursion
    return fractal(x-size*2/3*math.cos(angle), y-size*2/3*math.sin(angle), size/3, angle, n-1), fractal(x+size*2/3*math.cos(angle), y+size*2/3*math.sin(angle), size/3, angle, n-1), fractal((x-size/3*math.cos(angle) + x+size*1/2*math.cos(angle-math.pi/2))/2, (y-size*math.sin(angle)/3+y+size*1/2*math.sin(angle-math.pi/2))/2, size/3.225, angle - (math.pi/3-math.pi/50), n-1), fractal((x+size/3*math.cos(angle) + x+size*1/2*math.cos(angle-math.pi/2))/2, (y+size*math.sin(angle)/3 + y+size*1/2*math.sin(angle-math.pi/2))/2, size/3.225, angle + (math.pi/3-math.pi/50), n-1)
  #recursion end
  else:
    return 0;
pygame.init()

size = (720, 520)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("NIGHTMARENIGHTMARENIGHTMARENIGHTMARENIGHTMARENIGHTMARENIGHTMARENIGHTMARENIGHTMARENIGHTMARENIGHTMARENIGHTMARENIGHTMARENIGHTMARENIGHTMARENIGHTMARE")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    
    # --- Screen-clearing code goes here
    screen.fill("white")
    # --- Drawing code should go here
    fractal(360, 350, 350, 0, 5)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(1)
 
# Close the window and quit.
pygame.quit()