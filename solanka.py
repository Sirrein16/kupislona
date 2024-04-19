from pygame import*

okno = display.set_mode((1000,650))
fps = time.Clock()
game = True

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

    class stena(sprite.Sprite):
    def __init__(self, x,y,w,h):
        self.image = Surface((w,h))
        self.image.fill((10, 200, 250))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
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

    



    fps.tick(60)
    display.update()
 
