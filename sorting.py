def bubble(items):
    swap = True
    while swap:
        swapped = False
        for i in range(len(items)):
            if i > 0:
                if items[i] < items[i - 1]:
                    temp = items[i - 1]
                    items[i - 1] = items[i]
                    items[i] = temp
                    swapped = True
        if swapped == False:
            swap = False      
    return(items)