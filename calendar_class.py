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
            self.eventsS.append(e)
        elif e.day == "M":
            self.eventsM.append(e)
        elif e.day == "T":
            self.eventsT.append(e)
        elif e.day == "W":
            self.eventsW.append(e)
        elif e.day == "Th":
            self.eventsTh.append(e)
        elif e.day == "F":
            self.eventsF.append(e)
        elif e.day == "Sa":
            self.eventsSa.append(e)

    def display(self):
        print("Sunday Appointments")
        for item in self.eventsS:
            print(item.display_event(), end=' ')
            
        print("Monday Appointments")
        for item in self.eventsM:
            print(item.display_event(), end=' ')
            
        print("Tusday Appointments")
        for item in self.eventsT:
            print(item.display_event(), end=' ')
            
        print("Wednesday Appointments")
        for item in self.eventsW:
            print(item.display_event(), end=' ')

        print("Thursday Appointments")
        for item in self.eventsTh:
            print(item.display_event(), end=' ')

        print("Friday Appointments")
        for item in self.eventsF:
            print(item.display_event(), end=' ')

        print("Saturday Appointments")
        for item in self.eventsSa:
            print(item.display_event(), end=' ')

    def cancel(self, x):
        day = []
        
        if x.day == "S":
            day = self.eventsS
        elif x.day == "M":
            day = self.eventsM
        elif x.day == "T":
            day = self.eventsT
        elif x.day == "W":
            day = self.eventsW
        elif x.day == "Th":
            day = self.eventsTh
        elif x.day == "F":
            day = self.eventsF
        elif x.day == "Sa":
            day = self.eventsSa
            
        for item in day[:]:
            if item.name == x.name:
                day.remove(item)
                print(x.name + " canceled")
                return True
            else:
                print("Appointment not found")
                return False
