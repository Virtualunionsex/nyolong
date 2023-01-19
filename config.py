#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @Bae_wafaaa

import os
import logging

class Config:
  
#Your API HASH from my.telegram.org    
    API_ID = int(os.environ.get("API_ID", "18576653"))
#Your API HASH from my.telegram.org      
    API_HASH = os.environ.get("API_HASH", "d29fa01d174ec2ac0d5bd415f052d173")
#BOT TOKEN: @Botfather on telegram    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5647123835:AAHN6PUFsVpCFkxYuSdHlX4iW_Wc8Nuo7IU")
#Public channel username without '@'. Don't forget to add bot in channel as administrator.    
    FORCESUB = os.environ.get("FORCESUB", "akimax") 
#Owner user id   
    AUTH  = os.environ.get("OWNER_ID", "5143506371")
#Pyrogram string session using (https://replit.com/@KindKobra/Pyrogram-String-Gen?v=1)
    SESSION = os.environ.get("SESSION", "AQCV8ShRKtiHlOomLaPBDfs2MQm6y9vnVbBwNtkqTp-fZj8RTw3nCbwsk9tw-V6KGztX9sfj8uxAwb0OpvEx__CBjO0DGnSuNv05xYbTikMrqe_HuPyhsCYVsEw9F32KKwKAxKE8Uf7nhAUvwMOqRqCmiXc44Z6BiuaYc91zNm6AeHox_-YzeXF6frc-bfPGadZt9iwWOvNfS4Rdyo21_SmpkDH7iZ7ydVtk_kLn4c-pHtK1iwU_HNW2VXskeNVv2wYSyhQXMwQRvY-jTusB5z2etzvAr4Vhm4H4I4jAnjxABaDeWULzW9Z5nAfbvyxIEfbwJyEa2pE8HDNURM_ZkmzqAAAAATKTrcMA")
  
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
