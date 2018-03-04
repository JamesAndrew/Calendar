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
        self.V.append(x)

    def delete(self, x):
        self.T[self.node][self.node] = self.advance_clock()
        self.PL.append("delete(" + x + "), " + str(self.T[self.node][self.node]) + ", " + str(self.node))
        for item in self.V[:]:
            if item.name == x:
                self.V.remove(item)
                print(x + " deleted")
                return item
            else:
                print("Appointment not found")
                return False
