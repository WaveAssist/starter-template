import waveassist

waveassist.init()

# Fetch the originals
greeting = waveassist.fetch_data("greeting")          # "Hello, how are you"
customer = waveassist.fetch_data("customer")          # {'name': 'Frank', ...}

# Make a personalised greeting
custom_greeting = f"{greeting} {customer['name']}!"

# Build an enriched customer dict
customer_enriched = {
    "name": customer["name"],
    "age": customer["age"],
    "city": customer["city"].upper(),      # simple transform
    "name_length": len(customer["name"]),
    "greeting": custom_greeting,           # merged greeting
}

waveassist.store_data("customer", customer_enriched)
print("✔ Data transformed and stored")
