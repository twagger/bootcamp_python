"""Bank module"""
from datetime import datetime


class Account(object):
    """The account"""

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        """Transfer amount to account"""
        self.value += amount


def iscorrupted(account):
    """Check if the account is corrupted"""
    try:
        attributes = [a for a in dir(account)
                      if not a.startswith('__')
                      and not a.isupper()
                      and not a == 'transfer']
        if len(attributes) % 2 != 0:
            return True
        if any(a for a in attributes if a.startswith('b')):
            return True
        if not any(a for a in attributes if a.startswith('zip')
                   or a.startswith('addr')):
            return True
        if not all(a in attributes for a in ['name', 'id', 'value']):
            return True
        if not isinstance(account.name, str):
            return True
        if not isinstance(account.id, int):
            return True
        if not isinstance(account.value, int) and not isinstance(account.value,
                                                                 float):
            return True
        return False
    except TypeError as exc:
        raise TypeError("An Account is expected.") from exc


def remove_starting_b(name):
    """Fix the account removing the starting b on attribute"""
    while name.startswith('b'):
        name = name[1:]
    if not name:
        name = 'erased_name'
    return name


class Bank(object):
    """The bank"""

    def __init__(self):
        self.accounts = []

    def add(self, new_account):
        """ Add new_account in the Bank
            @new_account: Account() new account to append
            @return       True if success, False if an error occured
        """
        # Type check
        if not isinstance(new_account, Account):
            return False
        # Check if an account with the same name already exists
        if any(account for account in self.accounts if account.name == new_account.name) is True:
            print("Account already exists")
            return False
        try:
            self.accounts.append(new_account)
        except IndexError:
            return False
        return True

    def transfer(self, origin, dest, amount):
        """ Perform the fund transfer
            @origin: str(name) of the first account
            @dest:   str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return  True if success, False if an error occured
        """
        try:
            origin_acc = next((account for account in self.accounts
                               if account.name == origin), None)
            dest_acc = next((account for account in self.accounts
                             if account.name == dest), None)
            if amount < 0:
                return False
            if origin_acc is not None and dest_acc is not None:
                if origin_acc.value >= 0 and origin_acc.value >= amount:
                    # Check if the accounts are corrupted
                    if iscorrupted(origin_acc) or iscorrupted(dest_acc):
                        return False
                    elif origin != dest:
                        origin_acc.value -= amount
                        dest_acc.value += amount
                    return True
            return False
        except TypeError:
            return False
        except AttributeError:
            return False

    def fix_account(self, name):
        """ fix account associated to name if corrupted
            @name:  str(name) of the account
            @return True if success, False if an error occured
        """
        try:
            acc = next((account for account in self.accounts
                        if account.name == name), None)
            if acc and iscorrupted(acc) is True:
                attributes = [a for a in dir(acc)
                              if not a.startswith('__')
                              and not a.isupper()
                              and not a == 'transfer']

                # rename attributes starting with a b
                to_fix = [a for a in attributes if a.startswith('b')]
                for a in to_fix:
                    acc.__dict__[remove_starting_b(a)] = acc.__dict__.pop(a)

                # add a zip or an addr attribute
                if not any(a for a in attributes if a.startswith('zip')
                           or a.startswith('addr')):
                    acc.addr = "The Moon"

                # add name, id and value if they are missing
                if acc.name is None:
                    acc.name = "Dummy " + datetime.now().strftime('%s')
                if acc.id is None:
                    acc.id = int(datetime.now().strftime('%s'))
                if acc.value is None:
                    acc.value = 0

                # force name to be a string
                if not isinstance(acc.name, str):
                    try:
                        acc.name = str(acc.name)
                    except ValueError:
                        acc.name = "Dummy " + datetime.now().strftime('%s')

                # force id to be a int
                if not isinstance(acc.id, int):
                    try:
                        acc.id = int(acc.id)
                    except ValueError:
                        acc.id = int(datetime.now().strftime('%s'))

                # force value to be a float or an int
                if not isinstance(acc.value, int) and not isinstance(acc.value,
                                                                     float):
                    try:
                        acc.value = float(acc.value)
                    except ValueError:
                        acc.value = 0

                attributes = [a for a in dir(acc)
                              if not a.startswith('__')
                              and not a.isupper()
                              and not a == 'transfer']

                # add a filler attribute
                if len(attributes) % 2 == 1:
                    acc.filler = "filler"

                return True
            return False
        except TypeError:
            return False
        except AttributeError:
            return False
