n=1
#AP,
#PA (miss)
n=2
#PP,AP,
#PA,AA (miss)
n=3
#PPP,AAP,APP,PAP
#AAA,APA,PAA,PPA (miss)
n=4
#PPPP,
#PPAP,PAPP,APPP,APAP,AAPP,PAAP,AAAP
#PPAA,APPA,PAPA,PPPA,AAPA,APAA,PAAA (miss)
#AAAA (invalid case)

def number_of_ways_to_attend(days):
    if days<1:
        return 0
    basecase = {1:2,2:4,3:8,4:15}
    if not basecase.get(days):
        basecase[days] = number_of_ways_to_attend(days-1)+\
        number_of_ways_to_attend(days-2)+\
        number_of_ways_to_attend(days-3)+\
        number_of_ways_to_attend(days-4)
    return basecase[days]

def number_of_ways_miss_graduation(days):
    if days<1:
        return 0
    basecase = {1:1,2:2,3:4,4:7}
    if not basecase.get(days):
        basecase[days] = number_of_ways_miss_graduation(days-1)+\
        number_of_ways_miss_graduation(days-2)+\
        number_of_ways_miss_graduation(days-3)+\
        number_of_ways_miss_graduation(days-4)
    return basecase[days]

# print([number_of_ways_to_attend(i) for i in range(11)])
# print([number_of_ways_miss_graduation(i) for i in range(11)])

def execute(days):
    return "for %s days: %s/%s"%(days,number_of_ways_miss_graduation(days),number_of_ways_to_attend(days))


if __name__ == '__main__':
    print(execute(5))
    print(execute(10))
    x = int(input("How many days?"))
    print(execute(x))



