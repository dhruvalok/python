questions = [
    ("What is the capital of India?", ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"], "B", 1000),
    ("Which is the largest planet?", ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"], "C", 5000),
    ("Who wrote the Indian national anthem?", ["A. Rabindranath Tagore", "B. Bankim Chandra", "C. Neha Rani", "D. Baba Alok"], "D", 10000),
    ("What is the national animal of India?", ["A. Elephant", "B. Tiger", "C. lion", "D. Monkey"], "B", 20000)
]

winnings = 0
print("Welcome to KBC!")

for ques, options, answer, prize in questions:
    print(f"\n{ques}")
    for option in options:
        print(option)
    
    if input("Your answer: ").strip().upper() == answer:
        winnings += prize
        print(f"Sahi Jabab! Aap jeet gaye hain: Rs. {winnings}")
    else:
        print("Galat jabab, Chaliye khel ko yahi samapt karte hain.")
        break

print(f"\nYou take home Rs. {winnings}. Thanks for playing!")