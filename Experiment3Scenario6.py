class WeatherStation:
    def __init__(self):
        self.temperature = 0
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def unsubscribe(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def set_temperature(self, temperature):
        self.temperature = temperature
        print(f"\nWeather Station: Temperature changed to {temperature}°C")
        self.notify()

    def notify(self):
        for observer in self.observers:
            observer.update(self.temperature)


class Display:
    def update(self, temperature):
        pass


class PhoneDisplay(Display):
    def update(self, temperature):
        print(f"Phone Display: Temperature is {temperature}°C")


class TVDisplay(Display):
    def update(self, temperature):
        print(f"TV Display: Temperature is {temperature}°C")


class WebDisplay(Display):
    def update(self, temperature):
        print(f"Web Display: Temperature is {temperature}°C")


# Create weather station and displays
station = WeatherStation()

phone = PhoneDisplay()
tv = TVDisplay()
web = WebDisplay()

# Subscribe displays
station.subscribe(phone)
station.subscribe(tv)
station.subscribe(web)

# Temperature changes
station.set_temperature(25)
station.set_temperature(30)

# Unsubscribe TV display
station.unsubscribe(tv)

# Temperature changes after unsubscribe
station.set_temperature(28)
