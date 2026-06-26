
import os
import requests
import json

class StripeAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.stripe.com/v1"

    def _make_request(self, method, endpoint, data=None):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        url = f"{self.base_url}/{endpoint}"
        response = requests.request(method, url, headers=headers, data=data)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()

    def create_product(self, name, description=None):
        """Creates a new product in Stripe."""
        data = {"name": name}
        if description:
            data["description"] = description
        
        print(f"Creating product with data: {data}")
        return self._make_request("POST", "products", data)

    def create_price(self, product_id, amount_in_cents, currency="usd"):
        """Creates a new price for a product in Stripe."""
        data = {
            "product": product_id,
            "unit_amount": amount_in_cents,
            "currency": currency,
        }
        print(f"Creating price with data: {data}")
        return self._make_request("POST", "prices", data)

    def create_payment_link(self, price_id):
        """Creates a new payment link for a price in Stripe."""
        data = {
            "line_items[0][price]": price_id,
            "line_items[0][quantity]": 1,
        }
        print(f"Creating payment link with data: {data}")
        return self._make_request("POST", "payment_links", data)

def main():
    stripe_api_key = os.environ.get("STRIPE_API_KEY")
    if not stripe_api_key:
        print("Error: STRIPE_API_KEY environment variable not set.")
        return

    stripe_api = StripeAPI(stripe_api_key)

    # Example usage:
    try:
        product_name = "Hermes Business Agent Pro"
        product_description = "A professional-grade autonomous agent for business operations."
        new_product = stripe_api.create_product(product_name, product_description)
        print("Successfully created product:")
        print(json.dumps(new_product, indent=2))

        product_id = new_product['id']
        price_in_cents = 9999  # $99.99
        new_price = stripe_api.create_price(product_id, price_in_cents)
        print("\\nSuccessfully created price:")
        print(json.dumps(new_price, indent=2))

        price_id = new_price['id']
        payment_link = stripe_api.create_payment_link(price_id)
        print("\\nSuccessfully created payment link:")
        print(json.dumps(payment_link, indent=2))
        print(f"\\nPayment Link URL: {payment_link['url']}")

    except requests.exceptions.HTTPError as e:
        print(f"Error creating product: {e.response.text}")

if __name__ == "__main__":
    main()
