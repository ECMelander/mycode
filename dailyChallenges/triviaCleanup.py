#!/usr/bin/env python3
"""ECMelander | TLG at Alta3
    learning about html module
    simply cleaning up text, for basic game format see triviaCleanupb.py"""

def main() :
    import html

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

    trivQ = trivia["question"]
    trivCA = html.unescape(trivia["correct_answer"])
    trivIA0 = html.unescape(trivia["incorrect_answers"][0])
    trivIA1 = html.unescape(trivia["incorrect_answers"][1])
    trivIA2 = html.unescape(trivia["incorrect_answers"][2])

    print(trivQ)
    print(trivCA)
    print(trivIA0)
    print(trivIA1)
    print(trivIA2)

main()