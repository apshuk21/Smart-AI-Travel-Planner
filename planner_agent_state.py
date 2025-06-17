from typing_extensions import TypedDict, Optional
from langgraph.graph import MessagesState
from user_destination import DestinationInfo

class PlannerAgentState(TypedDict):
    messages: MessagesState
    destination_info: Optional[DestinationInfo]