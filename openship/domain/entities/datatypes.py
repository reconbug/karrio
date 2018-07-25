from typing import List, NamedTuple

class contact_type(NamedTuple):
    company_name: str = None
    person_name: str = None
    phone_number: str = None
    email_address: str = None

class address_type(NamedTuple):
    country_code: str
    state_or_province: str = None
    country_name: str = None
    postal_code: str = None
    city: str = None
    address_lines: List[str] = []

class package_type(NamedTuple):
    width: float
    height: float
    length: float
    weight: float
    id: str = None
    packaging_type: str = None
    description: str = None

class charges_payment_type(NamedTuple):
    type: str
    account_number: str

class insurance_type(NamedTuple):
    value: str
    currency: str

class party(NamedTuple):
    address: address_type
    contact: contact_type = None


class shipment_details(NamedTuple):
    packages: List[package_type]
    insurance: insurance_type = None 
    charges_payment: charges_payment_type = None 
    number_of_packages: int = None
    packaging_type: str = None
    is_dutiable: str = "N"
    currency: str = None
    total_weight: float = None
    weight_unit: str = "LB"
    dimension_unit: str = "IN"
    payment_country_code: str = None

class quote_request(NamedTuple):
    shipper: party 
    recipient: party
    shipment_details: shipment_details

class tracking_request(NamedTuple):
    tracking_numbers: List[str]
    language_code: str = None
    level_of_details: str = None


''' Generic response data types '''

class Charge:
    def __init__(self, name: str = None, value: str = None):
        self.name = name
        self.value = value

class TrackingEvent:
    def __init__(self, date: str, description: str, location: str, code: str, time: str = None, signatory: str = None):
        self.date = date
        self.time = time
        self.description = description
        self.location = location
        self.code = code
        self.signatory = signatory

class quote_details:
    def __init__(self, carrier: str, service_name: str, service_type: str, 
        base_charge: float, duties_and_taxes: float, total_charge: float, 
        delivery_time: str = None, pickup_time: str = None, delivery_date: str = None, 
        pickup_date: str = None, discount: float = None, extra_charges: List[Charge] = []):

        self.carrier = carrier
        self.service_name = service_name
        self.service_type = service_type
        self.base_charge = base_charge
        self.duties_and_taxes = duties_and_taxes
        self.total_charge = total_charge
        self.discount = discount
        self.extra_charges = extra_charges

        self.delivery_time = delivery_time
        self.pickup_time = pickup_time
        self.delivery_date = delivery_date
        self.pickup_date = pickup_date


class tracking_details():
    def __init__(self, carrier: str, tracking_number: str, shipment_date: str = None, events: List[TrackingEvent] = []): 
        self.carrier = carrier
        self.events = events
        self.shipment_date = shipment_date
        self.tracking_number = tracking_number