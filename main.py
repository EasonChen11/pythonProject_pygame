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
        self.image = pygame.Surface((50, 40))
        self.image.fill((0, 255, 0))
        self.rect =self.image.get_rect()
# 取的時間物件
clock = pygame.time.Clock()

# 遊戲迴圈
running = True
while running:
    clock.tick(FPS)                     # 一秒最多刷新FPS次
    # 取得輸入
    for even in pygame.event.get():     # 回傳所有動作
        if even.type == pygame.QUIT:    # 如果按下X ,pygame.QUIT 是按下X後的型態
            running = False             # 跳出迴圈
    # 更新遊戲
    # 畫面顯示
    screen.fill(WHITE)                     # screen 為上面宣告的display ,fill 傳入三個(R,G,B) ,每個0-255 ,代表濃度
    pygame.display.update()                      # 更新畫面
pygame.quit()
