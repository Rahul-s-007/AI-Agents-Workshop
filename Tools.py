from Actions.get_response_time import get_response_time
from Actions.get_response_time_ranking import get_response_time_ranking

tools = [
    {
        "function_name": "get_response_time",
        "function_call": get_response_time,
        "function_params": [
            {   "param_name": "url", 
                "type": str
            }
        ],
        "example_input": "google.com",
        "return_type": int,
        "description": "Returns the response time of a website in ms, returns -1 if the website is unreachable"
    },
    
    {
        "function_name": "get_response_time_ranking",
        "function_call": get_response_time_ranking,
        "function_params": [
            {   "param_name": "response_time", 
                "type": int
            }
        ],
        "example_input": "0.5",
        "return_type": int,
        "description": "Returns the ranking based upon the response time of a website"
    }
]