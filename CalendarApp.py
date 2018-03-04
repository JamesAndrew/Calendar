import node_class
import event_class
import calendar_class
    
# the start of calendar app
print("Calendar start")

# create node and calendar
n = node_class.Node()
c = calendar_class.Calendar()

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
        e = event_class.Event()
        n.insert(e)
        c.schedule(e)
        
    elif option == "2":
        print("display")
        c.display()
        
    elif option == "3":
        print("cancel")
        delete = input("name of appointment to delete")
        d = n.delete(delete)
        if d != False:
            c.cancel(d)
        
    else:
        print("invalid option, please try again")

    n.node_properties()
