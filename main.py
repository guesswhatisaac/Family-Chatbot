# INSTALL PYSWIP: pip install git+https://github.com/yuce/pyswip@master#egg=pyswip
# C:\Users\risaa\Documents\GitHub\Chatbot_MCO2

import process as prcs

def main():

    prompt = ''

    while prompt != "terminate":
        prompt = input("[ ] : ")
        print()
        prcs.process_prompt(prompt)


if __name__ == "__main__":
    main()