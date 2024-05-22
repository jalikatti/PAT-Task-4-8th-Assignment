### Kindly visit the below URL and convert the UML diagram into python 
# class and its methods
# https://github.com/rvsp/typescript-oops/blob/master/Practice/TV-class.md

class TV:
    def __init__(self, brand):
        self.brand = brand
        self.channel = 1  # Default channel
        self.price = 0  # Default price
        self.inches = 0  # Default inches
        self.on = False  # Default On/Off status
        self.volume = 50  # Default volume level

    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def set_channel(self, channel):
        if 1 <= channel <= 50:  # Assuming TV has 50 channels
            self.channel = channel

    def reset(self):
        self.channel = 1
        self.volume = 50
        self.on = False

    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"


class LEDTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = 0
        self.backlight = False

    def display_details(self):
        return f"Screen Thickness: {self.screen_thickness} inches, Energy Usage: {self.energy_usage} W, Lifespan: {self.lifespan} years, Refresh Rate: {self.refresh_rate} Hz"


class PlasmaTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = 0
        self.backlight = False

    def display_details(self):
        return f"Screen Thickness: {self.screen_thickness} inches, Energy Usage: {self.energy_usage} W, Lifespan: {self.lifespan} years, Refresh Rate: {self.refresh_rate} Hz"


# Test the classes
if __name__ == "__main__":
    led_tv = LEDTV("Sony", 0.5, 100, 5, 120)
    print(led_tv.status())  # Output: Sony at channel 1, volume 50
    print(led_tv.display_details())  # Output: Screen Thickness: 0.5 inches, Energy Usage: 100 W, Lifespan: 5 years, Refresh Rate: 120 Hz

    plasma_tv = PlasmaTV("Samsung", 0.6, 120, 6, 100)
    print(plasma_tv.status())  # Output: Samsung at channel 1, volume 50
    print(plasma_tv.display_details())  # Output: Screen Thickness: 0.6 inches, Energy Usage: 120 W, Lifespan: 6 years, Refresh Rate: 100 Hz
