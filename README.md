# pygame-overlay-base
Super Simple "Hello World" for a transparent PyGame overlay.

Only two dependencies: *PyGame, and PyWin32(Win32Gui, Win32Api, Win32Con)*

Once the main.py file is ran it will draw an example rectangle, the drawing code for the **filled rectangle** below (also on line 31 of main.py):

```py 
pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(0, 0, 60, 60))
```

This will result in an **overlay** like this:
![Image of OverlayExampleRect](https://media.discordapp.net/attachments/733974815735808041/753114041462816788/unknown.png?width=825&height=464)

In the ***drawing loop*** (starts at `#drawing loop` and ends at `#end drawing loop`), you can add on whatever type of shape you want using ***pygame.draw*** (documentation for it is below)

https://www.pygame.org/docs/ref/draw.html

We can even use the ```pygame.draw.line``` function to create a **bordered square**.

To do this, we can create a function called `drawBox` with a few parameters like **screen, color, x, y, width, height** and **thickness**. Then, we add four **pygame.draw.line**'s and change their **x, and y**, *start pos* and *end pos* accordingly. If done correctly, you should have a *drawBox* function ***like this:***

```py
def drawBox(screen, color, x, y, width, height, thickness):
    pygame.draw.line(screen, color, (x + width, y), (x, y), thickness) #Top
    pygame.draw.line(screen, color, (x, y + height), (x, y), thickness) #Left
    pygame.draw.line(screen, color, (x + width, y), (x + width, y + height), thickness) #Right
    pygame.draw.line(screen, color, (x, y + height), (x + width, y + height), thickness) #Bottom
```

Then we just need to call our *drawBox* function in our ***drawing loop***:

```py
#drawing loop
drawBox(screen, (255, 0, 0), 0, 0, 100, 100, 1)
#end drawing loop
```

Which will create this result:

![Image of OverlayExampleBorderedSquare](https://media.discordapp.net/attachments/733974815735808041/753119629978894376/unknown.png?width=825&height=464)
