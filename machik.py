# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# общая система:                                                                                                      # 
# у объекта есть параментры dx dy, которые стабильно к его rect.x/y прибавляются, умноженные на случайное число       # 
# периодически у объекта сбрасывается скорость                                                                        # 
# при каждом столкновении dx или dy умножаются на -1 и объект меняет направление                                      # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#from pygame import*

from random import*

class myachsotoni(sprite.Sprite):
  def __init__(self, pik, x,y,sw,sh): #  картинка, икс, игрек, ширина, высота
        super().__init__()
        self.image = transform.scale(image.load(img), (sw,sh))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dx = choice([-1,1]) # на старте выбирается случайное -1 или 1
        self.dy = choice([-1,1]) 
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


               
