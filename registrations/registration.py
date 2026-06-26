from failures.file_read import *
from enum import Enum


class VehicleCateories(Enum):
    Sedan = "Sedan"
    SUV = "SUV"
    Coupe = "Coupe"

    @classmethod
    def isValid(cls, vtype: str) -> bool:
        return vtype in cls._value2member_map_
        

class Vehicle:

    def __init__(self, feature: str, category: VehicleCateories):
        self.feature = feature
        self.category = category

    @classmethod
    def addingVehicle(cls, vtype: str, feature: str) -> tuple["Vehicle" | None, Exception]:
        if not VehicleCateories.isValid(vtype=vtype):
            return None, FailureValueUnforeseenInField(cls.VehicleType, "user registration")
        vehicle = Vehicle(feature=feature, category=VehicleCateories[vtype])
        return vehicle, None
        


class Registration:

    Username = "Username"
    Timestamp = "Timestamp"
    Nickname = "Preferred Name"
    Place = "Place Living, or Preferred Pickup Location (Street, City, State)"
    OwnsVehicle = "Owning a vehicle and ride-share ready next time?"
    Yes = "Yes"
    VehicleType = "Vehicle Type"
    VehicleFeature = "How do we recognize your vehicle?"

    def __init__(self, username: str, nickname: str, timestamp: str, place: str, owns: bool, vehicle: Vehicle | None, unresolution: bool) -> None:
        # basic info
        self.username = username
        self.nickname = nickname
        self.timestamp = timestamp
        self.place = place
        self.owns = owns
        self.vehicle = vehicle
        
        # marker in database identifying incomplete info with fallback casting during registration fulfillment
        self.unresolution = unresolution

    @classmethod
    def fulfillingRegistration(cls, info: dict[str, str]) -> tuple["Registration", Exception]:
        username = info[cls.Username]
        nickname = info[cls.Nickname]
        timestamp = info[cls.Timestamp]
        place = info[cls.Place]
        vehicle, exception = Vehicle.addingVehicle(vtype=info[cls.VehicleType], owns=info[cls.OwnsVehicle])
        owns = False if not vehicle else True
        registration = Registration(
            username=username, 
            nickname=nickname, 
            timestamp=timestamp, 
            place=place, 
            owns=owns, 
            vehicle=vehicle, 
            unresolution=not exception
        )

        if exception:
            return registration, exception
        return registration, None
