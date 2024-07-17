import pygame
import sys
from pygame.image import load
import random
from sprites import *
import os
import re
import copy
import math
import requests
# 初始化pygame
pygame.init()

def run_game():
    board_size_3 = screen_width_fa,screen_height=1920,1080
    screen_height = 1080
    screen_width = 1920
    screen_height = 1080  # 显示屏幕的高度
    board_height = 28 * 75 +30 # 整个棋盘的高度
    scroll_y  = 0  # 棋盘的垂直滚动位置 
    scroll_y_left  = 0  # 棋盘的垂直滚动位置 
    # 红框的位置和大小
    clip_rect = pygame.Rect(0, 155, screen_width, screen_height - 155)
    clip_rect_left = pygame.Rect(0, 265, screen_width, screen_height)
    # 设置棋盘大小和格子大小
    # 在游戏初始化部分*
    mouse_dragging = False
    scaling_factor = 2 / 3  # 适应150%的缩放
    board_size_2 = width, height = (screen_width, screen_height)
    board_size = width, height = (int(screen_width * scaling_factor), int(screen_height * scaling_factor))
    board = pygame.display.set_mode((board_size_2),pygame.DOUBLEBUF)
    grid_size = 30
    # 创建一个Clock对象来控制帧率
    clock = pygame.time.Clock()

    # 设置系统字体
    my_font = pygame.font.Font('fonts/bb4171.ttf', 18)

    icon = pygame.image.load('assets/icon.png')
    pygame.display.set_icon(icon)


    # 创建图层b/

    # def add_obstacle(row, col):
    #     if chessboard.board[row][col] == 0:
    #         chessboard.board[row][col] = 3
    #         x_pos = game_board.x + col * chessboard.cell_size
    #         y_pos = game_board.y + row * chessboard.cell_size
    #         obstacle_sprite = Obstacle((128,128,128), (x_pos, y_pos), chessboard.cell_size)
    #         obstacle_group.add(obstacle_sprite)
    # color_mapping = {
    #     pygame.K_1: (255, 0, 0),      # 红色
    #     pygame.K_2: (0, 255, 0),      # 绿色
    #     pygame.K_3: (0, 0, 255),      # 蓝色
    #     pygame.K_4: (255, 255, 0),    # 黄色
    #     pygame.K_5: (128, 0, 128),    # 紫色
    #     pygame.K_6: (0, 255, 255),    # 青色
    #     pygame.K_7: (255, 165, 0),    # 橙色
    #     pygame.K_8: (255, 192, 203),  # 粉色
    #     pygame.K_9: (128, 128, 128)   # 灰色
    # }
    # color_mapping = {
    # pygame.K_1: (86, 121, 63),   # 橄榄色
    # pygame.K_2: (178, 32, 52),   # 深红色
    # pygame.K_3: (103, 65, 184),  # 深紫色
    # pygame.K_4: (235, 243, 93),  # 浅黄色
    # pygame.K_5: (108, 85, 67),   # 棕色
    # pygame.K_6: (84, 238, 200),  # 亮青色
    # pygame.K_7: (119, 119, 119), # 灰色
    # pygame.K_8: (90, 220, 244),  # 天蓝色
    # pygame.K_9: (119, 221, 119),  # 浅绿色
    # pygame.K_10: (59, 59, 59),    # 暗灰色
    # pygame.K_11: (255, 140, 53),  # 橙色
    # pygame.K_12: (232, 42, 42),   # 鲜红色
    # pygame.K_13: (0, 0, 0),       # 黑色
    # pygame.K_14: (255, 255, 255), # 白色
    # pygame.K_15: (225, 52, 170)   # 粉红色
    # }
    colors = [
    (86, 121, 63),
    (178, 32, 52),
    (103, 65, 184),
    (235, 243, 93),
    (108, 85, 67),
    (84, 238, 200),
    (119, 119, 119),
    (90, 220, 244),
    (119, 221, 119),
    (59, 59, 59),
    (255, 140, 53),
    (232, 42, 42),
    (0, 0, 0),
    (255, 255, 255),
    (225, 52, 170)
    ]
    # 颜色块尺寸和间隔
    block_width, block_height = 30, 30
    block_margin = 5

    # 创建颜色块对象列表
    color_blocks = []
    for i, color in enumerate(colors):
        row = i // 5
        col = i % 5

        x = (block_width + block_margin) * col + block_margin +1500
        y = (block_height + block_margin) * row + block_margin +20

        color_blocks.append(ColorBlock(color, x, y, block_width, block_height))
    # 创建颜色块对象列表
    # color_blocks = [ColorBlock(color, x, y, width, height) for color in colors]
    background_layer = Layer()
    image_layer = Layer()
    boss_layer = Layer()
    line_sprites = pygame.sprite.Group()
    all_player_Group = pygame.sprite.Group() #所有玩家
    obstacles = pygame.sprite.Group() # 存储障碍物精灵组
    atk_obstacles = pygame.sprite.Group() # 存储障碍物精灵组
    chess_pieces_group = pygame.sprite.Group()
    chess_pieces_group_left = pygame.sprite.Group()
    image_pieces=pygame.sprite.Group()
    button_texts = pygame.sprite.Group()
    # 加载棋子图像
    # player1_image = load(f"assets/piece/Enemy_monster_{1}.png")
    # player1_image = pygame.transform.scale(player1_image, (30, 30))
    # player_images = [load(f"assets/piece/Enemy_monster_{1}.png")]
    screen_background= load("assets/screen/game_screen_background.png")
    screen_background_left = load("assets/screen/game_screen_left.jpg")
    screen_background_top = load("assets/screen/game_screen_top.jpg")
    logo_02 =load("assets/logo_02.png")
    round_button_path = load("assets/box/round.png")
    text_distance = load("assets/button/text_distance.jpg")
    text_distance_left = load("assets/button/text_distance_left.jpg")
    distance_button_path = load("assets/box/distance_box.png")
    attack_off_path =load("assets/button/attack_off.png")
    attack_on_path =load("assets/button/attack_on.png")
    draw_line_button_off_path = load("assets/button/draw_line_off.png")
    draw_line_button_on_path = load("assets/button/draw_line_on.png")
    background_1 = Background(screen_background,1920,(0,0))
    background_3 = Background(screen_background_left,290,(0,0))
    background_2 =Background(logo_02,250,(20,25))
    background_4 = Background(screen_background_top,1920,(0,0))
    background_layer.add(background_1)
    # background_layer.add(background_3)
    # background_layer.add(background_4)
    background_layer.add(background_2)

    def load_player_images(type, player_numbers):
        images = {}
        for number in player_numbers:
            file_path = f"assets/piece/{type}_{number}.png"
            images[number] = pygame.image.load(file_path)
        return images
    def wait_for_confirmation():
        print("若需确认请按Y，取消请按N")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:  # 假设按下 'Y' 键表示确认
                        return True
                    elif event.key == pygame.K_n:  # 按下 'N' 键表示取消
                        return False
    benevolent_images = load_player_images("Benevolent", range(1, 4))
    # player_1 = benevolent_images[1]
    # player_2 = benevolent_images[2]
    # player_3 = benevolent_images[3]
    # player_4 = benevolent_images[4]


    # def load_player_image(player_number):
    #     # 构建文件路径
    #     file_path = f"assets/piece/Benevolent_{player_number}.png"
    #     # 加载并返回图像
    #     return pygame.image.load(file_path)
    # good_player_1 = load_player_image(1)
    # player_2 = load_player_image(2)
    # player_3 = load_player_image(3)
    # player_4 = load_player_image(4)
    # player_5 = load_player_image(5)
    # player_6 = load_player_image(6)
    # plyaer_7 = load_player_image(7)
    # player_8 = load_player_image(8)
    # Enemy_monster_1 = load("assets/piece/Benevolent_1.png")
    # Enemy_monster_2 = load("assets/piece/player_2.png")
    # Enemy_monster_3 = load("assets/piece/player_3.png")
    # Enemy_monster_4 = load("assets/piece/player_4.png")


    # type_player_1 = Background(player_1,50,(0,200))
    # type_player_2 = Background(player_2,50,(50,200))
    # type_player_3 =Background(player_3,50,(0,200))
    # type_player_4 = Background(player_4,50,(0,200))
    # background_layer.add(type_player_1)
    # background_layer.add(type_player_2)
    # background_layer.add(type_player_3)
    
    # background_layer.add(type_player_4)
    def find_nearest_center(chessboard, mouse_x, mouse_y,goad):
        # 计算鼠标在棋盘上的相对位置
        rel_x, rel_y = mouse_x - goad[0], mouse_y - goad[1]

        # 计算鼠标所在的格子
        grid_x = rel_x // chessboard.cell_size
        grid_y = rel_y // chessboard.cell_size

        # 确保鼠标所在格子在棋盘范围内
        grid_x = max(0, min(grid_x, chessboard.cols - 1))
        grid_y = max(0, min(grid_y, chessboard.rows - 1))

        # 计算格子的中心点坐标
        center_x = goad[0] + grid_x * chessboard.cell_size + chessboard.cell_size // 2
        center_y = goad[1] + grid_y * chessboard.cell_size + chessboard.cell_size // 2
        grid_x_abs =  grid_x * chessboard.cell_size + chessboard.cell_size / 2
        grid_y_abs =  grid_y * chessboard.cell_size + chessboard.cell_size / 2
        center = (center_x,center_y)
        center_abs =(grid_x_abs, grid_y_abs)
        # print(center_abs)
        return center ,center_abs

    # 使用示例
    # chessboard 是 Chessboard 的一个实例
    # mouse_x, mouse_y 是鼠标的当前坐标
    # nearest_center_x, nearest_center_y = find_nearest_center(chessboard, mouse_x, mouse_y)


    def find_nearest_vertex(mouse_pos, grid_size, board_offset):
        # 计算相对于棋盘的位置
        relative_pos = (mouse_pos[0] - board_offset[0], mouse_pos[1] - board_offset[1])

        # 计算在网格中的位置
        grid_x = relative_pos[0] // grid_size
        grid_y = relative_pos[1] // grid_size
        # grid_x_abs = relative_pos[0] / grid_size
        # grid_y_abs = relative_pos[1] / grid_size
        
        # 计算网格内的偏移
        offset_x = relative_pos[0] % grid_size
        offset_y = relative_pos[1] % grid_size

        # 确定最近的顶点
        nearest_x = grid_x * grid_size if offset_x < grid_size / 2 else (grid_x + 1) * grid_size
        nearest_y = grid_y * grid_size if offset_y < grid_size / 2 else (grid_y + 1) * grid_size

        # 转换回棋盘的全局坐标
        vertex = (nearest_x + board_offset[0], nearest_y + board_offset[1])
        # center_abs =(grid_x_abs, grid_y_abs)
        return vertex


    def target_screen(path,target_width):
        original_image = pygame.image.load(path)
        # 计算等比例缩放后的高度
        aspect_ratio = original_image.get_width() / original_image.get_height()
        target_height = int(target_width / aspect_ratio)
        # 缩放图像
        scaled_image = pygame.transform.scale(original_image, (target_width, target_height))
        return scaled_image
    # 创建棋盘
    # board = pygame.display.set_mode(board_size,pygame.RESIZABLE,pygame.DOUBLEBUF)
    pygame.display.set_caption("Game")



    # 定义颜色
    white = (4, 199, 50)
    black = (0, 0, 0)
    red = (255, 0, 0)

    player1 = Player("assets/piece/Benevolent_1.png",50,(0,500),1,1)
    player2 = Player("assets/piece/Benevolent_2.png",50,(50,500),1,2)
    player3 = Player("assets/piece/Benevolent_3.png",50,(100,500),1,3)
    player4 = Player("assets/piece/Benevolent_4.png",50,(150,500),1,4)
    player5 = Player("assets/piece/Benevolent_5.png",50,(0,550),1,5)
    player6 = Player("assets/piece/Benevolent_6.png",50,(50,550),1,6)
    player7 = Player("assets/piece/Benevolent_7.png",50,(100,550),1,7)
    player8 = Player("assets/piece/Benevolent_8.png",50,(150,550),1,8)

    Balanced_1 = Player("assets/piece/Balanced_1.png",50,(0,600),1,1)
    Balanced_2 = Player("assets/piece/Balanced_2.png", 50, (50, 600), 1, 2)
    Balanced_3 = Player("assets/piece/Balanced_3.png", 50, (100, 600), 1, 3)
    Balanced_4 = Player("assets/piece/Balanced_4.png", 50, (150, 600), 1, 4)
    # Balanced_5 = Player("assets/piece/Balanced_5.png", 50, (200, 600), 1, 5)
    # Balanced_6 = Player("assets/piece/Balanced_6.png", 50, (250, 600), 1, 6)
    # Balanced_7 = Player("assets/piece/Balanced_7.png", 50, (300, 600), 1, 7)
    # Balanced_8 = Player("assets/piece/Balanced_8.png", 50, (350, 600), 1, 8)
    Monsters_1= Player("assets/piece/Monsters_1.png",50,(0,650),1,1)
    Monsters_2 = Player("assets/piece/Monsters_2.png", 50, (50, 650), 1, 2)
    Monsters_3 = Player("assets/piece/Monsters_3.png", 50, (100, 650), 1, 3)
    Monsters_4 = Player("assets/piece/Monsters_4.png", 50, (150, 650), 1, 4)
    # Monsters_5 = Player("assets/piece/Monsters_5.png", 50, (200, 700), 1, 5)
    # Monsters_6 = Player("assets/piece/Monsters_6.png", 50, (250, 700), 1, 6)
    # Monsters_7 = Player("assets/piece/Monsters_7.png", 50, (300, 700), 1, 7)
    # Monsters_8 = Player("assets/piece/Monsters_8.png", 50, (350, 700), 1, 8)
    all_player_Group.add(player1)
    all_player_Group.add(player2)
    all_player_Group.add(player3)
    all_player_Group.add(player4)
    all_player_Group.add(player5)
    all_player_Group.add(player6)
    all_player_Group.add(player7)
    all_player_Group.add(player8)
    all_player_Group.add(Balanced_1)
    all_player_Group.add(Balanced_2)
    all_player_Group.add(Balanced_3)
    all_player_Group.add(Balanced_4)
    all_player_Group.add(Monsters_1)
    all_player_Group.add(Monsters_2)
    all_player_Group.add(Monsters_3)
    all_player_Group.add(Monsters_4)
    # background_layer.add(player1.image)
    # background_layer.add(player2.image)
    # background_layer.add(player3.image)
    # background_layer.add(player4.image)
    # background_layer.add(player5.image)
    # background_layer.add(player6.image)
    # background_layer.add(player7.image)
    # background_layer.add(player8.image)
    # background_layer.add(Balanced_1.image)
    # background_layer.add(Balanced_2.image)
    # background_layer.add(Balanced_3.image)
    # background_layer.add(Balanced_4.image)
    # background_layer.add(Monsters_1.image)
    # background_layer.add(Monsters_2.image)
    # background_layer.add(Monsters_3.image)
    # background_layer.add(Monsters_4.image)
    # print(player1.rect)


    # print(player1.image_path)
    # image = Image.open(player1.image_path)
    # image.save("assets/test.png")
    chessboard = Chessboard(rows=26, cols=30, cell_size=75)
    chessboard_left = Chessboard(rows=300, cols=3, cell_size=90)
    chessboard_top = Chessboard(rows=3, cols=8, cell_size=75)
    game_board = GameBoard(chessboard, x=290, y= 155 + scroll_y)
    game_board_left = GameBoard(chessboard_left, x=-0, y= 265 )



    #region
    # 设定颜色、位置和大小
    my_rect_top = pygame.Rect(0, 0, 1200, 160)
    BUTTON_COLOR = (139, 69, 19)  # 棕色按钮
    TEXT_COLOR = (255, 255, 255)  # 白色文字
    button_font = pygame.font.SysFont(None, 24)
    # 设置按钮的位置和大小
    button_rect_round_text = pygame.Rect(40, 160, 50, 50)
    button_rect_round = pygame.Rect(120, 180, 40, 40)  # round
    color_button_rect = pygame.Rect(1400,50,50,50)
    draw_line_button_rect = pygame.Rect(1000,50,50,50) # color
    draw_line_atk_button_rect = pygame.Rect(1100,50,50,50) # atk
    button_rect_line_distance_text = pygame.Rect(1220,50,50,50) # distance_text
    button_rect_line_distance = pygame.Rect(1300,50,50,50) # distance
    
    
    # button_rect_round.center = (160, 220)
    # 回合数
    # 按钮属性
    BUTTON_COLOR_2 = (0, 100, 200)  # 蓝色按钮
    TEXT_COLOR_2 = (0, 150, 250)  # 鼠标悬停时的颜色
    button_rect_2 = pygame.Rect(500, 80, 200, 50)  # 按钮的位置和大小
    logo_rect = pygame.Rect(0, 0, 200, 100)
    button_rect_3 = pygame.Rect(1000, 100, 200, 50)  # 初始化
    button_text = '选择棋子'
    button_text_3 = '初始化'
    text_surface = my_font.render(button_text, True, (255, 255, 255))  #示例 白色文本
    round_count = 0
    previous_state = None  # 用于跟踪drawing_wall_butten的上一个状态
    line_tetton =True
    # 绘制按钮的函数
    def draw_button_2(surface, rect, text):
        text_render = my_font.render(text, True, (255, 0,  0))
        surface.blit(text_render, (rect.x + 20, rect.y + 10))


    # 绘制按钮的函数
    def draw_button(screen, text, button_rect, button_color, text_color):
        pygame.draw.rect(screen, button_color, button_rect)
        text_surf = button_font.render(text, True, text_color)
        text_rect = text_surf.get_rect(center=button_rect.center)
        screen.blit(text_surf, text_rect)

    # 绘制按钮的函数
    # def draw_button_text(screen,button_rect,image, text, center, text_color):
    #     # pygame.draw.rect(screen, button_color, button_rect)
    #     text_surf = button_font.render(text, True, text_color)
    #     text_rect = text_surf.get_rect(center=center)
    #     image.blit(text_surf,text_rect)
    #     screen.blit(image, button_rect)

    def draw_button_text(screen, button_rect, image, text, center,text_color,button_font):
        # 绘制按钮的背景图像
        screen.blit(image, button_rect)

        # 创建并绘制文本
        text_surf = button_font.render(text, True, text_color)
        text_rect = text_surf.get_rect(center=center)  # 确保文本居中于按钮
        screen.blit(text_surf, text_rect)


    def draw_text(screen, text, text_rect, text_color):
        font = pygame.font.SysFont(None, 24)
        text_surf = font.render(text, True, text_color)
        text_rect = text_surf.get_rect(topleft=text_rect.topleft)
        screen.blit(text_surf, text_rect)



    def distance(pos1, pos2):
        return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5

    def point_line_distance(line_start, line_end, point):
        # 计算线段向量和点到线段起点的向量
        line_vec = (line_end[0] - line_start[0], line_end[1] - line_start[1])
        point_vec = (point[0] - line_start[0], point[1] - line_start[1])

        line_len = line_vec[0] ** 2 + line_vec[1] ** 2
        if line_len == 0:
            return distance(point, line_start)

        # 计算投影点
        t = max(0, min(1, (point_vec[0] * line_vec[0] + point_vec[1] * line_vec[1]) / line_len))
        nearest = (line_start[0] + t * line_vec[0], line_start[1] + t * line_vec[1])

        # 返回点到最近点的距离
        return distance(point, nearest)


    def place_boss_on_board(boss, board_rows, board_cols, cell_size):
        # 确保boss不会放置在棋盘外，假设boss占据2x2格子
        max_row = board_rows - 2
        max_col = board_cols - 2

        # 随机选择起始点
        start_row = random.randint(0, max_row)
        start_col = random.randint(0, max_col)
        # 计算boss在屏幕上的位置
        boss_x = start_col * cell_size+295
        boss_y = start_row * cell_size+200 

        # 在棋盘上标记boss占据的位置
        boss.board[start_row ][start_col] = 8
        boss.board[start_row+1][start_col] = 8
        boss.board[start_row][start_col+1] = 8
        boss.board[start_row+1][start_col+1] = 8
        boss.rect.x = boss_x
        boss.rect.y = boss_y
        boss.rect.topleft = (boss_x, boss_y)
        # 同时调整boss的image（Background精灵）的位置
        if isinstance(boss.image, pygame.sprite.Sprite):
            boss.image.rect.topleft = (boss_x, boss_y)

        return boss

    def place_boss_on_board_set(boss, row, col, board_x, board_y, board_rows, board_cols, cell_size):
        # 确保boss不会放置在棋盘外，假设boss占据2x2格子
        max_row = board_rows - 2
        max_col = board_cols - 2

        # 确保输入的行列在有效范围内
        if row > max_row or col > max_col:
            return
            raise ValueError("输入的行或列超出棋盘范围")
            

        # 计算boss在屏幕上的位置
        boss_x = board_x + (col-1) * cell_size+6 
        boss_y = board_y + (row-1) * cell_size+6
        print(row,col)
        # 在棋盘上标记boss占据的位置
        boss.board[row][col] = 8
        boss.board[row + 1][col] = 8
        boss.board[row][col + 1] = 8
        boss.board[row + 1][col + 1] = 8

        # 调整boss的rect位置
        boss.rect.topleft = (boss_x, boss_y)

        # 如果boss有image属性且是Sprite类型，则调整其位置
        if isinstance(boss.image, pygame.sprite.Sprite):
            boss.image.rect.topleft = (boss_x, boss_y)

        return boss
    def create_chess_pieces(cell_size, spacing, board, rows, cols):
        pieces = pygame.sprite.Group()
        piece_types = ['Balanced', 'Benevolent', 'Monsters']
        piece_count = 8  # 每种棋子的数量
        y_offset = 0  # 初始的y轴偏移量

        for i, piece_type in enumerate(piece_types):
            for j in range(1, piece_count + 1):
                # 计算棋子的中心位置
                center_x = (j - 1) * (cell_size + spacing) + cell_size // 2
                center_y = i * (cell_size + spacing) + y_offset + cell_size // 2

                # 加载棋子图像
                image_path = os.path.join('assets/piece', f'{piece_type}_{j}.png')
                image = pygame.image.load(image_path)

                # 创建棋子并添加到组里
                piece = ChessPiece(image, (center_x+300, center_y-scroll_y_left), cell_size, board, rows, cols)
                pieces.add(piece)

            # 增加y轴偏移量，为下一排棋子留出空间
            y_offset += spacing

        return pieces
    
    def calculate_rect_center(board_x, board_y, cell_size, clicked_row, clicked_col):
    # 计算四个中心点的坐标
        center1_x = board_x + clicked_col * cell_size + cell_size // 2
        center1_y = board_y + clicked_row * cell_size + cell_size // 2

        center2_x = board_x + (clicked_col + 1) * cell_size + cell_size // 2
        center2_y = board_y + clicked_row * cell_size + cell_size // 2

        center3_x = board_x + clicked_col * cell_size + cell_size // 2
        center3_y = board_y + (clicked_row + 1) * cell_size + cell_size // 2

        center4_x = board_x + (clicked_col + 1) * cell_size + cell_size // 2
        center4_y = board_y + (clicked_row + 1) * cell_size + cell_size // 2

        # 计算四个中心点的平均坐标
        avg_center_x = (center1_x + center2_x + center3_x + center4_x) // 4
        avg_center_y = (center1_y + center2_y + center3_y + center4_y) // 4

        return avg_center_x, avg_center_y


    def find_nearest_vertex_2(board_x, board_y, cell_size, rows, cols, mouse_x, mouse_y):
        nearest_vertex = None
        min_distance = float('inf')

        # 遍历棋盘上的每个顶点
        for row in range(rows + 1):
            for col in range(cols + 1):
                vertex_x = board_x + col * cell_size
                vertex_y = board_y + row * cell_size

                # 计算鼠标与顶点的距离
                distance = math.sqrt((vertex_x - mouse_x) ** 2 + (vertex_y - mouse_y) ** 2)

                # 更新最近顶点
                if distance < min_distance:
                    min_distance = distance
                    nearest_vertex = (vertex_x, vertex_y)

        return nearest_vertex


    def find_nearest_vertex_3(board_x, board_y, cell_size, mouse_x, mouse_y):
    # 计算鼠标在棋盘格内的位置
        rel_x, rel_y = mouse_x - board_x, mouse_y - board_y

        # 找到鼠标所在的格子
        grid_x = rel_x // cell_size
        grid_y = rel_y // cell_size

        # 找到鼠标所在的格子
        
        # 计算格子内的相对位置
        rel_x_in_grid = rel_x % cell_size
        rel_y_in_grid = rel_y % cell_size

        # 根据相对位置确定最近的顶点
        if rel_x_in_grid < cell_size / 2:
            nearest_x = grid_x * cell_size + board_x
        else:
            nearest_x = (grid_x + 1) * cell_size + board_x

        if rel_y_in_grid < cell_size / 2:
            nearest_y = grid_y * cell_size + board_y
        else:
            nearest_y = (grid_y + 1) * cell_size + board_y
        cneter =(nearest_x, nearest_y)
        
        return cneter

    chess_manager = ChessPiecesManager(33, 0, board, 8)
    chess_manager.create_pieces(4, 4, 4)
    draw_a_z_pass = None
    
    #endregion


    # 创建玩家组
    # def generate_players(player_count):
    #     players = []
    #     for i in range(player_count):
    #         if i % 2 == 0:
    #             player = Player(black, i * grid_size, 0,1)
    #         else:
    #             player = Player(black, i * grid_size, board_size[1] - grid_size)
    #         players.append(player)
    #         all_sprites.add(player)
    #     return players

    # player_count = 4
    # players = generate_players(player_count)
    # image_layer.draw(board)
    # 状态变量
    chess_pieces = [
        {"image": "assets/piece/Monsters_1.png", "name": "棋子1", "selected": False},
        {"image": "assets/piece/Monsters_2.png", "name": "棋子2", "selected": False},
        # ... 其他棋子
    ]
    # 加载棋子图像
    for piece in chess_pieces:
        piece["image_surface"] = pygame.image.load(piece["image"]).convert_alpha()
        piece["image_surface"] = pygame.transform.scale(piece["image_surface"], (50, 50))  # 根据需要调整尺寸
        
    def draw_chess_piece_list(surface, chess_pieces, start_x, start_y, gap):
        for i, piece in enumerate(chess_pieces):
            x = start_x
            y = start_y + i * (50 + gap)
            surface.blit(piece["image_surface"], (x, y))
            # 这里可以添加代码绘制棋子的名称等信息
            
    selected_player = None
    moving_piece = None 
    drawing_wall = False
    drawing_wall_butten = False
    drawing_wall_butten_atk =False
    initialization_done = False # 初始化
    lines_to_remove = []
    selected_points = []
    selected_point = None  # 存储选定的点
    temporary_line = None  # 用于实时渲染的临时线条
    draw_button_pass =None
    logo_button_pass= None
    sprite_groups = MySpriteGroup()
    CellSprite_groups = pygame.sprite.Group()
    running = True
    show_piece_selection = False
    is_dragging =False
    last_operated_position = None  # 记录上一次操作的格子位置
    passed_cell = set()
    deleted_position = [] # 用于记录已删除格子的位置
    transparent_grid_image = MySprite("transparent_grid_image.png", (game_board.x, game_board.y))
    transparent_grid_image_2 = MySprite("path_to_save_combined_image.png", (game_board.x, game_board.y))
    # background_layer.add(transparent_grid_image_2)
    image_layer.add(transparent_grid_image_2)
    boss_little = ChessPiece(load("assets/piece/BOSS.png"),(750,100),chessboard_top.cell_size*1,1,1,9)
    boss = ChessPiece(load("assets/piece/BOSS.png"),(900,70),chessboard_top.cell_size*2,1,1,9)
    boss.type=4
    pieces_tops = create_chess_pieces(chessboard_top.cell_size*1*2/3.,0,chessboard_top.board,3,10)
    pieces_tops.add(boss_little)
    pieces_tops.add(boss)
    
    # 游戏循环
    while True:
        for event in pygame.event.get():
            background_layer.draw(board)
            scroll_y_ponit = int(scroll_y/-chessboard.cell_size)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # 一次性初始化内容
            if not initialization_done:
                # 这里放置初始化代码
                #---------- button ----------#
                round_button_text =Button_image(board,button_rect_round_text,text_distance_left,my_font,f"回合:",(87,207),(20,20,20),size =24)
                round_button =Button_image(board,button_rect_round,round_button_path,my_font,f"{round_count}",(147,207),TEXT_COLOR)
                color_button=Button_image(board,color_button_rect,round_button_path,my_font,)
                attack_button = Button_image(board,draw_line_atk_button_rect,attack_off_path,my_font,)
                draw_line_button = Button_image(board,draw_line_button_rect,draw_line_button_off_path,my_font,)
                distance_button_text =Button_image(board,button_rect_line_distance_text,text_distance,my_font,f"距离",(1257,77),(20,20,20),size =24)
                distance_button =Button_image(board,button_rect_line_distance,round_button_path,my_font,f"0",(1327,77),TEXT_COLOR)
                
                
                #---------- button ----------#
                # 
                # boss = Player("assets/piece/BOSS.png",chessboard.cell_size*2 - 10,(8000,550),4,0)
                
                # boss_layer.add(boss.image)
                
                all_player_Group.add(boss)
                initial_plyaer_1 = InputBox((1200, 50, 50, 50), (255,255,255), (0,0,0), my_font,"")
                
                # all_player_Group.add(boss_little)
                
                # boss_layer.add(boss_little.image)
                
                chess_piece_selection_interface = ChessPieceSelectionInterface(100, 50, 300, 500, chess_pieces)
                all_sprites = pygame.sprite.Group()
                all_sprites.add(chess_piece_selection_interface)
                button_test = ButtonSprite(pygame.Rect(800, 50, 300, 50), "初始文本", my_font,(0,0,0),(255, 255, 255,0))
                button_texts = pygame.sprite.Group(button_test)
                last_round_obstacles = []
                last_round_cell = []
                # 设置标志，避免再次执行这部分代码
                initialization_done = True
                
            # user_input_1 = initial_plyaer_1.handle_event(event)
            # # 使用正则表达式匹配数字1、2和3
            # if user_input_1:
            #     numbers = re.findall(r'\d+', user_input_1)
            #     # 将匹配到的数字转换为整数
            #     numbers = [int(num) for num in numbers]
            #     results = [x < 9 for x in numbers]
            #     if len(numbers)==3 and all(results):
            #         number_1 = numbers[0]
            #         number_2 = numbers[1]
            #         number_3 = numbers[2]
            #         chess_manager.update_pieces(number_1, number_2, number_3)
            #         print(numbers)
            #     elif len(numbers)==2:
            #         number_1 = numbers[0]
            #         number_2 = numbers[1]
            #         boss = place_boss_on_board_set(boss,number_1,number_2,game_board.x,game_board.y,chessboard.rows,chessboard.cols,chessboard.cell_size)
            #         pass
                # # 打印提取的数字
            # if event.type == pygame.VIDEORESIZE:
            # # 捕获新的宽度和高度
            #     width, height = event.size5
            #     # 重新设置窗口大小
            #     board = pygame.display.set_mode((width, height), pygame.RESIZABLE)

            if event.type == pygame.MOUSEBUTTONDOWN:
                for block in color_blocks:
                    if block.handle_event(event):
                        print(f"{block.color}")
                        chessboard.color = block.color
                if logo_rect.collidepoint(event.pos):  # 检查是否点击了按钮
                    show_piece_selection = not show_piece_selection  # 切换棋子选择列表的显示
                    print(show_piece_selection)
                elif event.button == 1: 
                    if draw_line_atk_button_rect.collidepoint(event.pos) and not drawing_wall_butten:
                        drawing_wall_butten_atk =not drawing_wall_butten_atk
                        if drawing_wall_butten_atk:
                            attack_button.update_image(attack_on_path)
                        if not drawing_wall_butten_atk:
                            attack_button.update_image(attack_off_path)
                        print("攻击")
                # elif button_rect_3.collidepoint(event.pos):     
                #     if wait_for_confirmation():  # 等待用户确认
                #         return  # 用户确认后重启游戏
                #     else:
                #         continue  # 用户取消，继续游戏
                if event.button == 1:  # 左键点击
                    if button_rect_round.collidepoint(event.pos):
                        round_count += 1 
                        chessboard_left.remove_row(3)
                        round_button.update_text(f"{round_count}")
                elif event.button == 3:  # 右键点击
                    if button_rect_round.collidepoint(event.pos):
                        round_count = max(0, round_count - 1)
                        round_button.update_text(f"{round_count}")
                elif event.button == 2:  # 鼠标中键按下
                    mouse_dragging = True
                
                
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 2:  # 鼠标中键释放
                    mouse_dragging = False
            
            # 处理拖动逻辑
            if mouse_dragging:
                mouseX, mouseY = pygame.mouse.get_pos()
                clicked_row = (mouseY - game_board.y) // chessboard.cell_size
                clicked_col = (mouseX - game_board.x) // chessboard.cell_size
                if 0 <= clicked_row < chessboard.rows and 0 <= clicked_col < chessboard.cols:
                    print(chessboard.board[clicked_row][clicked_col])
                    if chessboard.board[clicked_row][clicked_col]!=4 :
                        chessboard.board[clicked_row][clicked_col] |= 4
                    # print("存储2")
                    for obstacle in obstacles.sprites():
                        if obstacle.rect.collidepoint((mouseX, mouseY)):
                            obstacles.remove(obstacle)
                    # print(chessboard.board[clicked_row][clicked_col])
                    chessboard.add_obstacle(clicked_row + scroll_y_ponit, clicked_col)
                    color_alpha = chessboard.color + (200,)
                    obstacle = Obstacle(color_alpha,clicked_col*chessboard.cell_size+game_board.x,(clicked_row+scroll_y_ponit)*chessboard.cell_size+game_board.y,  chessboard.cell_size,chessboard.cell_size,clicked_row,clicked_col)
                    obstacles.add(obstacle)
                    obstacles.update(scroll_y)
                    # sprite_group = chessboard.draw_a_z(my_font,290,155,clicked_row+scroll_y_ponit,clicked_col,scroll_y,scroll_y_ponit)
                    # sprite_groups.add(sprite_group)
                    
                    # print(f"点击了{clicked_row},{clicked_col}")
            # 滚动事件
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                clicked_row = (mouseY - game_board.y) // chessboard.cell_size
                clicked_col = (mouseX - game_board.x) // chessboard.cell_size
                clicked_row_left = int((mouseY - game_board_left.y) / chessboard_left.cell_size)
                clicked_col_left = int((mouseX - game_board_left.x) / chessboard_left.cell_size)
                if event.button == 4 and 0 <= clicked_row < chessboard.rows and 0 <= clicked_col < chessboard.cols:  # 向上滚动
                    scroll_y = min(scroll_y + chessboard.cell_size, 0)  # 向上滚动一个格子的高度
                elif event.button == 5 and 0 <= clicked_row < chessboard.rows and 0 <= clicked_col < chessboard.cols:  # 向下滚动
                    scroll_y = max(scroll_y - chessboard.cell_size, -(board_height - screen_height))  # 向下滚动一个格子的高度
                if event.button == 4 and 0 <= clicked_row_left < chessboard_left.rows and 0 <= clicked_col_left < chessboard_left.cols:  # 向上滚动
                    scroll_y_left = min(scroll_y_left + chessboard_left.cell_size, 0)  # 向上滚动一个格子的高度
                elif event.button == 5 and 0 <= clicked_row_left < chessboard_left.rows and 0 <= clicked_col_left < chessboard_left.cols:  # 向下滚动
                    scroll_y_left = max(scroll_y_left - chessboard_left.cell_size, -(board_height - screen_height))  # 向下滚动一个格子的高度
                # 更新所有线条精灵的位置   
                for line in line_sprites:
                    line.update(scroll_y)
                board.set_clip(None)
                # 更新Layer对象的滚动偏移量
                boss_layer.set_scroll(scroll_y)
                
                image_layer.set_scroll(scroll_y)
                obstacles.update(scroll_y)
                # CellSprite_groups.update(scroll_y)
                
                
                
                # boss.update(scroll_y)
            # 鼠标点击事件处理
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouseX, mouseY = pygame.mouse.get_pos()
                clicked_row = int((mouseY - game_board.y-50) / chessboard.cell_size)
                clicked_col = int((mouseX - game_board.x-50) / chessboard.cell_size)
                print(clicked_row,clicked_col)
                if 0 <= clicked_row < chessboard.rows and 0 <= clicked_col < chessboard.cols:
                    print("操作")
                    if drawing_wall_butten:
                        mouseX, mouseY = pygame.mouse.get_pos()
                        mouseY -= scroll_y
                    
                        vertex = find_nearest_vertex((mouseX, mouseY), chessboard.cell_size, (game_board.x, game_board.y))
                        # 如果是第一次点击，记录起始点
                        if not selected_point:
                            # 记录第一个点并创建一条新的线条
                            selected_point = vertex
                            
                            temporary_line = LineSprite(selected_point, selected_point, scroll_y, color=(0, 0, 0), width=9)
                            line_sprites.add(temporary_line)
                        else:
                            temporary_line.end_pos = find_nearest_vertex((mouseX, mouseY), chessboard.cell_size, (game_board.x, game_board.y))
                            # 完成当前的线条并准备绘制新线条
                            selected_point = None
                            temporary_line = None
                    if drawing_wall_butten_atk and not draw_line_atk_button_rect.collidepoint(event.pos):
                        mouseX, mouseY = pygame.mouse.get_pos()
                        mouseY -= scroll_y
                        vertex,vertex_abs =find_nearest_center(chessboard,mouseX, mouseY, (game_board.x, game_board.y))
                        # print(selected_point)
                        # print(vertex_abs)
                        if not selected_point:
                            mouseX, mouseY = pygame.mouse.get_pos()
                            # 记录第一个点并创建一条新的线条
                            for line in line_sprites.sprites():
                                if line.type == 1:
                                    print(line.passed_cells)

                                    for (col, row) in line.passed_cells:
                                        chessboard.remove_obstacle(row, col, 4)  # 从棋盘上移除障碍
                                    for obstacle in obstacles.sprites():
                                        if obstacle.type == 1:
                                                obstacles.remove(obstacle)  # 移除 type 为 1 的障碍物
                                    line_sprites.remove(line)
                            
                                    

                            selected_point = vertex
                            temporary_line = LineSprite(selected_point, selected_point, scroll_y, (128, 128, 128), 9,vertex_abs)
                            temporary_line.type = 1
                            line_sprites.add(temporary_line)
                        else:
                            # 完成当前的线条并准备绘制新线条
                        
                            temporary_line.end_pos,_ =find_nearest_center(chessboard,mouseX, mouseY, (game_board.x, game_board.y))
                            print(temporary_line.start_pos_board,temporary_line.end_pos_board)
                            temporary_line.color_cells_along_line(temporary_line.start_pos,temporary_line.end_pos,(64, 64, 64),chessboard.cell_size,temporary_line.start_pos_board,temporary_line.end_pos_board,game_board.x,game_board.y)
                            print(temporary_line.distance) # 距离计算
                            distance_button.update_text(f"{temporary_line.distance}")
                            passed_cell = temporary_line.passed_cells
                            
                            
                            # print(temporary_line.passed_cells)
                            # print(temporary_line.passed_rect)
                            # for cells,rects in zip(temporary_line.passed_cells,temporary_line.passed_rect):
                            #     col,row = cells
                            #     x,y =rects[0],rects[1]
                            #     # print(row,col,x,y)
                            #     new_obstacle = Obstacle((192, 192, 192,128),x,y,chessboard.cell_size,chessboard.cell_size,row,col)
                            #     obstacles.add(new_obstacle)
                            #     obstacles.update(scroll_y)
                            #     chessboard.add_obstacle(row,col)
                            #     sprite_group = chessboard.draw_a_z(my_font,game_board.x,game_board.y,row,col,scroll_y,scroll_y_ponit)
                            #     sprite_groups.add(sprite_group)
                            selected_point = None
                            temporary_line = None
                        pass
            

            if event.type == pygame.MOUSEMOTION:
                # 如果已经有选定的起始点，则更新临时线条的结束位置
                if selected_point:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    mouseY -= scroll_y
                    if temporary_line:
                        # temporary_line.end_pos = find_nearest_vertex((mouseX, mouseY), chessboard.cell_size, (game_board.x, game_board.y))
                        temporary_line.end_pos = (mouseX, mouseY)
                    if drawing_wall_butten_atk:
                        _, temporary_line.end_pos_board = find_nearest_center(chessboard, mouseX, mouseY, (game_board.x, game_board.y))
                        temporary_line.end_pos = (mouseX, mouseY)
                        temporary_line.color_cells_along_line(temporary_line.start_pos, temporary_line.end_pos, (64, 64, 64), chessboard.cell_size, temporary_line.start_pos_board, temporary_line.end_pos_board, game_board.x, game_board.y)
                        for col, row in temporary_line.last_passed_cells:
                            for obstacle in obstacles.sprites():
                                if obstacle.cols == col and obstacle.rows == row:
                                    if obstacle.type == 1:
                                        obstacles.remove(obstacle)  # 移除 type 为 1 的障碍物
                                        chessboard.remove_obstacle(row, col, 4)  # 从棋盘上移除障碍 

                                # if obstacle.cols == col and obstacle.rows == row and obstacle.type == 0:
                                #     chessboard.add_obstacle(row, col)
                            # for sprite in sprite_groups.sprites():
                            #     if sprite.col == col and sprite.row == row  :
                            #         sprite_groups.remove(sprite)
                            
                        print(temporary_line.passed_cells)
                        for cells, rects in zip(temporary_line.passed_cells, temporary_line.passed_rect):
                            col, row = cells
                            x, y = rects[0], rects[1]
                            # 添加新障碍物
                            print(chessboard.board[row][col])
                            # if  not chessboard.board[row][col] &4 :
                            new_obstacle = Obstacle((192, 192, 192, 128), x, y, chessboard.cell_size, chessboard.cell_size, row, col)
                            new_obstacle.type =1
                            obstacles.add(new_obstacle)
                            obstacles.update(scroll_y)
                            chessboard.add_obstacle(row, col)
                                
                                # MySprite_text
                                # sprite_group = chessboard.draw_a_z(my_font, game_board.x, game_board.y, row, col, scroll_y, scroll_y_ponit)
                                # sprite_group.board[row][col] = 1
                                # sprite_groups.add(sprite_group)
                                # print(sprite_groups)

                # 如果是第一次点击，记录起始点
                # if not selected_points:
                #     selected_points.append(event.pos)
                # # 如果是第二次点击，记录终点，创建线条，然后重置选点列表
                # else:
                #     selected_points.append(event.pos)
                #     # 创建线条精灵
                #     new_line = LineSprite(selected_points[0], selected_points[1], color=(255, 0, 0), width=5)
                #     # 重置选点列表以便绘制新的线条
                #     selected_points = []


            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not drawing_wall_butten and not drawing_wall_butten_atk:
                
                # 获取鼠标当前的位置，并加5上滚动偏移
                mouseX, mouseY = pygame.mouse.get_pos()
                mouseY_last =mouseY
                mouseY += -scroll_y  # 加上负的滚动偏移，因为滚动向上是正值，向下是负值
                # 检查是否点击了左侧的棋子
                
                area_rect = pygame.Rect(300, 0, chessboard_top.cols*chessboard_top.cell_size, chessboard_top.rows*chessboard_top.cell_size - 50 )
                area_rect_2 =pygame.Rect(game_board_left.x, game_board_left.y, chessboard_left.cols*chessboard_left.cell_size, chessboard_left.rows*chessboard_left.cell_size)
                # 选择top棋子
                # if line_tetton:

                #     pass
                if area_rect.collidepoint(mouseX, mouseY_last):
                    for pieces_top in pieces_tops.sprites():
                        if pieces_top.rect.collidepoint(event.pos) and show_piece_selection:
                            cloned_piece = ChessPiece(pieces_top.image_original, pieces_top.rect.center, pieces_top.cell_size, pieces_top.board, pieces_top.rows, pieces_top.cols)
                            pieces_tops.add(cloned_piece)
                            if pieces_top.type ==4:
                                cloned_piece.type =4
                            moving_piece = pieces_top
                            # pieces_tops.add(pieces_top)
                            moving_piece.position = 3
                            moving_piece.inchessboard = 0
                            pieces_top.old_rect = pieces_top.rect
                            print(f"选中棋子{moving_piece}")

                            # chess_pieces_group.add(moving_piece)
                # for player in all_player_Group:
                #     if player.rect.collidepoint(event.pos) and player.type != 4:
                #         selected_piece = player
                #         moving_piece = None  # 确保不会移动棋盘上的棋子
                #         print(f"选中棋子{selected_piece.id}")
                #         break
                # 选择left棋子
                elif area_rect_2.collidepoint(event.pos):
                    mouseX, mouseY = pygame.mouse.get_pos()
                    mouseY += -scroll_y_left
                    # for pieces_top in chess_pieces_group.sprites() + chess_pieces_group_left.sprites():
                    #     # if pieces_top.rect.collidepoint((mouseX,mouseY)):
                            # 创建一个单点的rect用来检测碰撞
                    mouse_rect = pygame.Rect((mouseX, mouseY), (1, 1))
                    # 获取所有重叠的精灵
                    collided_sprites = [s for s in chess_pieces_group_left if mouse_rect.colliderect(s.rect)]
                    print(len(collided_sprites))
                    # 如果有多个重叠的精灵，随机选择一个
                    if len(collided_sprites) > 0:
                        selected_sprite = random.choice(collided_sprites)
                        # 这里可以处理选中的精灵
                        print(f"Selected sprite: {selected_sprite}")
                    moving_piece = selected_sprite
                    # 记录原始位置
                    print(f"选中棋子{moving_piece}")
                    # print(moving_piece.rows,moving_piece.cols)
                    moving_piece.old_rows = moving_piece.rows
                    moving_piece.old_cols = moving_piece.cols
                    moving_piece.position = 2
                    break
                # 如果左侧没有棋子被选中，检查棋盘上的棋子
                else:
                    for piece in chess_pieces_group.sprites():
                        mouseX, mouseY = pygame.mouse.get_pos()
                        print(piece.rect)
                        mouseY += -scroll_y
                        if piece.rect.collidepoint((mouseX,mouseY)):
                            moving_piece = piece
                            # 记录原始位置
                            # print(moving_piece.rows,moving_piece.cols)
                            moving_piece.old_rows = moving_piece.rows
                            moving_piece.old_cols = moving_piece.cols
                            break
                
                # 鼠标移动时更新棋子位置
            elif event.type == pygame.MOUSEMOTION:
                if moving_piece and pygame.mouse.get_pressed()[0]:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    moving_piece.rect.center = (mouseX, mouseY)
                    if moving_piece.position ==1:
                        moving_piece.update(-scroll_y)
                    elif moving_piece.position ==2:
                        moving_piece.update(-scroll_y_left)
                    else:
                        moving_piece.rect.center = (mouseX, mouseY)
                    #     print(scroll_y)
                    #     scroll = 0
                    # if moving_piece.position ==2:
                    #     scroll=scroll
                    # else:
                    #     scroll = scroll_y
                    # moving_piece.rect.centery = mouseY - scroll
                    

            # 放下棋子时更新棋盘状态
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if moving_piece:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    clicked_row = int((mouseY - game_board.y) / chessboard.cell_size)
                    clicked_col = int((mouseX - game_board.x) / chessboard.cell_size)
                    clicked_row_left = int((mouseY - game_board_left.y) / chessboard_left.cell_size)
                    clicked_col_left = int((mouseX - game_board_left.x) / chessboard_left.cell_size)
                    # print(clicked_row_left,clicked_col_left)
                    # 清除旧位置
                    if moving_piece.position ==1 :
                        print("旧位置")
                        print(moving_piece.old_rows,moving_piece.old_cols)
                        chessboard.board[moving_piece.old_rows][moving_piece.old_cols] &= ~ 1
                        # print("qwfqf",chessboard.board[moving_piece.old_rows][moving_piece.old_cols])

                    # 检查新位置是否合法并更新棋盘
                    T_top = 0 <= clicked_row_left < chessboard_left.rows and 0 <= clicked_col_left < chessboard_left.cols
                    if 0 <= clicked_row_left < chessboard_left.rows and 0 <= clicked_col_left < chessboard_left.cols:
                        center_x = game_board_left.x + clicked_col_left* chessboard_left.cell_size + chessboard_left.cell_size // 2
                        center_y = game_board_left.y + clicked_row_left * chessboard_left.cell_size + chessboard_left.cell_size // 2
                        moving_piece.rect.center = (center_x, center_y - scroll_y_left)
                        print(moving_piece.rect)
                        if moving_piece in pieces_tops.sprites(): 
                            pieces_tops.remove(moving_piece)
                        if moving_piece.position !=2:
                            new_piece_sprite = ChessPiece(moving_piece.image_original, (center_x, center_y- scroll_y_left), chessboard.cell_size,chessboard.board,clicked_row,clicked_col)
                            new_piece_sprite.position =2
                            chess_pieces_group_left.add(new_piece_sprite)   
                        print("l")
                        # print(moving_piece.rect.center)
                        moving_piece = None
                        
                    elif my_rect_top.collidepoint(mouseX, mouseY):
                        if moving_piece in pieces_tops.sprites(): 
                            pieces_tops.remove(moving_piece)
                            # print("超过")
                        print("你不能放置在这里")

                    elif 0 <= clicked_row < chessboard.rows and 0 <= clicked_col < chessboard.cols and moving_piece.inchessboard == 0 :
                        if  chessboard.board[clicked_row+scroll_y_ponit][clicked_col] in [0,4]  and moving_piece.position!=2:
                            chessboard.board[clicked_row+scroll_y_ponit][clicked_col] |= 1  # 更新新位置
                            # print("当前:",clicked_row+scroll_y_ponit)
                            moving_piece.rows = clicked_row+scroll_y_ponit  # 更新棋子行
                            moving_piece.cols = clicked_col  # 更新棋子列
                            moving_piece.position = 1 # 更新棋子局部位置
                            center_x = game_board.x + clicked_col * chessboard.cell_size + chessboard.cell_size // 2
                            center_y = game_board.y + clicked_row * chessboard.cell_size + chessboard.cell_size // 2
                            if moving_piece.type == 4:
                                mouseX, mouseY = pygame.mouse.get_pos()
                                center_x, center_y = find_nearest_vertex_3(game_board.x, game_board.y, chessboard.cell_size,mouseX, mouseY)
                                print(center_x)
                                new_piece_sprite = ChessPiece(moving_piece.image_original, (center_x, center_y-scroll_y), chessboard.cell_size*2,chessboard.board,moving_piece.rows,moving_piece.cols)
                                new_piece_sprite.type = 4
                                chess_pieces_group.add(new_piece_sprite)
                            else:
                                new_piece_sprite = ChessPiece(moving_piece.image_original, (center_x, center_y-scroll_y), chessboard.cell_size,chessboard.board,moving_piece.rows,moving_piece.cols)
                                chess_pieces_group.add(new_piece_sprite)
                            moving_piece.old_rows = new_piece_sprite.rows
                            moving_piece.old_cols = new_piece_sprite.cols
                            # ChessPiece5
                            # 更新棋子图形位置
                            # moving_piece.move(clicked_row,clicked_col,-scroll_y)
                            if moving_piece in pieces_tops.sprites(): 
                                pieces_tops.remove(moving_piece)
                            moving_piece = None
                        else:
                            if moving_piece in pieces_tops.sprites(): 
                                pieces_tops.remove(moving_piece)
                            print("这是违规的！")
                    elif 0 <= clicked_row < chessboard.rows and 0 <= clicked_col < chessboard.cols and moving_piece.position!=2:
                            if  chessboard.board[clicked_row+scroll_y_ponit][clicked_col] in [0,4] :
                                chessboard.board[clicked_row+scroll_y_ponit][clicked_col] |= 1  # 更新新位置
                                # print(chessboard.board[clicked_row+scroll_y_ponit][clicked_col])
                                moving_piece.rows = clicked_row+scroll_y_ponit  # 更新棋子行
                                moving_piece.cols = clicked_col  # 更新棋子列
                                moving_piece.position = 1 # 更新棋子位置
                                
                                if moving_piece.type == 4:
                                    mouseX, mouseY = pygame.mouse.get_pos()
                                    center_x, center_y = find_nearest_vertex_3(game_board.x, game_board.y, chessboard.cell_size,mouseX, mouseY)
                                    print(center_x)
                                    moving_piece.type = 4
                                    moving_piece.rect.center =(center_x,center_y-scroll_y)
                                else:
                                    center_x = game_board.x + clicked_col * chessboard.cell_size + chessboard.cell_size // 2
                                    center_y = game_board.y + clicked_row * chessboard.cell_size + chessboard.cell_size // 2
                                    # ChessPiece5
                                    # 更新棋子图形位置
                                    moving_piece.rect.center =(center_x,center_y-scroll_y)
                                # moving_piece.move(clicked_row,clicked_col,-scroll_y)
                                if moving_piece in pieces_tops.sprites(): 
                                    pieces_tops.remove(moving_piece)
                                moving_piece = None
                    
                    # elif 0 <= clicked_row_left < chessboard_left.rows and 0 <= clicked_col_left < chessboard_left.cols:
                    #         print(1)
                    else:
                        print("移动到棋盘外,这是违规的！")
            #计算行的时候考虑偏移量
            # # 检测按键事件并变更棋子图像为灰度
            # elif event.type == pygame.KEYDOWN:
                
            # 事件循环中的键盘事件处理
            
            # 事件循环中的鼠标事件处理
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 1 and drawing_wall:  # 左键且处于绘制模式
            #         mouseX, mouseY = pygame.mouse.get_pos()
            #         # 计算点击的棋盘格坐标
            #         print(121)
            #         col = (mouseX - game_board.x) // chessboard.cell_size
            #         row = (mouseY - game_board.y) // chessboard.cell_size
            #         # 标记围墙的位置
            #         chessboard.add_wall(row, col)

            #     elif event.button == 3 and drawing_wall:  # 右键且处于绘制模式，删除围墙
            #         mouseX, mouseY = pygame.mouse.get_pos()
            #         col = (mouseX - game_board.x) // chessboard.cell_size
            #         row = (mouseY - game_board.y) // chessboard.cell_size
            #         # 移除围墙的标记
            #         chessboard.remove_wall(row, col)            
                    
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:  # 假设按 'W' 键进入绘制围墙模式
                    drawing_wall_butten = not drawing_wall_butten and not drawing_wall_butten_atk  # 切换绘制状态
                    if drawing_wall_butten:
                        draw_line_button.update_image(draw_line_button_on_path)
                    if not drawing_wall_butten:
                        draw_line_button.update_image(draw_line_button_off_path)
                    print("绘制模式:",drawing_wall_butten)
                    button_test.toggle_text()
                if event.key == pygame.K_z:  # 假设按 'z' 表示行动结束
                    # center_x = game_board_left.x + clicked_col_left* chessboard_left.cell_size + chessboard_left.cell_size // 2
                    # center_y = game_board_left.y + clicked_row_left * chessboard_left.cell_size + chessboard_left.cell_size // 2-scroll_y_left
                    # previous_state(center_x)
                    # center_x = game_board_left.x + clicked_col_left * chessboard_left.cell_size + chessboard_left.cell_size // 2
                    # center_y = game_board_left.y + clicked_row_left * chessboard_left.cell_size + chessboard_left.cell_size // 2
                    print(game_board_left.x,game_board_left.y)
                    chessboard_left.add_tick(load("assets/tick.png"),game_board_left.x,game_board_left.y)
                    print(scroll_y_left)
                if event.key == pygame.K_x:  # 假设按 'x' 表示删除
                    chessboard_left.remove_row(3)
                # elif event.type == pygame.KEYDOWN:
                #     if event.key in color_mapping:
                #         chessboard.update_color(color_mapping[event.key])
                        # chessboard.color = color_mapping[event.key]

                # if event.key == pygame.K_x:  # 检测 'x' 键
                #     if selected_piece:  # 确保有棋子被选中
                #         # 获取棋子的位置和尺寸
                #         piece_x, piece_y,_,_ = selected_piece.rect
                #         piece_size = selected_piece.image_face.get_size()

                #         # 计算“X”的起点和终点坐标
                #         start_pos1 = (piece_x, piece_y)
                #         end_pos1 = (piece_x + piece_size[0], piece_y + piece_size[1])
                #         start_pos2 = (piece_x + piece_size[0], piece_y)
                #         end_pos2 = (piece_x, piece_y + piece_size[1])
                #         print(f"{start_pos1},{end_pos1},{start_pos2},{end_pos2}")
                #         print("X")
                #         # chessboard在屏幕上绘制“X”
                #         pygame.draw.line(board, (255, 250, 0), start_pos1, end_pos1, 50)  # 红色线条，宽度为2
                #         pygame.draw.line(board, (255, 0, 0), start_pos2, end_pos2, 50)
                        
                if event.key == pygame.K_x:  # 检测 'x' 键
                    # if selected_piece:  # 确保有棋子被选中
                    #     # 将棋子的图像变为灰度
                    #     print("灰度化")
                    #     grayscale_image = pygame.Surface(selected_piece.image_face.get_size())
                    #     # grayscale_image.blit(selected_piece.image_face, (0, 0))
                    #     for i in range(grayscale_image.get_width()):
                    #         for j in range(grayscale_image.get_height()):
                    #             pixel = grayscale_image.get_at((i, j))
                    #             avg = (pixel.r + pixel.g + pixel.b) // 3
                    #             grayscale_image.set_at((i, j), (avg, avg, avg))
                    #     # 获取棋子的位置
                    #     piece_x, piece_y,piece_x_2,piece_y_2 = selected_piece.rect
                    #     print(grayscale_image)
                    #     selected_piece.image_face = grayscale_image
                    #     selected_piece_image = Background(grayscale_image,piece_x_2,(piece_x,piece_y))
                        
                        # print(piece_x, piece_y )
                        # # 在屏幕上绘制灰度图像
                        pass
                        # image_layer.add(selected_piece_image)
                        
                        # board.blit(grayscale_image, (piece_x, piece_y))
                        # continue  # 跳过事件循环中的剩余部分
                # elif event.key == pygame.K_SPACE: #空格
                #     mouseX, mouseY = pygame.mouse.get_pos()
                #     mouseY += -scroll_y
                #     clicked_row = (mouseY - game_board.y) // chessboard.cell_size
                #     clicked_col = (mouseX - game_board.x) // chessboard.cell_size
                #     if 0 <= clicked_row < chessboard.rows and 0 <= clicked_col < chessboard.cols:
                #         center_x = game_board.x + clicked_col * chessboard.cell_size + chessboard.cell_size // 2
                #         center_y = game_board.y + clicked_row * chessboard.cell_size + chessboard.cell_size // 2
                        
                #         try:
                #             if chessboard.board[clicked_row][clicked_col] in (0, 1, 4, 5) and hasattr(selected_piece, 'image_face'):  # 确保目标位置可以放置
                #                 # print([clicked_row],[clicked_col])
                #                 # print(boss.board[clicked_row][clicked_col])
                #                 print("放置前",(chessboard.board[clicked_row][clicked_col]))
                #                 (chessboard.board[clicked_row][clicked_col]) |= 1
                #                 print("放置后",(chessboard.board[clicked_row][clicked_col]))
                #                 chessboard.add_piece(clicked_row,clicked_col)
                #                 new_piece_sprite = ChessPiece(selected_piece.image_face, (center_x, center_y), chessboard.cell_size,chessboard.board,clicked_row,clicked_col)
                #                 chess_pieces_group.add(new_piece_sprite)
                #         except:
                #             pass
                #     else:
                #         print('该位置不能放置棋子')
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # 右键点击开始拖动
                is_dragging = True
                delete_performed = False

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:  # 右键释放结束拖动
                is_dragging = False

            elif event.type == pygame.MOUSEMOTION:
                if is_dragging and not delete_performed:               # continue  # 跳过事件循环中的剩余部分
            # elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # 右键点击
                    mouseX, mouseY = pygame.mouse.get_pos()
                    mouseX_last, mouseY_last = mouseX, mouseY
                    # 调整 mouseX 和 mouseY 以匹配棋盘的实际位置
                    mouseX -= game_board.x
                    mouseY -= game_board.y + scroll_y

                    clicked_row = mouseY // chessboard.cell_size
                    clicked_col = mouseX // chessboard.cell_size
                    if last_operated_position != (clicked_row, clicked_col):
                        last_operated_position = (clicked_row, clicked_col)  # 更新操作的格子位置
                        clicked_row_left = int((mouseY_last - game_board_left.y) / chessboard_left.cell_size)
                        clicked_col_left = int((mouseX_last - game_board_left.x) / chessboard_left.cell_size)
                        line_removed = False  # 新增变量用于标记是否移除了line
                        obstacle_removed = False
                        if 0 <= clicked_row_left < chessboard_left.rows and 0 <= clicked_col_left < chessboard_left.cols:
                            for piece in chess_pieces_group_left.sprites():
                                    if piece.rect.collidepoint((mouseX_last, mouseY_last - scroll_y_left)):
                                        chess_pieces_group_left.remove(piece)
                                        # chessboard.board[clicked_row][clicked_col] &= ~1
                                        print(piece)
                        closest_line = None
                        min_distance = float('inf')
                        for line in line_sprites.sprites():
                            distance_point = point_line_distance(line.start_pos, line.end_pos, (mouseX + game_board.x, mouseY + game_board.y))
                            if distance_point < 10 and distance_point < min_distance:
                                closest_line = line
                                min_distance = distance_point

                        if closest_line:
                            line_sprites.remove(closest_line)
                            print(closest_line)
                            line_removed = True  #    
                            break
                        # for cellsprite in CellSprite_groups:
                        #     if cellsprite.rect.collidepoint((mouseX_last, mouseY_last - scroll_y_left)):
                        #         CellSprite_groups.remove(cellsprite)
                        #         print(cellsprite)
                                
                        if 0 <= clicked_row < chessboard.rows and 0 <= clicked_col < chessboard.cols:
                            print(chessboard.board[clicked_row][clicked_col])
                            if not line_removed and chessboard.board[clicked_row][clicked_col] & 4:
                                for obstacle in obstacles.sprites():
                                    if obstacle.rect.collidepoint((mouseX + game_board.x, mouseY + game_board.y + scroll_y)):
                                        obstacles.remove(obstacle)
                                        # print(obstacle)
                                        print("移除障碍物之前",chessboard.board[clicked_row][clicked_col])
                                        chessboard.board[clicked_row][clicked_col] &= ~4
                                        print("移除障碍物之后",chessboard.board[clicked_row][clicked_col])
                                        print([clicked_row],[clicked_col])
                                        if obstacle.type ==1 :
                                            for line in line_sprites.sprites():
                                                if line.type ==1:
                                                    line_sprites.remove(line)
                                            for obstacle in obstacles.sprites():
                                                if obstacle.type == 1:
                                                    obstacles.remove(obstacle)
                                        
                                        for sprite in sprite_groups:
                                            if sprite.row== clicked_row and sprite.col == clicked_col:
                                                sprite_groups.remove(sprite)
                                        obstacle_removed = True
                                        # break  # 如果找到一个匹配的精灵，就跳出循环
                            if not obstacle_removed and not line_removed and  chessboard.board[clicked_row][clicked_col] & 1:  # 确保目标位置非空
                                for piece in chess_pieces_group.sprites():
                                    if piece.rect.collidepoint((mouseX + game_board.x, mouseY + game_board.y)):
                                        chess_pieces_group.remove(piece)
                                        chessboard.board[clicked_row][clicked_col] &= ~1
                                        print(piece)

                        # if (clicked_row,clicked_col) not in deleted_position:
                        #     deleted_position.append((clicked_row,clicked_col))
                        # print(deleted_position)
                    # is_dragging = False
                        # chessboard.board[clicked_row][clicked_col] =0
                        # else:
                        #     for line in line_sprites:
                        #         if point_line_distance(line.start_pos, line.end_pos, (mouseX + game_board.x, mouseY + game_board.y)) < 10:
                        #             print(1)
                        #             line_sprites.remove(line)
                        #             break
            # # 放置棋子
            # elif event.type == pygame.KEYDOWN:
                

            # elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # 右键点击
            #     mouseX, mouseY = pygame.mouse.get_pos()
            #     clicked_row = (mouseY - game_board.y) // chessboard.cell_size
            #     clicked_col = (mouseX - game_board.x) // chessboard.cell_size
            #     chessboard.remove_obstacle(clicked_row, clicked_col)


        # print(scroll_y)
        # print(scroll_y_ponit)
        
        # draw_button_2(board, button_rect_2, button_text)  # 按钮
        
        # chess_manager.pieces_group.draw(board)
        # for sprite in sprite_groups:
        #     sprite.set_scroll_y(scroll_y)
        sprite_groups.update(scroll_y)
        board.set_clip(clip_rect) # 设置剪裁区域，仅在剪裁区域内绘制
        
        # game_board_left.draw_well(board,scroll_y_left) # 障碍物
        
        # CellSprite_groups.draw(board)
        image_layer.draw(board)
        obstacles.draw(board)  # 绘制所有障碍物精灵
        
        
        game_board.draw_well(board,scroll_y) # 黑线
        for row in range(chessboard.rows): # 绘制围墙
            for col in range(chessboard.cols):
                if chessboard.board[row][col] == 'wall':
                    # 这里需要根据实际情况调整绘制围墙的逻辑
                    pygame.draw.line(board, (0, 0, 0), (col * chessboard.cell_size + game_board.x, row * chessboard.cell_size + game_board.y),
                                    ((col + 1) * chessboard.cell_size + game_board.x, (row + 1) * chessboard.cell_size + game_board.y), 2)
        boss_layer.draw(board)
        
        
        sprite_groups.draw(board) #字母
        # sprite_groups.empty
        for piece in chess_pieces_group: # 绘制棋子
            # 如果棋子正在移动，则应用滚动偏移量
            if piece == moving_piece:
                if piece.position == 2:
                    scroll=scroll_y_left
                else:
                    scroll=scroll_y       
                # 直接渲染到屏幕上的位置需要加上滚动偏移
                board.blit(piece.image, (piece.rect.topleft[0], piece.rect.topleft[1] + scroll))
            else:
                if piece.position == 2:
                    scroll=scroll_y_left
                else:
                    scroll=scroll_y
                # 如果棋子不在移动，按照其在棋盘上的位置绘制
                board.blit(piece.image, (piece.rect.x, piece.rect.y + scroll))
        for line in line_sprites:
            line.draw_line(board)
        
        board.set_clip(None) #裁剪结束
        board.set_clip(clip_rect_left)
        chessboard_left.draw_tick_pieces(board,scroll_y_left)
        for piece in chess_pieces_group_left: # 绘制棋子
            # 如果棋子正在移动，则应用滚动偏移量
            if piece == moving_piece:
                if piece.position == 2:
                    scroll=scroll_y_left
                else:
                    scroll=scroll_y       
                # 直接渲染到屏幕上的位置需要加上滚动偏移
                board.blit(piece.image, (piece.rect.topleft[0], piece.rect.topleft[1] + scroll))
            else:
                if piece.position == 2:
                    scroll=scroll_y_left
                else:
                    scroll=scroll_y
                # 如果棋子不在移动，按照其在棋盘上的位置绘制
                board.blit(piece.image, (piece.rect.x, piece.rect.y + scroll))
        
        board.set_clip(None) #裁剪结束
        #---------- button ----------#
        # draw_button(board, f"round: {round_count}", button_rect, BUTTON_COLOR, TEXT_COLOR)
        # round_button =Button_image(board,button_rect_round,round_button_path,my_font,f"{round_count}",(147,207),TEXT_COLOR)
        # attack_button = Button_image(board,draw_line_atk_button_rect,attack_off_path,my_font,)
        round_button_text.draw()
        round_button.draw()
        color_button.draw()
        attack_button.draw()
        draw_line_button.draw()
        distance_button.draw()
        distance_button_text.draw()
        # draw_button_text(board, button_rect_round,round_button_path,f" {round_count}",(140,210),TEXT_COLOR,my_font)
        # round_button.draw(board)
        # board.blit(text_surface, (500, 0)) #选择棋子
        # pygame.draw.rect(board, chessboard.color, pygame.Rect(850,30,50,50), width=50)
        # draw_button(board, f"{drawing_wall_butten_atk}", pygame.Rect(1200,50,50,50),(255,255,255), (128,128,128,0))
        draw_button(board, f"", pygame.Rect(1407,57,40,40),chessboard.color, (128,128,128,0))
        #---------- button ----------#
        if show_piece_selection:
            pieces_tops.draw(board)
        # initial_plyaer_1.update()
        # initial_plyaer_1.draw(board)
        
        # chessboard_left.piece_sprites(board)
        # boss_layer.draw(board)
        # chessboard.update_board_display(my_font,game_board.x,game_board.y,scroll_y,scroll_y_ponit)
        for block in color_blocks:
            block.draw(board)
        pygame.display.update()
        clock.tick(60)

# while True:
#     run_game()

url = "http://139.196.171.229:5000/hello"
response = requests.get(url=url)
if response.status_code == 200:
    permission = response.json()["permission"]
    print(permission)
    if permission:
        while True:
            run_game()
else:
    input()


    