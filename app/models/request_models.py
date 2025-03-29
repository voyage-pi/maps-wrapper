from pydantic import BaseModel
from typing import List, Literal, Optional

class Location(BaseModel):
    latitude: float
    longitude: float    

class ComputeRoutesRequest(BaseModel):
    origin: Location
    destination: Location
    intermediate: Optional[List[Location]] = []  # Optional, empty by default
    travelingMode: Literal["WALK", "DRIVE", "BICYCLE", "TRANSIT", "TWO_WHEELER"] = "DRIVE"  # Default to DRIVE