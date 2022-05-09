# https://www.youtube.com/watch?v=61eX0bFAsYs&ab_channel=GrandmaCan-%E6%88%91%E9%98%BF%E5%AC%A4%E9%83%BD%E6%9C%83
import pygame
FPS = 60    # 60針
WHITE = (255, 255, 255)
WIDTH = 500
HEIGHT = 600
# 遊戲初始化 and 創建視窗
pygame.init()
# 視窗大小
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("first game")    # 視窗標題

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))   # 創造平面
        self.image.fill((0, 255, 0))    # 設定平面顏色
        self.rect = self.image.get_rect()   # 把圖片加框線(可設定中心、上方...) (自己的邊界=圖片框線)(rect=rectangle矩形)
        # self.rect.x = 200                   # 設定座標位
        # self.rect.y = 200
        self.rect.centerx  = WIDTH/2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 8
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

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# 取的時間物件
clock = pygame.time.Clock()

# 遊戲迴圈
running = True
while running:
    clock.tick(FPS)                     # 一秒最多刷新FPS次(1秒跑最多幾次while)
    # 取得輸入
    for even in pygame.event.get():     # 回傳所有動作
        if even.type == pygame.QUIT:    # 如果按下X ,pygame.QUIT 是按下X後的型態
            running = False             # 跳出迴圈
    # 更新遊戲
    all_sprites.update()                # 執行all_sprites群組內所有成員的update函式
    # 畫面顯示
    screen.fill(WHITE)                     # screen 為上面宣告的display ,fill 傳入三個(R,G,B) ,每個0-255 ,代表濃度
    all_sprites.draw(screen)            # 把all_sprites群組內的東西印在畫面
    pygame.display.update()                      # 更新畫面
pygame.quit()
