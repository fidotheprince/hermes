from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

# a method that checks if the user has entered a number
def is_number(num_str):
    try:
        int(num_str)
        return True
    except ValueError:
        return False

# a method that analyzes the text derived from the user
def analyze_text():
    # Document loader
    loader = TextLoader("data.txt")
    # Index that wraps above steps
    index = VectorstoreIndexCreator().from_loaders([loader])
    # Question-answering
    question = "What's the most time effective way to complete each of the tasks in the data.txt file?"

    answer = index.query(question)

    print(answer)

# a method that collects the data from the user and implements the above methods
def collect_data():
    # Prompt the user to enter some text
    num_str = input("Hello how many tasks do you have to complete today? ")
    
    if is_number(num_str):
        
        print("Thank you, please enter your tasks below:")

        num_times = int(num_str)

        for i in range(num_times):

            text = input(f"Please enter a task {i}: ")
            # Open the file in write mode ('w')
            with open("data.txt", "a") as file:
                # Write the text to the file
                file.write(f"Task {i}: " + text + "\n")
                # Close the connection to the file
        
        print("Thank you, your tasks have been saved, please wait while we analyze your tasks...")
        analyze_text()
    else:
        print("You did not enter a number")



def main():
    collect_data()


main()