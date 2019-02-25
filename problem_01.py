def problem_01(list_x, int_y):
    """
    Write a function that:
    takes a list x and an int y as input
    returns a new list that is made of every y element of list x
    example: list_x = [1,2,3,4,5,6,7,8,9] int_y = 2 return [2,4,6,8] 
    """
    list_r = []
    for i in range(0,len(list_x)):
        if ((i + 1) % int_y) == 0:
            list_r.append(list_x[i])
    return list_r
