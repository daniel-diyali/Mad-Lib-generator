# The following program generates an AI-based Mad Lib Story
from openai import OpenAI

client = OpenAI(
    api_key = "API key"
)

print("Please enter the following prompts: \n1. An emotion \n2. A color \n3. A noun \n4. An adjective " +
      "\n5. A verb (past tense) \n6. A plural noun \n7. A type of food \n8. Another adjective " +
      "\n9. A verb \n10. A noun (plural) \n11. An occupation \n12. A type of animal " +
      "\n13. An adjective \n14. A verb (past tense) \n15. A noun \n16. A name \n17. Another name \n")

listOfWords = []
stringOfWords = ""

for i in range(17):
    getInput = input("Enter a response to prompt #" + str(i + 1) + ": ")
    listOfWords.append(getInput)

system_data = [
    {"role": "system", "content": "Generate a horror two-paragraph Mad Lib story using the words."},
    {"role": "user", "content": stringOfWords.join(listOfWords)}
]

response = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = system_data
)

assistant_response = response.choices[0].message.content
system_data.append({"role": "assistant", "content": assistant_response})
print("Assistant: " + assistant_response)