import mymodule
line =mymodule.line(15)
# months = ["january", "february", "march", "april", "may", "june" , "july", "august","septemr",\
# "october", "november", "december"]
# print(months[0:-1])
#  QUIZ NO 2>>>
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2018', 'March 20, 2019',
                 'March 9, 2020']


# TODO: Modify this line so it prints the last three elements of the list
eclipse_dates = eclipse_dates[-3:]
print(eclipse_dates)

# QUIZ NO
sentence1 = "I wish to register a complaint."
sentence2 = ["I", "wish", "to", "register", "a", "complaint", "."]

print(line)
print(sentence1[3-1])
sentence2[0:1]= ["we","want"]
print(sentence2[:])
# method
#new_str = "\n".join(["fore", "aft", "starboard", "port"])
new_str = " ".join(["fore", "aft", "starboard", "port"])
print(new_str)

print(len(new_str))
line = mymodule.line(15)
print(line,'\n')
