import boto3

# use sqs service
sqs = boto3.resource('sqs')

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
        print("name day start - end")
        for item in self.V:
            item.display_event()
        print()

        print("Partial Log")
        print("operation, event, T, node")
        for item in self.PL:
            print(item, end=' ')
        print()

    def get_node_id(self):
        return self.node

    def get_time(self):
        return self.clock

    def hasrec(self, t, e, k):
        n = e.get_node()
        p = ((4*k)) + n
        print(p)
        print(int(t[p]) >= int(e.time))
        return int(t[p]) >= int(e.time)

    def advance_clock(self):
        self.clock += 1
        return self.clock

    def insert(self, sqs, x):
        self.T[self.node][self.node] = self.advance_clock()
        self.PL.append("insert," + x.name + "," + str(self.T[self.node][self.node]) + "," + str(self.node))
        self.V.append(x)

        if len(x.part) > 0:
            self.send(sqs, x.part[0], "insert", x)
            
        

    def delete(self, x):
        self.T[self.node][self.node] = self.advance_clock()
        self.PL.append("delete," + x.name + "," + str(self.T[self.node][self.node]) + "," + str(self.node))
        for item in self.V[:]:
            if item.name == x:
                self.V.remove(item)
                print(x + " deleted")
                if len(x.part) > 0:
                    self.send(sqs, x.part[0], "schedule", x)
                return item
            else:
                print("Appointment not found")
                return False

    def send(self, sqs, k, m, e):
        table = ""
        for row in self.T:
            for elem in row:
                table = table + str(elem)
        print(table)
                
        sqs.get_queue_by_name(QueueName='node' + str(k)).send_message(MessageBody=m + "," + e.name \
            + "," + str(self.T[self.node][self.node]) + "," + str(self.node) + "," + table)         

    def receive(self, sqs):
        q = sqs.get_queue_by_name(QueueName='node' + str(self.node))
        msg = q.receive_messages()
        me = msg[0].body.split(',')
        print(me)

        tk = []
        n = 4
        m = 4
        for i in range(16):
            tk.append(0)

        tab = str(me[4])
        p = 0
        for i in range(n):
            for j in range(m):
                p = ((4*i)) + j
                tk[i][j] = tab[p]
        
        NE = ""
        v = False
        if not self.hasrec(me[1], self.node):
            NE = me[1]
              
        if me[0] != "delete":
            for item in self.V[:]:
                if item.name == me[1]:
                    v = True
            if v or NE == me[1]:
                self.PL.append("delete,")

        for i in range(0, 4):
            self.T[self.node][i] = max(self.T[self.node][i], tk[me[3]][i])

        for i in range(0, 4):
            for j in range(0, 4):
                self.T[i][j] = max(self.T[i][j], tk[i][j])

        self.PL.append(me[0] + "," + me[1] + "," + str(self.T[self.node][self.node]) + "," + str(self.node))

        msg[0].delete_message()

