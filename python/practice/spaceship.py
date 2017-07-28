class Spaceship:
    def __init__(self,name,speed = 0,time_in_space = 0, height = 20,
     model = "unknown", weight = 10,
     fuel_level = 10, tank_capacity = 10, passenger_capacity = 4):
        self.name = name
        self.speed = speed
        self.time_in_space = time_in_space
        self.height = height
        self.model = model
        self.weight = weight
        self.fuel_level = fuel_level
        self.tank_capacity = tank_capacity
        self. passenger_capacity = passenger_capacity
    def description(self):
        print """
        Name is %s
        Speed is warp %d
        time_in_space %d
        height is %d
        model is %s
        weight is %d
        fuel level is %d
        tank capacity is %d
        passenger capacity is %d
        """ % (self.name,self.speed)

    def accelerate(self, rate):
        self.speed+= rate


enterprise = Spaceship('Enterprise', 2,) #name,speed,size
enterprise.description()
enterprise.accelerate(4)

print enterprise.speed
# enterprise.how_fast
