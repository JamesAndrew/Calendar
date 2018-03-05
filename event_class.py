class Event:
    time = 0
    node = 0
    
    name = ""
    day = ""
    start = 0
    end = 0
    part = []

    def __init__(self, node):
        self.node = node;
        self.name = input("name of appointment?")
        self.day = input("is it on S, M, T, W, Th, F, or Sa?")
        self.start = int(input("start time?"))
        self.end = int(input("end time?"))
        parts = input("more than 1 person y/n?")
        if parts == 'y':
            self.part.append(input("which node?"))

    def set_time(self, time):
        self.time = time

    def get_node(self):
        return self.node

    def display_event(self):
        print(self.name + " " + self.day + " " + str(self.start) + " - " + str(self.end))
