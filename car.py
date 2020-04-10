========  CAR  ========

class Car:
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction

if __name__ == "__main__":
    import json
    detail = json.loads(input())

    color = detail["color"]
    max_speed = float(detail["max_speed"])
    acceleration = float(detail["acceleration"])
    tyre_friction = float(detail["tyre_friction"])

    car = Car(color=color, max_speed=max_speed, acceleration=acceleration,
              tyre_friction=tyre_friction)

    print("-".join([car.color, str(car.max_speed), str(car.acceleration),
                    str(car.tyre_friction)]))
                    
O/P = Red-250.0-10.0-3.0



========  CAR_ENGINE_STARTED_OR_NOT  ========


class Car:
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction
        self.is_engine_started = False
        
    def start_engine(self):
        self.is_engine_started = True

if __name__ == "__main__":
    import json
    detail = json.loads(input())

    color = detail["color"]
    max_speed = float(detail["max_speed"])
    acceleration = float(detail["acceleration"])
    tyre_friction = float(detail["tyre_friction"])

    car = Car(color=color, max_speed=max_speed, acceleration=acceleration,
              tyre_friction=tyre_friction)

    is_engine_started_1 = car.is_engine_started
    car.start_engine()
    is_engine_started_2 = car.is_engine_started

    print("-".join([str(is_engine_started_1), str(is_engine_started_2)]))
    
O/P = False-True

========  CAR_CURRENT_SPEED  ========


class Car:
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction
        self.current_speed = 0

if __name__ == "__main__":
    import json
    detail = json.loads(input())

    color = detail["color"]
    max_speed = float(detail["max_speed"])
    acceleration = float(detail["acceleration"])
    tyre_friction = float(detail["tyre_friction"])

    car = Car(color=color, max_speed=max_speed, acceleration=acceleration,
              tyre_friction=tyre_friction)

    print(car.current_speed)
O/P = 0    
