from channels.generic.websocket import AsyncWebsocketConsumer


class ConversationConsumer(AsyncWebsocketConsumer):
    """
    Consumer for handling WebSocket connections for chat conversations.
    """

    async def connect(self):
        """
        Called when the WebSocket is handshaking as part of the connection process.
        """
        await self.accept()

    async def disconnect(self, close_code):
        """
        Called when the WebSocket closes.
        """
        pass

    async def receive(self, text_data=None, bytes_data=None):
        """
        Called when a message is received from the WebSocket.
        """
        # Handle incoming messages here
        pass
