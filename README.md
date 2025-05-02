# QR Code Telegram Bot

A Telegram bot built with Python and the Aiogram framework, designed to create and decode QR codes seamlessly. This bot allows users to generate QR codes from text and extract data from QR code images, with robust user management and feedback features.

## Features

- **QR Code Generation**: Users can send text (e.g., URLs, messages, or contacts) to generate a QR code. The bot uses the `pyqrcode` library to create a PNG image, saves it in a structured directory, and sends it back with a styled caption.
- **QR Code Decoding**: The bot processes uploaded images to detect and decode QR codes using OpenCV (`cv2`). It returns the extracted content or, if decoding fails, crops the QR code region and suggests online decoders.
- **User Management**: Integrates with a PostgreSQL database via `asyncpg` to store user details (username, full name, Telegram ID). Admins receive notifications about new users and the total user count.
- **Feedback System**: Users can submit feedback, which is sent to admins for review, fostering user engagement.
- **File Management**: Utilizes `pathlib` and `os` to organize generated and processed files with unique filenames (using timestamps or incremental indices).
- **Error Handling**: Gracefully handles errors, such as invalid inputs or decoding issues, providing clear messages or fallback options.

## Tech Stack

- **Python Libraries**:
  - `aiogram`: Telegram bot framework
  - `pyqrcode`: QR code generation
  - `opencv-python` (`cv2`): QR code detection and decoding
  - `asyncpg`: PostgreSQL database interaction
  - `numpy`: Image processing support
  - Standard libraries: `time`, `pathlib`, `os`, `re`
- **Database**: PostgreSQL (for user data storage)
- **Platform**: Telegram

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/qr-code-bot.git
   cd qr-code-bot
   ```

2. Install dependencies:
   ```bash
   pip install aiogram pyqrcode opencv-python asyncpg numpy
   ```

3. Set up environment variables:
   - Create a `.env` file with your Telegram bot token and database credentials (e.g., `BOT_TOKEN`, `DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`).
   - Configure the `ADMINS` list in `data/config.py` for admin notifications.

4. Set up a PostgreSQL database and update the connection details in your configuration.

5. Run the bot:
   ```bash
   python bot.py
   ```

## Usage

- **Start the Bot**: Use the `/start` command to receive a welcome message and main menu.
- **Create QR Code**: Select "Create QRcode" from the menu, send text, and receive a QR code image.
- **Decode QR Code**: Send an image containing a QR code, and the bot will extract and return its content.
- **Leave Feedback**: Choose "Feedback" from the menu and submit your comments.

## Directory Structure

- `downloads/categories/photoes/`: Stores downloaded images and generated QR codes.
- `keyboards/`: Contains default keyboard layouts for the bot.
- `states/`: Defines finite state machine (FSM) states for handling user input.
- `data/config.py`: Configuration file for bot settings (e.g., admin IDs).

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for bug reports, feature requests, or improvements.
