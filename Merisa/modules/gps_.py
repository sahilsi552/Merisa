"""MIT License

Copyright (c) 2023-24 Noob-QuantamBot

          GITHUB: NOOB-MUKESH
          TELEGRAM: @MR_SUKKUN

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM
import asyncio
from .. import QuantamBot as mukesh
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
@mukesh.on_message(filters.command(["gps"]))
async def gps(bot, message):
#     await message.delete()
    if len(message.command) < 2:
        return await message.reply_text(
            "**Example:**\n\n`/gps [latitude , longitude]`")
    x = message.text.split(' ')[1].split(',')

    try:    
        """
        ---------github :-NOOB-MUKESH -----
        ---------telegram : @itz_legend_coder-----
        """
        geolocator = Nominatim(user_agent="legend-QuantamBot")
#         zoom=[0-18]

        location = geolocator.reverse(x,addressdetails=True, zoom=18)
        address=location.raw['address'] 
        # Traverse the data
        city = address.get('city', '')
        state = address.get('state', '')
        country = address.get('country', '')
        latitude = location.latitude
        longitude = location.longitude
        url=[[IKB("Open with:🌏ɢᴏᴏɢʟᴇ ᴍᴀᴘs ",url=f"https://www.google.com/maps/search/{latitude},{longitude}") ]]

    #     await message.reply_text(f"{gm}")
        await message.reply_venue(latitude, longitude,f"{city}",f"{state} ,{country}",reply_markup=IKM(url))
    except Exception as e:
        await message.reply_text(f"I can't find that \nDue to {e}")
@mukesh.on_message(filters.command(["distance"]))
async def distance(bot, message):
    await message.delete()
    if len(message.command) < 2:
        return await message.reply_text(
            "**Example:**\n\n`/distance [latitude , longitude],[latitude , longitude]`")

    x = message.text.split(" ")[1].split(',',2)[0:2]
    y = message.text.split(" ")[1].split(',',4)[2:4]
    try:

        """
        ---------github :-NOOB-MUKESH -----
        ---------telegram : @itz_legend_coder-----
        """
        distance=(great_circle(x,y).miles)

        await message.reply_text(f"Total distance between {x[0]},{x[1]} and {y[0]},{y[1]} is {distance}")
        
    except Exception as e:
        await message.reply_text(f"I can't find that \nDue to {e}")
        

__HELP__ = """
sᴇɴᴅs ʏᴏᴜ ᴛʜᴇ ɢᴘs ʟᴏᴄᴀᴛɪᴏɴ ᴏғ ᴛʜᴇ ɢɪᴠᴇɴ ǫᴜᴇʀʏ...

 ❍ /gps <ʟᴏᴄᴀᴛɪᴏɴ>*:* ɢᴇᴛ ɢᴘs ʟᴏᴄᴀᴛɪᴏɴ.
 ❍ /distance  to measure distance 
"""

__MODULE__ = "Gᴘs"