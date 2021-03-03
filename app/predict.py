"""Machine learning function"""

from fastapi import APIRouter
from pydantic import BaseModel, confloat, conint

router = APIRouter()

class AirBnb_rentals(BaseModel):
    num_baths: confloat(ge=0, le=10)
    number_of_reviews: int
    neighborhood: str
    bedrooms: conint(gt=0, lt=10)
    minimum_nights_avg_ntm: int


@router.post('/predict_rent')
async def predict(rent: AirBnb_rentals):
    '''Data model base working model 
       # Usage: 
         - To be filled unit4         
         - model is in place
         - Post Method'''
    rent_price = (500*rent.bedrooms + 100*rent.num_baths + 10*rent.number_of_reviews)*rent.minimum_nights_avg_ntm
    return { 'Predicted Price is = ': rent_price}
          