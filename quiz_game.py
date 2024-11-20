# A Quiz Game

questions = (
    ("What is the capital of India?"),
    ("Which animal gives the biggest egg?"),
    ("What is the largest planet in our solar system?"),
    ("What is the formula of glucose?"),
)

options = (
    ("A.Delhi", "B.Mumbai", "C.Kolkata", "D.Chennai"),
    ("A.Dog", "B.Hen", "C.Elephant", "D.Ostrich"),
    ("A.Venus", "B.Mars", "C.Jupiter", "D.Saturn"),
    ("A.C6H12O6", "B.C12H22O11", "C.C6H10O5", "D.CH2cl2"),
)

score = 0
answers = ["A", "D", "C", "A"]  # in this we are going to keep correct answers
answeredByUser = []  # in this we are going to store the answers User given

for question, option in zip(questions, options):
    print(question)
    for opt in option:
        print(opt, end=" ")
    print()
    answer = input("Enter your answer: ").upper()
    answeredByUser.append(answer)
    # checking if the answer is correct or not
    if answer == answers[questions.index(question)]:
        score += 1
        print("Correct answer😎")
    else:
        print("Wrong answer😓")

print("---------Result----------")
print("Your score is: ", score)

