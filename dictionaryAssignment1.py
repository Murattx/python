days={"1":"Monday","2":"Tuesday","3":"Wednesday","4":"Thursday","5":"Friday","6":"Saturday","7":"Sunday"}

remove_days=input("Please enter day numbers to remove: ")

if len(remove_days)==2:
        dayOne=days.pop(remove_days[0])
        print (dayOne," will be removed")

        dayTwo=days.pop(remove_days[1])
        print (dayTwo," will be removed")

        print("Remaining days are:",days.values())
else:
    print("Please enter 2 days")
