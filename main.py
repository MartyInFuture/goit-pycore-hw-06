from collections import UserDict

class Field:
  def __init__(self, value):
    self.value = value

  def __str__(self):
    return str(self.value)

class Name(Field):
  pass

class PhoneSizeException(Exception):
  def __init__(self, message = 'Phone number should be 10 digits!'):
    super().__init__(message)

class Phone(Field):
  def __init__(self, value):
    if len(value) != 10:
      raise PhoneSizeException
    else:
      self.value = value

class Record():
  def __init__(self, name):
    self.name = Name(name)
    self.phones = []

  def __str__(self):
    return str({'name': self.name.value, 'phones': [p.value for p in self.phones]})

  def add_phone(self, new_phone):
    self.phones.append(Phone(new_phone))

  def remove_phone(self, phone):
    phone_to_remove = self.find_phone(phone)

    if phone_to_remove:
      self.phones.remove(phone_to_remove)
  
  def edit_phone(self, phone, new_phone):
    found_phone = self.find_phone(phone)

    if found_phone:
      phone_index = self.phones.index(found_phone)
      self.phones[phone_index] = Phone(new_phone)
  
  def find_phone(self, phone):
    found_phone = next(p for p in self.phones if p.value == phone)
    return found_phone


class AddressBook(UserDict):
  def add_record(self, record):
    self.data[record.name.value] = record

  def find(self, name):
    return self.data.get(name)
  
  def delete(self, name):
    if name in self.data:
      del self.data[name]
    



# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555
john.add_phone('1111111111')
john.remove_phone('5555555555')
print(john)

# Видалення запису Jane
book.delete("Jane")
