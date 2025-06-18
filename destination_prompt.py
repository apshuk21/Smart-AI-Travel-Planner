from langchain_core.prompts import PromptTemplate
from user_destination import destination_parser_format_instructions

prompt = PromptTemplate(
    template="""
    Extract the structured travel destination information from the following user query.

    Use your general knowledge of well-known locations to infer missing fields like country, region, postal code, latitude, and longitude if the destination is unambiguous (e.g., Kyoto in Japan, or Jaipur in India). If the city is vague or not well-known, leave such fields blank.

    Return only the structured data in valid JSON format.

    {format_instructions}

    Query: {user_input}
    """,
    input_variables=["user_input"],
    partial_variables={"format_instructions": destination_parser_format_instructions}
)