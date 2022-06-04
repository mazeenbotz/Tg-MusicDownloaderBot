class Chat:
    def __init__(self, msg):
        self.chat_id = msg['chat']['id']
        self.user_input = msg['text']
        self.user_input = self.user_input.replace('@MZN_MusicDownloaderBot', '')
        self.user_name = msg['from']['first_name']
        self.message_id = msg['message_id']

        self.messages = {
            'king': 'Our Bots'
START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("📨 Support", url="https://t.me/JaguarBots"),
            InlineKeyboardButton("📚 Source Code", url="https://github.com/ImJanindu/47MusicPlayerBot")
        ]
    ]
)
