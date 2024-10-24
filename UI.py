from Airport import Airport
from Passenger import Passengers
from Plane import Planes
airport = Airport()

def is_int(x):
    try:
        int(x)
        return True
    except ValueError:
        return False
def print_menu():
    print("Menu:")
    print("q. Print all planes")
    print("1. Create Passenger")
    print("2. Replace Passenger")
    print("3. Update Passenger")
    print("4. Delete Passenger")
    print("5. Create Plane")
    print("6. Replace Plane")
    print("7. Update Plane")
    print("8. Delete Plane")
    print("9. Sort by passenger last name.")
    print("10. Sort by number of passengers in plane.")
    print("11. Sort by number of passengers with first name starting with a given starting string.")
    print("12. Sort by concatenating number of passengers to destination.")
    print("13. Search by passengers that have the same first 3 numbers in passport number.")
    print("14. Search passengers in given plane by given string in either first or last name of passengers.")
    print("15. Search planes by name of passenger.")
    print("16. Form groups of k passengers with different names.")
    print("17. Form groups of k planes with the same destination but different airline company.")
    print("0. Exit")


def read_option():
    stop = False
    while not stop:
        n = input("Choose from menu: ")
        if n == '0':
            stop = True

        elif n == 'q':
            for plane in airport.get_all_planes():
                print(Planes.__str__(plane))

        elif n == '1':
            first = input("Enter the first name: ")
            last = input("Enter the last name: ")
            pass_num = input("Enter the passport number: ")
            i = int(input("Enter the index of the plane: "))
            passenger = Passengers(first, last, pass_num)
            airport.add_pass(passenger, i)

        elif n == '2':
            first = input("Enter the first name: ")
            last = input("Enter the last name: ")
            pass_num = input("Enter the passport number: ")
            i = int(input("Enter the index of the plane: "))
            i2 = int(input("Enter the index of the passenger to modify: "))
            passenger = Passengers(first, last, pass_num)
            airport.update_passenger(passenger, i, i2)

        elif n == '3':
            t = input('Choose what to update: \n 1. First name: \n 2. Last name: \n 3. Passport number: ')
            if t == '1':
                first = input("Enter the first name: ")
                j = int(input("Enter the index of the plane: "))
                i = int(input("Enter the index of the passenger: "))
                airport.replace_first_name(j, i, first)
            elif t == '2':
                last = input("Enter the last name: ")
                j = int(input("Enter the index of the plane: "))
                i = int(input("Enter the index of the passenger: "))
                airport.replace_last_name(j, i, last)
            elif t == '3':
                pass_num = input("Enter the passport number")
                i = int(input("Enter the index of the plane: "))
                j = int(input("Enter the index of the passenger: "))
                airport.replace_num(j, i, pass_num)

        elif n == '4':
            i = int(input("Enter the index of the plane: "))
            j = int(input("Enter the index of the passenger: "))
            airport.delete_pass(i, j)

        elif n == '5':
            num = input("Enter the plane number: ")
            air_comp = input("Enter the air company: ")
            seats = input("Enter the number of seats: ")
            destination = input("Enter the destination: ")
            plane = Planes(num, air_comp, seats, destination, [])
            airport.add_plane(plane)

        elif n == '6':
            num = input("Enter the plane number: ")
            air_comp = input("Enter the air company: ")
            seats = input("Enter the number of seats: ")
            destination = input("Enter the destination: ")
            plane = Planes(num, air_comp, seats, destination, [])
            i = int(input("Enter the index of the plane: "))
            airport.update_plane(plane, i)

        elif n == '7':
            pass

        elif n == '8':
            i = int(input("Enter the index of the plane: "))
            airport.remove_plane(i)

        elif n == '9':
            num = int(input("Enter plane number to sort: "))
            if not is_int(num):
                raise Exception(f"Invalid entry: {num} is not a number.")

            for passenger in Airport().sort_by_last_name(num):
                print(Passengers.__str__(passenger))

        elif n == '10':
            for plane in airport.sort_by_num_pass():
                print(Planes.__str__(plane))

        elif n == '11':
            substr = input("Enter string to search by: ")
            for plane in Airport().sort_by_first_name(substr):
                print(Planes.__str__(plane))

        elif n == '12':
            for plane in Airport().sort_by_concatenation():
                print(Planes.__str__(plane))

        elif n == '13':
            for plane in Airport().search_pass_num():
                print(plane)

        elif n == '14':
            substr = input("Enter the substring to search by: ")
            num = int(input("Enter the plane index to search in: "))
            for plane in Airport().search_by_substr(substr, num):
                print(plane)

        elif n == '15':
            name = str(input("Enter the name of the passenger to search: "))
            for plane in Airport().search_by_firstname(name):
                print(plane)

        elif n == '16':
            k = int(input("Enter the length of the groups: "))
            i = int(input("Enter the index of the plane to form groups in: "))
            for passenger in Airport().check_groups(k, i):
                print("\n")
                for elem in passenger:
                    print(Passengers.__str__(elem))

        elif n == '17':
            k = int(input("Enter the size of the groups to form: "))
            for elem in Airport().check_group(k):
                print('\n')
                for plane in elem:
                    print(Planes.__str__(plane))

        else:
            print("Invalid choice. Please try again: ")
