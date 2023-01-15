from flask import Flask, redirect, send_file, jsonify, make_response
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



app = Flask(__name__, static_url_path='/static')

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def purchase(access_token, pixel_id, ip, money):
    FacebookAdsApi.init(access_token=access_token)
    user_data = UserData(
            client_ip_address = ip,
            client_user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
            fbc='fb.1.' + str(int(time.time())) + '.' +  str(random_with_N_digits(10)),
            fbp='fb.1.' + str(int(time.time())) + '.' + str(uuid.uuid4().hex)
        )

    custom_data = CustomData(
            currency='usd',
            value=float(money)
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

    return event_response

def subscribe(access_token, pixel_id, ip, money):
    FacebookAdsApi.init(access_token=access_token)
    user_data = UserData(
            client_ip_address = ip,
            client_user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
            fbc='fb.1.' + str(int(time.time())) + '.' +  str(random_with_N_digits(10)),
            fbp='fb.1.' + str(int(time.time())) + '.' + str(uuid.uuid4().hex)
        )

    custom_data = CustomData(
            currency='usd',
            value=float(money)
        )

    event = Event(
            event_name='Subscribe',
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

    return event_response

#http://127.0.0.1:5000/send_action/EAASVRpCCd0YBAPZBUuVJa4FaStlGF9ZBxjGkpBgbcxZCh0enFs47XAClP7jWqfNjNucFDkEZC6cUFhWt5R1e3BZAVFkp7d0ePLQLxGdukUTQ87BqqOM0L6cc4u3UbHnMOL8ZBd2IZB2FrIw9Hszl7aEBrbGUJ6C9priD8Ce8XVi0mquGTMpTdGKiPVZCZB7FNapAZD/885868472454982/91.242.112.214/0/10
@app.get('/send_action/<access_token>/<pixel_id>/<ip>/<int:a_type>/<money>')
def send_action(access_token, pixel_id, ip, a_type, money):
    try:
        if a_type == 0:
            event = purchase(access_token, pixel_id, ip, money)
        else:
            event = subscribe(access_token, pixel_id, ip, money)

        return make_response(jsonify(str(event)), 201)
    except Exception as ex:
        return make_response(jsonify(str(ex)), 201)

app.run()