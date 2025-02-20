from fastapi import FastAPI, Query
from typing import Union

app = FastAPI()

@app.get("/hotels/")
async def get_hotels(location: str, 
                     datefrom: str, 
                     dateto: str, 
                     has_pool: Union[bool,None], 
                     stars: Union[int, None]=Query(None, le=5, ge=1)):
    
    return {"hotels": "all"}