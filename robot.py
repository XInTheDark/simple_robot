# Make a simple robot assistant
# Something wrong with make_response
# Still not fixed


def break_up(self):
    self = self.split(' ')
    return self


def make_response(self):
    recognised = False
    get_cmd = False
    database = {
        "hello": "Nice to meet you. What can I do for you?",
        "hi": "Nice to meet you. What can I do for you?",
        "hey": "Nice to meet you. What can I do for you?",
        "goodbye": "Bye. See you next time!",
        "quit": "Bye. See you next time!",
        "exit": "Bye. See you next time!",
        "bye": "Bye. See you next time!",
        "tell joke": """Here's a joke:
How much wood would a woodchuck chuck if a woodchuck could chuck wood?
Answer: As many cookies as Cookie Monster could muster if Cookie Monster could master cooking cookies.""",
        "nice": "Thank you!",
        "great": "Thank you!",
        "excellent": "Thank you!",
        "yeah": "Thank you!",
        "good": "Thank you!",
        "bad": "Sorry I made you upset.",
        "horrible": "Sorry I made you upset.",
        "terrible": "Sorry I made you upset.",
        "hate": "Sorry I made you upset.",
        "lol": "What's funny?",
        "funny": "What's funny?",
        "haha": "What's funny?",
        "tell story": """Okay, here's a story.
Once upon a time...
Okay, I don't remember.""",
        "rap": """I know a bit of how to rap:
Peter Piper picked a peck of pickled peppers
A peck of pickled peppers Peter Piper picked
If Peter Piper picked a peck of pickled peppers
Where’s the peck of pickled peppers Peter Piper picked?

She sells seashells by the seashore,
How can a clam cram in a clean cream can?
Can it can a can as a canner can can a can?""",
        "talk dirty": """I know how to talk dirty:
The carpet needs vacuuming.
Humus. Compost. Pumice. Silt. Gravel.""",
        "translate": "Opening translator...",
        "help": "Say something...",
        "cmd": "Opening cmd..."
    }
    # print(database.get(self))

    self = self.lower()
    # print('words',words)
    for i in database:
        # print(i)
        if i in self:
            recognised = True
            value = database.get(i)
            print(value)

    if self == 'cmd':
        get_cmd = True

    elif self == "bye" or self == "goodbye" or self == "quit" or self == "exit":
        exit()

    elif self == 'access_database':
        print('To access my database, enter the password.')
        password = input('>')
        if password == 'jmz118118':
            print('Database:')
            print(database)
        else:
            print('Invalid password')

    # Translate error
    elif self == "translate":
        print("Translate function is not working. We are fixing this issue.")
#         self = self.replace("translate", "")
#         from PyDictionary import PyDictionary
#         dictionary = PyDictionary()
#         key = input("Enter 'meaning', 'translate', 'antonym', or 'synonym' to get the respective results: ")
#         key = key.lower()
#         if key == 'meaning':
#             print(dictionary.meaning(str(self)))
#         if key == 'translate':
#             print(dictionary.translate(str(self), 'zh'))
#         elif key == 'antonym':
#             print(dictionary.antonym(str(self)))
#         elif key == 'synonym':
#             print(dictionary.synonym(str(self)))
#
#         print("""\nProviders:
# Meanings: WordNet
# Translation: Google Translate
# Synonyms & Antonyms: thesaurus.com""")

    if get_cmd:
        import os
        import sys
        from termcolor import colored

        input_symbol = colored('_', attrs=['reverse', 'blink'])
        file_path = sys.executable
        repeat = True

        while repeat:
            cmd = input(file_path + input_symbol)
            os.system(cmd)
            if cmd == 'exit':
                repeat = False
            break

    if not recognised:
        print("Sorry, I don't understand.")


def robot():
    print('Welcome to robot.py')
    print('What can I do for you?')

    while True:
        query = input('>')
        make_response(query)


robot()

# For Test:
# make_response('hello')
# make_response('cmd')
