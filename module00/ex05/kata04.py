# Put this at the top of your kata04.py file
kata = (0, 4, 132.42222, 10000, 12345.67)

print("module_{0[0]:02}, ex_{0[1]:02} : {0[2]:.2f}, {0[3]:.2e}, {0[4]:.2e}".format(kata))