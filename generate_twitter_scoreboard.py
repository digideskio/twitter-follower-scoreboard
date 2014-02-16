#!/usr/bin/env python
# encoding: utf-8
"""
generate_twitter_scoreboard.py

Created by Sanders Kleinfeld on Sun Feb 16 15:46:00 EST 2014
Copyright (c) 2014 Sanders Kleinfeld. All rights reserved.
"""

import json
import os
import twitter
import yaml

CONFIG = os.path.join(os.path.dirname(__file__), 'config.yml')
f = open(CONFIG)
app_config = yaml.safe_load(f)
f.close()

auth_creds = twitter.oauth.OAuth(app_config['oauth_token'], app_config['oauth_secret'],
                                 app_config['consumer_key'], app_config['consumer_secret'])

tw_obj = twitter.Twitter(auth=auth_creds)
