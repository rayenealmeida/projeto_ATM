import pygame
import pygame_gui 
from pygame.locals import *
from pygame_gui import UIManager, elements

pygame.init()

# Definição das cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Configurações da janela
WINDOW_SIZE = (400, 300)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Exemplo Pygame GUI')

# Configuração do Pygame GUI
ui_manager = UIManager(WINDOW_SIZE)

# Criação da caixa de texto
text_box_rect = pygame.Rect(100, 100, 200, 30)
text_box = elements.UITextEntryLine(relative_rect=text_box_rect, manager=ui_manager)

# Criação do botão
button_rect = pygame.Rect(150, 150, 100, 30)
button = elements.UIButton(relative_rect=button_rect, text="Exibir", manager=ui_manager)

clock = pygame.time.Clock()
is_running = True

user_text = ""  # Variável para armazenar o texto digitado pelo usuário

while is_running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == QUIT:
            is_running = False

        # Atualiza a interface do Pygame GUI
        ui_manager.process_events(event)

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button:
                    # Exibe o texto armazenado na variável quando o botão for pressionado
                    print("Texto digitado:", user_text)

        # Verifica se o botão foi clicado usando o evento pygame.MOUSEBUTTONDOWN
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                ui_manager.process_events(event)

    ui_manager.update(time_delta)

    screen.fill(WHITE)

    # Desenha a interface do Pygame GUI
    ui_manager.draw_ui(screen)

    # Obtém o texto digitado na caixa de texto
    user_text = text_box.get_text()

    pygame.display.update()

pygame.quit()