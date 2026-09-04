from fastapi import FastAPI, Query, Path

app = FastAPI(
    title="My First Project",
    version="1.0.0",
    description="FastAPI project"
)

products = [
    {"id": 1, "name": "Apple", "price": 150, "is_available": True},
    {"id": 2, "name": "Banana", "price": 200, "is_available": False},
    {"id": 3, "name": "Kiwi", "price": 100, "is_available": True},
    {"id": 4, "name": "Tomato", "price": 120, "is_available": False},
    {"id": 5, "name": "Potato", "price": 180, "is_available": True},
    {"id": 6, "name": "Apple", "price": 250, "is_available": False},
    {"id": 7, "name": "Pineapple", "price": 120, "is_available": True},
    {"id": 8, "name": "Cherry", "price": 150, "is_available": False}
]

@app.get("/")
def read_root():
    return {"Hello": "World"}

# @app.get("/products")
# def read_products(category: str = None, limit: int = Query(10, ge=1), offset: int = 0):
#     return {
#         "category": category,
#         "limit": limit,
#         "offset": offset,
#     }

@app.get("/products")
def read_products(name: str | None = None, limit: int | None = None, is_available: bool = True):
    filtered_products = products

    if name:
        filtered_products = [product for product in filtered_products if product["name"].lower() == name.lower()]

    if limit:
        filtered_products = filtered_products[:limit]

    filtered_products = [product for product in filtered_products if product["is_available"] == is_available]

    return filtered_products



@app.get("/products/{product_id}")
def read_products(product_id: int = Path(ge=1)):
    for product in products:
        if product["id"] == product_id:
            return product

    return {"message": "Product not found"}





















