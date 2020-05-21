import pygame

class Sprite():

    def __init__(self, image, game):
        """
        Inicjalizacjia postaci
        :param image: obraz postaci, domyślna pozycja (0, 0)
        :param game: obiekt gry, w której występuje postać
        """
        self.image = image
        self.position = [0, 0]
        self.game = game
        self.reset()

    def update(self):
        """
        Wywolywanie w pętli w celu aktualizacji, w klasie rodzicu nie robi nic
        :return:
        """
        pass

    def draw(self):
        """
        Rysuje postać na ekranie w jej aktualnej pozycji
        :return:
        """
        self.game.surface.blit(self.image, self.position)

    def reset(self):
        """
        Wywołanie na początku gry, resetuje postać
        :return:
        """
        pass


class Cheese(Sprite):
    """
    Obiekt sera sterowany przez gracza
    """
    def reset(self):
        """
        Resetuje pozycję sera i zatrzymuje ruch
        Przywraca prędkość ruchu do wartości poczatkowej
        :return:
        """
        self.movingUp = False
        self.movingDown = False
        self.movingLeft = False
        self.movingRight = False

        self.position[0] = (self.game.width - self.image.get_width()) / 2
        self.position[1] = (self.game.height - self.image.get_height()) / 2
        self.movement_speed = [5, 5]

    def update(self):
        """
        Reswtuje pozycję sera i zatrzymuje ruch
        :return:
        """
        if self.movingUp:
            self.position[1] = self.position[1] - (self.movement_speed[1])
        if self.movingDown:
            self.position[1] = self.position[1] + (self.movement_speed[1])
        if self.movingLeft:
            self.position[0] = self.position[0] - (self.movement_speed[0])
        if self.movingRight:
            self.position[0] = self.position[0] + (self.movement_speed[0])

        if self.position[0] < 0:
            self.position[0] = 0
        if self.position[1] < 0:
            self.position[1] = 0
        if self.position[0] + self.image.get_width() > self.game.width:
            self.position[0] = self.game.width - self.image.get_width()
        if self.position[1] + self.image.get_height() > self.game.height:
            self.position[1] = self.game.height - self.image.get_height()

    def StartMoveUp(self):
        """
        Rozpoczęcie ruchu sera w górę
        :return:
        """
        self.movingUp = True

    def StopMoveUp(self):
        """
        Zatrzymanie ruchu sera w górę
        :return:
        """
        self.movingUp = False

    def StartMoveDown(self):
        """
        Rozpoczęcie ruchu sera w dół
        :return:
        """
        self.movingDown = True

    def StopMoveDown(self):
        """
        Zatrzymanie ruchu sera w dół
        :return:
        """
        self.movingDown = False

    def StartMoveLeft(self):
        """
        Rozpoczęcie ruchu sera w lewo
        :return:
        """
        self.movingLeft = True

    def StopMoveLeft(self):
        """
        Zatrzymanie ruchu sera w lewo
        :return:
        """
        self.movingLeft = False

    def StartMoveRight(self):
        """
        Rozpoczęcie ruchu sera w prawo
        :return:
        """
        self.movingRight = True

    def StopMoveRight(self):
        """
        Zatrzymanie ruchu sera w prawo
        :return:
        """
        self.movingRight = False



class CrackerChase():
    """
    Goń krakersa, parchu.
    """
    def play_game(self):
        init_result = pygame.init()
        if init_result[1] != 0:
            print("Biblioteka pygame nie została poprawnie zainstalowana")
            return

        self.width = 800
        self.height = 600
        self.size = (self.width, self.height)

        self.surface = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Goń krakersa, goń krakersa!")
        background_image = pygame.image.load('background.jpg')
        self.background_sprite = Sprite(image=background_image, game=self)

        cheese_image = pygame.image.load('cheese.png')
        self.cheese_sprite = Cheese(image=cheese_image,
                                    game=self)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            for e in pygame.event.get():
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return
                    elif e.key == pygame.K_UP:
                        self.cheese_sprite.StartMoveUp()
                    elif e.key == pygame.K_DOWN:
                        self.cheese_sprite.StartMoveDown()
                    elif e.key == pygame.K_LEFT:
                        self.cheese_sprite.StartMoveLeft()
                    elif e.key == pygame.K_RIGHT:
                        self.cheese_sprite.StartMoveRight()
                elif e.type == pygame.KEYUP:
                    if e.key == pygame.K_UP:
                        self.cheese_sprite.StopMoveUp()
                    elif e.key == pygame.K_DOWN:
                        self.cheese_sprite.StopMoveDown()
                    elif e.key == pygame.K_LEFT:
                        self.cheese_sprite.StopMoveLeft()
                    elif e.key == pygame.K_RIGHT:
                        self.cheese_sprite.StopMoveRight()

            self.background_sprite.draw()
            self.background_sprite.update()
            self.cheese_sprite.draw()
            self.cheese_sprite.update()
            pygame.display.flip()


game = CrackerChase()
game.play_game()