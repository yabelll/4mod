#O(N ** 2)
#def strcounter(s):
#    for sy in set (s):
#        count = 0
#        for sub_sy in s:
#            if sy == sub_sy:
#                count += 1
#        print(f'{sy} - {count}')
    
#strcounter('advfs')

#O(N)
#def strcounter(s):
#    for sym in set(s):
#        count = 0
#        print(f'{sym} - {s.count(sym)}')

#strcounter('zzzzz')

def strcounter(s):
    for sym in set(s):
        count = 0
        print(f'{sym} - {s.count(sym)}')

strcounter('zzzzz')