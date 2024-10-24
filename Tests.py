import unittest
from Airport import Airport
from Passenger import Passengers
from Plane import Planes
airport = Airport()


class Tests(unittest.TestCase):
    def setUp(self):
        self.passengers = []
        self.airport = []
        self.pass0 = Passengers('Alisha', 'Keys', 53270)
        self.pass1 = Passengers('George', 'Beach', 52340)
        self.pass2 = Passengers('Nick', 'Smith', 23450)
        self.pass3 = Passengers('Joseph', 'Smith', 96430)
        self.pass4 = Passengers('John', 'Orvil', 11110)
        self.pass5 = Passengers('George', 'Dean', 21210)
        self.passengers.append(self.pass0)
        self.passengers.append(self.pass1)
        self.passengers.append(self.pass2)
        self.passengers.append(self.pass3)
        self.passengers.append(self.pass4)
        self.passengers.append(self.pass5)
        self.plane1 = Planes(1, 'Boeing', 10, 'Berlin', passengers=[])
        self.plane1.add_pass(self.pass0)
        self.plane1.add_pass(self.pass1)
        self.plane1.add_pass(self.pass2)
        self.plane1.add_pass(self.pass3)
        self.plane1.add_pass(self.pass4)
        self.plane1.add_pass(self.pass5)

        self.pass6 = Passengers('Homer', 'Simpson', 45890)
        self.pass7 = Passengers('Marge', 'Simpson', 45900)
        self.pass8 = Passengers('Bart', 'Simpson', 45910)
        self.pass9 = Passengers('Lisa', 'Simpson', 45920)
        self.pass10 = Passengers('Maggie', 'Simpson', 45930)
        self.plane2 = Planes(2, 'Spirit', 10, 'Belgium', passengers=[])
        self.plane2.add_pass(self.pass6)
        self.plane2.add_pass(self.pass7)
        self.plane2.add_pass(self.pass8)
        self.plane2.add_pass(self.pass9)
        self.plane2.add_pass(self.pass10)

        self.pass11 = Passengers('Oscar', 'Johnson', 53010)
        self.pass12 = Passengers('Samantha', 'Jacobs', 11760)
        self.pass13 = Passengers('Myron', 'Clarkson', 71010)
        self.pass14 = Passengers('Lorelle', 'Hudson', 41090)
        self.pass15 = Passengers('Hilda', 'Dayton', 37120)
        self.pass16 = Passengers('George', 'Lobo', 53900)
        self.pass17 = Passengers('Carley', 'Shroud', 61090)
        self.plane3 = Planes(3, 'Airline2', 10, 'Frankfurt', passengers=[])
        self.plane3.add_pass(self.pass11)
        self.plane3.add_pass(self.pass12)
        self.plane3.add_pass(self.pass13)
        self.plane3.add_pass(self.pass14)
        self.plane3.add_pass(self.pass15)
        self.plane3.add_pass(self.pass16)
        self.plane3.add_pass(self.pass17)
        self.airport.append(self.plane1)
        self.airport.append(self.plane2)
        self.airport.append(self.plane3)

    def test_get_first_name(self):
        self.assertEqual(self.pass0.get_first_name(), 'Alisha')
        self.assertEqual(self.pass17.get_first_name(), 'Carley')
        self.assertEqual(self.pass16.get_first_name(), 'George')

    def test_get_last_name(self):
        self.assertEqual(self.pass0.get_last_name(), 'Keys')
        self.assertEqual(self.pass10.get_last_name(), 'Simpson')
        self.assertEqual(self.pass12.get_last_name(), 'Jacobs')

    def test_get_pass_num(self):
        self.assertEqual(self.pass0.get_pass_num(), 53270)
        self.assertEqual(self.pass2.get_pass_num(), 23450)
        self.assertEqual(self.pass3.get_pass_num(), 96430)

    def test_set_first_name(self):
        self.pass0.set_first_name('Reginald')
        self.assertEqual(self.pass0.get_first_name(), 'Reginald')
        self.pass10.set_first_name('Gabiță')
        self.assertEqual(self.pass10.get_first_name(), 'Gabiță')

    def test_set_last_name(self):
        self.pass0.set_last_name('Silly Goose')
        self.assertEqual(self.pass0.get_last_name(), 'Silly Goose')
        self.pass17.set_last_name('Bitch')
        self.assertEqual(self.pass17.get_last_name(), 'Bitch')

    def test_set_pass_num(self):
        self.pass5.set_pass_num(1234)
        self.assertEqual(self.pass5.get_pass_num(), 1234)
        self.pass10.set_pass_num(0000)
        self.assertEqual(self.pass10.get_pass_num(), 0000)

    def test_get_first_digits(self):
        self.assertEqual(self.pass10.get_first_digits(), 459)
        self.assertEqual(self.pass17.get_first_digits(), 610)

    def test_check_for_substr(self):
        self.assertEqual(self.pass1.check_for_substr('Geo'), True)
        self.assertEqual(self.pass1.check_for_substr('Beac'), True)
        self.assertEqual(self.pass3.check_for_substr('jo'), False)

    def test_get_name_number(self):
        self.assertEqual(self.plane1.get_name_number(), 1)
        self.assertEqual(self.plane2.get_name_number(), 2)
        self.assertEqual(self.plane3.get_name_number(), 3)

    def test_get_air_comp(self):
        self.assertTrue(self.plane1.get_air_comp(), 'Boeing')
        self.assertNotEqual(self.plane2.get_air_comp(), 'Boeing')
        self.assertEqual(self.plane3.get_air_comp(), 'Airline2')

    def test_get_seats(self):
        self.assertTrue(self.plane1.get_seats(), 10)
        self.assertNotEqual(self.plane2.get_seats(), 0)
        self.assertEqual(self.plane3.get_seats(), 10)

    def test_get_dest(self):
        self.assertTrue(self.plane1.get_dest(), 'Berlin')
        self.assertNotEqual(self.plane2.get_dest(), 'Berlin')
        self.assertEqual(self.plane3.get_dest(), 'Frankfurt')

    def test_get_passengers(self):
        self.assertTrue(self.plane1.get_passengers(), [self.pass0, self.pass1, self.pass2, self.pass3, self.pass4, self.pass5])
        self.assertNotEqual(self.plane2.get_passengers(), [])
        self.assertEqual(self.plane2.get_passengers(), [self.pass6, self.pass7, self.pass8, self.pass9, self.pass10])

    def test_set_name_number(self):
        self.plane1.set_name_number('Error 404')
        self.assertEqual(self.plane1.get_name_number(), 'Error 404')
        self.plane2.set_name_number('The plane that took down the twin towers')
        self.assertEqual(self.plane2.get_name_number(), 'The plane that took down the twin towers')

    def test_set_air_comp(self):
        self.plane1.set_air_comp('Gatekeep')
        self.assertEqual(self.plane1.get_air_comp(), 'Gatekeep')
        self.plane2.set_air_comp('Gaslight')
        self.assertNotEqual(self.plane1.get_air_comp(), 'Spirit')
        self.plane3.set_air_comp('Girlboss')
        self.assertEqual(self.plane3.get_air_comp(), 'Girlboss')

    def test_set_seats(self):
        self.plane1.set_seats(666)
        self.assertEqual(self.plane1.get_seats(), 666)
        self.plane2.set_seats(420)
        self.assertEqual(self.plane2.get_seats(), 420)
        self.plane1.set_seats(69)
        self.assertNotEqual(self.plane1.get_seats(), 10)

    def test_set_dest(self):
        self.plane1.set_dest('Hell')
        self.assertEqual(self.plane1.get_dest(), 'Hell')
        self.plane2.set_dest('Venus')
        self.assertEqual(self.plane2.get_dest(), 'Venus')
        self.plane1.set_dest('Asshole')
        self.assertNotEqual(self.plane1.get_dest(), 'Hell')

    def test_get_all_passengers(self):
        self.assertIn('The passenger Alisha Keys with passport number 5327', self.plane1.get_all_passengers())
        self.assertNotIn('The passenger George Dean with passport number 2121', self.plane2.get_all_passengers())
        self.assertIn('The passenger George Dean with passport number 2121', self.plane1.get_all_passengers())

    def test_add_pass(self):
        self.pass01 = Passengers('Alina', 'Buliga', 6969)
        self.plane1.add_pass(self.pass01)
        self.assertIn(self.pass01, self.plane1.get_passengers())

    def test_delete_pass(self):
        self.plane1.delete_pass(self.pass0)
        self.assertEqual(self.plane1.get_passengers(), [self.pass1, self.pass2, self.pass3, self.pass4, self.pass5])
        self.assertNotIn(self.pass0, self.plane1.get_passengers())

    def test_get_passenger_count(self):
        self.assertEqual(self.plane1.get_passenger_count(), 6)
        self.assertEqual(self.plane2.get_passenger_count(), 5)
        self.assertEqual(self.plane3.get_passenger_count(), 7)

    def test_check_for_str(self):
        self.assertEqual(self.plane1.check_for_str(str(self.pass5.get_first_name()), 'Geo'), True)
        self.assertEqual(self.plane2.check_for_str(str(self.pass7.get_first_name()), 'Geor'), False)
        self.assertEqual(self.plane2.check_for_str(str(self.pass7.get_first_name()), 'Ma'), True)

    def test_check_plane(self):
        self.assertEqual(self.plane1.check_plane('Ge'), 2)
        self.assertEqual(self.plane2.check_plane('Geor'), 0)
        self.assertEqual(self.plane3.check_plane('C'), 1)

    def test_concatenate_lst(self):
        self.assertEqual(self.plane1.concatenate_lst(), '6Berlin')
        self.assertEqual(self.plane2.concatenate_lst(), '5Belgium')

    def test_get_length(self):
        self.assertEqual(self.plane1.get_length(), 7)
        self.assertEqual(self.plane2.get_length(), 8)

    def test_check_pass_num(self):
        self.assertEqual(self.plane2.check_pass_num(), True)
        self.assertEqual(self.plane3.check_pass_num(), False)
        self.assertEqual(self.plane1.check_pass_num(), False)

    def test_check_by_name(self):
        self.assertEqual(self.plane1.check_by_name('Nick'), True)
        self.assertEqual(self.plane2.check_by_name('Nick'), False)
        self.assertEqual(self.plane1.check_by_name('Goerge'), False)

    def test_sort_by_last_name(self):
        self.assertNotIn(airport.sort_by_last_name(1), [self.pass1])

    def test_sort_by_first_name(self):
        self.assertNotEqual(airport.sort_by_first_name('Geo'), self.plane2, self.plane3)
        self.assertNotEqual(airport.sort_by_first_name('Alf'), self.plane2, self.plane3)

    def test_sort_by_concatenation(self):
        self.assertNotEqual(airport.sort_by_concatenation(), self.plane2, self.plane3)
        self.assertNotEqual(airport.sort_by_concatenation(), self.plane1)

    def test_search_pass_num(self):
        self.assertNotEqual(airport.search_pass_num(), self.plane2)
        self.assertNotEqual(airport.search_pass_num(), self.plane1)
        self.assertNotEqual(airport.search_pass_num(), self.plane3)

    def test_search_by_substr(self):
        self.assertNotEqual(airport.search_by_substr('Geo', 0), self.pass1, self.pass5)
        self.assertNotEqual(airport.search_by_substr('Al', 2), self.pass2)

    def test_search_by_firstname(self):
        self.assertNotEqual(airport.search_by_firstname('George'), self.plane1, self.plane3)

