import waveassist

waveassist.init()

# Store the base greeting and a sample customer record
waveassist.store_data("greeting", "Hello, how are you")
waveassist.store_data(
    "customer",
    {"name": "Frank", "age": 30, "city": "San Francisco"}
)

print("✔ Demo data stored")
