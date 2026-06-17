from pydantic import BaseModel, ConfigDict

class FlightRequest(BaseModel):
    origin: str
    dest: str
    airline: str
    month: int
    day_of_week: int
    distance: float
    crs_dep_time: int

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "origin": "JFK",
                "dest": "ATL",
                "airline": "DL",
                "month": 7,
                "day_of_week": 2,
                "distance": 760,
                "crs_dep_time": 900
            }
        }
    )