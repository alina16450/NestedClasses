from Passenger import Passengers

class Planes:

    def __init__(self, name_number, air_comp, seats, dest, passengers):
        self.name_number = name_number
        self.air_comp = air_comp
        self.seats = seats
        self.dest = dest
        self.passengers = passengers
        self.lst_pass = []

    def get_name_number(self):
        """
        :return: the plane name by instance.
        """
        return self.name_number

    def get_air_comp(self):
        """
        :return: the plane air company by instance.
        """
        return self.air_comp

    def get_seats(self):
        """
        :return: the number of seats available to passengers.
        """
        return self.seats

    def get_dest(self):
        """
        :return: the plane destination by instance.
        """
        return self.dest

    def get_passengers(self):
        """
        :return: the full list of passengers in a plane by instance.
        """
        return self.lst_pass

    def set_name_number(self, name_number):
        """
        :param name_number: new number for plane to assign.
        """
        self.name_number = name_number

    def set_air_comp(self, air_comp):
        """
        :param air_comp: new air company name to assign.
        """
        self.air_comp = air_comp

    def set_seats(self, seats):
        """
        :param seats: new number of seats available to passengers.
        """
        self.seats = seats

    def set_dest(self, dest):
        """
        :param dest: new destination name to assign.
        """
        self.dest = dest

    def get_all_passengers(self):
        """
        :return: the full list of passengers in a plane using the string function for passengers.
        """
        lst = []
        for passenger in self.lst_pass:
            lst.append(Passengers.__str__(passenger))
        result = '\n'.join(lst) + '\n'
        return result

    def add_pass(self, passenger):
        """
        :param passenger: given in the form of the passenger class,
        adds the passenger to the list of passengers.
        """
        self.lst_pass.append(passenger)

    def delete_pass(self, i):
        """
        :param i: deletes a passenger instance from the list of passengers.
        """
        del self.lst_pass[i]

    def update_pass(self, passenger, i):
        self.lst_pass[i] = passenger

    def update_first_name(self, i, name):
        self.lst_pass[i].set_first_name(name)

    def update_last_name(self, i, name):
        self.lst_pass[i].set_last_name(name)

    def update_pass_num(self, i, num):
        self.lst_pass[i].set_pass_num(num)

    def get_passenger_count(self):
        """
        Counts the number of passengers in the plane using the string function for passengers.
        :return: the final count.
        """
        passenger_count = 0
        for _ in self.lst_pass:
            passenger_count += 1
        return passenger_count

    @staticmethod
    def check_for_str(elem, st):  # for check_plane
        """
        Used internally for checking if a string stars with a given element.
        :param elem: the element to check.
        :param st: the string to check by.
        :return: returns True if the string starts with the elem, False otherwise.
        """
        check = False
        if elem.startswith(st):
            check = True
        return check

    def check_plane(self, st):  # for 3
        """
        Used internally for checking each passenger in the list,
        calls on check_for_str to check each passenger first name for the start string.
        If a passenger is found meeting that condition, it will add 1 to a counter.
        :param st: the string to check for in the passengers first name.
        :return: the final count of how many passengers met the condition in a plane.
        """
        count = 0
        for passenger in self.lst_pass:
            if Planes.check_for_str(str(passenger.get_first_name()), st):
                count += 1
        return count

    def concatenate_lst(self):  # for get_lengths
        """
        Used internally to concatenate the passenger count and destination of a plane.
        :return: The concatenated string.
        """
        num = self.get_passenger_count()
        dest = self.get_dest()
        new_str = str(num) + dest
        return new_str

    def get_length(self):  # for 4
        """
        Used internally to get the length of the concatenated string of passenger count and destination.
        :return: the length as int of the concatenated string.
        """
        return len(self.concatenate_lst())

    def check_pass_num(self):  # for 5
        """
        Used internally to check if there are two passengers in the plane with the same first 3 digits of a passport number.
        :return: A true or false statement.
        """
        found = False
        for i in range(len(self.lst_pass)-1):
            for j in range(i+1, len(self.lst_pass)):
                if self.lst_pass[i].get_first_digits() == self.lst_pass[j].get_first_digits():
                    found = True
        return found

    def check_by_name(self, name):  # for 7
        """
        Used internally to check if there is a passenger with a given first name in a plane.
        :param name: The name given by user.
        :return: True or false depending on if a match was found.
        """
        found = False
        for i in range(len(self.lst_pass)):
            if self.lst_pass[i].get_first_name() == name:
                found = True
        return found

    def __str__(self):
        a = f"Plane number: {self.name_number}\nAir Company: {self.air_comp}\nSeats: {self.seats}\nDestination: {self.dest}\nWith passengers: {self.get_all_passengers()}"
        return a
