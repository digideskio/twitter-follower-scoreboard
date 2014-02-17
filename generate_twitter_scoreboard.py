#!/usr/bin/env python
# encoding: utf-8
"""
generate_twitter_scoreboard.py

Use data in config.yml to generate follower-count information for a set of Twitter screennames,
and output to a JSON file

Created by Sanders Kleinfeld on Sun Feb 16 15:46:00 EST 2014
Copyright (c) 2014 Sanders Kleinfeld. All rights reserved.
"""

import json
import os
import twitter
import yaml

CONFIG = os.path.join(os.path.dirname(__file__), 'config.yml')
JSON_OUTPUT_FILE = os.path.join(os.path.dirname(__file__), 'public', 'scoreboard.json')

json_output = [] # start with an empty list

f = open(CONFIG)
app_config = yaml.safe_load(f)
f.close()

auth_creds = twitter.oauth.OAuth(app_config['oauth_token'], app_config['oauth_secret'],
                                 app_config['consumer_key'], app_config['consumer_secret'])

screen_names = [user['screen_name'] for user in app_config['twitter_users']]

tw_obj = twitter.Twitter(auth=auth_creds)

userdata = tw_obj.users.lookup(screen_name=','.join(screen_names), timeout=1)

for user in userdata:
    # Match up the user record in our config with the corresponding record in returned Twitter data using "screen_name"
    corresponding_config_user = [config_user for config_user in app_config['twitter_users'] if config_user['screen_name'].lower() == user['screen_name'].lower()][0]
    json_output.append({'screen_name': user['screen_name'], 
                        'display_name': corresponding_config_user['display_name'],
                        'followers_count': user['followers_count'],
                        'avatar': user['profile_image_url']
                        })

# Sort list by follower count, in descending order
json_output.sort(key=lambda user: user['followers_count'], reverse=True)

f = open(JSON_OUTPUT_FILE, 'w')
f.write(json.dumps(json_output, indent=1, sort_keys=True))
f.close()
