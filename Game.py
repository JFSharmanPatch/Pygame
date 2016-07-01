import pygame

WIDTH = 1024
HEIGHT = 1024

alien = Actor('spaceship')
alien.pos = 170,130
alien.x_dir = 0
alien.y_dir = 0

#character = Actor('space')
#character.pos = 683,290


def update():
    global alien
    global character
    if keyboard.w:
        alien.top -=10
        alien.image = 'spaceship'
    elif keyboard.s:
        alien.bottom +=10
        alien.image = 'spaceship2'
    if keyboard.a:
        alien.left -=10
        alien.image = 'spaceship3'
    elif keyboard.d:
        alien.right +=10
        alien.image = 'spaceship4'
    
    #pygame.transform.rotate(alien,100)
  
    
    #if keyboard.up:
        #character.top -=10
    #elif keyboard.down:
        #character.bottom +=10
    #if keyboard.left:
        #character.left -=10
    #elif keyboard.right:
        #character.right +=10


def draw():
    global alien
    screen.fill((0,171,255))
    #character.draw()
    alien.draw()
    
    
def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt()

def set_alien_hurt():
    alien.image = 'explosion2'
    sounds.depthcharge.play()
    clock.schedule_unique(set_alien_normal, 5.0)

def set_alien_normal():
    alien.image = 'spaceship'
