import logging
from typing import Union

from pyrogram import filters, Client, types
from pyrogram.types import User, Message

from config import KEYWORDS, WHO_TO_SEND_USERNAME
from loader import app
import re
logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO,
                    # level=logging.DEBUG,  # Можно заменить на другой уровень логгирования.
                    )


def extract_username(text: str) -> Union[None, str]:
    username = re.search("(?<=@)\w+", text)
    if username:
        return username.group()
    return None


def get_fullname(message: Message) -> str:
    name = message.from_user.first_name
    if message.from_user.last_name:
        name += f' {message.from_user.last_name}'
    return name


def has_keyword(text, keywords):
    return any(keyword in text for keyword in keywords)


@app.on_message(~filters.service)
async def watch(client: Client, message: types.Message):
    if message.text and has_keyword(message.text, KEYWORDS):
        # username = extract_username(message.text)
        try:
            user = await app.get_users(WHO_TO_SEND_USERNAME)
            # await app.forward_messages(user.id, message.chat.id, message.id)

            if not message.from_user.username:
                name = get_fullname(message)
            else:
                name = f'@{message.from_user.username}'
            await app.send_message(user.id, f'{message.text}\n\nАвтор: {name}')
            logging.info(f'Отправил сообщение от {name}')
        except Exception as e:
            logging.error(e)


if __name__ == '__main__':
    app.run()
