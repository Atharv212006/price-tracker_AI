from fastapi import FastAPI
from pydantic import BaseModel
from scraper import get_price

app = FastAPI()

# temporary storage
tracked_products = []

# -------- models --------
class PriceRequest(BaseModel):
    url: str

class TrackRequest(BaseModel):
    url: str
    target_price: float


# -------- API: get price --------
@app.post("/get-price")
def get_current_price(data: PriceRequest):
    price = get_price(data.url)

    if price:
        return {"price": price}
    return {"error": "Price not found"}


# -------- API: track product --------
@app.post("/track")
def track_product(data: TrackRequest):
    tracked_products.append({
        "url": data.url,
        "target_price": data.target_price
    })

    return {"message": "Tracking started"}


# -------- optional check --------
@app.get("/check-now")
def check_now():
    results = []

    for product in tracked_products:
        price = get_price(product["url"])

        if price and price <= product["target_price"]:
            results.append({
                "url": product["url"],
                "price": price,
                "status": "BUY NOW"
            })

    return {"results": results}