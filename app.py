"""
This module handles task data provided by a user, processes the input, 
saves it to a file, and analyzes the tasks to answer a preset question.
"""

from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chat_models import ChatOpenAI

def is_number(num_str):
    """
    Check if the provided string can be converted to an integer.
    
    Parameters:
    num_str (str): The string to be checked.
    
    Returns:
    bool: True if the string can be converted to an integer, False otherwise.
    """
    try:
        int(num_str)
        return True
    except ValueError:
        return False

def analyze_text():
    """
    Load a text document, create an index for it, and use this index 
    to answer a pre-defined question.
    """
    # Specify the LLM
    llm = ChatOpenAI(temperature=0.5)

    # Document loader
    loader = TextLoader("data.txt")
    # Index that wraps above steps
    index = VectorstoreIndexCreator().from_loaders([loader])
    # Question-answering
    question = "Can you help me draft some key milestones for being able to complete each large task?"

    answer = index.query(question, llm=llm)

    print(answer)

def collect_data():
    """
    Collect a number of tasks from the user, save them to a text file, 
    and call analyze_text() to process and analyze the tasks.
    """
    # Prompt the user to enter some text
    num_str = input("Hello how many tasks do you have to complete today? ")
    if is_number(num_str):
        print("Thank you, please enter your tasks below:")

        num_times = int(num_str)

        for i in range(num_times):

            text = input(f"Please enter a task {i}: ")
            # Open the file in write mode ('w')
            with open("data.txt", "a", encoding='utf-8') as file:
                # Write the text to the file
                file.write(f"Task {i}: " + text + "\n")
                # Close the connection to the file
        print("Thank you, your tasks have been saved, please wait while we analyze your tasks...")
        analyze_text()
    else:
        print("You did not enter a number")

def main():
    """
    Main entry point of the application.
    """
    collect_data()


if __name__ == "__main__":
    main()
