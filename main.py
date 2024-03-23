from abc import ABC, abstractmethod

class ChatTransport(ABC):

    @abstractmethod
    def add_handler(self, event):
        pass

    @abstractmethod
    async def send_message(self, msg):
        pass

    @abstractmethod
    async def run(self):
        pass

class ChatTransportDiscord(ChatTransport):
    # Implementation specific to Discord API

class ChatTransportTelegram(ChatTransport):
    # Implementation specific to Telegram API

class SimpleBusinessLogicBot:

    def init(self, chat_transport):
        self.transport = chat_transport

    async def handle_message(self, event):
        msg = event.message  # Assuming event object has message attribute
        response = f"Hi! Your message was received: {msg}"
        await self.transport.send_message(response)

    async def run(self):
        await self.transport.add_handler(self.handle_message)
        await self.transport.run()

# Example Usage
if name == "main":
    # Choose the chat transport (Discord or Telegram)
    transport = ChatTransportDiscord()  # Replace with ChatTransportTelegram for Telegram

    # Initialize and run the bot
    bot = SimpleBusinessLogicBot(transport)
    asyncio.run(bot.run())
