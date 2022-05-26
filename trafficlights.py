import time


class TrafficLight:

  STATE = ['red', 'green', 'yellow']
  SCHEDULE = [1,9,3]
    
    
  

  def cycle(self):
    self.state[int(self.cycle_state)] += 1

    if self.state[int(self.cycle_state)] >= len(TrafficLight.STATE):
      self.state[int(self.cycle_state)] = 0
      self.cycle_state = not self.cycle_state

    print(self.query())
    time.sleep(TrafficLight.SCHEDULE[self.state[int(self.cycle_state)]])
  
  def query(self):
    return f"LightEW is {TrafficLight.STATE[self.state[0]]}\nLightNS is {TrafficLight.STATE[self.state[1]]}\n"
      
  def __init__(self, roadNS:str, roadEW:str ):
    self.state = [0,0]
    self.cycle_state = False
    self.name = f"{roadNS} X {roadEW}"
    

intersection1 = TrafficLight("John Xina Rd", "Bing Chilling Ave")
print(intersection1.query())

Cycles = int(input("How many cycles do you want to run?: ")) 


for _i in range(Cycles * 2* len(TrafficLight.SCHEDULE)):
  
  intersection1.cycle()
  
