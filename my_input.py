from machine import ADC, Pin
class Input():
    def __init__(self):
        self.xAxis = ADC(Pin(28))
        self.yAxis = ADC(Pin(29))
        self.buttonB = Pin(5,Pin.IN, Pin.PULL_UP) #B
        self.buttonA = Pin(6,Pin.IN, Pin.PULL_UP) #A
        self.buttonStart = Pin(7,Pin.IN, Pin.PULL_UP) #A
        self.buttonSelect = Pin(8,Pin.IN, Pin.PULL_UP) #A
    
    def A(self):
        if self.buttonA.value() == 0:
            return True
        else:
            return False
    
    def B(self):
        if self.buttonB.value() == 0:
            return True
        else:
            return False
        
    def Start(self):
        if self.buttonStart.value() == 0:
            return True
        else:
            return False
    
    def Select(self):
        if self.buttonSelect.value() == 0:
            return True
        else:
            return False
    
    def x(self, down=20000, up=50000):
        _temp = self.yAxis.read_u16()
        if(_temp<down):
            return -1
        elif(_temp>up):
            return 1
        else:
            return 0
    
    def y(self, down=20000, up=50000):
        _temp = self.xAxis.read_u16()
        if(_temp<down):
            return -1
        elif(_temp>up):
            return 1
        else:
            return 0
    
    def x_raw(self):
        return self.yAxis.read_u16()

    def y_raw(self):
        return self.xAxis.read_u16()
    
    def test(self):
        import time
        while True:
            print(f"x:{self.x()} y:{self.y()} x_raw:{self.x_raw()} y_raw:{self.y_raw()} A:{self.A()} B:{self.B()} Start:{self.Start()} Select:{self.Select()}")
            if self.Start() and self.Select():
                return
            time.sleep_ms(50)
            