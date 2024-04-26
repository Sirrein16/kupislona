from pygame import*


okno = display.set_mode((800,600))
game = True
fps = time.Clock()

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
        if kn[K_a]:
            self.lastx = self.rect.x
            self.rect.x -= 5
        if kn[K_d]:
            self.lastx = self.rect.x
            self.rect.x += 5
        if kn[K_s]:
            self.lasty = self.rect.y
            self.rect.y += 5
        if kn[K_w]:
            self.lasty = self.rect.y
            self.rect.y -= 5

    def move2(self):
        self.ris()
        kn = key.get_pressed()
        if kn[K_LEFT]:
            self.lastx = self.rect.x
            self.rect.x -= 5
        if kn[K_RIGHT]:
            self.lastx = self.rect.x
            self.rect.x += 5
        if kn[K_DOWN]:
            self.lasty = self.rect.y
            self.rect.y += 5
        if kn[K_UP]:
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
  def __init__(self, pik, x,y,sw,sh): #  картинка, икс, игрек, ширина, высота
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

ball = myachsotoni("картинка", серединапоХ, серединапоУ, ширина, высота)

# пример использования в цикле while
    
#...
if sprite.collide_rect(ball, ещёктото): # тоже для вертикальных стенок
  ball.dy *= -1 

if sprite.collide_rect(ball, горизонтальнаястена):
  ball.dx *= -1

fon = image.load('fons.jpg')
fon = transform.scale(fon, (800,600))

vrag = gameobject('gg2.png', 800, 200, 20, 20)

hero = player('ggs.png', 200,200, 35,35)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    okno.blit(fon,(0,0))
    #okno.fill((255,255,0)) # заливка после фона не нужна
    fps.tick(60)
    hero.move()
    hero2.move2()
    display.update()
   # стёр повторы кода

