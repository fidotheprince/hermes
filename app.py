from langchain.llms import OpenAI

#access openai api and select model
llm = OpenAI(temperature=0.9, model_name="ada")

#collects generated tex
resp = llm.predict("I like to eat")

print(resp)



