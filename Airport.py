from Plane import Planes
from Passenger import Passengers


class Airport:
    def __init__(self):
        self.airport_lst = []

    @staticmethod
    def my_search(lst, condition):
        """
        The static search method that is implemented in all the search functions in plane.
        :param lst: Given list to search in, either the passengers or the plane.
        :param condition: The condition to search for in each instance of the list.
        :return: A new list with only the instances that met the given condition.
        """
        result = []
        for inst in lst:
            if condition(inst):
                result.append(inst)
        if len(result) == 0:
            print("No instances were found in the list. Try again.")
        else:
            return result

    @staticmethod
    def my_sort(lst, key):
        """
        A static sort method called for each sort functions in plane.
        It enters a while loop, and checks index by index if the first element is greater than the second,
        based on the key. If such an element is found, they are swapped and the while loop is entered again. If
        no swaps are made, the while loop gets exited and the list is returned.
        :param lst: Given list to sort, either the list of passengers or list of planes.
        :param key: The key to sort by for each instance of the list.
        :return: The new sorted list.
        """
        swapped = False
        while not swapped:
            swapped = True
            for i in range(0, len(lst) - 1):
                if key(lst[i]) > key(lst[i + 1]):
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
                    swapped = False
        return lst

    @staticmethod
    def my_backtrack(lst: list, n: int, k: int) -> list[list[int]]:
        """
        Backtracking method that takes in a list of indexes and groups them based on the input k. Each iteration checks if
        the length of the group equals k, and if it does not it enters a for loop which checks that a unique index combination
        is created. Starts by removing the first item of the list, and then going down each option left, until all of them have been
        used for a unique combination.
        :param lst: A list of indexes to work with, usually given from another function.
        :param n: The length of the list of indexes.
        :param k: The desired length of the groups to return.
        :return: A list of all the possible combinations of the indexes of size k.
        """
        res = []

        def backtrack(start, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return

            for i in range(start, n):
                comb.append(i)
                backtrack(i+1, comb)
                comb.pop()
        backtrack(lst[0], [])
        return res

    def sort_by_last_name(self, num):  # 1
        """
        Calls on get_last_name function as the list to sort by, and the list of passengers as the list to sort.
        :param num: The number of the plane to search in.
        :return: The list of passengers in the plane, sorted alphabetically by last name.
        """
        for i in range(len(self.airport_lst)):
            if self.airport_lst[i].get_name_number() == num:
                key = lambda p: p.get_last_name()
                self.airport_lst[i] = self.my_sort(self.airport_lst[i].get_passengers(), key)
                return self.airport_lst[i]

    def sort_by_num_pass(self):  # 2
        """
        Calls on get_passenger_count function as the key to sort by, and the list of planes to sort.
        :return: The list of planes sorted by the number of passengers in each plane.
        """
        key = lambda x: x.get_passenger_count()
        self.airport_lst = self.my_sort(self.airport_lst, key)
        return self.airport_lst

    def sort_by_first_name(self, st):  # 3
        """
        Calls on check_plane as the key to sort by, which returns an int count of how many passengers in a plane have a first name starting
        with a given string. Uses the airport list as the list to sort.
        :param st: The string to sort by, which is given by user.
        :return: The list of planes sorted by how many passengers were found in each plane containing that given string.
        """
        key = lambda x: x.check_plane(st)
        self.airport_lst = self.my_sort(self.airport_lst, key)
        return self.airport_lst

    def sort_by_concatenation(self):  # 4
        """
        Calls on get_length as the key to sort by, which returns the length of the concatenated number of passengers in a plane and destination.
        Sorts the list of planes by the length of the concatenated string.
        :return: The list of planes sorted.
        """
        key = lambda x: x.get_length()
        self.airport_lst = self.my_sort(self.airport_lst, key)
        return self.airport_lst

    def search_pass_num(self):  # 5
        """
        Calls on check_pass_num as the key to sort by, which checks for any passengers in a plane that have the same first 3 digits
        in their passport number. Searches in the list of planes.
        :return: The list of planes that have passengers that met the criteria specified.
        """
        key = lambda x: x.check_pass_num()
        return self.my_search(self.airport_lst, key)

    def search_by_substr(self, substr, i):  # 6
        """
        Calls on check_for_substr as the key to sort by, which checks first and last name of each passenger, to see if it starts with a substring.
        :param substr: The substring to search for, given by the user.
        :param i: The index of the plane that is being searched, also given by the user.
        :return: A list of the passengers that met the criteria.
        """
        key = lambda x: x.check_for_substr(substr)
        return self.my_search(self.airport_lst[i].get_passengers(), key)

    def search_by_firstname(self, name):  # 7
        """
        Calls on check_by_name as the key to sort by, which checks if there is a passenger with a given first name in a plane.
        Then it checks that for each plane in airport.
        :param name: The name we are checking for, given by the user.
        :return: The list of planes that contain that name.
        """
        key = lambda x: x.check_by_name(name)
        return self.my_search(self.airport_lst, key)

    def groups_by_last_name(self, k, i):  # 8
        """
        Calls on my_backtrack and enters all the required parameters for the group by last name function. It iterates through
        the list of passengers and creates a list of indexes for each one in a given plane, and also gets the length of that list.
        :param k: The size of the groups that we are trying to form.
        :param i: The index of the plane we are working with.
        :return: A list of lists containing the unique groups of indexes.
        """
        lst = self.airport_lst[i].get_passengers()
        index_lst = []
        for i in range(len(lst)):
            index_lst.append(i)
        key1 = len(index_lst)
        final_lst = self.my_backtrack(index_lst, key1, k)
        return final_lst

    def check_groups(self, k, i):  # 8
        """
        Function that finishes up the groups by last name request, by going through each list in the list of lists returned
        by groups_by_last_name and checking if any of the passengers in the groups have the same last name. If any match is
        found, the loop moves on to the next group. If no match is found, group gets added to a new list.
        :param k: The size of the groups we are looking to form.
        :param i: The index of the plane we are working with.
        :return: A list of all the final groups, which do not contain any passengers with the same last name.
        """
        new_lst = []
        lst = self.airport_lst[i].get_passengers()
        for group in self.groups_by_last_name(k, i):
            c = False
            for j in range(k-1):
                for t in range(j+1, k):
                    if lst[group[j]].get_last_name() == lst[group[t]].get_last_name():
                        c = True
            if not c:
                new_lst.append(group)
        l = []
        for elem1 in new_lst:
            c = []
            for o in elem1:
                c.append(lst[o])
            l.append(c)
        return l

    def index_by_dest(self):  # 9
        """
        Used internally to get a list of indexes of the planes that have the same destination.
        :return: The final list of indexes.
        """
        temp_lst = []
        for i in range(0, len(self.airport_lst)-1):
            for j in range(i+1, len(self.airport_lst)):
                if self.airport_lst[i].get_dest() == self.airport_lst[j].get_dest() and self.airport_lst[i] not in temp_lst:
                    temp_lst.append(self.airport_lst[i])
                    temp_lst.append(self.airport_lst[j])
        return temp_lst

    def groups_by_dest(self, k):  # 9
        """
        Used internally to plug in the list of indexes from index_by_dest into my_backtrack, as well as the length of the list of indexes.
        :param k: The size of the groups being requested for my_backtrack.
        :return: A list of unique combinations of k size of passengers who have the same destination.
        """
        lst = self.index_by_dest()
        index_lst = []
        for i in range(len(lst)):
            index_lst.append(i)
        key1 = len(lst)
        final_lst = self.my_backtrack(index_lst, key1, k)
        lt = []
        for elem1 in final_lst:
            c = []
            for o in elem1:
                c.append(lst[o])
            lt.append(c)
        return lt

    def check_group(self, k):  # 9
        """
        Final check for groups who have the same destination, this function checks each plane in each group in our list of groups,
        and if it sees two planes with the same airline company, it does not include it as a final group.
        :param k: The size of the groups being requested for my_backtrack.
        :return: A list of unique combinations of k size of passengers with the same destination and different airline companies.
        """
        temp_lst = []
        for group in self.groups_by_dest(k):
            c = True
            for i in range(k-1):
                for j in range(i+1, k):
                    if group[i].get_air_comp() != group[j].get_air_comp() and group[i].get_dest() == group[j].get_dest():
                        c = False
            if not c:
                temp_lst.append(group)

        return temp_lst

    def get_all_planes(self):  # q
        """
        Returns the final list of planes, used for testing.
        :return: List of planes in the __str__ format.
        """
        return self.airport_lst

    def add_pass(self, passenger, i):
        self.airport_lst[i].add_pass(passenger)

    def update_passenger(self, passenger, i, i2):
        self.airport_lst[i].update_pass(passenger, i2)

    def replace_first_name(self, j, i, name):
        self.airport_lst[j].update_first_name(i, name)

    def replace_last_name(self, j, i, name):
        self.airport_lst[j].update_last_name(i, name)

    def replace_num(self, j, i, num):
        self.airport_lst[j].update_pass_num(i, num)

    def delete_pass(self, j, i):
        self.airport_lst[j].delete_pass(i)

    def add_plane(self, plane):
        self.airport_lst.append(plane)

    def update_plane(self, plane, i):
        self.airport_lst[i] = plane

    def remove_plane(self, i):
        del self.airport_lst[i]
