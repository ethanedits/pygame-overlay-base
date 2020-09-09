import pygame
import win32api
import win32gui
import win32con
from win32api import GetSystemMetrics

pygame.init()
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
screen = pygame.display.set_mode((width, height), pygame.NOFRAME) #, pygame.FULLSCREEN
done = False

fuchsia = (255, 0, 128)  # Transparency color

# Set window transparency color
hwnd = pygame.display.get_wm_info()["window"]

win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOSIZE) #| win32con.SWP_NOMOVE

while not done:

  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
  screen.fill(fuchsia)

  #drawing functions
  #Example: 
  pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(0, 0, 60, 60))

  pygame.display.update()
