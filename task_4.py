_journal_dict = {}

def save(question, count):
    _journal_dict[question] = count

def function(question, right_answers_list, n):
    print(f'Here is the question: {question}')
    for i in range(n):
        guess = input('Enter your guess: ').lower()
        if guess not in right_answers_list:
            continue
        else:
            save(question, i + 1)
            break
    if question not in _journal_dict.keys():
        save(question, 0)
    return _journal_dict


def log(question):
    return f"Загадка {question} отгадана с {_journal_dict[question]} попытки"


#if __name__ == "__main__":
#    print(function("2 + 3", ["5", "3 + 2", "4 + 1"], 2))
function("2+2=", ['5', '4+1'], 2)
function('3+5=', ['8', '4+4'], 3)
print(log('2+2='))
