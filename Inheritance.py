class Device:
    def __init__(self,name,connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected  = True

    def __str__(self):
        return f"Device {self.name!r}({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print("Disconnected")


class Printer(Device):
    def __init__(self,name,connected_by,capacity):
        #calling base class constructor
        super().__init__(name,connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

