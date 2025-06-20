# py-max-api

Python SDK for the MAX Bot API

## Installation

```bash
pip install py-max-api
```

## Quick Start

```python
from py_max_api import Bot, Dispatcher

from py_max_api.bot_types import Update


bot = Bot('YOUR_TOKEN')
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
def start(update: Update):
    bot.send_message(update.message.sender.user_id, text="Hello, world!")

if __name__ == "__main__":
    dp.start_polling()
```

## Features

- Full support for MAX Bot API methods
- Dispatcher with decorators for easy event handling
- Type-safe models (Pydantic)
- Built-in filters and extensibility

## License

MIT 