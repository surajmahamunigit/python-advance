######################### slice operator  ###################

# s[begin:end:step]

s='abcdefghijk'

# S  = a  b  c  d  e  f  g  h  i  j  k
#      0  1  2  3  4  5  6  7  8  9  10

print(s[:])  # abcdefghijk --> whole string

print(s[2:7])  # cdefg  --> from 2nd index to 6th index

print(s[2:7:2])  # ceg --> 2,4,6th index

print(s[2:7:3])  # cf --> 2nd and 5th index

## Examples

s='abcdefghijk'

#    -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
# S  = a  b  c  d  e  f  g  h  i  j  k
#      0  1  2  3  4  5  6  7  8  9  10

print("step examples: ")

print(len(s))  # 11


# case 1:
print()
print("Case 1")

print(s[1:6:2])  # forward direction --> begin=1, end=6 --> substring of index 1 to 5 --> bdf

print(s[::1])  # forward direction --> begin=0, end =len(s)=11 --> substring of index 0 to len-1 (0-10) --> abcdefghijk

print(s[::-1])  # backward direction  --> begin=-1, end=-(len+1)=12 --> substring from -1 to -12 --> kjihgfedcba

print(s[3:7:-1])  # backward direction  --> begin=3, end=8 --> we can go forward from 3 to 8, not backward. so, empty string --> ''


# case 2:
print()
print("Case 2")

print(s[7:4:-1]) # backward direction --> begin=7, end=5 --> hgf

print(s[0:10000:1]) # forward direction -->begin=0, end=999 --> abcdefghijk  --> No IndexError (slice never raises IndexError)

print(s[-4:1:-1])  # backward direction --> begin=-4, end=2 --> hgfedc

print(s[-4:1:-2]) # backward direction --> begin=-, end=2 --> hfd

print(s[5:0:1]) # end=0 --> empty string

#print(s[9:0:0]) # slice step cant be 0 --> ValueError


# case 3:
print()
print("Case 3")

print(s[0:-10:-1]) # backward direction --> begin=0,end=-9 --> empty string

print(s[0:-12:-1]) # backward direction --> begin=0,end=-10 --> a

print(s[0:0:1]) # end=0 --> empty string

print(s[0:-9:-2]) # backward direction --> begin=0,end=-8 --> empty string


# case 4:
print()
print("Case 4")

print(s[-5:-9:-2]) # backward direction --> begin=-5,end=-8 --> gfed

print(s[10:-1:-1]) # end=0 --> empty string ''

print(s[1000:2:-1]) # backward direction --> begin=1000, end=3 --> kjihgfed


