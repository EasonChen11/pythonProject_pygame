# https://www.youtube.com/watch?v=61eX0bFAsYs&ab_channel=GrandmaCan-%E6%88%91%E9%98%BF%E5%AC%A4%E9%83%BD%E6%9C%83
# image https://drive.google.com/drive/folders/10-SA2Fiyf5cm3jUNW2s1zskh0-2eQl9V
import time

import pygame
import random

FPS = 60    # 60針
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WIDTH = 500
HEIGHT = 600
# 遊戲初始化 and 創建視窗
pygame.init()
# 視窗大小
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("first game")    # 視窗標題

# 背景音樂
pygame.mixer.init()
pygame.mixer.music.load(f"./music/{random.randrange(0, 6)}.mp3")
pygame.mixer.music.play()

# 載入圖片 convert 轉成pygame 易讀檔案
player_image = pygame.image.load("./img/player.png").convert()
background = pygame.image.load("./img/background.png").convert()
bullet_image = pygame.image.load("./img/bullet.png").convert()
rocks_image = []
for i in range(0, 7):
    rocks_image.append(pygame.image.load(f"./img/rock{i}.png").convert())
rock_score = {}
damage = {}
for i in range(0, 7):
    rock_score[rocks_image[i]] = rocks_image[6-i].get_rect().width / 2
    damage[rocks_image[i]] = i+1

font_name = pygame.font.match_font('arial')  # 取的字型
def draw_text(surface, text, size, x, y):
    font = pygame.font.Font(font_name, size)    # 給定字型和大小# font:字型 render:使成為
    text_surface = font.render(text, True, WHITE)   # 製造文字平面(文字,Anti-aliasing{抗鋸齒文字},字體顏色)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surface.blit(text_surface, text_rect)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((50, 40))   # 創造平面
        # self.image.fill((0, 255, 0))    # 設定平面顏色
        self.image = pygame.transform.scale(player_image, (50, 38))     # 轉換圖片長寬
        self.image.set_colorkey(BLACK)  # 把顏色設為透明
        self.rect = self.image.get_rect()   # 把圖片加框線(可設定中心、上方...) (自己的邊界=圖片框線)(rect=rectangle矩形)
        # self.rect.x = 200                   # 設定座標位
        # self.rect.y = 200
        self.radius = 20
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx  = WIDTH/2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 8
        self.HP = 500

    def update(self):
        key_pressed = pygame.key.get_pressed()  # 取得鍵盤哪個鍵被按下的bool，函式會傳回list包含每個按鍵的bool(有按=True,else=False)
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += 8
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= 8
        if self.rect.left > WIDTH:
            self.rect.right = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

    def hit(self, which_rock):
        self.HP -= damage[which_rock]

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((30, 40))   # 創造平面
        # self.image.fill(RED)    # 設定平面顏色
        self.image_origin = random.choice(rocks_image)  # choice 從set中任選一個
        self.image_origin.set_colorkey(BLACK)
        self.image = self.image_origin.copy()
        self.rect = self.image.get_rect()   # 把圖片加框線(可設定中心、上方...) (自己的邊界=圖片框線)(rect=rectangle矩形)
        self.radius = self.rect.width/2
        self.rect.x = random.randrange(0, WIDTH-self.rect.width)      # 設定座標位
        self.rect.y = random.randrange(-180, -100)
        self.speedx = random.randrange(-3, 3)
        self.speedy = random.randrange(2, 10)
        self.total_degree = 0
        self.rotate_degree = int(random.choice([-3, 3]))
    def rotate(self):
        self.total_degree += self.rotate_degree
        self.total_degree = self.total_degree % 360
        self.image = pygame.transform.rotate(self.image_origin, self.total_degree)  # 旋轉圖片
        center = self.rect.center
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center   # 重新定位
    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
            self.kill()
            r = Rock()
            all_sprites.add(r)
            rocks.add(r)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_image
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()   # 把圖片加框線(可設定中心、上方...) (自己的邊界=圖片框線)(rect=rectangle矩形)
        self.rect.centerx = x      # 設定座標位
        self.rect.bottom = y
        self.speedy = -10
        self.radius = 0.5
    def update (self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()     # 把所有包含此sprite 的Group 刪除此元素

all_sprites = pygame.sprite.Group()
rocks = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
    r = Rock()
    rocks.add(r)
    all_sprites.add(r)
# 分數
score = 0
# 取的時間物件
clock = pygame.time.Clock()

# 遊戲迴圈
running = True
while running:
    clock.tick(FPS)                     # 一秒最多刷新FPS次(1秒跑最多幾次while)
    Ult = False
    # 取得輸入
    for event in pygame.event.get():     # 回傳所有動作
        if event.type == pygame.QUIT:    # 如果按下X ,pygame.QUIT 是按下X後的型態
            running = False             # 跳出迴圈
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
    # 更新遊戲
    all_sprites.update()                # 執行all_sprites群組內所有成員的update函式

    hits = pygame.sprite.groupcollide(rocks, bullets, True, True, pygame.sprite.collide_circle)   # 檢查Group之間是否有碰撞(倒數兩個決定是否kill sprite)(最後一個給判斷邊界，預設矩形)
                                                                # 上面回傳 dictionary {key:rock,value:bullet}
    for rock, bullet in hits.items():
        score += rock_score[rock.image_origin]
        r = Rock()
        rocks.add(r)
        all_sprites.add(r)

    hits = pygame.sprite.spritecollide(player, rocks, False, pygame.sprite.collide_circle)
    if hits:
        player.hit(hits[0].image_origin)
        hits[0].kill()
        r = Rock()
        rocks.add(r)
        all_sprites.add(r)
    if player.HP <= 0:
        running = False

    # 畫面顯示
    # screen.fill(WHITE) # screen 為上面宣告的display ,fill 傳入三個(R,G,B) ,每個0-255 ,代表濃度
    screen.blit(background, (0, 0))     # blit(畫) 第一個是圖片，第二個是位置
    all_sprites.draw(screen)            # 把all_sprites群組內的東西印在畫面
    draw_text(screen, str(int(score)), 18, WIDTH / 2, 10)
    draw_text(screen, f"HP:{int(player.HP)}", 18, WIDTH / 4, 10)
    pygame.display.update()                      # 更新畫面=pygame.display.flip()更新全部，update可以有參數
pygame.mixer.music.stop()

quit_game = True
pygame.mixer.music.load("./music/fail.mp3")
pygame.mixer.music.play()
fail = pygame.image.load("./img/fail.png").convert()
fail = pygame.transform.scale(fail, (WIDTH, HEIGHT-3))

while quit_game:
    for event in pygame.event.get():     # 回傳所有動作
        if event.type == pygame.QUIT:    # 如果按下X ,pygame.QUIT 是按下X後的型態
            quit_game = False             # 跳出迴圈
    screen.blit(fail, (0, 0))
    pygame.display.update()
pygame.mixer.music.stop()

pygame.quit()
