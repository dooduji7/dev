import pygame

pygame.init()  # 초기화 (반드시 필요)

# 화면크기 설정
screen_width = 720  #가로
screen_heigh = 960  #세로

screen = pygame.display.set_mode((screen_width,screen_heigh))

#화면타이틀 설정
pygame.display.set_caption = ("Choice Game")

# 이미지 로드
background =  pygame.image.load("D:\\Python_Project\\Game_Image\\Backuround.jpg")

# 스프라이트(캐릭터) 로드
character = pygame.image.load("D:\\Python_Project\\Game_Image\\character.Png")

# 이미지 크기 취득
character_size = character.get_rect().size
character_width = character_size[0] #가로
character_heigh = character_size[1] #세로
character_X_Pos = (screen_width /2) - (character_width/2)  #가로 중앙
character_Y_Pos = screen_heigh - character_heigh #화면 하단


# Event loop

running = True #계임 실행중 여부

while running:
    # 실행중 이벤트 수집
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Quit Event 수신시  종료 (화면창에서 X 버튼 누를시)
            running = False
    screen.blit(background,(0,0)) # 배경 그리기
    screen.blit(character, (character_X_Pos, character_Y_Pos )) #캐릭터 생성 (그리기)
    pygame.display.update() #게임 화면  갱신

#Pygame 종료
pygame.quit()





