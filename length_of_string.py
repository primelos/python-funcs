# Write your x_length_words function here:
def x_length_words(sentence, x):
  a = sentence.split(' ')
  # print(a)
  for i in a:
    # print(len(i))
    if len(i) >= x:
      return True
    else:
      return False
      
# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True