import pickle
import time
from Monitor_czasu.BTCInput import *


class Session():
    __min_session_length = 0.5
    __max_session_length = 3.5

    @staticmethod
    def validate_session_length(session_length):
        '''
        Validates a session length and returns
        True if the session is valid or False if not
        '''
        if session_length < Session.__min_session_length:
            return False
        if session_length > Session.__max_session_length:
            return False
        return True

    def __init__(self, session_length):
        if not Session.validate_session_length:
            raise Exception('Invalid session length')
        self.__session_length = session_length
        self.__session_end_time = time.localtime()
        self.__version = 1

    @property
    def session_length(self):
        return self.__session_length

    @property
    def session_end_time(self):
        return self.__session_end_time

    def check_version(self):
        pass

    def __str__(self):
        template = 'Date: {0} Length: {1}'
        date_string = time.asctime(self.__session_end_time)
        return template.format(date_string, self.__session_length)


class Contact():
    __min_text_length = 4

    __open_fee = 30
    __hourly_fee = 50

    @staticmethod
    def validate_text(text):
        '''
        Validates text to be stored in the contact
        storage.
        True if the text is valid, false if not
        '''
        if len(text) < Contact.__min_text_length:
            return False
        else:
            return True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not Contact.validate_text(name):
            raise Exception('Invalid name')
        self.__name = name

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        if not Contact.validate_text(address):
            raise Exception('Invalid address')
        self.__address = address

    @property
    def telephone(self):
        return self.__telephone

    @telephone.setter
    def telephone(self, telephone):
        if not Contact.validate_text(telephone):
            raise Exception('Invalid telephone')
        self.__telephone = telephone

    @property
    def hours_worked(self):
        return self.__hours_worked

    @property
    def billing_amount(self):
        return self.__billing_amount

    def __init__(self, name, address, telephone):
        self.name = name
        self.address = address
        self.telephone = telephone
        self.__hours_worked = 0
        self.__billing_amount = 0
        self.__sessions = []
        self.__version = 3

    @property
    def session_report(self):
        report_strings = map(str, self.__sessions)
        report_result = '\n'.join(report_strings)
        return report_result

    def __str__(self):
        template = '''Name: {0}
        Address: {1}
        Telephone: {2}
        Hours on the case: {3}
        Amount to bill: {4}
        Sessions
        {5}
        '''
        return template.format(self.name, self.address, self.telephone,
                               self.hours_worked, self.billing_amount,
                               self.session_report)

    def check_version(self):
        '''
        Checks the version number of this instance of
        Contact and upgrades the object if required.
        '''
        if self.__version == 1:
            self.__billing_amount = 0
            self.__version = 2

        if self.__version == 2:
            self.__sessions = []
            self.__version = 3

        for session in self.__sessions:
            session.check_version()

    def add_session(self, session_length):
        '''
        Adds the value of the parameter
        onto the hours spent with this contact
        Raises an exception if the session length is invalid
        '''
        if not Session.validate_session_length(session_length):
            raise Exception('Invalid session length')
        self.__hours_worked = self.__hours_worked + session_length
        amount_to_bill = Contact.__open_fee + (Contact.__hourly_fee * session_length)
        self.__billing_amount = self.__billing_amount + amount_to_bill
        session_record = Session(session_length)
        self.__sessions.append(session_record)


def new_contact():
    '''
    Reads in a new contact and stores it
    '''
    print('Create new contact')
    name = read_text('Enter the contact name: ')
    address = read_text('Enter the contact address: ')
    telephone = read_text('Enter the contact phone: ')
    try:
        new_contact = Contact(name=name, address=address, telephone=telephone)
    except Exception as e:
        print('Invalid contact:', e)
        return
    contacts.append(new_contact)


def find_contact(search_name):
    '''
    Finds the contact with the matching name
    Returns a contact instance or None if there is
    no contact with the given name
    '''
    search_name = search_name.strip()
    search_name = search_name.lower()
    for contact in contacts:
        name = contact.name
        name = name.strip()
        name = name.lower()
        if name.startswith(search_name):
            return contact
    return None


def display_contact():
    '''
    Reads in a name to search for and then displays
    the content information for that name or a
    message indicating that the name was not found
    '''
    print('Find contact')
    search_name = read_text('Enter the contact name: ')
    contact = find_contact(search_name)
    if contact != None:
        print(contact)
    else:
        print('This name was not found.')


def edit_contact():
    '''
    Reads in a name to search for and then allows
    the user to edit the details of that contact
    If there is no contact the funciton displays a
    message indicating that the name was not found
    '''
    print('Edit contact')
    search_name = read_text('Enter the contact name: ')
    contact = find_contact(search_name)
    if contact != None:
        try:
            print('Name: ', contact.name)
            new_name = read_text('Enter new name or . to leave unchanged: ')
            if new_name != '.':
                contact.name = new_name
            new_address = read_text('Enter new address or . to leave unchanged: ')
            if new_address != '.':
                contact.address = new_address
            new_phone = read_text('Enter new telephone or . to leave unchanged: ')
            if new_phone != '.':
                contact.telephone = new_phone
        except Exception as e:
            print('Edit failed:', e)
    else:
        print('This name was not found.')


def add_session_to_contact():
    '''
    Reads in a name to search for and then allows
    the user to add a session spent working for
    that contact
    '''
    print('add session')
    search_name = read_text('Enter the contact name: ')
    contact = find_contact(search_name)
    if contact != None:
        print('Name: ', contact.name)
        print('Previous hours worked:', contact.hours_worked)
        session_length = read_float(prompt='Session length: ')
        try:
            contact.add_session(session_length)
            print('Updated hours worked:', contact.hours_worked)
        except Exception as e:
            print('Add hours failed:', e)
    else:
        print('This name was not found.')


def save_contacts(file_name):
    '''
    Saves the contacts to the given filename
    Contacts are stored in binary as pickled file
    Exceptions will be raised if the save fails
    '''
    print('save contacts')
    with open(file_name, 'wb') as out_file:
        pickle.dump(contacts, out_file)


def load_contacts(file_name):
    '''
    Loads the contacts from the given filename
    Contacts are stored in binary as pickled file
    Exceptions will be raised if the load fails
    '''
    global contacts
    print('Load contacts')
    with open(file_name, 'rb') as input_file:
        contacts = pickle.load(input_file)
    for contact in contacts:
        contact.check_version()


menu = '''Time Tracker
1. New Contact
2. Find Contact
3. Edit Contact
4. Add Session
5. Exit Program
Enter your command: '''

filename = 'vsncontacts.pickle'
try:
    load_contacts(filename)
except:
   print('Contacts file not found')
   contacts=[]

while True:
    command = read_int_ranged(prompt=menu, min_value=1, max_value=5)
    if command == 1:
        new_contact()
    elif command == 2:
        display_contact()
    elif command == 3:
        edit_contact()
    elif command == 4:
        add_session_to_contact()
    elif command == 5:
        save_contacts(filename)
        break