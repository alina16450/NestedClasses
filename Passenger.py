class Passengers:

    def __init__(self, first_name, last_name, pass_num):
        self.first_name = first_name
        self.last_name = last_name
        self.pass_num = pass_num

    def get_first_name(self):
        """
        :return: The first name of the passenger by instance.
        """
        return self.first_name

    def get_last_name(self):
        """
        :return: The last name of the passenger by instance.
        """
        return self.last_name

    def get_pass_num(self):
        """
        :return: The passenger number of the passenger by instance.
        """
        return self.pass_num

    def set_first_name(self, first_name):
        """
        :param first_name: The first name to assign to passenger.
        """
        self.first_name = first_name

    def set_last_name(self, last_name):
        """
        :param last_name: The last name to assign to passenger.
        """
        self.last_name = last_name

    def set_pass_num(self, pass_num):
        """
        :param pass_num: The passenger number to assign to passenger.
        """
        self.pass_num = pass_num

    def get_first_digits(self):
        """
        Used internally to get the first 3 digits of a passenger number.
        :return: The first 3 digits.
        """
        return self.get_pass_num() // 100

    def check_for_substr(self, substr):  # for 6
        """
        Used internally to check if a passenger has a first name or last name starting with a substring.
        :param substr: The given substring to check for each passenger name.
        :return: A true or false statement depending on if it was a match.
        """
        t = False
        a = self.get_first_name()
        b = self.get_last_name()
        if a.startswith(substr) or b.startswith(substr):
            t = True
        return t

    def __str__(self):
        p = 'The passenger ' + str(self.first_name) + " " + str(self.last_name) + ' with passport number ' + str(self.pass_num)
        return p
