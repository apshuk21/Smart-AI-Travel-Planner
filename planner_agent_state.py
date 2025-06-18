from typing_extensions import TypedDict
from typing import Optional, Annotated, List
from langgraph.graph.message import add_messages
from langchain_core.messages import AnyMessage
from user_destination import DestinationInfo

class PlannerAgentState(TypedDict):
    messages: Annotated[List[AnyMessage], add_messages]
    destination_info: Optional[DestinationInfo]