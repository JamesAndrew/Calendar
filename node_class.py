import boto3

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

    def get_node_id(self):
        return self.node

    def get_time(self):
        return self.clock

    def hasrec(e, k):
        return self.T[k][e.get_node()] >= e.get_time()

    def advance_clock(self):
        self.clock += 1
        return self.clock

    def insert(self, sqs, x):        
        self.T[self.node][self.node] = self.advance_clock()
        self.PL.append("insert(" + x.name + "), " + str(self.T[self.node][self.node]) + ", " + str(self.node))
        self.V.append(x)

        if len(x.part) > 0:
            self.send(sqs, x.part[0], "schedule", x)

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

    def send(self, sqs, k, m, e):
        sqs.get_queue_by_name(QueueName='node' + str(k)).send_message(MessageBody=m)         

    def receive(self, sqs):
        q = boto3.resource('sqs')       
        if self.node == 0:
            q = sqs.get_queue_by_name(QueueName='node0')
        elif self.node == 1:
            q = sqs.get_queue_by_name(QueueName='node1')
        else:
            print("I don't have a queue!")

        msg = q.receive_messages()
        for message in msg:
            print(message.body)

