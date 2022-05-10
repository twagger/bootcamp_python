import attr


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
        self.value += amount


def iscorrupted(account):
    try:
        attributes = [attr for attr in dir(account)
                      if not attr.startswith('__') and not attr.isupper()]
        if len(attributes) % 2 != 0:
            return True
        if any(a for a in attributes if a.startswith('b')):
            return True
        if not any(a for a in attributes if a.startswith('zip') or a.startswith('addr')):
            return True
        if not all(a in attributes for a in ['name', 'id', 'value']):
            return True
        if not isinstance(account.name, str):
            return True
        if not isinstance(account.id, int):
            return True
        if not isinstance(account.value, int) and not isinstance(account.value, float):
            return True
        return False
    except TypeError:
        raise TypeError("An Account is expected.")


class Bank(object):
    """The bank"""

    def __init__(self):
        self.accounts = []

    def add(self, new_account):
        """ Add new_account in the Bank
            @new_account: Account() new account to append
            @return       True if success, False if an error occured
        """
        if not isinstance(new_account, Account):
            return (False)
        try:
            self.accounts.append(new_account)
        except IndexError:
            return (False)
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
            if origin_acc is not None and dest_acc is not None:
                if origin_acc.value >= 0 and origin_acc.value >= amount:
                    if iscorrupted(origin_acc) or iscorrupted(dest_acc):
                        return False
                    elif origin != dest:
                        origin_acc.value -= amount
                        dest_acc.value += amount
                    return True
            return False
        except TypeError:
            return False

    def fix_account(self, name):
        """ fix account associated to name if corrupted
            @name:  str(name) of the account
            @return True if success, False if an error occured
        """
        # ... Your code ...