import dspy 

class ProductCart(dspy.Predict):
    def __init__(self):
        super().__init__(signature="product, cart_items -> summary")

    def forward(self, product:str, cart_items:str) -> str:
        return f"You have {product} in your cart along with {cart_items}"
    
product_cart = ProductCart()
print(product_cart(product="RAM kit", cart_items="2.5 inch 512GB SSD"))
