from datetime import datetime, timedelta
from email import message

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from create_user import CreateUser


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()
create_user = CreateUser()
new_user = create_user.create_user()
flight_search = FlightSearch()


ORIGIN_CITY = "LON"


if sheet_data[0]["iataCode"] == "":
    for data in sheet_data:
        data["iataCode"] = flight_search.get_destination_code(data["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_data()

tomrrow = datetime.now() + timedelta(days=1)
six_month = datetime.now() + timedelta(days=6*30)

for destination in sheet_data:
    flight = flight_search.search_flight_prices(
        origin_city_code=ORIGIN_CITY,
        destination_city_code=destination["iataCode"],
        from_time=tomrrow,
        to_time=six_month
    )
    if flight is not None:
        if flight.price < destination["lowestPrice"]:
            message += f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

            if flight.stop_overs > 0:
                message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

            notification_manager.send_sms(message)
