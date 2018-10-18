import pygame
import random

#color
color = {
    'white': (255,255,255),
    'black': (0,0,0),
    'd_gray': (51,51,51),
    'l_gray': (238,238,238)
}

class Ball:
    def __init__(self, x, y, w, h, vX, vY):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.vX = vX    #velocity in X dir
        self.vY = vY    #velocity in Y dir

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def display(self, screen):
        ball = self.rect()
        pygame.draw.ellipse(screen, color['l_gray'], ball)

    def update(self):
        self.x += self.vX
        self.y += self.vY

class Paddle:
    def __init__(self, x, y, w, h, speed):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.velocity = 0
        self.speed = speed
    
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def display(self, screen):
        paddle = self.rect() 
        pygame.draw.rect(screen, color['l_gray'], paddle)

    def update(self):
        self.y += self.velocity

    def keyPressed(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.velocity = -1 * self.speed
            elif event.key == pygame.K_DOWN:
                self.velocity = self.speed

class Pong:
    def __init__(self):

        #init pygame env
        pygame.init()
        WIDTH = 640
        HEIGHT = 480
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Pong')
        
        #init objects in env
        self.ball = Ball(WIDTH/2,HEIGHT/2,13,13,3,3)
        self.paddle = Paddle(WIDTH - 10,HEIGHT/2,10,70,3)
        
        self.gameLoop = True
        self.score = 0

    def play(self):
        #for framerate
        clock = pygame.time.Clock()
        
        self.gameLoop = True

        while self.gameLoop:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    gameLoop = False
                    exit()
                else:
                    self.paddle.keyPressed(event)

            self.draw()
            self.collision_handler()


    def collision_handler(self):
        
        #collision of ball with paddle
        if self.ball.rect().colliderect(self.paddle.rect()):
            self.ball.vX = -1 * self.ball.vX
            self.score += 1

        #did ball cross top or bottom
        if self.ball.y + self.ball.height >= self.screen.get_height():
            self.ball.vY = -1 * self.ball.vY
        elif self.ball.y <= 0:
            self.ball.vY = -1 * self.ball.vY

        #did ball cross right or left
        if self.ball.x + self.ball.width >= self.screen.get_width():
            pygame.quit()
            self.gameLoop = False
            return
        elif self.ball.x <= 0:
            self.ball.vX = -1 * self.ball.vX
        
        #did paddle cross top or bottom
        if self.paddle.y + self.paddle.height >= self.screen.get_height():
            self.paddle.y = self.screen.get_height() - self.paddle.height
        elif self.paddle.y <= 0:
            self.paddle.y = 0

    def draw(self):
        self.screen.fill(color['d_gray'])
        font = pygame.font.Font(None, 32)
        score_text = font.render("Score: " + str(self.score), True, color['white'])
        self.screen.blit(score_text, (0,0))

        self.ball.update()
        self.ball.display(self.screen)
        self.paddle.update()
        self.paddle.display(self.screen)

        pygame.display.update()

if __name__ == '__main__':
    Pong().play()
