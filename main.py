# -*- coding: utf-8 -*-
import time
import uuid
from random import randint
from facebook_business.adobjects.serverside.event import Event
from facebook_business.adobjects.serverside.event_request import EventRequest
from facebook_business.adobjects.serverside.user_data import UserData
from facebook_business.adobjects.serverside.custom_data import CustomData
from facebook_business.adobjects.serverside.action_source import ActionSource
from facebook_business.api import FacebookAdsApi

access_token = 'EAASVRpCCd0YBAPZBUuVJa4FaStlGF9ZBxjGkpBgbcxZCh0enFs47XAClP7jWqfNjNucFDkEZC6cUFhWt5R1e3BZAVFkp7d0ePLQLxGdukUTQ87BqqOM0L6cc4u3UbHnMOL8ZBd2IZB2FrIw9Hszl7aEBrbGUJ6C9priD8Ce8XVi0mquGTMpTdGKiPVZCZB7FNapAZD'
pixel_id = '885868472454982'

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

FacebookAdsApi.init(access_token=access_token)

user_data = UserData(
    client_ip_address = '91.242.112.214',
    client_user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    fbc='fb.1.' + str(int(time.time())) + '.' +  str(random_with_N_digits(10)),
    fbp='fb.1.' + str(int(time.time())) + '.' + str(uuid.uuid4().hex)
)

custom_data = CustomData(
    currency='usd',
    value=1.0
)

event = Event(
    event_name='Purchase',
    event_time=int(time.time()),
    action_source = ActionSource.OTHER,
    user_data=user_data,
    custom_data=custom_data,
)

events = [event]

event_request = EventRequest(
    events=events,
    pixel_id=pixel_id)

event_response = event_request.execute()

print(event_response)


