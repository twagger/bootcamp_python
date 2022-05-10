from the_bank import Account, Bank


if __name__ == "__main__":
    bank = Bank()
    acc_valid_1 = Account('Sherlock Holmes',
                          zip='NW1 6XE',
                          addr='221B Baker street',
                          info="great detective!",
                          value=1000000.0)
    acc_valid_2 = Account('James Watson',
                          zip='NW1 6XE',
                          addr='221B Baker street',
                          value=25000.0,
                          info=None)
    acc_invalid_1 = Account("Adam",
                            value=42,
                            zip='0',
                            addr='Somewhere')
    acc_invalid_2 = Account("Bender Bending Rodríguez",
                            zip='1',
                            addr='Mexico',
                            value=42,
                            binfo='bite my shiny little ass')
    acc_invalid_3 = Account("Charlotte",
                            info='Somewhere in the Milky Way',
                            value=42)
    acc_invalid_4 = Account("Douglass",
                            zip='42',
                            addr='boulevard bessieres',
                            value=42,
                            info="")
    acc_invalid_5 = Account("Edouard",
                            zip='3',
                            value=55)

    bank.add(acc_valid_1)
    bank.add(acc_valid_2)
    bank.add(acc_invalid_1)
    bank.add(acc_invalid_2)
    bank.add(acc_invalid_3)
    bank.add(acc_invalid_4)
    bank.add(acc_invalid_5)

    print("# 1. Non existing accounts")
    if bank.transfer('William John', 'Smith Jane', 1000.0) is False:
        print('Failed')
        bank.fix_account('William John')
        bank.fix_account('Smith Jane')
    
    if bank.transfer('William John', 'Smith Jane', 1000.0) is False:
        print('Failed')
    else:
        print('Success')

    print("# 2. Account with an even number of attributes")
    if bank.transfer('Sherlock Holmes', 'Adam', 1000.0) is False:
        print('Failed')
        bank.fix_account('Adam')
    
    if bank.transfer('Sherlock Holmes', 'Adam', 1000.0) is False:
        print('Failed')
    else:
        print('Success')

    print("# 3. Account with an attribute starting with a b")
    if bank.transfer('Sherlock Holmes', 'Bender Bending Rodríguez', 1000.0) is False:
        print('Failed')
        bank.fix_account('Bender Bending Rodríguez')
    
    if bank.transfer('Sherlock Holmes', 'Bender Bending Rodríguez', 1000.0) is False:
        print('Failed')
    else:
        print('Success')

    print("# 4. Account with no zip or addr")
    if bank.transfer('Sherlock Holmes', 'Charlotte', 1000.0) is False:
        print('Failed')
        bank.fix_account('Charlotte')
    
    if bank.transfer('Sherlock Holmes', 'Charlotte', 1000.0) is False:
        print('Failed')
    else:
        print('Success')

    print("# 5. Account with no name, id or value")
    next(a for a in bank.accounts if a.name == "Douglass").value = None
    next(a for a in bank.accounts if a.name == "Douglass").id = None
    if bank.transfer('Sherlock Holmes', 'Douglass', 1000.0) is False:
        print('Failed')
        bank.fix_account('Douglass')
    
    if bank.transfer('Sherlock Holmes', 'Douglass', 1000.0) is False:
        print('Failed')
    else:
        print('Success')

    print("# 6. Account with wrong types for name, id or value")
    next(a for a in bank.accounts if a.name == "Edouard").id = "42"
    next(a for a in bank.accounts if a.name == "Edouard").value = "42"
    if bank.transfer('Sherlock Holmes', 'Edouard', 1000.0) is False:
        print('Failed')
        bank.fix_account('Edouard')
    
    if bank.transfer('Sherlock Holmes', 'Edouard', 1000.0) is False:
        print('Failed')
    else:
        print('Success')
