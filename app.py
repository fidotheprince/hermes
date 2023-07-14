from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
# Document loader
loader = TextLoader("data.txt")
# Index that wraps above steps
index = VectorstoreIndexCreator().from_loaders([loader])
# Question-answering
question = "What's the most time effective way to complete each of the tasks in the data.txt file?"

answer = index.query(question)

print(answer)


