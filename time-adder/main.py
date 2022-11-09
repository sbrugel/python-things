def main():
    total = 0
    ans = 1
    while ans > 0:
        ans = int(input('Enter a time amount to add (0 or negative # to stop): '))
        if ans > 0:
            total += ans
    print('Total time: ' + min_to_hhmm(total) + '; ' + str(total))

def min_to_hhmm(min):
    hours = int(min / 60)
    mins = min - (hours * 60)
    return str(hours) + 'h' + str(mins) + 'm'

def hhmm_to_min(hhmm):
    hours = 0
    if hhmm.index('h') != -1:
        hours = int(hhmm[0:hhmm.index('h')])
    mins = int(hhmm[hhmm.index('h')+1:hhmm.index('m')])
    return hours*60 + mins

main()