from collections import UserDict


class InvalidLengthError(Exception):
    pass


class InvalidFormatError(Exception):
    pass


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except InvalidLengthError as le:
            print(le)
        except InvalidFormatError as fe:
            print(fe)

    return inner


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        self.value = value


class Phone(Field):
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if len(new_value) != 10:
            raise InvalidLengthError(
                'Error. Phone number should be 10 characters long.')
        elif not new_value.isdigit():
            raise InvalidFormatError(
                'Error. Phone number should contain only digits.')
        else:
            self.__value = new_value


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: { '; '.join(p.value for p in self.phones) if len(self.phones) else 'No phones added.'}"

    @input_error
    def add_phone(self, phone):
        if self.__is_phone_available(phone):
            print('Phone is already added.')
        else:
            self.phones.append(Phone(phone))
            print(f'Phone is added: {phone}.')

    @input_error
    def edit_phone(self, current_phone, new_phone):
        index = self.__find_phone_index(current_phone)
        if index is not None:
            self.phones[index] = Phone(new_phone)
            print(f'Phone is edited: {new_phone}.')
        else:
            print('Phone is not found.')
            return None

    def find_phone(self, phone):
        if self.__is_phone_available(phone):
            print(f'Phone is found: {phone}.')
            return phone
        else:
            print('Phone is not found.')
            return None

    def remove_phone(self, phone):
        index = self.__find_phone_index(phone)
        if index is not None:
            del self.phones[index]
            print(f'Phone is deleted: {phone}.')
        else:
            print('Phone is not found.')

    def __find_phone_index(self, phone):
        return next((i for i, item in enumerate(self.phones) if item.value == phone), None)

    def __is_phone_available(self, phone):
        return self.__find_phone_index(phone) is not None


class AddressBook(UserDict):
    def add_record(self, record):
        name = record.name
        self.data[name.value] = record
        print(f'Record is added to address book: {record}')

    def find(self, name):
        if name in self.data:
            record = self.data[name]
            print(f'Record is found: {record}')
            return record
        else:
            print('Record is not found.')
            return None

    def delete(self, name):
        if name in self.data:
            record = self.data[name]
            del self.data[name]
            print(f'Record is deleted: {record}.')
        else:
            print('Record is not found.')
