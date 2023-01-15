import time
import uuid
from random import randint
from facebook_business.adobjects.serverside.content import Content
from facebook_business.adobjects.serverside.custom_data import CustomData
from facebook_business.adobjects.serverside.delivery_category import DeliveryCategory
from facebook_business.adobjects.serverside.event import Event
from facebook_business.adobjects.serverside.event_request import EventRequest
from facebook_business.adobjects.serverside.gender import Gender
from facebook_business.adobjects.serverside.user_data import UserData
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.serverside.action_source import ActionSource

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

access_token = 'EAASVRpCCd0YBAPZBUuVJa4FaStlGF9ZBxjGkpBgbcxZCh0enFs47XAClP7jWqfNjNucFDkEZC6cUFhWt5R1e3BZAVFkp7d0ePLQLxGdukUTQ87BqqOM0L6cc4u3UbHnMOL8ZBd2IZB2FrIw9Hszl7aEBrbGUJ6C9priD8Ce8XVi0mquGTMpTdGKiPVZCZB7FNapAZD'
pixel_id = '885868472454982'

FacebookAdsApi.init(access_token=access_token)

for i in range(1, 100):
        
    user_data_0 = UserData(
        client_ip_address="192.168.0.1",
        client_user_agent="test",
        fbc='fb.1.' + str(int(time.time())) + '.' +  str(random_with_N_digits(10)),
        fbp='fb.1.' + str(int(time.time())) + '.' + str(uuid.uuid4().hex),
    )
    event_0 = Event(
        event_name="ViewContent",
        event_time= int(time.time()),
        user_data=user_data_0,
        action_source=ActionSource.APP
    )

    events = [event_0]

    event_request = EventRequest(
        events=events,
        pixel_id=pixel_id
    )

    event_response = event_request.execute()

    print(event_response)