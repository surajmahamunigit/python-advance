#split(operator) is used to split given string based on operator/delimiter and returns list as output

#seprator.join(): it joins the given operator based on the separator you specified

s1="Apple software Inc"

#split()
split_s1=s1.split()  # no operator, considers space as input

#input: split_s1 = ["Apple","Software","Inc"]
#join()
print("output: ", " ".join(split_s1) )

s2="02-01-2026"
split_s2=s2.split("-") # ["02","01,"2026"]

#join
# input: ["02","01","2026"]
print("Output:", " ".join(split_s2) )  # output: 02 01 2026