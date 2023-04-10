import random


def read_answers(filename):
    """
    Reads the answers from a file and returns them as a list.

    :param filename: string
    :return: list of answers
    """
    try:
        with open(filename, 'r') as f:
            answers = f.readlines()
            f.close()
        return answers
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return []


def display_question(question_num, question):
    """
    display the question , if option not None so the question is multiple choice so must display options else just
    display the answer
    :param question_num:
    :param question:
    """
    # print the question
    print(f"{question_num}. {question['question']}")
    if question['options']:
        for option in question['options']:
            print(f"\t{option}")


def store_quastion_information_in_dictionary(line, answer):
    """
    checks if the answer is 'T' or 'F' to determine if the question is true/false, or else it splits the line by ';'
    to get the question and options and add the questions to questions dictionary.
    :param line: string
    :param answer: char
    """
    if answer.lower() == 'T'.lower() or answer.lower() == 'F'.lower():
        questions[len(questions) + 1] = {"type": "true/false", "question": line, 'options': None,
                                         "answer": answer}
    else:
        question_parts = line.strip().split(';')
        question = question_parts[0]
        options = question_parts[1:]
        questions[len(questions) + 1] = {"type": "multiple choice", 'question': question, 'options': options,
                                         "answer": answer}


def read_questions():
    """
    Reads in questions and answers from files and stores them in a dictionary.

    Returns:
    None.
    """
    try:
        multiple_choice_answers = read_answers("MCA.txt")
        true_or_false_answers = read_answers("TorFA.txt")
        with open("questions.txt") as f:
            flag = False
            for line in f:
                if line.strip() == "multiple choice questions:":
                    # i is index to put the answer in dictionary
                    i = 0
                    flag = True
                    continue
                if flag:
                    store_quastion_information_in_dictionary(line, multiple_choice_answers[i].strip())

                    i += 1

                else:
                    if line.strip() == "True or false questions:":
                        # i is index to put the answer in dictionary , this is to be sure its zero
                        i = 0
                        continue
                    store_quastion_information_in_dictionary(line, true_or_false_answers[i].strip())
                    i += 1
    except FileNotFoundError:
        print("The file doesn't exist.")
    except Exception as e:
        print("An error occurred:", e)


def generate_quiz():
    """
    Generates a quiz by selecting all questions from the questions dictionary in a random order.
    Asks the user to answer each question and keeps track of the score.
    """
    score = 0
    # randomly select all question (i select all to make sure no duplicate question asked)
    question_numbers = random.sample(list(questions.keys()), len(questions))

    # print the selected questions
    for i, number in enumerate(question_numbers):
        question = questions[number]
        display_question(i + 1, question)
        user_answer = input("Enter Your Answer: \n")
        if user_answer.lower() == questions[number]["answer"].lower():
            score += 1
            print("Correct")
        else:
            print("Incorrect")
        print(f"Your score is {score} from {len(questions)}")
    score_and_write_to_file(score)


def score_and_write_to_file(score):
    """
    write the score to file
    :param score: int
    """
    try:
        with open("score.txt", 'w') as f:
            f.write(str(score))
    except FileNotFoundError:
        print("The file doesn't exist.")
    except Exception as e:
        print("An error occurred:", e)


def main():
    """
    run the program
    """
    read_questions()
    generate_quiz()


if __name__ == '__main__':
    questions = {}
    main()
