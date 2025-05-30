import waveassist

waveassist.init()

greeting   = waveassist.fetch_data("greeting")
customer   = waveassist.fetch_data("customer")
transformed_greeting = customer.get('greeting')
print(f"Original greeting: {greeting}")
print(f"Transformed customer:   {customer}")
print(f"Transformed greeting: {transformed_greeting}")


