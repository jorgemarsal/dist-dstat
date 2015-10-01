class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    BHEADER = '\033[1;95m'
    BOKBLUE = '\033[1;94m'
    BOKGREEN = '\033[1;92m'
    BWARNING = '\033[1;93m'
    BFAIL = '\033[1;91m'


def to_green(string, bold=True):
    if bold != True:
        return bcolors.OKGREEN + string + bcolors.ENDC
    return bcolors.BOKGREEN + string + bcolors.ENDC

def to_yellow(string, bold=True):
    if bold != True:
        return bcolors.WARNING + string + bcolors.ENDC
    return bcolors.BWARNING + string + bcolors.ENDC

def to_red(string, bold=True):
    if bold != True:
        return bcolors.FAIL + string + bcolors.ENDC
    return bcolors.BFAIL + string + bcolors.ENDC


def to_blue(string, bold=True):
    if bold != True:
        return bcolors.OKBLUE + string + bcolors.ENDC
    return bcolors.BOKBLUE + string + bcolors.ENDC