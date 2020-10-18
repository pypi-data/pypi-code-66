import datetime as dt
from datetime import timezone
from scam.CommManager import CommManager


class CLI:
    def __init__(self):
        try:
            self.cm = CommManager()
        except Exception as e:
            print("Error: " + str(e))
    def run(self):
        destinations = self.cm.get_destinations()
        print("Commands: type 1 to look up a reservation, 2 to book a ride, 3 to exit.")
        cmd = str(input())
        if cmd == "1":
            try:
                print("Commands: type 1 to get a reservation from a name, 2 to get a reservation from an ID")
                command = str(input())
                if command == "1":
                    print("insert input:")
                    name = str(input())
                    result = self.cm.get_reservations(-1, name)
                    print()
                    for res in result:
                        print_result(res)
                        print()
                elif command == "2":
                    print("insert input:")
                    res_id = int(input())
                    result = self.cm.get_reservations(res_id)
                    print(result)
                    print_result(result)
                else:
                    print("invalid command")
            except Exception as e:
                print("Error: " + str(e))
        elif cmd == "2":
            try:
                print("Type a destination number:")
                printdestinations(destinations)
                destination = int(input())

                if not checkdestination(destination, destinations):
                    raise ValueError("Invalid destination. Type a valid destination number")

                date_str = input("Type datetime as d-m-Y H:M \n")
                date_dt = dt.datetime.strptime(date_str, '%d-%m-%Y %H:%M')
                timestamp = int(dt.datetime.timestamp(date_dt))
                if not checkdate(date_dt):
                    raise ValueError("Datetime must come after current datetime")

                n_people = int(input("Number of people \n"))
                res_name = input("Under the name of \n")
                phone = input("Phone number \n")

                check = self.cm.make_reservation(location=destination, persons=n_people, name=res_name,
                                                 phone_number=phone, reservation=timestamp)

                if check:
                    print("Success")
                else:
                    raise Exception("Failed")
            except Exception as e:
                print("Error: " + str(e))
        else:
            print("Invalid command")


def checkdate(date):
    return isinstance(date, dt.datetime) and date > dt.datetime.now()


def checkdestination(destination, destinations):
    keys = [d['id'] for d in destinations]
    return destination in keys


def printdestinations(destinations):
    for d in destinations:
        print(str(d['id'])+". "+d['name'])


def print_result(res):
    for key in res:
        if key != "reservation":
            print(str(key) + ": " + str(res[key]))
        else:
            print(str(key) + ": " + str(dt.datetime.fromtimestamp(res[key])))