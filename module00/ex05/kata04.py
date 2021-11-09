t = ( 0, 4, 132.42222, 10000, 12345.67)
result = "day_" + str(t[0]).zfill(2) + ", "
result += "ex_" + str(t[1]).zfill(2) + " : "
result += "{:.2f}".format(t[2]) + ", "
result += "{:.2e}".format(t[3]) + ", "
result += "{:.2e}".format(t[4])
print(result)