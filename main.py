import random

HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# ======כאן יש להוסיף אוסף של מילים=====
words = ["noa", "pyton", "hangman", "java", "pencil", "word"]


# ============כאן יכתבו הפונקציות=============
def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])

    print("Missed letter: " + ','.join(missedLetters))
    print()
    temp=""
    for letter in secretWord:
        if (letter in correctLetters):
            temp+=letter
        else:
            temp+='_'
    print(temp)

def getGuess(alreadyGuessed):
    letter = input("Guess a letter: ")
    # while(True):
    if (letter in alreadyGuessed):
            print("You have already guessed that letter. Choose again...")
            return ""
    elif(not(letter.isalpha()) or len(letter)>1):
            print("invalid input. Choose again...")
            return ""
        # letter=input("Guess a letter: ")
    if (letter not in alreadyGuessed and letter.isalpha() and len(letter) == 1):
            return letter


def playAgain():
    ans = input("Do you want to play again? (yes or no)")
    return ans == "yes"


# ======== כאן תחילת המשחק ============
missedLetters = ""
correctLetters = " "
gameIsDone = False
secretWord = words[random.randint(0, len(words) - 1)]
while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
    # המשתמש מקיש אות ובודקים אם זה תקין

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # בדיקה אם השחקן ניצח
        foundAllLetters = True

        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break

        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # בדיקה האם השחקן הפסיד
        if len(missedLetters)  == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(
                len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    # האם השחקן רוצה לשחק שוב?? 
    # אתחול המשתנים והמשחק מתחדש...
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = words[random.randint(0, len(words) - 1)]
        else:
            break