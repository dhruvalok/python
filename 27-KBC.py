# questions = [
#     {"question": "What is the capital of India?", 
#      "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
#      "answer": "B",
#      "prize": 1000},
#     {"question": "Which is the largest planet in our solar system?", 
#      "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
#      "answer": "C",
#      "prize": 5000},
#     {"question": "Who wrote the Indian national anthem?", 
#      "options": ["A. Rabindranath Tagore", "B. Bankim Chandra Chattopadhyay", "C. Sarojini Naidu", "D. Mahatma Gandhi"],
#      "answer": "A",
#      "prize": 10000},
#     {"question": "What is the national animal of India?", 
#      "options": ["A. Elephant", "B. Tiger", "C. Lion", "D. Peacock"],
#      "answer": "B",
#      "prize": 20000}
# ]

# winnings = 0

# print("Welcome to KBC - Kaun Banega Crorepati!")
# for i, q in enumerate(questions, start=1):
#     print(f"\nQuestion {i}: {q['question']}")
#     for option in q["options"]:
#         print(option)
    
#     user_answer = input("Your answer (A/B/C/D): ").strip().upper()
    
#     if user_answer == q["answer"]:
#         winnings += q["prize"]
#         print(f"Correct! You have won Rs. {q['prize']}. Total winnings: Rs. {winnings}")
#     else:
#         print("Wrong answer! Game over.")
#         break

# print(f"\nYou are taking home Rs. {winnings}. Thanks for playing KBC!")


questions = [
    ("What is the capital of India?", ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"], "B", 1000),
    ("Which is the largest planet?", ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"], "C", 5000),
    ("Who wrote the Indian national anthem?", ["A. Rabindranath Tagore", "B. Bankim Chandra"], "A", 10000),
    ("What is the national animal of India?", ["A. Elephant", "B. Tiger"], "B", 20000)
]

winnings = 0
print("Welcome to KBC!")

for q, options, answer, prize in questions:
    print(f"\n{q}")
    for option in options:
        print(option)
    
    if input("Your answer: ").strip().upper() == answer:
        winnings += prize
        print(f"Correct! Total winnings: Rs. {winnings}")
    else:
        print("Wrong! Game over.")
        break

print(f"\nYou take home Rs. {winnings}. Thanks for playing!")