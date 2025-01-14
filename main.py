from fastapi import FastAPI, HTTPException
"""
This module defines a FastAPI application with an endpoint to fetch building data by ID.

Classes:
    Building (BaseModel): A Pydantic model representing a building with attributes id, building_name, and built_on.

Functions:
    get_by_id(id: int) -> Building:
        API endpoint that fetches building data by ID from a predefined list of buildings.
        Args:
            id (int): The ID of the building to fetch.
        Returns:
            Building: The building data if found.
        Raises:
            HTTPException: If the building with the specified ID is not found.

Usage:
    Run the application using Uvicorn if this script is run directly.
"""
from pydantic import BaseModel
from typing import Literal
from datetime import datetime
import aiohttp

# Initialize the FastAPI app
app = FastAPI()

# Define a Pydantic model for the building data
class Building(BaseModel):
    id: int
    building_name: str
    built_on: datetime

# Predefined list of buildings
buildings = [
    Building(id=1, building_name="Central Library", built_on=datetime(1985, 6, 15)),
    Building(id=2, building_name="Science Hall", built_on=datetime(1992, 9, 1)),
    Building(id=3, building_name="Art Gallery", built_on=datetime(2005, 3, 20)),
    Building(id=4, building_name="Student Union", built_on=datetime(2010, 11, 5)),
    Building(id=5, building_name="Engineering Block", built_on=datetime(2018, 2, 28)),
    Building(id=6, building_name="Residential Hall A", built_on=datetime(1999, 8, 14)),
    Building(id=7, building_name="Health Center", built_on=datetime(2002, 5, 3)),
    Building(id=8, building_name="Sports Complex", built_on=datetime(2015, 7, 22)),
    Building(id=9, building_name="Administration Building", built_on=datetime(1980, 1, 10)),
    Building(id=10, building_name="Computer Science Lab", built_on=datetime(2020, 4, 18)),
]

@app.get("/building/{id}", response_model=Building)
async def get_by_id(id: int):
    """API endpoint that fetches building data by ID from a predefined list of buildings."""
    # Iterate through the list of buildings to find the one with the matching ID
    for i in buildings:
        if(i.id == id):
            return i
    # Raise an HTTP 404 exception if the building is not found
    raise HTTPException(status_code=404, detail="Building not found")

# Run the application using Uvicorn if this script is run directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)