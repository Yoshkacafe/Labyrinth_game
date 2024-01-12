import pygame
import os

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED_LIGHT = (245, 66, 66)
HIT_BOX_BLOCK = 30
HIT_BOX_PLAYER = 20

class Player():
    """
    Spawn a player
    """
    
    def __init__(self, screen, position_x, position_y, vel, map):
        self.screen = screen
        self.position_x = position_x
        self.position_y = position_y
        self.vel = vel
        self.player = pygame.Rect(0, 0, 0, 0)
        self.life = 3
        self.map = map

    def draw(self):
        width = 15
        height = 15
        self.player = pygame.Rect(self.position_x, self.position_y, width, height)
        pygame.draw.rect(self.screen, RED_LIGHT, self.player)

    def top(self):
        if self.canMoveTop((self.position_x, self.position_y - self.vel)):
            self.position_y -= self.vel

    def down(self):
        if self.canMoveRightBottom((self.position_x, self.position_y + self.vel)):
            self.position_y += self.vel

    def right(self):
        if self.canMoveRightBottom((self.position_x + self.vel, self.position_y)):
            self.position_x += self.vel
    
    def left(self):
        if self.canMoveTopLeft((self.position_x - self.vel, self.position_y)):
            self.position_x -= self.vel

    def canMoveTop(self, preshot):
        for obstacle_rect in self.map.player_collision:
            if obstacle_rect.y <= preshot[1] and obstacle_rect.y + HIT_BOX_BLOCK >= preshot[1] and :
                return False
        return True

    def canMoveRightBottom(self, preshot):
        for obstacle_rect in self.map.player_collision:
            if obstacle_rect.x <= preshot[0] and obstacle_rect.x + HIT_BOX_BLOCK >= preshot[0] + HIT_BOX_PLAYER:
                if obstacle_rect.y <= preshot[1] and obstacle_rect.y + HIT_BOX_BLOCK >= preshot[1] - HIT_BOX_PLAYER:
                    return False
        return True
    
    def clear_player(self):
        pygame.draw.rect(self.screen, WHITE, (self.position_x, self.position_y, 15, 15))
