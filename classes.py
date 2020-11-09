class Vehicle:
    def __init__(self,make,model,year,weight,repair,NeedsMaintenance=False,TripsSinceMaintenance=0):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.repair = repair
        self.NeedsMaintenance = NeedsMaintenance
        self.TripsSinceMaintenance = TripsSinceMaintenance
    def maintenance_light(self):
        if self.NeedsMaintenance == True:
            print("This vehicle needs maintenance!")
    def is_repaired(self,xrepair):
        self.repair = xrepair
        if self.repair == True:
            self.TripsSinceMaintenance = 0
            self.NeedsMaintenance = False
            self.repair = False

class Cars(Vehicle):
    def __init__(self,make,model,year,weight,repair=False,NeedsMaintenance=False,TripsSinceMaintenance=0,drive=False,stop=False,isDriving=False):
        Vehicle.__init__(self,make,model,year,weight,repair,NeedsMaintenance=False,TripsSinceMaintenance=0)
        self.drive = drive
        self.stop = stop
        self.isDriving = isDriving
    def set_drive(self,xdrive):
        self.drive = xdrive
        if self.drive == True:
            self.stop = False
            self.isDriving = True
            if self.TripsSinceMaintenance > 100:
                    self.NeedsMaintenance = True
                    print(f"This {self.model} requires maintenance!")
    def set_stop(self,xstop):
        self.stop = xstop
        while self.drive == True:
            if self.stop == True:
                self.isDriving = False
                self.TripsSinceMaintenance += 1
                if self.TripsSinceMaintenance > 100:
                    self.NeedsMaintenance = True
                    print(f"This {self.model} requires maintenance!")
                self.drive = False

class Airplanes(Vehicle):
    def __init__(self,make,model,year,weight,repair=False,NeedsMaintenance=False,TripsSinceMaintenance=0,Fly=False,Land=False,isFlying=False):
        Vehicle.__init__(self,make,model,year,weight,repair,NeedsMaintenance=False,TripsSinceMaintenance=0)
        self.Fly = Fly
        self.Land = Land
        self.isFlying = isFlying
    def set_Fly(self,xFly):
        if self.NeedsMaintenance == True:
            print("ERROR!  This plane can't fly until it's repaired!")
        elif self.NeedsMaintenance == False:
            self.Fly = xFly
            if self.Fly == True:
                self.Land = False
                self.isFlying = True
    def set_Land(self,xLand):
        if self.isFlying == False:
            print("This plane is not flying.")
        elif self.isFlying == True:
            self.Land = xLand
            if self.Land == True:
                self.TripsSinceMaintenance += 1
                if self.TripsSinceMaintenance > 100:
                    self.NeedsMaintenance = True
                    print(f"This {self.model} requires maintenance!")
                self.Fly = False
                self.isFlying = False

Eleanor = Cars("Ford","mustang",1968,2000)

AirForceOne = Airplanes("Boeing","777",1985,20000)

Mary = Cars("Aston Martin","DB7",1999,1800)

Madeline = Cars("Cadillac","Eldorado",1959,3000)

for x in range(1,52):
    Eleanor.set_drive(True)
    Eleanor.set_stop(True)

for x in range(1,33):
    Mary.set_drive(True)
    Mary.set_stop(True)

for x in range(1,102):
    Madeline.set_drive(True)
    Madeline.set_stop(True)
    AirForceOne.set_Fly(True)
    AirForceOne.set_Land(True)

vehicles=[]
vehicles.append(Eleanor)
vehicles.append(AirForceOne)
vehicles.append(Mary)
vehicles.append(Madeline)

for x in vehicles:
    print(x.make,x.model,x.year,x.weight,x.repair,x.NeedsMaintenance,x.TripsSinceMaintenance)
