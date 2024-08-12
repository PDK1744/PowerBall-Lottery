import random

print('''Powerball Lottery

Each powerball lottery ticket cost $2. The jackpot for this game is $1.586 billion! The odds are 1 in 292,201,338.

This simulation gives you thr thrill of playing without wasting real money''')

# Player enters the first five numbers, 1 to 69:
while True:
  print('Enter 5 different numbers from 1-69, with spaces between each number.')
  print('For example: 5 17 23 42 60')
  response = input('> ')
  #Make sure there is 5 numbers
  numbers = response.split()
  if len(numbers) != 5:
    print('Please enter 5 numbers, separated by spaces.')
    continue

  # Convert to Int
  try:
    for i in range(5):
      numbers[i] = int(numbers[i])
  except:
    print('Please enter 5 numbers, separated by spaces.')

    continue

  # Make sure numbers are between 1 and 69
  for i in numbers:
    if not (1 <= i <+ 69):
      print('The numbers must be between 1 and 69.')
      continue 

  # Check for duplicates
  # Create a set from numbers to remove duplicates
  if len(set(numbers)) != 5:
    print('You must enter 5 different numbers.')
    continue

  break 

  ######################

  # Player input Powerball number
  while True:
    print('Enter a number from 1-26.')
    response = input('> ')
    
  # Convert to Int
  try:
    powerBall = int(respones)
  except:
    print('Please enter a number. Between 1 to 26')
    continue
  # Check num is between 1 and 26
  if not (1 <= powerBall <= 26):
    print('Powerball number must be between 1 and 26.')
    continue 

  break 

  # Get number of plays
  while True:
    print('How many times would you like to play? (Max: 100000)')
    response('> ')
  # Convert to int
  try:
    numPlays = int(response)
  except:
    print('Please enter a number.')
    continue 
  # Check num is between 1 - 100,000
  if not (1 <= numPlays <= 100000):
    print('You can play 1 to 100,000 times.')
    continue
    
  break 

  # Run the Sim
price = '$' + str(numPlays * 2)
print('It cost', price, 'to play', numPlays, 'times.')
input('Press enter to start...')

possibleNumbers = list(range(1, 70))
for i in range(numPlays):
  #Come up with winning numbers
  random.shuffle(possibleNumbers)
  winningNumbers = possibleNumbers[0:5]
  winningPowerball = random.randint(1, 26)
  #Display Winning Numbers
  print('The winning numbers are: ')
  allWinningNums = ''
  for num in winningNumbers:
    allWinningNums += str(num) + ' '
  print(allWinningNums.ljust(21), end='')

  #Compare numbers
  if (set(numbers) == set(winningNumbers) and powerBall == winningPowerball):
    print()
    print('You won the jackpot!')
    break 
  else:
    print(' You lost.')
print('You have wasted', price)
print('Thanks for playing!')
