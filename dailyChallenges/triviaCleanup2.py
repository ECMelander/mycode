#!/usr/bin/env python3

import html

trivia= {
        "category": "Entertainment: Film",
        "type": "multiple",
        "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
        "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
        "incorrect_answers": [
            "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
            "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
            "&quot;Round up the usual suspects.&quot;"
        ]
    }

trivQ = trivia["question"]
trivCA = html.unescape(trivia["correct_answer"])
trivIA0 = html.unescape(trivia["incorrect_answers"][0])
trivIA1 = html.unescape(trivia["incorrect_answers"][1])
trivIA2 = html.unescape(trivia["incorrect_answers"][2])
# theAnswer = "C"

print(trivQ)

print(f"A. {trivIA0}")
print(f"B. {trivIA1}")
print(f"C. {trivCA}")
print(f"D. {trivIA2}")

uAnswer = input("What is the correct answer? \n A B C or D \n> ")

if uAnswer.upper() == "C":
    print("That is correct!")
else:
    print("Sorry, the correct answer is C)"
