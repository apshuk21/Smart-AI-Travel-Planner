from user_destination import DestinationInfo

def build_query(base_text: str, destination_info: DestinationInfo, suffix: str = "") -> str:
    """
    Constructs a Tavily-friendly query using DestinationInfo.
    Appends lat/lon if available.
    """
    location_str = (
        f"{destination_info.city or destination_info.destination or ''}, "
        f"{destination_info.region or ''}, "
        f"{destination_info.country or ''}".strip(", ")
    )
    
    if destination_info.latitude and destination_info.longitude:
        geo_hint = f"(Latitude: {destination_info.latitude}, Longitude: {destination_info.longitude})"
        return f"{base_text} in {location_str} {geo_hint} {suffix}".strip()
    
    return f"{base_text} in {location_str} {suffix}".strip()
