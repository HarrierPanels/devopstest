# Credits
"""
@Description: EPAM DevOps Essentials Quizz & Knowledge Check tests
@Version: v1.0
@Credits: Real Python, HarrierPanels
@Website: https://aviasimulator.blogspot.com
@GitHub: https://github.com/HarrierPanels
@Links: https://realpython.com
"""
    
# Global
import pathlib, random, emoji, sys
from string import ascii_lowercase

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

NUM_QUESTIONS_PER_TEST = 30
QUESTIONS_PATH = pathlib.Path(__file__).parent / "questions.toml"
print("\nWelcome to EPAM DevOps Essentials Quizz & Knowledge Check tests!\n")

# Driver
def run_test():
    questions = prepare_questions(
        QUESTIONS_PATH, num_questions=NUM_QUESTIONS_PER_TEST
    )

    num_correct = 0
    for num, question in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        num_correct += ask_question(question)

    #Score    
    def score():
        score = num_correct*100/num
        if num_correct == num:
            return emoji.emojize("[:star::star::star::star::star:] Exellent!")
        elif score >= 70 and score < 100:
            return emoji.emojize("[:star::star::star::star:-] Good!")      
        elif score >= 50 and score < 70:
            return emoji.emojize("[:star::star::star:--] Average!")   
        elif score >= 30 and score < 50:
            return emoji.emojize("[:star::star:---] Poor!")       
        elif score > 0 and score < 30:
            return emoji.emojize("[:star:----] Too bad!")          
        else:
            return emoji.emojize("[-----] Worst ever!")             
   
    print(f"\nYou got {num_correct} correct out of {num} questions.", score())   
    
    # Exit
    while True:
        answer = input("\nDo you want to start over or choose another topic [y/n]: ")
        if answer.lower().startswith("y"):
            print("Ok carry on then.\n")
            run_test()
        elif answer.lower().startswith("n"):
            print("Ok bye!")
            sys.exit()
        else:
            print("Please answer yes(y) or no(n).")
            
# Preprocessing   
def prepare_questions(path, num_questions):
    topic_info = tomllib.loads(path.read_text())
    topics = {
        topic["label"]: topic["questions"] for topic in topic_info.values()
    }
    topic_label = get_answers(
        question="Which topic do you want to take",
        alternatives=topics,
    )[0]
   
    questions = topics[topic_label]
    num_questions = min(num_questions, len(questions))
    return random.sample(questions, k=num_questions)           
   
# Ask questions
def ask_question(question):
    correct_answers = question["answers"]
    alternatives = question["answers"] + question["alternatives"]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answers = get_answers(
        question=question["question"],
        alternatives=ordered_alternatives,
        num_choices=len(correct_answers),
        hint=question.get("hint"),
    )
    if set(answers) == set(correct_answers):
        print(emoji.emojize("Correct! :thumbs_up:"))
        correct = True
    else:
        is_or_are = " is" if len(correct_answers) == 1 else "s are"
        print("\n- ".join([f"No, the answer{is_or_are}:"] + correct_answers))
        correct = False

    if "explanation" in question:
        print(f"\nEXPLANATION:\n{question['explanation']}")

    return 1 if correct else 0

# Get answers
def get_answers(question, alternatives, num_choices=1, hint=None):
    print(f"{question}?")
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    if hint:
        labeled_alternatives["?"] = "Hint"
           
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while True:
        plural_s = "" if num_choices == 1 else f"s (choose {num_choices})"
        answer = input(f"\nChoice{plural_s}? ")
        answers = set(answer.replace(",", " ").split())

        # Handle hints
        if hint and "?" in answers:
            print(f"\nHINT: {hint}")
            continue

        # Handle invalid answers
        if len(answers) != num_choices:
            plural_s = "" if num_choices == 1 else "s, separated by comma or space"
            print(f"Please choose {num_choices} answer{plural_s}")
            continue
            
        # Python 3.6 or older
        invalid = [
            answer for answer in answers if answer not in labeled_alternatives
        ]
        if invalid:
            print(
                f"{invalid[0]} is not a valid choice. "
                f"Please use {', '.join(labeled_alternatives)}"
            )
            continue

        return [labeled_alternatives[answer] for answer in answers]

# Driver call
if __name__ == "__main__":
    run_test()
