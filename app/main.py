from fastapi import FastAPI, Query
from typing import Optional, Union
from datetime import date

from pydantic import BaseModel
#Use Optional to make a parameter optional and if not provided it will be None
#Use Query to add validation to the parameters


app = FastAPI()

class SHotel(BaseModel):
    name: str
    location: str
    stars: int
    has_pool: bool
    price: float

@app.get("/hotels/", response_model=list[SHotel])
async def get_hotels(location: str, 
                     datefrom: Union[date,str], 
                     dateto: Union[date,str], 
                     has_pool: Optional[bool], 
                     stars: Optional[int]=Query(None, le=5, ge=1)) -> list[SHotel]:
    
    return [{"name": "Hotel A",
            "location": location,
            "stars": stars,
            "has_pool": has_pool,
            "price": 100.0}]

async def get_hotels(location: str, 
                     datefrom: date, 
                     dateto: date, 
                     has_pool: Optional[bool], 
                     stars: Optional[int]=Query(None, le=5, ge=1)) :
    
    return {"hotels": "all"}

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
