import random

import fastapi

app = fastapi.FastAPI()

@app.get("/generate_name")
# Default is none if there nothing passed in then it is none.  If required then it doesn't have string =. So this is optional
#new API parameter, like ends_with, includes, or length
async def generate_name(starts_with: str = 'n', ends_with: str = 'a'):
    names = ["Minnie", "Margaret", "Myrtle", "Noa", "Nadia"]
    if starts_with:
        names = [n for n in names if n.lower().startswith(starts_with.lower()) and n.lower().endswith(ends_with.lower())]
    if len(names) == 0:
        raise fastapi.HTTPException(status_code=404, detail="No name found")
    random_name = random.choice(names)
    return {"name": random_name}

@app.get("/generate_pet_name")
# Default is none if there nothing passed in then it is none.  If required then it doesn't have string =. So this is optional
#new API parameter, like ends_with, includes, or length
async def generate_name(starts_with: str = 'n', ends_with: str = 'a'):
    names = ["Brownie", "Fluffy", "Myrtle", "Noa", "Nadia"]
    if starts_with:
        names = [n for n in names if n.lower().startswith(starts_with.lower()) and n.lower().endswith(ends_with.lower())]
    if len(names) == 0:
        raise fastapi.HTTPException(status_code=404, detail="No name found")
    random_name = random.choice(names)
    return {"name": random_name}