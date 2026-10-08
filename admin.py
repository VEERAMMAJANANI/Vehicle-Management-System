vehicle={}

class admin_panel:
    def __init__(self,vehicle):
        self.vehicle=vehicle

    def add_vehicle(self,vehicle_number,vehicle_brand,vehicle_type,vehicle_rent):
        try:
            if not vehicle_number: 
                raise ValueError("Vehicle number cannot be empty.")
            if not vehicle_brand: 
                raise ValueError("Vehicle brand cannot be empty.") 
            if not vehicle_type: 
                raise ValueError("Vehicle type cannot be empty.") 
            if not vehicle_rent: 
                raise ValueError("Vehicle rent cannot be empty.") 
            if vehicle_number in self.vehicle:
                 raise ValueError("Vehicle already exists.") 
            try: 
                vehicle_rent = float(vehicle_rent) 
            except ValueError: 
                raise ValueError("Vehicle rent must be a number.")
            try: 
                vehicle_number = str(vehicle_number) 
            except ValueError: 
                raise ValueError("Vehicle number must be a number.")
            self.vehicle[vehicle_number] = {
                "number" : vehicle_number,
                "Brand" : vehicle_brand,
                "Type" : vehicle_type,
                "Rent" :vehicle_rent,
                "available" : True
            }
            print(f"🚗Vehicle: {vehicle_number} was added successfully!✅")
        except ValueError as e:
            print(f"❌Error: {e}")
        except Exception as e: 
            print(f"❌ Unexpected error: {e}")

    def view_inventory(self):
        try:
            if not self.vehicle:
                print("❌No vehicle available.")
                return
            for vehicle_number,vehicle_data in self.vehicle.items():
                status ="Available" if vehicle_data["available"] else "Rented"
                print(
                        f"Number: {vehicle_number}\n"
                        f"Brand: {vehicle_data['Brand']}\n"
                        f"Type: {vehicle_data['Type']}\n"
                        f"Rent: {vehicle_data['Rent']}"
                    )
        except Exception as e:
            print(f"❌Error: {e}")


    