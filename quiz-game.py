
# 5. Quiz Game
# Create a basic quiz game that:
# Contains a list of 5–10 questions stored in a dictionary (or list of dicts).
# Asks the user each question and records their answers.
# At the end, displays:
# The user’s score (e.g., 7/10)
# Correct answers for any questions they got wrong
# Skills practiced: loops, dictionaries, input, comparison, counters, print formatting
# The python project group for the fullfillment of the coursework at Datanomics



## Some inputs are ndeed to complete this code

quiz_questions = [
    {
        "question": "Where is the African Union HQ located?",
        "options": ["A) Nairobi", "B) Addis Ababa", "C) Kampala", "D) Acra"],
        "answer": "B"
    },
    {
        "question": "Which country is located in the Eastern part of Ethiopia?",
        "options": ["A) Somalia", "B) Sudan", "C) South Sudan", "D) Eriteria"],
        "answer": "A"
    },
    {
        "question": "Which city is the furthest from Addis Ababa?",
        "options": ["A) Adama", "B) Hawassa", "C) Mekele", "D) Bahir Dar"],
        "answer": "C"
    },
    {
        "question": "Which river flows the longest distance outside Ethiopia?",
        "options": ["A) Awash", "B) Omo", "C) Kebena", "D) Abay"],
        "answer": "A"
    },
    {
        "question": "Which blood groups are the universal donors and universal recipients?",
        "options": ["A) A and O-", "B) O- and AB+", "C) O- and AB-", "D) A and AB+"],
        "answer": "B"
    }
]

# Initialize score and wrong answer tracker
score = 0
wrong = []

# Start the quiz
print("\n Welcome to the Datanomics Quiz Game!\n")

# Ask each question
for q in quiz_questions:
    print(q["question"])
    for opt in q["options"]:
        print(opt)
    
    user = input("Your answer (A/B/C/D): ").strip().upper()

    if user == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print("Wrong.\n")
        wrong.append((q["question"], user, q["answer"]))

# Show final results
print("=" * 10)
print(f" Final Score: {score} out of {len(quiz_questions)}")
print("=" * 10 + "\n")

# Show incorrect answers
if wrong:
    print(" Review of incorrect answers:\n")
    for q_text, user_ans, correct_ans in wrong:
        print(f" {q_text}")
        print(f"Your answer: {user_ans}")
        print(f"Correct answer: {correct_ans}\n")
else:
    print(" Excellent! You got all answers right!\n")

print(" Thank you for playing the Datanomics Quiz!\n")


