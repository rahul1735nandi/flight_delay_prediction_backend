from pydantic import BaseModel, ConfigDict, Field

class FlightRequest(BaseModel):
    origin: str = Field(min_length=3, max_length=3)
    dest: str = Field(min_length=3, max_length=3)
    airline: str = Field(min_length=2)
    month: int = Field(ge=1, le=12)
    day_of_week: int = Field(ge=1, le=7)
    distance: float = Field(ge=0)
    crs_dep_time: int = Field(ge=0, le=2359)

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