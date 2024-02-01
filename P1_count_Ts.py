# This program counts the number of times
# the letter T (uppercase or lowercase)
# appears in a string

def main():
  # create a variable to hold the count
  # The variable must start at 0
  count = 0
  
  # Get a string from user
  my_string = input('Enter a sentence: ')
  
  # Count the T's
  for ch in my_string:
    if ch == 'T' or ch == 't':
      count += 1
  
  # print the result
  print(f'The letter T appears {count} times.')
  
# call main function
if __name__ == '__main__':
  main()