from langchain_core.messages import AIMessage
from langchain_core.tools import tool

@tool
def get_food_by_nutrients(data: str):
    """Call to get food by nutrients."""
    print('in tool call data is ' + data)
    if data.lower() == 'calcium':
        return ["Milk", "Soya Beans", "Nuts", "Fish "]
    if data.lower() == 'protein':
        return ["Eggs", "Legumes", "Quinoa", "Nuts and Seeds "]
    else:
        return []