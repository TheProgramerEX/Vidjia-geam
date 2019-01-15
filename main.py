import pygame
# import GIFImage
# import pyglet

pygame.init()
#def main():
  #boi = GIFImage("animations/lil boi.gif")
  #if event.key == pygame.K_z:
        #boi.render(DS, (player.rect.y, player.rect.x))

  #if __name__ == "__main__":
       #main()

DS = pygame.display.set_mode((640, 480))
W, H = DS.get_size()
clock = pygame.time.Clock()
FPS = 60

PLAYER_IMAGE = pygame.Surface((15, 27))

PLAYER_IMAGE = pygame.image.load('animations/lil boi1.png')
attack = pygame.image.load('animations/enemy boi.png')

#DS.blit(PLAYER_IMAGE, (0,0))
"""PLAYER_IMAGE.fill((70, 240, 120))"""


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super(Platform, self).__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill((90, 90, 120))
        self.rect = self.image.get_rect(topleft=(x, y))


class Level:

    def __init__(self):
        self.platforms = pygame.sprite.Group()
        for x, y, width, height in self.level:
            platform = Platform(x, y, width, height)
            self.platforms.add(platform)

    def shift(self, amount):
        for sprite in self.platforms:
            sprite.rect.x += amount


class LVL_01(Level):

    def __init__(self):
        self.level = [
            (20, 20, 150, 20), (120, 200, 200, 20), (400, 440, 100, 20),
            (40, 100, 200, 20), (320, 300, 150, 20), (520, 550, 100, 20),
            (60, 100, 140, 20), (300, 200, 100, 20), (290, 440, 100, 20),
            (40, 100, 100, 20), (350, 300, 150, 20), (95, 550, 150, 20),
            (250, 20, 150, 20), (450, 100, 150, 20), (650, 50, 150, 20),
            (60, 20, 140, 20), (425, 200, 100, 20), (370, 350, 50, 20),
            (200, 100, 50, 20), (200, 370, 70, 20)
        ]
        Level.__init__(self)



class Player(pygame.sprite.Sprite):

    def __init__(self, pos, level):
        super(Player, self).__init__()
        self.image = PLAYER_IMAGE
        self.rect = self.image.get_rect(center=pos)
        self._vx = 0
        self._vy = 0
        self._spritex = pos[0]
        self._spritey = pos[1]
        self.level = level
        self._gravity = .9

    def update(self):
        self.grav()
        self._spritex += self._vx
        self.rect.centerx = self._spritex

        block_hit_list = pygame.sprite.spritecollide(self, self.level, False)
        for block in block_hit_list:
            if self._vx > 0:
                self.rect.right = block.rect.left
            elif self._vx < 0:
                self.rect.left = block.rect.right
            self._spritex = self.rect.centerx

        self._vy += self._gravity
        self._spritey += self._vy
        self.rect.centery = self._spritey

        block_hit_list = pygame.sprite.spritecollide(self, self.level, False)
        for block in block_hit_list:
            if self._vy > 0:
                self.rect.bottom = block.rect.top
            elif self._vy < 0:
                self.rect.top = block.rect.bottom
            self._spritey = self.rect.centery
            self._vy = 0
            if self.rect.y >= H - self.rect.height and self._vy >= 0:
                self._vy = 0
                self.rect.y = H - self.rect.height

    def jump(self):
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards.
        if len(platform_hit_list) > 0 or self.rect.bottom >= H:
            self._vy = -19

    def grav(self):
        """Calculate effect of gravity."""
        if self._vy == 0:
            self._vy = 1
        else:
            self._vy += .35

        # See if we are on the ground.
        if self.rect.y >= H - self.rect.height and self._vy >= 0:
            self._vy = 0
            self.rect.bottom = H
            # You have to update the _spritey pos as well.
            self._spritey = self.rect.centery


level_list = [LVL_01()]
current_level_index = 0
current_level = level_list[current_level_index]
player = Player([340, 100], current_level.platforms)
active_sprite_group = pygame.sprite.Group(player)
active_sprite_group.add(current_level.platforms)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                print("PRESSED!")
                PLAYER_IMAGE.blit(attack, (0, 0))
                pygame.display.update()
            elif event.key == pygame.K_LEFT:
                player._vx = -3
            elif event.key == pygame.K_RIGHT:
                player._vx = 3
            elif event.key == pygame.K_UP:
                player.jump()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and player._vx < 0:
                player._vx = 0
            elif event.key == pygame.K_RIGHT and player._vx > 0:
                player._vx = 0



    active_sprite_group.update()

    if player.rect.x >= 500:
        diff = player.rect.x - 500
        player.rect.x = 500
        # You have to update the _spritex pos as well.
        player._spritex = player.rect.centerx
        current_level.shift(-diff)
    if player.rect.x <= 120:
        diff = 120 - player.rect.x
        player.rect.x = 120
        # You have to update the _spritex pos as well.
        player._spritex = player.rect.centerx
        current_level.shift(diff)

    DS.fill((50, 50, 50))
    active_sprite_group.draw(DS)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
