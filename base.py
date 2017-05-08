import pygame
from pygame.locals import *

class App():
    def __init__(self,width,height,title="pygame window",icon=None):
        self.running = False
        self.size = (width,height)
        self.title = title
        self.icon = icon
        pygame.init()

    def init(self):
        """Commands to be processed before the application starts"""
        pygame.display.set_caption(self.title)
        if self.icon != None:
            self.icon = pygame.image.load(self.icon)
            pygame.display.set_icon(self.icon)
        self.display = pygame.display.set_mode(self.size, pygame.HWSURFACE | DOUBLEBUF)
        return True

    def __loop__(self):
        """Commands processed every frame"""
        pass

    def __events__(self, event):
        """Event Handling"""
        if event.type == pygame.QUIT:
            self.running = False

    def __render__(self):
        """Rendering"""
        pygame.display.flip()

    def __cleanup__(self,e=None):
        """Commands to be processed when quiiting"""
        pygame.quit()
        if e != None:
            raise e

    def start(self):
        """Start the application"""
        ex = None
        self.running = self.init()
        
        while self.running == True:
            try:
                for event in pygame.event.get():
                    self.__events__(event)

                self.__loop__()
                self.__render__()
            except Exception,e:
                self.running = False
                ex = e
    

        self.__cleanup__(ex)
