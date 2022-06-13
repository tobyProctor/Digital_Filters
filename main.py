# Importing Required Libraries
import numpy as np
import matplotlib.pyplot as plt
import sys
import pygame

COLOUR_BACKGROUND = (12, 22, 79)
SCREEN_RES_X = 1400
SCREEN_RES_Y = 900
COLOUR_SUN = (255, 255, 0)
RANGE = 35

time = np.arange(0, RANGE, 0.01)
print(time)
amplitude = np.sin(time) + np.sin(10*time)*0.3 + np.sin(100*time)*0.1
print(amplitude)
fft = abs(np.fft.fft(amplitude))

# Plotting time vs amplitude using plot function from pyplot
#plt.plot(time, fft)
plt.plot(time, amplitude)

# Settng title for the plot in blue color
plt.title('Sine Wave', color='b')

# Setting x axis label for the plot
plt.xlabel('Time'+ r'$\rightarrow$')

# Setting y axis label for the plot
plt.ylabel('Sin(time) '+ r'$\rightarrow$')

# Showing grid
plt.grid()

# Highlighting axis at x=0 and y=0
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

# Finally displaying the plot
plt.show()

game_tick = 0

pygame.init()
screen = pygame.display.set_mode([SCREEN_RES_X, SCREEN_RES_Y])

def main():
    screen.fill(COLOUR_BACKGROUND)

    while True:
        # Exit on close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(COLOUR_BACKGROUND)
        for x in range(len(time)):
            x_y_modifier = ((SCREEN_RES_X-100)/RANGE)/2
            x_x_modifier = SCREEN_RES_Y/4+100
            y_y_modifier = -0.1
            y_x_modifier = 30+(SCREEN_RES_X/2)
            pygame.draw.circle(screen, COLOUR_SUN, ((time[x]*x_y_modifier)+y_x_modifier, (fft[x]*y_y_modifier)+x_x_modifier), 1)

        for x in range(len(time)):
            x_y_modifier = ((SCREEN_RES_X-40)/RANGE)/2
            x_x_modifier = SCREEN_RES_Y/4
            y_y_modifier = SCREEN_RES_Y/8
            y_x_modifier = 20
            pygame.draw.circle(screen, COLOUR_SUN, ((time[x]*x_y_modifier)+y_x_modifier, (amplitude[x]*y_y_modifier)+x_x_modifier), 2)
            #print("{}, {}".format((time[x]*(SCREEN_RES_X/RANGE)), ((amplitude[x]*(SCREEN_RES_Y/4))+(SCREEN_RES_Y/2))))
            pygame.display.flip()

if __name__ == "__main__":
    main()