class Event:
    name = ""
    day = ""
    start = 0
    end = 0
    part = ""

    def __init__(self):
        self.name = input("name of appointment?")
        self.day = input("is it on S, M, T, W, Th, F, or Sa?")
        self.start = int(input("start time?"))
        self.end = int(input("end time?"))

    def display_event(self):
        print(self.name + " " + self.day + " " + str(self.start) + " - " + str(self.end))
