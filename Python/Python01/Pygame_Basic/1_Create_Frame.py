import pygame

pygame.init()  # 초기화 (반드시 필요)

# 화면크기 설정 
screen_width = 480  #가로 
screen_heigh = 640  #세로 

screen = pygame.display.set_mode((screen_width,screen_heigh)) 

#화면타이틀 설정
pygame.display.set_caption = ("Choice Game")

# Event loop 

running = True #계임 실행중 여부 

while running:
    # 실행중 이벤트 수집
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: # Quit Event 수신시  종료 (화면창에서 X 버튼 누를시)
            running = False
#Pygame 종료 
pygame.quit()
 





