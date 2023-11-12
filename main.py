import re
import wget
import os
from pyrogram import Client, filters

app = Client("herrTeufel", api_id=29238210, api_hash='fa0dc3269a82546efd021964cd2c7bda')


@app.on_message(filters.text)
def on_message(client, message):
    if "Download" in message.text and message.from_user.id == client.get_me().id:
        link_match = re.search(r'\b(?:https?://|www\.)\S+\b', message.text)
        if link_match:
            file_url = link_match.group(0)
            downloaded_file = wget.download(file_url)
            client.send_document(
                chat_id=message.chat.id,
                document=downloaded_file,
                caption="خدمت شما!",
                reply_to_message_id=message.id
            )
            os.remove(downloaded_file)


app.run()
