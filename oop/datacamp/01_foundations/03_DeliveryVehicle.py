"""
Level 1: Class vs. Instance Attributes 
Scenario: Vehicle Fleet Tracker

Create a DeliveryVehicle class.

Instance Attributes: vehicle_id (str), current_mileage (float, default 0.0).

Class Attributes: company_name = "FastTrack Delivery", total_vehicles_created (int, increments on each instantiation), total_fleet_mileage (float, starts at 0.0).

Instance Method: drive(miles) — increases both the specific vehicle's current_mileage and the global total_fleet_mileage.

"""
class DeliveryVehicle:
    company_name= "FastTrack Delivery"
    total_vehicles_created = 0
    total_fleet_mileage = 0.0
    def __init__(self,vehicle_id,current_mileage=0.0):
        self.vehicle_id = vehicle_id
        self.current_mileage = current_mileage
        DeliveryVehicle.total_vehicles_created += 1

    def drive(self,miles):
        DeliveryVehicle.total_fleet_mileage += miles
        self.current_mileage +=miles


if __name__ == "__main__":
    # Reset class state in case tests are rerun
    DeliveryVehicle.total_vehicles_created = 0
    DeliveryVehicle.total_fleet_mileage = 0.0

    # 1. Test Initial Instantiation & Class Attributes
    v1 = DeliveryVehicle(vehicle_id="TRUCK-01")
    assert v1.vehicle_id == "TRUCK-01"
    assert v1.current_mileage == 0.0
    assert DeliveryVehicle.company_name == "FastTrack Delivery"
    assert v1.company_name == "FastTrack Delivery"  # Access via instance
    assert DeliveryVehicle.total_vehicles_created == 1

    # 2. Test Multiple Instantiations
    v2 = DeliveryVehicle(vehicle_id="VAN-02")
    assert DeliveryVehicle.total_vehicles_created == 2

    # 3. Test Mileage Accumulation (Instance vs Class State)
    v1.drive(15.0)
    assert v1.current_mileage == 15.0
    assert v2.current_mileage == 0.0
    assert DeliveryVehicle.total_fleet_mileage == 15.0

    v2.drive(25.5)
    assert v1.current_mileage == 15.0
    assert v2.current_mileage == 25.5
    assert DeliveryVehicle.total_fleet_mileage == 40.5

    print("Level 1 Tests Passed Successfully!")  
        