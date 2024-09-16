questions = (
    "What’s the smallest country in the world?",
    "What’s the capital of Canada?",
    "Name the longest river in the world?",
    "How many days does it take for the Earth to orbit the Sun?",
    "How many bones are in the human body?",
    "Hau many elements are un the periodic table?",
)
 
options = (
    ("A. Vatican", "B. Luxemburg", "C. Belgia", "D. India"),
    ("A. Montreal", "B. Vancouver", "C. Toronto", "D. Ottawa"),
    ("A. Nil", "B. Amazon", "C. Nipru", "D. Volga"),
    ("A. 364", "B. 367", "C. 365", "D. 366"),
    ("A. 204", "B. 205 ", "C. 207", "D. 203"),
    ("A. 116", "B. 117", "C. 118", "D. 119"),
)
 
answers = ("A", "D", "A", "C", "B", "C")
 
 
guesses = []
score = 0
question_number = 0
 
 
for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_number]:
        print(option)
 
    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_number]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_number]} is the correct answer.")
    question_number += 1
 
 
print("----------------------")
print("       RESULTS        ")
print("----------------------")
 
print("Answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()
 
print("Guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()
 
score = int(score / len(questions) * 100)
print(f"Your score is {score}%")