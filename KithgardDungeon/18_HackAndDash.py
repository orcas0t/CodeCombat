hero.moveRight()
# Break open the "Chest" before using the loop to escape the maze!
hero.attack("Chest")
# Return back back into the main hallway.
hero.moveDown()

while True:
    # Move 3 times.
    hero.moveRight(3)
    # Move 3 times more.
    hero.moveDown(3)
    
    