from failures.file_read import *
from enum import Enum


class VehicleCateories(Enum):
    Sedan = "Sedan"
    SUV = "SUV"
    Coupe = "Coupe"

class Vehicle:

    def __init__(self, feature: str, vtype: str):
        self.feature = feature
        self.category = VehicleCateories[vtype]


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
        vtype = info[cls.VehicleType]
        owns = info[cls.OwnsVehicle] == cls.Yes and vtype in VehicleCateories
        vehicle = Vehicle(feature=info[cls.VehicleFeature], vtype=vtype) if owns else None
        
        friction = True if vtype not in VehicleCateories else False
        registration =  Registration(username=username, nickname=nickname, timestamp=timestamp, place=place, owns=owns, vehicle=vehicle, unresolution=friction)
        if friction:
            return registration, FailureValueUnforeseenInField(cls.VehicleType, "user registration")
        
        return registration, None
