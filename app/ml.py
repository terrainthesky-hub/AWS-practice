"""Machine learning functions"""

from fastapi import APIRouter

router = APIRouter()

# @router.post('/predict')
# async def predict(item: Item):
#     """Predict house prices in California."""
#     y_pred = 200000
#     return {'predicted_price': y_pred}


# import pandas as pd
# from pydantic import BaseModel

# features = ['bedrooms', 'total_rooms', 'house_age']

# class House(BaseModel):
#     """Data model to parse the request body JSON."""
#     bedrooms: int
#     total_rooms: float
#     house_age: float

#     def to_df(self):
#         """Convert pydantic object to pandas dataframe with 1 row."""
#         return pd.DataFrame([dict(self)])


# @router.post('/predict')
# async def predict(house: House):
#     """Predict house prices in California."""
#     X_new = house.to_df()
#     y_pred = 200000
#     return {'predicted_price': y_pred}