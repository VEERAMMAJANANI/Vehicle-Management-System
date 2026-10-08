import json

def load_data():
    try:
        with open("data.json","r") as file:
            data=json.load(file)

        vehicle =data.get("vehicle",{})
        customer=data.get("customer",{})

        return vehicle, customer
    
    except FileNotFoundError:
        return {},{}
    
    except json.JSONDecodeError:
        print("data.json contain Invalid data")
        return {},{}

def save_data(vehicle,customer):
    data={"vehicles":vehicle,
          "customers":customer
          }
    try:
        with open("data.json","w") as file:
            json.dump(data,file,indent=4)

        print("Data saved successfully!")

    except Exception as e:
        print(f"Error while saving data:{e}")