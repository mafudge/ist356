#input => Process => output

reading = float(input("Sensor Reading: "))

if reading > 10:
    status = "Opening"
else:
    status = "Closing"

print(f"{status} the door")