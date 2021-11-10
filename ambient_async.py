"""Run an example script to quickly test."""
import asyncio
import logging
import os
from aiohttp import ClientSession
import pandas as pd
from aioambient import API
from aioambient.errors import AmbientError

_LOGGER = logging.getLogger()

API_KEY = "05b65312f6124981839c02294a7f8316c4e91a8260fa4948b4a43cf41d474a02"
APP_KEY = "2b82311de1b0422d9c638a7001a9674ccd97402e1506437ca6dc6b29c11322d8"


async def main() -> None:
    """Create the aiohttp session and run the example."""
    logging.basicConfig(level=logging.INFO)
    async with ClientSession() as session:
        try:
            api = API(APP_KEY, API_KEY, session=session)

            devices = await api.get_devices()
            _LOGGER.info("Devices: %s", devices)

            for device in devices:
                details = await api.get_device_details(device["macAddress"])
                header = "dateutc,winddir,windspeedmph,windgustmph,maxdailygust,tempf,hourlyrainin,eventrainin,dailyrainin,weeklyrainin,monthlyrainin,totalrainin,baromrelin,baromabsin,humidity,tempinf,humidityin,uv,solarradiation,feelsLike,dewPoint,feelsLikein,dewPointin,loc,date\n"
                if not os.path.exists('log.csv'):
                    with open('log.csv','w+') as f:
                        f.write(header)
                for detail in details:
                    with open('log.csv','a+') as f:	
                        dateutc = detail['dateutc']
                        winddir = detail['winddir']
                        windspeedmph = detail['windspeedmph']
                        windgustmph = detail['windgustmph']
                        maxdailygust = detail['maxdailygust']
                        tempf = detail['tempf']
                        hourlyrainin = detail['hourlyrainin']
                        eventrainin = detail['eventrainin']
                        dailyrainin = detail['dailyrainin']
                        weeklyrainin = detail['weeklyrainin']
                        monthlyrainin = detail['monthlyrainin']
                        totalrainin = detail['totalrainin']
                        baromrelin = detail['baromrelin']
                        baromabsin = detail['baromabsin']
                        humidity = detail['humidity']
                        tempinf = detail['tempinf']
                        humidityin = detail['humidityin']
                        uv = detail['uv']
                        solarradiation = detail['solarradiation']
                        feelsLike = detail['feelsLike']
                        dewPoint = detail['dewPoint']
                        feelsLikein = detail['feelsLikein']
                        dewPointin = detail['dewPointin']
                        loc = detail['loc']
                        date = detail['date']
                        f.write(f'{dateutc},{winddir},{windspeedmph},{windgustmph},{maxdailygust},{tempf},{hourlyrainin},{eventrainin},{dailyrainin},{weeklyrainin},{monthlyrainin},{totalrainin},{baromrelin},{baromabsin},{humidity},{tempinf},{humidityin},{uv},{solarradiation},{feelsLike},{dewPoint},{feelsLikein},{dewPointin},{loc},{date}\n')
                _LOGGER.info("Device Details (%s): %s", device["macAddress"], details)

        except AmbientError as err:
            _LOGGER.error("There was an error: %s", err)


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())