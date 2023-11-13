import re
import wget
import os
from pyrogram import Client, filters

app = Client("herrTeufel", api_id=29238210, api_hash='fa0dc3269a82546efd021964cd2c7bda')


# @app.on_message(filters.text)
# def on_message(client, message):
#     if "Download" in message.text and message.from_user.id == client.get_me().id:
#         link_match = re.search(r'\b(?:https?://|www\.)\S+\b', message.text)
#         if link_match:
#             file_url = link_match.group(0)
#             downloaded_file = wget.download(file_url)
#             client.send_document(
#                 chat_id=message.chat.id,
#                 document=downloaded_file,
#                 caption="خدمت شما!",
#                 reply_to_message_id=message.id
#             )
#             os.remove(downloaded_file)

@app.on_message(filters.text & filters.private)
def on_message(client, message):
    if "Download" in message.text:
        link_match = re.search(r'\b(?:https?://|www\.)\S+\b', message.text)
        if link_match:
            file_url = link_match.group(0)

            # Send "Please wait" message
            wait_message = client.send_message(
                chat_id=message.chat.id,
                text="در حال دانلود، لطفاً صبر کنید...",
                reply_to_message_id=message.id
            )

            try:
                downloaded_file = wget.download(file_url)

                # Send "Download completed" message
                client.send_message(
                    chat_id=message.chat.id,
                    text="دانلود با موفقیت انجام شد. در حال ارسال...",
                    reply_to_message_id=message.id
                )
                async def progress(current, total):
                    print(f"{current * 100 / total:.1f}%")

                # Send the downloaded file
                client.send_document(
                    chat_id=message.chat.id,
                    document=downloaded_file,
                    caption="خدمت شما!",
                    progress=progress,
                    reply_to_message_id=message.id
                )

            finally:
                # Remove the downloaded file
                os.remove(downloaded_file)

                # Optionally, you can send an additional message after the upload
                client.send_message(
                    chat_id=message.chat.id,
                    text="آپلود با موفقیت انجام شد."
                )


app.run()
