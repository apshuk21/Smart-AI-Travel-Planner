from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Optional

class DestinationInfo(BaseModel):
    destination: str = Field(..., description="The general name of the travel destination (e.g., Kyoto)")
    city: Optional[str] = Field(None, description="The specific city of the destination")
    country: Optional[str] = Field(None, description="The country of the destination")
    pincode: Optional[str] = Field(None, description="Postal code for the destination, if available")
    region: Optional[str] = Field(None, description="Broader region or area (e.g., Kansai, Tuscany)")
    latitude: Optional[float] = Field(None, description="Latitude of the destination for geospatial queries")
    longitude: Optional[float] = Field(None, description="Longitude of the destination for geospatial queries")

destination_parser = PydanticOutputParser(pydantic_object=DestinationInfo)

destination_parser_format_instructions = destination_parser.get_format_instructions()