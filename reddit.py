#! /usr/bin/python3
import praw
from praw.models import Message
import json
from time import sleep

print("Logging in...")
with open('creds/creds.json') as json_file:
    data = json.load(json_file)

    reddit = praw.Reddit(client_id=data["id"],
                         client_secret=data["secret"],
                         password=data["password"],
                         user_agent='testscript by /u/fakebot3',
                         username=data["username"])

    try:
        while 1:
            sleep(30)

            unread_messages = []
            for item in reddit.inbox.unread(limit=None):
                if isinstance(item, Message):
                    unread_messages.append(item)
                    print("-- {} --\n\n--> {}".format(item.subject, item.body))
                    answer = input("-> ")
                    answer = answer.replace("\\n", "\n\n\n\n")
                    if answer != "":
                        item.reply(answer, )
                    print("\n-- -- -- -- -- -- --\n")


            reddit.inbox.mark_read(unread_messages)


    except KeyboardInterrupt:
        print("Quitting....")
