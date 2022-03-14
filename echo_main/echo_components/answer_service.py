"""
Answer Question Mode
=====================
Answer question method
----------------------
.........................

*Use it like this*::
    from answer_service import answer_mode
    question = "who is the queen of england"
    answer_service(question)
"""

import requests
import logging

logging.basicConfig(level=logging.DEBUG)


def answer_mode(question: str) -> str:
    """Takes a users question in string format
    Returns results from wolframalpha api in json format
    raises Error when question is not found or server error

    Args:
        question (str): a string of text

    Returns:
        str: response to the question from api
    """
    query = question
    query_url = f"http://api.wolframalpha.com/v2/query?" \
                f"appid=J68K85-EE7Y6JKREV" \
                f"&input={query}" \
                f"&format=plaintext" \
                f"&output=json"
    try:
        r = requests.get(query_url).json()
        data = r["queryresult"]["pods"][1]["subpods"][0]
        final_data = data["plaintext"]
        return final_data
    except Exception:
        logging.debug("request not found")
        return "Sorry i didnt quiet understand,Try asking me another question"
