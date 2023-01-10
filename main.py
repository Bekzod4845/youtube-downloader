import os
from aiogram import *
from config import *
from pytube import YouTube

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, "SALOM YOUTUBEDAN VIDEO YUKLOVCHI BOT\n"
                                    "SILKA TASHLANG")


@dp.message_handler()
async def bot_message(message: types.Message):
    chat_id = message.chat.id
    url = message.text
    yt = YouTube(url)
    if message.text.startswith == 'https://www.youtube.com/' or 'https://youtu.be/':
        await bot.send_message(chat_id, f"*VIDEO YUKLANYABDI* : {yt.title}\n"
                                        f"*KANAL* : [{yt.author}]({yt.channel_url})", parse_mode="Markdown")
        await download_youtube_video(url, message, bot)


async def download_youtube_video(url, message, bot):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension="mp4")
    stream.get_highest_resolution().download(f'{message.chat.id}', f'{message.chat.id}_{yt.title}')
    with open(f"{message.chat.id}/{message.chat.id}_{yt.title}", 'rb') as video:
        await bot.send_video(message.chat.id, video, caption="*BU VIDEO*", parse_mode="Markdown")
        os.remove(f"{message.chat.id}/{message.chat.id}_{yt.title}")


if __name__ == '__main__':
    executor.start_polling(dp)
