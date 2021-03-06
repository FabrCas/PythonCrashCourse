import pygame.font

class Button():

    def __init__(self, ai_settings, screen, msg):
        self.ai_settings=ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # proprieta' del bottone
        self.width, self.height = 360, 100
        self.button_color= (0,0,0)
        self.text_color = (0,255,0)
       # self.font = pygame.font.SysFont("gigi", 38, False, False)  #Possibile errore in mancanza di font

        self.font = pygame.font.SysFont("arial", 38, False, False)

        # costruzione della rect per il bottone
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center= self.screen_rect.center

        # messaggio bottone
        self.set_msg(msg)

    def set_msg(self,msg):
        # da stringa a immagine renderizzata al centro del bottone
        self.msg_image = self.font.render(msg,True,self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


#--info fonts-------------------------------------------------------------------
def get_fonts():
    print("font disponibili: \n")
    for font in pygame.font.get_fonts():
        print(font)

def get_default_font():
    print(pygame.font.get_default_font())