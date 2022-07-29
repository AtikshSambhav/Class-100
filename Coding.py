class Car(object):
    
    def __init__(self,company,model,engine):
        self.company=company
        self.model=model
        self.engine=engine

    def start(self):
        print("Started",self.engine)   

    def stop(self):
        print("Stopped",self.engine) 

car1=Car("Lamborghini","Aventador","V12")
car2=Car("Rolls Royce","Ghost","V8") 

print(car1.start())
print(car2.stop())









