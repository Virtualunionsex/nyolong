#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @Bae_wafaaa

import os
import logging

class Config:
  
#Your API HASH from my.telegram.org    
    API_ID = int(os.environ.get("API_ID", "16246834"))
#Your API HASH from my.telegram.org      
    API_HASH = os.environ.get("API_HASH", "29b3ffa9245c07f05375b92f38e8f13d")
#BOT TOKEN: @Botfather on telegram    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5716827359:AAE3NJPyZkXHATL8m3AmLVxFy0-NNhKOOog")
#Public channel username without '@'. Don't forget to add bot in channel as administrator.    
    FORCESUB = os.environ.get("FORCESUB", "nakama_asl") 
#Owner user id   
    AUTH  = os.environ.get("OWNER_ID", "1715348447")
#Pyrogram string session using (https://replit.com/@KindKobra/Pyrogram-String-Gen?v=1)
    SESSION = os.environ.get("SESSION", "AQA2XUL_FSP0tZDev1APSt4yiPX5z8wHwwV_Eo8PEp1u2PzVzzZbz-Weaw4f8ivwCvHD0_tVI51tGVENPzAv5JkjhjonCvsWoPQi5Af3arDeDc_jqGv0ct_8mqBYQAmyklCv9LorAO_kKI6yWT05zyrjkcxodW8RPMlcuMmWDbdDHJfGT3EodeIq5I4kcCjytTubRGTBkIAdOv8YuXmrzENG33yNv0NbmDtXmKY_98D5rXeSQjvcBUfHREw7fUbQ0g2YH5V9hYHrlpehTymXaLtQIa03kFan-oKjqrJgHPeh47dWXE3p1y5389yz-0ldEYOXX-oHBO8NQUv6f0jE8QILZj4j3wA")
  
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
