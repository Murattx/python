names = ["David", "Michael", "John", "James", "Greg", "Mark", "William", "Richard", "Thomas", "Steven",

   "Mary", "Susan", "Maria", "Karen", "Lisa", "Linda", "Donna", "Patricia", "Debra", "Eric"]

scores = [99, 87, 78, 86, 68, 94, 76, 97, 56, 98, 76, 87, 79, 90, 73, 93, 82, 69, 97, 98]

scores.sort()

scores.reverse()

maxNumValue=scores[0]

print("Maximum Score is :" ,maxNumValue)

print("NUmbe rof students got that sore is: ", scores.count(maxNumValue))
