import pygame
import random
import time
import game_framework
import main_state
import gameover_state

# 1. 게임 초기화
pygame.init()
running = True

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# 2. 게임창 옵션 설정
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# title = "My Game"
# pygame.display.set_caption(title)

# 3. 게임 내 필요한 설정
clock = pygame.time.Clock()

ss = None
left_go = False
right_go = False
space_go = False
m_list = []  # 초기화 되지 않게 while문 밖으로
a_list = []
k = 0
black = (0, 0, 0)
white = (255, 255, 255)
color = (0, 0, 0)  # 검은색RGB





class obj:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.move = 0
    def put_img(self, address):
        if address[-3:] == "png":
            self.img = pygame.image.load(address).convert_alpha()
        else:
            self.img = pygame.image.load(address)
            self.sx, self.sy = self.img.get_size()
    def change_size(self, sx, sy):
        self.img = pygame.transform.scale(self.img, (sx, sy))
        self.sx, self.sy = self.img.get_size()
    def show(self):
        screen.blit(self.img, (self.x, self.y))

# a.x-b.sx <= b.x <= a.x + a.sx
# a.y-b.

def crash(a, b):        #충돌처리함수
    if (a.x-b.sx <= b.x) and (b.x <= a.x+a.sx):
        if (a.y - b.sy <= b.y) and (b.y <= a.y+a.sy):
            return True
        else:
            return False
    else:
        return False




def enter():
    global ss, k
    ss = obj()
    ss.put_img("airplane.png")
    ss.change_size(100, 100)
    ss.x = round(size[0] / 2 - ss.sx / 2)
    ss.y = size[1] - ss.sy - 5
    ss.move = 5  # 비행선 이동속도
    # ss = pygame.image.load("airplane.png").convert_alpha()
    # ss = pygame.transform.scale(ss, (100, 100))
    # ss_sx, ss_sy = ss.get_size()
    # ss_x = round(size[0]/2 - ss_sx/2)  # round함수 : 반올림
    # ss_y = size[1] - ss_sy - 5



    # 4. 메인 이벤트
    #SB = 0
def exit():
    global ss
    #del ss

def pause():
    pass
def resume():
    pass
def handle_events():
    global k, left_go, right_go, space_go

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_framework.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_go = True
            elif event.key == pygame.K_RIGHT:
                right_go = True
       #     elif event.key == pygame.K_UP:
        #        up_go = True
            elif event.key == pygame.K_SPACE:
                space_go = True
                k = 0   #space를 눌렀을 때 끊어짐 방지
            elif event.key == pygame.K_ESCAPE:
                game_framework.change_state(main_state)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_go = False
            elif event.key == pygame.K_RIGHT:
                right_go = False
          #  elif event.key == pygame.K_UP:
          #      up_go = False
            elif event.key == pygame.K_SPACE:
                space_go = False


def update():
    global k, left_go, right_go, space_go

    if left_go == True:
        ss.x -= ss.move
        if ss.x <= 0:
            ss.x = 0
    elif right_go == True:
        ss.x += ss.move
        if ss.x >= size[0] - ss.sx:         #ss.sx : 비행선의 크기
            ss.x = size[0] - ss.sx
    #elif up_go == True:
     #   ss.y += ss.move
      #  if ss.y >= size[0] - ss.sy:         #ss.sx : 비행선의 크기
       #     ss.y = size[0] - ss.sy


    if space_go == True and k % 6 == 0:        #미사일 / k 미사일 발생 빈도를 6분의1로 줄이기
        mm = obj()
        mm.put_img("lazer.png")
        mm.change_size(30, 30)
        mm.x = round(ss.x + ss.sx/2 - mm.sx/2)
        mm.y = ss.y - mm.sy - 10
        mm.move = 15  # 비행선 이동속도
        m_list.append(mm)   #장바구니에 담기
    k += 1
    d_list = []             #미사일 지우기 del사용X
    for i in range(len(m_list)):    # 미사일 이동
        m = m_list[i]
        m.y -= m.move     #mm.y 미사일의 왼쪽 위
        if m.y <= -m.sy:
            d_list.append(i)
    for d in d_list:
        del m_list[d]

    if random.random() < 0.03 :     #적 랜덤 생성
        aa = obj()
        aa.put_img("alien1.png")
        aa.change_size(50, 50)
        aa.x = random.randrange(0, size[0]-aa.sx-round(ss.sx/2))     #randrange : 랜덤 위치제한
        aa.y = 10
        aa.move = 1  # 비행선 이동속도
        a_list.append(aa)
    d_list = []
    for i in range(len(a_list)):    #
        a = a_list[i]
        a.y += a.move     #
        if a.y >= size[1]:        #화면밖으로 나갔다면
            d_list.append(i)
    for d in d_list:
        del a_list[d]

    dm_list = []
    da_list = []
    for i in range(len(m_list)):
        for j in range(len(a_list)):
            m = m_list[i]
            a = a_list[j]
            if crash(m, a) == True:
                dm_list.append(i)
                da_list.append(j)
    dm_list = list(set(dm_list))    #중복을 제거하고 싶을 때 : list(set(aaa))
    da_list = list(set(da_list))

    for dm in dm_list:
        del m_list[dm]
    for da in da_list:
        del a_list[da]

    for i in range(len(a_list)):
        a = a_list[i]
        if crash(a, ss) == True:
            #SB = 1
            #time.sleep(1)
            game_framework.change_state(gameover_state)


def draw():
    screen.fill(black)
    ss.show()
    clock.tick(60)
    for m in m_list:
        m.show()
    for a in a_list:
        a.show()
    pygame.display.flip()