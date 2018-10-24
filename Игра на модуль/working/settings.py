# Игровые настройки
TITLE = "Скакун!"
WIDTH = 480
HEIGHT = 600
FPS = 60
FONT_NAME = 'arial'
HS_FILE = "highscore.txt"
SPRITESHEET = "spritesheet_jumper.png"

# Своиства игрока
PLAYER_ACC = 0.6 #скорость ходьбы
PLAYER_FRICTION = -0.12 #Скорость полёта 
PLAYER_GRAV = 0.8 #Гравитация
PLAYER_JUMP = 20 #высота прыжка   

# Своиства игры
BOOST_POWER = 50 #высота буста
POW_SPAWN_PCT = 5 #частота выподения
MOB_FREQ = 5000 #частота появления моба
PLAYER_LAYER = 2 #Игрок на главном плане
PLATFORM_LAYER = 1 #платaформа на среднем плане
POW_LAYER = 1 #буст на среднем плане
MOB_LAYER = 2 #моб на первом плане
CLOUD_LAYER = 0 #Облака на заднем плане

# Стартовая платворма
PLATFORM_LIST = [(0, HEIGHT - 60),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4 - 50),
                 (125, HEIGHT - 350),
                 (350, 200),
                 (175, 100)]

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 191, 255)
BGCOLOR = LIGHTBLUE
