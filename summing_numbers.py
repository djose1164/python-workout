def mysum(numbers: list, start:int = 0):
    output = 0
    for i in numbers:
        output += i

    return output + start

def average(numbers: list):
    return mysum(numbers) / len(numbers)

def count_string(strings: list):
    """Write a function that takes a list of words (strings). It should return 
    a tuple containing three integers, representing the length of the shortest 
    word, the length of the longest word, and the average word length
    """
    longest = len(strings[0])
    shortest = len(strings[1]) if len(strings[1]) < len(strings[0]) \
                               else len(strings[0])
    for string in strings:
        if len(string) > longest:
            longest = len(string) 
        elif len(string) < shortest:
            shortest = len(string)
    
    mean = average([shortest, longest])
    return (shortest, longest, mean)

def sum_whaterver(args: list):
    """Write a function that takes a list of Python objects. Sum the objects that 
    either are integers or can be turned into integers, ignoring the others. 
    """
    so_far = 0
    for current in args:
        try:
            so_far += int(current)
        except:
            continue

    return so_far
print(sum_whaterver(["hola", "e", 2, 34.2, '23', 'hola']))