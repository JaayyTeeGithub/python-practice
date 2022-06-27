def solve(k, bulbs):
    """
    O is off. X is on. If bulb is switched off the bulb to the right is switched. First bulb is switched k times.
    :param k: times to be switched
    :param bulbs: string of bulbs
    :return: string of bulbs
    """

    bulb_string = bulbs
    switches = k
    new_bulbs = ''
    while switches > 0:  # execute operations k times
        changed_bulbs = ''
        for index in range(0, len(bulb_string)):  # iterate over bulbs
            if bulb_string[index] == 'X':  # if on
                changed_bulbs = changed_bulbs + 'O'  # change to off
                new_bulbs = changed_bulbs + bulb_string[index + 1: len(bulb_string)]  # concat changed and remaining
            elif bulb_string[index] == 'O':  # if off
                changed_bulbs = changed_bulbs + 'X'  # add X to changed bulbs
                new_bulbs = changed_bulbs + bulb_string[index + 1: len(bulb_string)]  # add changed to remaining bulbs
                switches = switches - 1  # switch done, bulb to right not being changed, switches decreased
                break  # leave for loop
        bulb_string = new_bulbs  # set bulb str to new bulb str
    return bulb_string


bulbs = 'XOXO'
# OXXO
# XXXO
print(solve(2, bulbs))

