def verbing(str_input):
    if len(str_input) >= 3:
        if len(str_input) - str_input.rfind('ing') == 3:
            str_res = str_input + 'ly'
        else:
            str_res = str_input + 'ing'
    else:
        str_res = str_input
    return str_res


def not_bad(str_input):
    occur_not = str_input.find('not')
    occur_bad = str_input.find('bad')
    if occur_not == -1 or occur_bad == -1 or occur_bad < occur_not:
        str_res = str_input
    else:
        str_res = str_input[0:occur_not] + 'good' + str_input[occur_bad + 3:]
    return str_res
