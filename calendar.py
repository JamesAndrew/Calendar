class Node:
    node = 0
    clock = 0
    T = []
    V = []
    PL = []

    def __init__(self):
        self.node = int(input("node id 0,1,2, or 3?"))

        print("initializing T")
        n = 4
        m = 4
        for i in range(n):
            column = []
            for j in range(m):
                column.append(0)
            self.T.append(column)

    def node_properties(self):
        print("Time Table")
        for row in self.T:
            for elem in row:
                print(elem, end=' ')
            print()

        print("Dictionary")
        for item in self.V:
            print(item, end=' ')
        print()

        print("Partial Log")
        for item in self.PL:
            print(item, end=' ')
        print()

    def advance_clock(self):
        self.clock += 1
        return self.clock

    def insert(self, x):        
        self.T[self.node][self.node] = self.advance_clock()
        self.PL.append("insert(" + x.name + "), " + str(self.T[self.node][self.node]) + ", " + str(self.node))
        V.append(x)

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

class Calendar:
    eventsS = []
    eventsM = []
    eventsT = []
    eventsW = []
    eventsTh = []
    eventsF = []
    eventsSa = []

    def schedule(self, e):
        if e.day == "S":
            self.eventsS.append(event)
        elif e.day == "M":
            self.eventsM.append(event)
        return event

    def display(self):
        print("Sunday Appointments")
        for item in self.eventsS:
            print(item.display_event(), end=' ')
        print("Monday Appointments")
        for item in self.eventsM:
            print(item.display_event(), end=' ')

    def cancel(self):
        pass
    
# the start of calendar app
print("Calendar start")

# create node and calendar
n = Node()
c = Calendar()

# main loop of calendar app
loop = True
while loop:
    print()
    print("Options")
    print("0 - quit")
    print("1 - schedule appointment")
    print("2 - display calendar")
    print("3 - cancel appointment")

    option = input("which option?")
    if option == "0":
        loop = False
    elif option == "1":
        print("schedule")
        e = Event()
        n.insert(e)
        
    elif option == "2":
        print("display")
        c.display()
    elif option == "3":
        print("cancel")
        c.cancel()
    else:
        print("invalid option, please try again")

    n.node_properties()
