import requests


def answer_mode(question: str) -> str:
    """
    Takes a users question in string format
    Returns results from wolframalpha api in json format
    raises Error when question is not found or server error
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
        return "Sorry i didnt quiet understand,Try asking me another question"
