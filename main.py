from src.admin import admin_panel
from src.customer import customerpanel
from storage import load_data,save_data

def main_display():
    print("-"*30)
    print(f"🎉Welcome to Janani Rentals🎉")
    print("-"*30)
    print("Choose an Option : ")
    print("1.Admin panel")
    print("2.Customer Panel")
    print("3.Exit")

def admin_display():
    print("*"*30)
    print(f"😍Welcome to Admin Panel😍")
    print("*"*30)
    print("Choose an Option : ")
    print("1. Add Vehicle🚗")
    print("2. View Inventory")
    print("3. Exit Admin Panel") 

def customer_display():
    print("^"*30)
    print(f"🙌Welcome to Customer Panel🙌")
    print("^"*30)
    print("Choose an Option : ")
    print("1. Register Customer📃")
    print("2. View Available Vehicles🚗")
    print("3. Rent Vehicle")
    print("4. Return Vehicle")
    print("5. Exit Customer panel")

def main():
    vehicle,customer=load_data()
    

    admin=admin_panel(vehicle)
    customer_panel=customerpanel(customer,vehicle)

    while True:
        try:
            main_display()
            user_choice = input("Enter you choice 1/2/3 : ")
            if user_choice == "3":
                print(f"🙏Thank you for using Janani Rendels🙏")
                break
            elif user_choice == "1":
                while True:
                    try:
                        admin_display()
                        admin_choice=input("Enter Your choice 😊: ")
                        if admin_choice == "3":
                            print("Exiting the Admin Panel")
                            break
                        elif admin_choice == "1":
                            vehicle_number=input("Enter Vehicle Number : ")
                            vehicle_brand=input("Enter the Vehicle Brand : ")
                            vehicle_type= input("Enter the Vehicle Type : ")
                            vehicle_rent=input("Enter the Vehicle Rent : ")
                            admin.add_vehicle(vehicle_number,vehicle_brand,vehicle_type,vehicle_rent)
                            save_data(vehicle,customer)
                        elif admin_choice == "2":
                            print("Displaying all the vehicles : ")
                            admin.view_inventory()
                        else:
                            print("Invalid Choice .use 1/2/3")
                    except Exception as e:
                        print(f"❌Admin Panel Error:{e}")
            elif user_choice == "2":
                while True:
                    try:
                        customer_display()
                        customer_choice=input("Enter Your Choice 😊: ")
                        if customer_choice == "5":
                            print("Exiting the Customer Panel")
                            break
                        elif customer_choice == "1":
                            cid=input("Enter Customer ID: ")
                            name=input("Enter Customer Name: ")
                            customer_panel.registercustomer(cid,name)
                            save_data(vehicle,customer)
                        elif customer_choice == "2":
                            customer_panel.displayavailablevehicle()
                        elif customer_choice == "3":
                            cid=input("Enter customer ID: ")
                            vid=input("Enter Vehicle ID: ")
                            customer_panel.rentvehicle(cid,vid)
                            save_data(vehicle,customer)
                        elif customer_choice == "4":
                            cid=input("Enter Customer ID: ")
                            customer_panel.returnvehicle(cid)
                            save_data(vehicle,customer)
                        else:
                            print("❌Invalid Choice. use 1/2/3/4/5")
                    except Exception as e:
                        print(f"❌Customer Panel Error:{e}")
            else:
                print("❌Invalid choice. only choice 1/2/3")
        except KeyboardInterrupt: 
            print("\n👋 Program stopped by user.") 
            break
        except Exception as e:
            print(f"Unexcepted Error:{e}")

if __name__ == "__main__":
    main()