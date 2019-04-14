def main():

    # This file is just to create my list of questions and I will start with one question
    #and then it will be dynamically updated by the user

    import json
    dict = {1: {"what is good instrument": "flute"}}

    with open('my_dict.json', 'w') as f:
        json.dump(dict, f)


main()