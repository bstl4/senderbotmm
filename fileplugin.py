from mmpy_bot import Plugin, listen_to
from mmpy_bot import Message

class MyPlugin(Plugin):

    @listen_to("Отправь сообщения людям")

    async def send_message (self, message: Message):
            self.driver.reply_to(message, "Без вопросов, гони список пользователей, свой токен и текст сообщения")
