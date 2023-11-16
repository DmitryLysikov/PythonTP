class Transport():
    def __init__(self, *args, **kwargs):
        self.coordinates = kwargs.get("coordinates")
        self.speed = kwargs.get("speed")
        self.brand = kwargs.get("brand")
        self.year = kwargs.get("year")
        self.number = kwargs.get("number")

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        if isinstance(coordinates, tuple):
            f_item, s_item = coordinates
            if isinstance(f_item, float) and isinstance(s_item, float):
                self._coordinates = coordinates
            else:
                raise ValueError
        else:
            raise ValueError

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        if speed > 0 and isinstance(speed, float):
            self._speed = speed
        else:
            raise ValueError

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        if isinstance(brand, str):
            self._brand = brand
        else:
            raise ValueError

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if 0 < year <= 2023 and isinstance(year, int):
            self._year = year
        else:
            raise ValueError

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        if isinstance(number, int):
            self._number = number
        else:
            raise ValueError

    def __str__(self):
        attributes = vars(self)
        attributes_str = "\n".join(f"{key} - {value}" for key, value in attributes.items())
        return f"{self.__class__.__name__}\n{attributes_str}"

    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        '''
        Присутствие транспортного средства в пределах заданнй области
        pos_x, pos_y - координата левого верхнего угла области
        length, width - длина и ширина области
        '''
        if (pos_x <= self.coordinates[0] <= pos_x + length and
                pos_y <= self.coordinates[1] <= pos_y + width):
            return True
        else:
            return False


class Passenger():
    def __init__(self, *args, **kwargs):
        self.passengers_capacity = kwargs.get("passengers_capacity")
        self.number_of_passengers = kwargs.get("number_of_passengers")

    @property
    def passengers_capacity(self):
        return self._passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        if passengers_capacity > 0 and isinstance(passengers_capacity, int):
            self._passengers_capacity = passengers_capacity
        else:
            raise ValueError

    @property
    def number_of_passengers(self):
        return self._number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        if number_of_passengers >= self._passengers_capacity and isinstance(number_of_passengers, int):
            return "Нету столько мест"
        else:
            self.__number_of_passengers = number_of_passengers


class Cargo():
    def __init__(self, *args, **kwargs):
        self.carrying = kwargs.get("carrying")

    @property
    def carrying(self):
        return self._carrying

    @carrying.setter
    def carrying(self, carrying):
        if carrying > 0 and isinstance(carrying, float):
            self._carrying = carrying
        else:
            raise ValueError


class Plane(Transport):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.height = kwargs.get('height')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if isinstance(height, float):
            self._height = height
        else:
            raise ValueError


class Auto(Transport):
    pass

class Ship(Transport):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.port = kwargs.get("port")
        self.name = kwargs.get("name")

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        if isinstance(port, str):
            self._port = port
        else:
            raise ValueError

    @property
    def name(self):
        return self._port

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise ValueError

class Car(Auto):
    pass
class Bus(Auto, Passenger):
    def __init__(self, *args, **kwargs):
        Auto.__init__(self, *args, **kwargs)
        Passenger.__init__(self, *args, **kwargs)

class CargoAuto(Auto, Cargo):
    def __init__(self, *args, **kwargs):
        Auto.__init__(self,*args, **kwargs)
        Cargo.__init__(self, *args, **kwargs)

class Boat(Ship):
    pass

class PassengerShip(Ship, Passenger):
    def __init__(self, *args, **kwargs):
        Ship.__init__(self,  *args, **kwargs)
        Passenger.__init__(self, *args, **kwargs)

class CargoShip(Ship, Cargo):
    def __init__(self, *args, **kwargs):
        Ship.__init__(self,*args, **kwargs)
        Cargo.__init__(self, *args, **kwargs)


class Seaplane(Plane, Ship):
    def __init__(self, *args, **kwargs):
        Plane.__init__(self, *args, **kwargs)
        Ship.__init__(self, *args, **kwargs)


trans = Boat(name="MERS",
             coordinates=(1.0, 1.0),
             speed=10.0,
             brand="MERS S23",
             year=2023,
             number=1,
             port="Port123",
             height=20.0,
             carrying=10.0,
             passengers_capacity=5,
             number_of_passengers=3)
print(trans)
