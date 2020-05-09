# Write your make_spoonerism function here:
def make_spoonerism(word1, word2):
  a = word1[0]
  b = word2[0]
 
  c = word1[0].replace(a,b) + word1[1:]
  d = word2[0].replace(b,a) + word2[1:]
  e = c + ' ' + d
  return e

# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a


# OR
# OR


# # Write your make_spoonerism function here:
# def make_spoonerism(word1, word2):
#   return word2[0]+word1[1:]+" "+word1[0]+word2[1:]

# # Uncomment these function calls to test your tip function:
# print(make_spoonerism("Codecademy", "Learn"))
# # should print Lodecademy Cearn
# print(make_spoonerism("Hello", "world!"))
# # should print wello Horld!
# print(make_spoonerism("a", "b"))
# # should print b a
