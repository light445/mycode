import sys
import pygame
from Settings import Settings
class AlienInvasion:
    '''管理游戏资源和行为的类'''
    def __init__(self):
        '''初始化游戏并创建游戏资源'''
        pygame.__init__('AlineInvasion')
        self.clock =pygame.time.Clock()
        self.screen=pygame.display.set_mode((1200,800))
        pygame.display.set_caption('Alien Invasion')
        #设置背景色
        self.bg_color=(230,230,230)
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_hight)
        )

    def run_game(self):
        '''开始游戏的主循环'''
        while True:
            #倾听键盘和耳机事件
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    sys.exit()

            #每次循环都重绘屏幕
            self.screen.fill(self.settings.bg_color)
            self.screen.fill(self.bg_color)
            #让最近绘制的屏幕可见
            pygame.display.flip()
            self.clock.tick(60)
if __name__=='__main__':
    #创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()










