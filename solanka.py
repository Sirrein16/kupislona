from pygame import*

okno = display.set_mode((1200,700))
game = True
fps = time.Clock()

dx = -2
dy = -2

class gameobject(sprite.Sprite):
    def __init__(self, img, x,y,w,h):
        super().__init__()
        self.image = transform.scale(image.load(img), (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.lastx = self.rect.x
        self.lasty = self.rect.y
    def ris(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))
      

class player(gameobject):
    def move(self):
        self.ris()
        kn = key.get_pressed()
        if self.rect.x > 50 and  kn[K_a]:
            self.lastx = self.rect.x
            self.rect.x -= 5
        if self.rect.x < 1100 and  kn[K_d]:
            self.lastx = self.rect.x
            self.rect.x += 5
        if self.rect.y < 550  and kn[K_s]:
            self.lasty = self.rect.y
            self.rect.y += 5
        if self.rect.y > 50 and kn[K_w]:
            self.lasty = self.rect.y
            self.rect.y -= 5
       


class stena(sprite.Sprite): # перенёс класс стены наверх
    def __init__(self, x,y,w,h):
        self.image = Surface((w,h))
        self.image.fill((10, 200, 250))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def ris(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))

from random import*

class myachsotoni(sprite.Sprite):
    def __init__(self, img, x,y,sw,sh): #  картинка, икс, игрек, ширина, высота
        super().__init__()
        self.image = transform.scale(image.load(img), (sw,sh))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dx = choice([-1,1]) # на старте выбирается случайное -1 или 1
        self.dy = choice([-1,1])  # choice([-3,-2,-1,1,2,3])
    def ris(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))
    def skok(self):
      self.rect.x += self.dx
      self.rect.y += self.dy
      if self.rect.y > 575:
          self.dy *= -1
      if self.rect.y < 75:
          self.dy *= -1
      if self.rect.x > 50:
          self.dx *= -1
      if self.rect.x < 1100:
          self.dx *= -1
        

ball = myachsotoni("images.png", 780, 280, 60,60)

fon = image.load('fons.jpg')
fon = transform.scale(fon, (1200,700))

vrag = gameobject('gg2.png', 800, 200, 100, 100)

hero = player('ggs.png', 200,200, 100,100)


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    okno.blit(fon,(0,0))
    #okno.fill((255,255,0)) # заливка после фона не нужна
    fps.tick(60)
    hero.move()
    vrag.ris()
    vrag.rect.x += dx
    vrag.rect.y += dy
    if sprite.collide_rect(hero,vrag):
        dx *= -1
        dy *= -1
        vrag.rect.x = 800
        vrag.rect.y = 200
        hero.rect.x = 200
        hero.rect.y = 200
    ball.skok()
    ball.ris()
    display.update()
   # стёр повторы кода
