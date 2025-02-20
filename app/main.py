from fastapi import Depends, FastAPI, Query
from typing import Optional, Union
from datetime import date

from pydantic import BaseModel
#Use Optional to make a parameter optional and if not provided it will be None
#Use Union to allow multiple types for a parameter
#Use Query to add validation to the parameters
#Depends is used to define the dependencies for the endpoint

app = FastAPI()

class HotelSearchArgs:
    def __init__(self, location: str, datefrom: Union[date,str], dateto: Union[date,str], has_pool: Optional[bool], stars: Optional[int]):
        self.location = location
        self.datefrom = datefrom
        self.dateto = dateto
        self.has_pool = has_pool
        self.stars = stars
    

@app.get("/hotels/")
async def get_hotels(search_args:HotelSearchArgs = Depends()):
    
    return search_args

class SBookings(BaseModel):
    room_id: int
    datefrom: date
    dateto: date
    guests: int
    has_children: bool
    price: float

@app.post("/bookings/")
async def create_booking(booking: SBookings):
    return {"booking": booking}
