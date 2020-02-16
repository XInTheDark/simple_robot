# Make a simple robot assistant


def break_up(self):
    self = self.split(' ')
    return self


def make_response(self):
    global recognised, get_cmd
    import os
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
        "joke": """Here's a joke:
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
        "story": """Okay, here's a story.
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
        "dirty": """I know how to talk dirty:
The carpet needs vacuuming.
Humus. Compost. Pumice. Silt. Gravel.""",
        "translate": "Opening translator..."
    }
    # print(database.get(self))

    words = break_up(self)
    # print('words',words)
    for i in words:
        i = i.lower()
        # print(i)
        if i == 'cmd':
            get_cmd = True
        else:
            get_cmd = False

        if i in database:
            recognised = True
            value = database.get(i)
            print(value)
        else:
            if not recognised:
                recognised = False

        if i == "bye" or i == "goodbye" or i == "quit" or i == "exit":
            exit()

        # Translate error
        if i == "translate":
            words.remove(i)
            from PyDictionary import PyDictionary
            dictionary = PyDictionary()
            key = input("Enter 'meaning', 'translate', 'antonym', or 'synonym' to get the respective results: ")
            key = key.lower()
            if key == 'meaning':
                print(dictionary.meaning(str(words)))
            elif key == 'translate':
                print(dictionary.translate(str(words), 'zh'))
            elif key == 'antonym':
                print(dictionary.antonym(str(words)))
            elif key == 'synonym':
                print(dictionary.synonym(str(words)))
            else:
                print('Invalid!')
            print("""\nProviders:
Meanings: WordNet
Translation: Google Translate
Synonyms & Antonyms: thesaurus.com""")

    if get_cmd:
        import os
        import sys
        import time
        from termcolor import colored

        print('Opening cmd...')
        time.sleep(2)
        input_symbol = colored('_', attrs=['reverse', 'blink'])
        file_path = sys.executable
        repeat = True

        while repeat:
            time.sleep(1)
            cmd = input(file_path + input_symbol)
            os.system(cmd)
            if cmd == 'exit':
                repeat = False
            break

    if not recognised:
        print("Sorry, I don't understand.")

    return get_cmd


def robot():
    print('Welcome to robot.py')
    print('What can I do for you?')
    while True:
        query = input('>')
        make_response(query)

    # For Test:
    # print(make_response('hello'))
