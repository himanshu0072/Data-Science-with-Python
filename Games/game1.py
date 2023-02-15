import pgzrun

box = Rect((50, 50), (150, 100))
box2 = Rect((600, 50), (100, 100))
# box3 = Rect((350, 50), (100, 100))

bvx = 2
b2vx = -3
# b3vx = 2


def draw():
    screen.fill("black")
    screen.draw.filled_rect(box, 'yellow')
    screen.draw.filled_rect(box2, 'red')
    # screen.draw.filled_rect(box3, 'green')

def update():
    # box.x += 2  # move the item from left to right
    # box2.x -= 2  # move the box from right to left
    # box3.y += 2  # move the box from up to down
    global bvx, b2vx
    box.x += bvx
    box2.x += b2vx
    # box3.y += b3vx
    if box.colliderect(box2):
        bvx = -bvx
        b2vx = -b2vx
        sounds.cling.play()

    if box.left < 0:
        bvx = - bvx
    if box2.right > 800:
        b2vx = -b2vx


pgzrun.go()
