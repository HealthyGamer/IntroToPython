class Player:
  __init__(self, id, xp=0, attack=1, hp=1):
    self.id = id
    self.xp = xp
    self.attack = attack
    self.hp = hp
  
  isNewPlayer(self):
    return true
  
  isAlive(self):
    return true
  
  attack(self):
    return 1
  
  takeDamage(self):
    return self.isAlive()
  
  updateHealth(self):
    return self.isAlive()
  
  loadPlayer(self)
    return true
    
    
    
