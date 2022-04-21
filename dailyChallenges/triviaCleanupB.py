#!/usr/bin/env python3
"""ECMelander | TLG at Alta3
    learning about html module"""


import html

def main():

    # a trivia output from https://opentdb.com/api_config.php with HTML formatting issues
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

    # establishing variables from the dictionary above
    trivQ = trivia["question"]
    trivCA = html.unescape(trivia["correct_answer"])
    trivIA0 = html.unescape(trivia["incorrect_answers"][0])
    trivIA1 = html.unescape(trivia["incorrect_answers"][1])
    trivIA2 = html.unescape(trivia["incorrect_answers"][2])

    # print the trivia question with multiple choice
    print(f"\n{trivQ}")

    print(f" A. {trivIA0}")
    print(f" B. {trivIA1}")
    print(f" C. {trivCA}")
    print(f" D. {trivIA2}")

    # collect user input
    uAnswer = input("\nWhat is the correct answer? \n A B C or D \n> ")

    # conditional to determine if input is correct
    if uAnswer.upper() == "C":
        print("That is correct!")
    else:
        print("Sorry, the correct answer is C")

main()