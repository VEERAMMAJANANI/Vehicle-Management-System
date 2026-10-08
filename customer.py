class customerpanel:
  def __init__(self,customer,vehicle):
    self.customer=customer
    self.vehicle=vehicle

  def registercustomer(self,customer_id,name):
    try:
      if not customer_id:
        raise ValueError("Customer ID cannot be empty.")
      if not name: 
        raise ValueError("Customer name cannot be empty.")
      if customer_id in self.customer: 
        raise ValueError("Customer ID already exists.")
      self.customer[customer_id]={
        "customername":name,
        "rent_vehicle":None

      }
      print(f"👦🏻Customer {name} added Successfully")
    except ValueError as e:
       print(f"❌ Error: {e}") 
    except Exception as e:
      print(f"❌ Unexpected error: {e}")

  def displayavailablevehicle(self):
    try:
      print("-----Available Vehicles------")
      available=False
      for vehicle_number,vehicle_data in self.vehicle.items():
        if vehicle_data["available"]:
          print(f"ID:{vehicle_number},\n Brand:{vehicle_data["Brand"]},\n Type:{vehicle_data["Type"]},\n rent:{vehicle_data["Rent"]}")
          available=True

      if not available:
        print("vehicle not Available😞")
    except Exception as e:
      print("❌Error:{e}")
        

  def rentvehicle(self,customer_id,vehicle_id):
    try:
      if customer_id not in self.customer:
        raise ValueError("Customer Doesn't Exist❌")
        return

      if vehicle_id not in self.vehicle:
        raise ValueError("Vehicle doesn't available❌")
        return

      if not self.vehicle[vehicle_id]["available"]:
        raise ValueError("Vehicle Already Rented")
        return
      if self.customer[customer_id]["rent_vehicle"] is not None: 
        raise ValueError( "Customer already has a rented vehicle." )

      self.vehicle[vehicle_id]["available"]=False 
      self.customer[customer_id]["rent_vehicle"]=vehicle_id
      print(f"{self.customer[customer_id]["customername"]} rented {self.vehicle[vehicle_id]["Brand"]} {self.vehicle[vehicle_id]["Type"]}")
    except Exception as e:
      print(f"❌Error:{e}")

  def returnvehicle(self,customer_id):
    try:
      if customer_id not in self.customer:
        raise ValueError("customer doesn't Exist❌")
        return
      rented=self.customer[customer_id]["rent_vehicle"]
      if not rented:
        print("Vehicle is not Rented By customer")
        return
      self.vehicle[rented]["available"]=True
      print(f"{self.customer[customer_id]["customername"]} returned {self.vehicle[rented]["Brand"]} ({self.vehicle[rented]["Type"]})")
      self.customer[customer_id]["rent_vehicle"]=None
    except ValueError as e:
      print(f"❌Error:{e}")
    except Exception as e:
      print(f"Unexpected Error:{e}")


