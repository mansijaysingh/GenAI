device_status="active"
temperature=30

if device_status=="active" :
  if temperature>35:
    print("Alert: High temperature detected! Activating cooling system.")
  else:
    print("Temperature is within safe limits.")
else:
  print("Device is offline.")