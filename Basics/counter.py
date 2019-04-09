from collections import Counter

text = 'Leasing seems beneficial right now You pay less monthly payments\
You can always increase your lease or buy the car if you like it\
No hassle of reselling it to strangers. Go back to dealer to return it\
Excellent for 3-4 year period for 17500 miles/year\
You get a new car every time you start a new lease\
Best options in December to lease\
The entire difference is $1000 overall in the amount that you save if you buy as opposed to lease but you pay less amount plus you could always make a delayed decision to purchase it during the lease\
Immediate depreciation of car once you buy it\
Cons\
Maintenance costs might be high\
In case of accident, you have to get it properly repaired as opposed if you owned\ it, you\'d have the freedom to do whatever you wanted with it\
Insurance costs inc or dec with new lease?'

word_list = text.split()
# print(word_list)

counter = Counter(word_list).most_common(3)
print(counter)
