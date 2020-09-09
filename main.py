import pygame
import win32api
import win32gui
import win32con
from win32api import GetSystemMetrics

pygame.init() #Initializing our pygame window
width = GetSystemMetrics(0) #Getting computers resolution width
height = GetSystemMetrics(1) #Getting computers resolution height
screen = pygame.display.set_mode((width, height), pygame.NOFRAME) #Creating our screen, setting it to NOFRAME so we dont see the windows default UI (Minimize, Fullscreen, Exit)
done = False #For our while loop

fuchsia = (255, 0, 128)  # Transparency color

# Set window transparency color
hwnd = pygame.display.get_wm_info()["window"]

win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY) #Setting window color to transparent
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOSIZE) #Setting window to always be on top

while not done:

  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
  screen.fill(fuchsia) #Setting the screen blank every frame so that the drawings will update in realtime

  #drawing loop
  pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(0, 0, 60, 60)) #Example
  #end drawing loop
    
  pygame.display.update() #Updating display every frame so that the drawings will update in realtime, allowing you to change the pygame.draw objects attributes (positon, color, etc.) in realtime
