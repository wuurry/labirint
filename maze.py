from pygame import *
'''Необходимые классы'''
 
#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
   #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (50, 50))
       
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()

        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed 
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed 
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


class Enemy(GameSprite):
    direction = 'up'
    def update(self):
        if self.rect.y <= 300:
            self.direction = 'down'
        if self.rect.y >= 500:
            self.direction  = 'up'
        if self.direction =='up':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

    def update1(self):
        if self.rect.x <= 600:
            self.direction = 'right'
        if self.rect.x >= 820:
            self.direction  = 'left'
        if self.direction =='left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        
    def update2(self):
        if self.rect.y <= 40:
            self.direction = 'down'
        if self.rect.y >= 370:
            self.direction  = 'up'
        if self.direction =='up':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

    def update3(self):
        if self.rect.y <= 40:
            self.direction = 'down'
        if self.rect.y >= 230:
            self.direction  = 'up'
        if self.direction =='up':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
            

class Treasure(GameSprite):
    direction = 'up'
    def update(self):
        if self.rect.y <= 520:
            self.direction = 'down'
        if self.rect.y >= 520:
            self.direction  = 'up'
        if self.direction =='up':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
            

class Boost(GameSprite):
    direction = 'up'
    def update(self):
        if self.rect.y <= 10:
            self.direction = 'down'
        if self.rect.y >= win_height - 85:
            self.direction  = 'up'
        if self.direction =='up':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed


class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
       # картинка стены - прямоугольник нужных размеров и цвета

        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
       # каждый спрайт должен хранить свойство rect - прямоугольник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
        
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


#Игровая сцена:
win_width = 1000
win_height = 800
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))
 
#Персонажи игры:
player = Player('hero2.jpg', 10, 700, 4)
monster = Enemy('cyborg2.jpg', 600, 530, 5)
monster1 = Enemy('cyborg2.jpg', 240, 330, 10)
monster2 = Enemy('cyborg2.jpg', 925, 200, 4)
monster3 = Enemy('cyborg2.jpg', 600, 50, 5)
monster4 = Enemy('cyborg2.jpg', 210, 150, 6)
monster5 = Enemy('cyborg2.jpg', 340, 230, 5)
monster6 = Enemy('cyborg2.jpg', 475, 200, 6)
final = Treasure('treasure2.png', 525, 485, 1)
boost = Boost('boost.png',  925, 720, 0)


w1 = Wall(255, 0, 0, 100, 20 , 900, 10)
w2 = Wall(255, 0, 0, 100, 20 , 10, 650)
w3 = Wall(255, 0, 0, 100, 580, 500, 10)
w4 = Wall(255, 0, 0, 100, 780 , 800, 10)
w5 = Wall(255, 0, 0, 590, 120 , 10, 550)
w6 = Wall(255, 0, 0, 215, 280, 385, 10)
w7 = Wall(255, 0, 0, 890, 280 , 10, 500)
w8 = Wall(255, 0, 0, 600, 280, 185, 10)
w9 = Wall(255, 0, 0, 715, 580, 185, 10)
w10 = Wall(255, 0, 0, 715, 200, 185, 10)
w11 = Wall(255, 0, 0, 715, 360, 185, 10)
w12 = Wall(255, 0, 0, 600, 450, 185, 10)
w13 = Wall(255, 0, 0, 600, 200, 185, 10)
w14 = Wall(255, 0, 0, 890, 120 , 10, 80)
w15 = Wall(255, 0, 0, 310, 380 , 10, 200)
w16 = Wall(255, 0, 0, 410, 280 , 10, 200)
w17 = Wall(255, 0, 0, 500, 380 , 10, 200)


font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))

finish = False
game = True
clock = time.Clock()
FPS = 75
 
#музыка
win_width = 1000
win_height = 800
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')
 
while game:
    for e in event.get():
        if e.type == QUIT:
           game = False

    if finish != True:
        window.blit(background,(0, 0))
        
        player.update()
        player.reset()
        monster.reset()
        monster.update1()
        monster1.reset()
        monster1.update()
        monster2.reset()
        monster2.update2()
        monster3.reset()
        monster3.update1()
        monster4.reset()
        monster4.update3()
        monster5.reset()
        monster5.update3()
        monster6.reset()
        monster6.update3()
        boost.update()
        boost.reset()
        final.reset()
        boost.reset()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()
        w11.draw_wall()
        w12.draw_wall()
        w13.draw_wall()
        w14.draw_wall()
        w15.draw_wall()
        w16.draw_wall()
        w17.draw_wall()

        if sprite.collide_rect(player, final):
            print('Победа')
            window.blit(win, (200, 200))
            finish = True
            money.play()
        if sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5)  or sprite.collide_rect(player, w7) or sprite.collide_rect(player, w8) or sprite.collide_rect(player, w9) or sprite.collide_rect(player, w10) or sprite.collide_rect(player, w11) or sprite.collide_rect(player, w12) or sprite.collide_rect(player, w13) or sprite.collide_rect(player, w14) or sprite.collide_rect(player, w15) or sprite.collide_rect(player, w16) or sprite.collide_rect(player, w17):
            print('Поражение')  
            window.blit(lose, (200, 200))  
            finish = True
            kick.play() 
            print('Поражение!!!!!')
        if sprite.collide_rect(player, monster6):
            print('Поражение')
            window.blit(lose, (200, 200))   
            finish = True
            kick.play()
        if sprite.collide_rect(player, monster5):
            print('Поражение')
            window.blit(lose, (200, 200))   
            finish = True
            kick.play()
        if sprite.collide_rect(player, monster4):
            print('Поражение')
            window.blit(lose, (200, 200))   
            finish = True
            kick.play()
        if sprite.collide_rect(player, monster3):
            print('Поражение')
            window.blit(lose, (200, 200))   
            finish = True
            kick.play()  
        if sprite.collide_rect(player, monster2):
            print('Поражение')
            window.blit(lose, (200, 200))   
            finish = True
            kick.play()
        if sprite.collide_rect(player, monster1):
            print('Поражение')
            window.blit(lose, (200, 200))   
            finish = True
            kick.play()
        if sprite.collide_rect(player, monster):
            print('Поражение')
            window.blit(lose, (200, 200))   
            finish = True
            kick.play()
        if sprite.collide_rect(player, boost):
            player.speed = 6

        display.update()
        clock.tick(FPS)