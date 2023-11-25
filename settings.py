class Settings:
    '''存储游戏《外星人入侵》中所有设置的类'''

    def __init__(self):
        '''初始化游戏的静态设置'''
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 60)

        #飞船的设置
        self.ship_limit = 3

        #子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullet_allowed = 100

        #外星人设置
        self.fleet_drop_speed = 10

        #开始按钮设置
        self.button_width = 200
        self.button_height = 50
        self.button_color = (0, 135, 0)
        self.button_text_color = (255, 255, 255)

        #得分提示设置
        self.score_text_color = (255, 255, 255)

        #以什么速度加快游戏的节奏
        self.speedup_scale = 1.1
        #外星人分数的提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''初始化随游戏进行而变化的设置'''        
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        #fleet_direction为1时表示向右，为-1时表示向左
        self.fleet_direction = 1

        #记分设置
        self.alien_points = 10

    def increase_speed(self):
        '''提高速度设置的值和外星人分数'''
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
