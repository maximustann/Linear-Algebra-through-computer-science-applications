from politics_lab import create_voting_dict
from politics_lab import most_similar
from politics_lab import policy_compare
from politics_lab import least_similar

f = open("./US_Senate_voting_data_109.txt", mode = 'r')
mylist = list(f)
l = [word for word in mylist]
vd = create_voting_dict(l)
print(most_similar('Chafee', vd))
print(least_similar('Santorum', vd))
