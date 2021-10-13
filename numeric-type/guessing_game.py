import random

def get_base():
    bases = (2, 10, 16)
    base = int(input("What base do you wanna use (2, 10, 16): "))
    
    if base not in bases:
        raise AttributeError("Invalid base!")
    
    return base

def convert_number_base(number: int, base: int):
    bases_methods = {
        2: bin, 
        10: int, 
        16: hex
    }
    return bases_methods[base](number)

def guessing_game():
    answer = random.randint(0, 100)
    base = get_base()
    
    answer = convert_number_base(answer, base)
    
    counter = 3
    while counter := counter - 1:
        number = int(input("\nGuess the correct number: "))
        number = convert_number_base(number, base)
        
        if number == answer:
            print("Just right")
            return
        
        if number > answer:
            print("Too high")
        else:
            print("Too low")
        
    msg: str = "Not guessed in time"
    print(f"{msg:*>25}")

def guess_word():
    words = {
        1: "hola",
        2: "como",
        3: "adios",
        4: "why",
        5: "bye",
        6: 'pera',
        7: 'linux',
        8: 'ball',
        9: 'bola',
    }
    counter = 3
    while True:
        answer = random.choice(list(words.values()))
        word = input(f"Guess the word. Start with '{answer[0]}': ")
        
        if word == answer:
            print("Just right!")
            return
        
        if not counter:
            break
        else:
            print("Try again!\n")
        
        counter -= 1
    
    print("No in time.")
        
    
if __name__ == '__main__':
    guess_word()
    