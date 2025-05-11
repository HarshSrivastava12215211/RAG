
def calculator_tool(query: str) -> str:
    try:
        result = eval(query.split("calculate", 1)[-1].strip())
        return f"The result is: {result}"
    except Exception as e:
        return f"Error evaluating expression: {e}"

def dictionary_tool(query: str) -> str:
    import requests
    term = query.split("define", 1)[-1].strip()
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{term}")
    if response.status_code == 200:
        meaning = response.json()[0]["meanings"][0]["definitions"][0]["definition"]
        return f"{term}: {meaning}"
    else:
        return f"Definition for '{term}' not found."
