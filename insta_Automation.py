# import os 
# import glob
# cookie_del = glob.glob("config/*cookie.json")
# os.remove(cookie_del[0])

# from os import remove
# remove("path of JSON file")

import os
if os.path.isfile("path/to/config/file.json"):
    os.remove("path/to/config/file.json")

import instabot
# rest of your code goes here

from instabot import Bot
bot = Bot()
bot.login(username="sahilborole30",password="borole30")
# bot.follow("the.boys.life")

# bot.upload_photo("D:\python\Py_project\hw.png")

# bot.unfollow("the.boys.life")

# bot.send_message("Helo ,Good Morning",["the.boys.life","mom"])

# followers = bot.get_user_followers("sahilborole30")

# for fol in followers:
#     print(bot.get_user_info(fol))

following = bot.get_user_following("sahilborole30")

for fol in following:
    print(bot.get_user_info(fol))

