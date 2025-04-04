def main():
    # for the beginning of the sentence
 SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my"

 # Prompt the user for input
 adjective : str = input("Please type an adjective and press enter: ")
 noun : str = input("Please type a noun and press enter: ")
 verb : str = input("Please type a verb and press enter: ")

 # Create the full sentence using the inputs
 sentence = f"{SENTENCE_START} {adjective} {noun} {verb}!"

 # Print the final sentence
 print(sentence)



if __name__ == '__main__':
    main()