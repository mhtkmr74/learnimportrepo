import heapq


class VechileManagement():

    def __init__(self, parking_slot_size=0):
        self.counter = 1
        self.p_slot_size = parking_slot_size
        self.p_slot_data = dict()
        self.vacated_slot = list()
        heapq.heapify(self.vacated_slot)

    def park_vechile(self, vechile_no, driver_age):
        '''
        Get vechile no and driver age.
        Based on the available slot, it tries to allocate the slot near to gate.
        If no slot is available it raises an exception.
        '''
        if self.p_slot_size < self.counter and not self.vacated_slot:
            # All slots are full
            return "Parking slot is full"

        elif self.vacated_slot:
            # get the first empty slot and assign it to user
            nearest_empty_slot = heapq.heappop(self.vacated_slot)
            self.p_slot_data[nearest_empty_slot] = [vechile_no, driver_age]
            return f"Car with vehicle registration number {vechile_no} has been parked at slot number {nearest_empty_slot}"

        else:
            # The slots till now are full and hense giving the next slot to user
            self.p_slot_data[self.counter] = [vechile_no, driver_age]
            self.counter = self.counter + 1
            return f"Car with vehicle registration number {vechile_no} has been parked at slot number {self.counter - 1}"

    def vacate_slot(self, slot):
        '''
        Takes the slot as an input and check if there is vechile at the given slot.
        if there is vechile on a given slot then it vacates the slot
        Else raises exception, if no slot s available.
        '''
        # check if slot is there, if no slot raise exception ---- Main
        if slot in self.vacated_slot:
            return f"Sorry the slot you are trying to vacate {slot} is already vacated."
        else:
            heapq.heappush(self.vacated_slot, slot)
            vechile_details = self.p_slot_data[slot]
            self.p_slot_data[slot] = None
            return f"""Slot number {slot} vacated, the car with vehicle registration number {vechile_details[0]} left the space, the driver of the car was of age {vechile_details[1]}"""

    def get_vechile_details_from_age(self, age):
        '''
        Get the age of driver.
        Check all the parked vechile's driver age.
        if it matches then add it in list and return
        '''
        vechile_details = list()
        for slot_no in self.p_slot_data:
            parked_vechile_data = self.p_slot_data[slot_no]
            if parked_vechile_data and parked_vechile_data[1] == age:
                vechile_details.append(parked_vechile_data[0])
        return ', '.join(vechile_details)

    def get_slot_with_vechile_no(self, vechile_no):
        '''
        Get the vechile number
        Check all the parked vechile's vechile number.
        if it matches then return the slot
        Vechile number is always uniques as it is in real world
        '''
        for slot_no in self.p_slot_data:
            parked_vechile_data = self.p_slot_data[slot_no]
            if parked_vechile_data and parked_vechile_data[0] == vechile_no:
                return slot_no
        return "No Vechile found with given Vechile Number"

    def get_slot_nos_from_age(self, age):
        '''
        Get all the vechiles slot whose driver age matches with given age
        '''
        slot_details = list()
        for slot_no in self.p_slot_data:
            parked_vechile_data = self.p_slot_data[slot_no]
            if parked_vechile_data and parked_vechile_data[1] == age:
                slot_details.append(str(slot_no))
        return ', '.join(slot_details)


def vechile_management_fun(inp_file_path):
    '''
    Read file for input.
    Call VechileManagement function based on input.
    Prints the output in console
    '''
    inp_file = open(inp_file_path, 'r')
    vechile_obj = None
    for row in inp_file:
        row_data = row.split(' ')

        if row_data[0] == "Create_parking_lot":
            slots = int(row_data[1])
            vechile_obj = VechileManagement(slots)
            print(f"Created parking of {slots} slots")

        elif row_data[0] == "Park":
            vechile_number = row_data[1]
            driver_age = int(row_data[3])
            print(vechile_obj.park_vechile(vechile_number, driver_age))

        elif row_data[0] == "Slot_numbers_for_driver_of_age":
            driver_age = int(row_data[1])
            print(vechile_obj.get_slot_nos_from_age(driver_age))

        elif row_data[0] == "Vehicle_registration_number_for_driver_of_age":
            driver_age = int(row_data[1])
            print(vechile_obj.get_slot_nos_from_age(driver_age))

        elif row_data[0] == "Slot_number_for_car_with_number":
            vechile_no = row_data[1]
            print(vechile_obj.get_slot_with_vechile_no(vechile_no))

        elif row_data[0] == "Leave":
            slot_to_vacate = int(row_data[1])
            print(vechile_obj.vacate_slot(slot_to_vacate))
        else:
            print("Wrong Input Passed")


if __name__ == "__main__":
    inp_file_path = input("Please give exact path for input file:- ")
    vechile_management_fun(inp_file_path)
