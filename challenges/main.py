def multiplication_table(number, limit):
    table = []
    # TODO: use a for loop to build a list of number * 1 through number * limit
    for i in range (1, limit +1):
       
        table.append (number *i)
    return table