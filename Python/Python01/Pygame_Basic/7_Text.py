import pygame

pygame.init()  # 초기화 (반드시 필요)

# 화면크기 설정
screen_width = 720  #가로
screen_heigh = 960  #세로
#Fps
set_Fps = 60

screen = pygame.display.set_mode((screen_width,screen_heigh))

#화면타이틀 설정
pygame.display.set_caption = ("Choice Game")

#FPS 
clock = pygame.time.Clock()

# 이미지 로드
background =  pygame.image.load("D:\\Python_Project\\Game_Image\\Backuround.jpg")

# 스프라이트(캐릭터) 로드
character = pygame.image.load("D:\\Python_Project\\Game_Image\\character.Png")

# 적 캐릭터 enemy
enemy = pygame.image.load("D:\\Python_Project\\Game_Image\\enemy.Png")

# 캐릭터 이미지 크기 취득
character_size = character.get_rect().size
character_width = character_size[0] #가로
character_heigh = character_size[1] #세로
character_X_Pos = (screen_width /2) - (character_width/2)  #가로 중앙
character_Y_Pos = screen_heigh - character_heigh #화면 하단

#이동 좌표 
to_X  = 0 
to_Y  = 0 

#이동 속도
char_Speed = 0.6


# 적 캐릭터 이미지 크기 취득
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0] #가로
enemy_heigh = enemy_size[1] #세로
enemy_X_Pos = (screen_width /2) - (enemy_width/2)  #가로 중앙
enemy_Y_Pos = (screen_heigh/2) - (enemy_heigh/2)  #화면 하단


# 글꼴 설정
game_font = pygame.font.Font(None,40)
fore_color = (255,255,255)
#시간표시 
total_time = 10 

#게임 시작시간 
Start_tick = pygame.time.get_ticks()

# Event loop
running = True #계임 실행중 여부

while running:
    # 실행중 이벤트 수집
    dt  = clock.tick(set_Fps) #프레임설정
    # print("FPS" + str(clock.get_fps()))
    
    #시간표시 타이머
    elapsed_time =  (pygame.time.get_ticks() - Start_tick) /1000
    disp_time = str(int(total_time - elapsed_time))
    timer = game_font.render(disp_time, True, fore_color) 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Quit Event 수신시  종료 (화면창에서 X 버튼 누를시)
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_X -= char_Speed 
            elif event.key == pygame.K_RIGHT:
                to_X += char_Speed
            elif event.key == pygame.K_UP:
                to_Y -= char_Speed
            elif event.key == pygame.K_DOWN:
                to_Y += char_Speed

        if event.type == pygame.KEYUP:
            if event.type == pygame.K_LEFT  or pygame.K_RIGHT:
                to_X = 0 
            elif event.type == pygame.K_UP  or pygame.K_DOWN:
                to_Y = 0 

    character_X_Pos += to_X * dt
    character_Y_Pos += to_Y * dt

    #화면 벗어남 방지처리(X축)
    if character_X_Pos  < 0  :
        character_X_Pos = 0
    if character_X_Pos >= (screen_width - character_width):
        character_X_Pos = (screen_width - character_width)
    #화면 벗어남 방지처리 (Y축)
    if character_Y_Pos  <= 0  :
        character_Y_Pos = 0
    if character_Y_Pos >= (screen_heigh - character_heigh):
        character_Y_Pos = (screen_heigh - character_heigh)
    
    # 캐릭터, 적 이미지 충돌 처리 
    # 캐릭터
    character_rect = character.get_rect()
    character_rect.left = character_X_Pos
    character_rect.top =  character_Y_Pos
    
    # 적
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_X_Pos
    enemy_rect.top = enemy_X_Pos
    
    # 충동 체크 
    if character_rect.colliderect(enemy_rect):
        print("충돌하였습니다.")
        running = False

    screen.blit(background,(0,0)) # 배경 그리기
    screen.blit(character, (character_X_Pos, character_Y_Pos )) #캐릭터 생성 (그리기)
    screen.blit(enemy, (enemy_X_Pos, enemy_Y_Pos )) #캐릭터 생성 (그리기)
    screen.blit(timer,(10,10))
    
    pygame.display.update() #게임 화면  갱신

#Pygame 종료
pygame.quit()





