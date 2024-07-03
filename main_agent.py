import os

from openai import OpenAI
from Prompts import react_prompt
from Helpers.json_helper import extract_json
from Tools import tools

# import sys
# write output to logs file
# sys.stdout = open("logs.txt", "w")

# Load environment variables
import os
from dotenv import load_dotenv
load_dotenv()

# Create an instance of the OpenAI class
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_text_with_conversation(messages, model = "gpt-3.5-turbo"):
    response = client.chat.completions.create(
        model=model,
        messages=messages
        )
    return response.choices[0].message.content

system_prompt = react_prompt(tools)
# print(system_prompt)

user_prompt = "what is the response time rank for youtube.com?"
# user_prompt = "what is the response time rank for youtube.com and google.com?"

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt},
]

available_actions = {
    tool["function_name"]: tool["function_call"] for tool in tools
}

print("Available actions: ", available_actions.keys())

print("Starting conversation...")
turn_count = 1
max_turns = 10

while turn_count < max_turns:
    print (f"Loop: {turn_count}")
    print("-------------------------------------------------------------")
    turn_count += 1

    response = generate_text_with_conversation(messages, model="gpt-4")
    messages.append({"role": "assistant", "content": response})
    print(response)
    json_function = extract_json(response)

    if json_function:
            function_name = json_function[0]['function_name']
            function_parms = json_function[0]['function_params']
            if function_name not in available_actions:
                raise Exception(f"Unknown action: {function_name}: {function_parms}")
            print(f" -- running {function_name} {function_parms}")
            action_function = available_actions[function_name]
            #call the function
            result = action_function(**function_parms)
            function_result_message = f"Action_Response: {result}"
            messages.append({"role": "user", "content": function_result_message})
            print(function_result_message)
    else:
        break

print("Conversation ended.")
print("-------------------------------------------------------------")

# print("Messages:")
# for message in messages:
#     print(f"{message['role']}: {message['content']}")