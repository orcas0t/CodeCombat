# Defeat the ogres.


while True:
    hero.moveDown()
    hero.moveRight()
    enemy = hero.findNearestEnemy()
    while enemy:
        hero.attack(enemy)
        enemy = hero.findNearestEnemy()
                    
    hero.moveDown()
    break
        

