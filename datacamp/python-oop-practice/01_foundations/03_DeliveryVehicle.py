"""
Level 1: Class vs. Instance Attributes 
Scenario: Vehicle Fleet Tracker

Create a DeliveryVehicle class.

Instance Attributes: vehicle_id (str), current_mileage (float, default 0.0).

Class Attributes: company_name = "FastTrack Delivery", total_vehicles_created (int, increments on each instantiation), total_fleet_mileage (float, starts at 0.0).

Instance Method: drive(miles) — increases both the specific vehicle's current_mileage and the global total_fleet_mileage.

"""
class DeliveryVehicle:
    COMPANY_NAME= "FastTrack Delivery"
    total_vehicles_created = 0
    total_fleet_mileage = 0.0
    def __init__(self,vehicle_id,current_mileage=0.0):
        self.vehicle_id = vehicle_id
        self.current_mileage = current_mileage
        DeliveryVehicle.total_vehicles_created += 1

    def drive(self,miles):
        DeliveryVehicle.total_fleet_mileage += miles
        self.miles +=miles

        
        