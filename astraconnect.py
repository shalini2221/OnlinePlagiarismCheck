# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 11:06:10 2022

@author: hp
"""

def getAstraHTTPClient():
    """Get Astra connection information from environment variables"""

    ASTRA_DB_ID = os.environ.get('ASTRA_DB_ID')
    ASTRA_DB_REGION = os.environ.get('ASTRA_DB_REGION')
    ASTRA_DB_APPLICATION_TOKEN = os.environ.get('ASTRA_DB_APPLICATION_TOKEN')
    
    # setup an Astra Client
    return create_client(astra_database_id=ASTRA_DB_ID,
                         astra_database_region=ASTRA_DB_REGION,
                         astra_application_token=ASTRA_DB_APPLICATION_TOKEN)