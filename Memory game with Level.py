
# 원본코드 출처 : https://youtu.be/Qsk-xsi73YA 


import pygame
from pygame import display
from random import*
from pygame.constants import HIDDEN
from pygame.draw import rect
from pygame.version import PygameVersion
pygame.init()


# 레벨에 맞게 환경을 설정
def setup(lv):
    # 숫자 노출 시간 정의
    global disp_time
    disp_time = 7 - (lv//3)
    disp_time = max(disp_time, 1)
    
    # 화면에 나타날 숫자 정의
    num_cnt = (lv // 3) + 5
    num_cnt = min(num_cnt, 20)
    
    # 화면에 grid 형태로 수 배치
    shuf_grid(num_cnt)



# 숫자 섞기
def shuf_grid(n_cnt):
    rows = 5
    columns = 9
    
    cell_size = 130 # 그리드별 가로, 세로 크기
    btn_size = 110  # 그리드내 실제 버튼 크기
    
    scr_left_margin = 55 # 왼쪽 여백
    scr_top_margin = 20  # 위쪽 여백
    
    grid=[[0 for col in range(columns)] for row in range(rows)]
    n = 1 # 시작 수, n_cnt 까지 수 생성
    
    while n <= n_cnt:
        r_idx = randrange(0, rows)    # x축 기준 위치
        c_idx = randrange(0, columns) # y축 기준 위치
        
        if grid[r_idx][c_idx] == 0:
            grid[r_idx][c_idx] = n # 숫자 n 배정
            n += 1
            
            # 현 그리드 기준 x, y 위치 신출
            center_x = scr_left_margin+(c_idx*cell_size)+cell_size/2
            center_y = scr_top_margin+(r_idx*cell_size)+cell_size/2
            
            # 숫자버튼 만들기
            btn = pygame.Rect(0, 0, btn_size, btn_size)
            btn.center = (center_x, center_y)
            
            n_btns.append(btn)  



# 시작화면 표시
def display_st_scr():
    pygame.draw.circle(screen, WHITE, st_btn.center, 60, 5)
    msg = g_font.render(f"{cur_lv}", True, WHITE)
    msg_rect = msg.get_rect(center=st_btn.center)
    screen.blit(msg, msg_rect)
    
    
    
# 게임화면 표시
def display_game_scr():
    global hidden
    
    if not hidden:
        elapse = (pygame.time.get_ticks()-st_ticks) / 1000
        if elapse > disp_time:
            hidden = True
    
    for idx, rect in enumerate(n_btns, start = 1):
        if hidden:
            # 사각버튼 그리기
            pygame.draw.rect(screen, WHITE,rect)
        else:
            # 숫자 써넣기
            cell_txt = g_font.render(str(idx), True, WHITE)
            txt_rect = cell_txt.get_rect(center=rect.center)
            screen.blit(cell_txt, txt_rect)
        


# pos 에 해당하는 버튼 확인
def chk_btn(pos):
    global start
    global st_ticks
    
    if start:
        chk_n_btns(pos)
    elif st_btn.collidepoint(pos):
        start = True
        st_ticks = pygame.time.get_ticks() # 타이머 시작



def chk_n_btns(pos):
    global hidden, start, cur_lv
    
    for btn in n_btns:
        if btn.collidepoint(pos):
            if btn == n_btns[0]: # 올바른 수 클릭 시
                del n_btns[0]
                if not hidden:
                    hidden = True
            else:
                g_over() # 틀린 수 클릭 시
                
            break
    if len(n_btns) == 0: # 모든 수를 순서대로 클릭한 경우
        start = False
        hidden = False
        cur_lv += 1
        setup(cur_lv)
        
        
        
# 게임 오버 시
def g_over():
    global running
    
    running = False
    msg = g_font.render(f"Current Level: {cur_lv}", True, WHITE)
    msg_rect = msg.get_rect(center=(scr_width/2, scr_height/2))
    screen.fill(BLACK)
    screen.blit(msg, msg_rect)



# 게임화면 초기화
scr_width = 1280 # 화면 폭
scr_height = 720 # 화면 높이
screen = pygame.display.set_mode((scr_width, scr_height))
pygame.display.set_caption("Memory Game")
g_font = pygame.font.Font(None, 120) # 게임 내 택스트 폰트

# 시작 버튼
st_btn = pygame.Rect(0, 0, 120, 120)
st_btn.center = (120, scr_height-120)

# 색
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)

n_btns=[]  # 플레이어가 누를 버튼 관리
cur_lv = 1 # 현 레벨
disp_time = None # 숫자 표시 시간
st_ticks = None  # 현재 시간 정보 저장


start = False  # 게임시작 여부 판단
hidden = False # 숫자 숨김 여부
 
setup(1) # 게임시작 전 레벨 초기화



# 게임 루프
running = True
while running == True:
    click_pos = None
    
    #이벤트 루프
    for event in pygame.event.get():  # 이벤트 종류
        if event.type == pygame.QUIT: # 창 닫힘
            running = False # 루프 탈출
            
        elif event.type == pygame.MOUSEBUTTONUP: # 사용자가 마우스 클릭
            click_pos = pygame.mouse.get_pos()
            print(click_pos)
    
    
    # 화면을 검게 칠함
    screen.fill(BLACK)
    
    
    if start:
        display_game_scr() # 게임 화면 표시
    else:
        display_st_scr()   # 시작 화면 표시
    
    if click_pos:
        chk_btn(click_pos)

    
    pygame.display.update() # 화면 업데이트
            
            
            
# 프로그램 종료 시
pygame.time.delay(3000) # 현재 레벨은 3초 간 표시
pygame.quit() # 게임 프로그램을 종료