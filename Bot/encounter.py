class Encounter:
  __init__(self, player)
    self.id = 0
    self.mob = Mob()
    self.player = player
    
  playerAttack(self):
    damage = self.player.attack()
    self.mob.hp -= damage
    if(self.mob.isAlive())
    
    else
    end
  
 
class Mob:
  __init__(self)
    self.hp = 10
    self.attack = 1
  
  isAlive(self):
    return true
