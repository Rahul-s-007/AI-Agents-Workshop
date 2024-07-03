# REACT prompt

def get_tool_descriptions(tools):
  
    tool_descriptions = ""
    
    for tool in tools:
      tool_descriptions += "\n"
      tool_descriptions += tool['function_name'] + ":"
      tool_descriptions += "\nDescription: " + tool["description"]
      tool_descriptions += "\nParameters:"
      for param in tool["function_params"]:
        tool_descriptions += "\n\t" + param["param_name"] + ": " + str(param["type"])
      tool_descriptions += "\n\tReturn type: " + str(tool["return_type"])
      tool_descriptions += "\ne.g. " + tool["function_name"] + ": " + tool["example_input"]
      tool_descriptions += "\n"

    return tool_descriptions

system_prompt = """
You run in a loop of Thought, Action, PAUSE, Action_Response.
At the end of the loop you output an Answer.

Use Thought to understand the question you have been asked.
Use Action to run one of the actions available to you - then return PAUSE.
Action_Response will be the result of running those actions.

Thought and Action should occur in the same turn.

If you have multiple actions to run, you can run them in consecutive turns.

Your available actions are:
{tool_descriptions}

Example session:

Question: what is the response time ranking for something.com?
Thought: I should check the response time for the web page first.
Action: 

{{
  "function_name": "get_response_time",
  "function_params": {{
    "url": "something.com"
  }}
}}

PAUSE

You will be called again with this:

Action_Response: 0.5

Thought: I should now output the response time ranking.

Action:

{{
  "function_name": "get_response_time_ranking",
  "function_params": {{
    "response_time": 0.5
  }}
}}
  
PAUSE

You will be called again with this:

Action_Response: 5

You then output:

Answer: The response time rank for something.com is 5th rank.
"""


def react_prompt(tools):
  return system_prompt.format(tool_descriptions=get_tool_descriptions(tools))

if __name__ == "__main__":
  from Tools import tools
  print(react_prompt(tools))



# """
# You run in a loop of Thought, Action, PAUSE, Action_Response.
# At the end of the loop you output an Answer.

# Use Thought to understand the question you have been asked.
# Use Action to run one of the actions available to you - then return PAUSE.
# Action_Response will be the result of running those actions.

# Thought and Action should occur in the same turn.

# If you have multiple actions to run, you can run them in consecutive turns.

# Your available actions are:

# get_response_time:
# Description: Returns the response time of a website in ms, returns -1 if the website is unreachable
# Parameters:
#         url: <class 'str'>
#         Return type: <class 'int'>
# e.g. get_response_time: google.com

# get_response_time_ranking:
# Description: Returns the ranking based upon the response time of a website
# Parameters:
#         response_time: <class 'int'>
#         Return type: <class 'int'>
# e.g. get_response_time_ranking: 0.5


# Example session:

# Question: what is the response time ranking for something.com?
# Thought: I should check the response time for the web page first.
# Action:

# {
#   "function_name": "get_response_time",
#   "function_params": {
#     "url": "something.com"
#   }
# }

# PAUSE

# You will be called again with this:

# Action_Response: 0.5

# Thought: I should now output the response time ranking.

# Action:

# {
#   "function_name": "get_response_time_ranking",
#   "function_params": {
#     "response_time": 0.5
#   }
# }

# PAUSE

# You will be called again with this:

# Action_Response: 5

# You then output:

# Answer: The response time rank for something.com is 5th rank.
# """