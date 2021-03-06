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
            print(item)
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
        self.PL.append("delete," + x + "," + str(self.T[self.node][self.node]) + "," + str(self.node))
        for item in self.V[:]:
            if item.name == x:
                self.V.remove(item)
                print(x + " deleted")
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
            + "," + str(self.T[self.node][self.node]) + "," + str(self.node) + "," + table \
            + "," + e.day + "," + str(e.start) + "," + str(e.end))         

    def receive(self, sqs):
        q = sqs.get_queue_by_name(QueueName='node' + str(self.node))
        msg = q.receive_messages()
        me = msg[0].body.split(',')
        print(me)

        tk = []
        n = 4
        m = 4
        for i in range(n):
            column = []
            for j in range(m):
                column.append(0)
            tk.append(column)

        tab = str(me[4])
        p = 0
        for i in range(0, 4):
            for j in range(0, 4):
                p = ((4*i)) + j
                tk[i][j] = tab[p]
              
        self.PL.append(me[0] + "," + me[1] + "," + me[2] + "," + me[3])

        if me[0] == "insert":
            self.V.append(me[1] + "," + me[5] + "," + me[6] + "," + me[7])
        #elif me[0] == "delete":
            

        for i in range(0, 4):
            self.T[self.node][i] = max(int(self.T[self.node][i]), int(tk[int(me[3])][i]))

        for i in range(0, 4):
            for j in range(0, 4):
                self.T[i][j] = max(int(self.T[i][j]), int(tk[i][j]))
