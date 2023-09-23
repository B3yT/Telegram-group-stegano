# Telegram-group-stegano
 
Telegram groups are not encrypted, to add an extra layer of security I created this app!

This Python code is a graphical application developed with PySide2 to perform secret message encoding and decoding operations within PNG images. The application also allows for cleaning up temporary files generated during the process. Here's a description of the main features and components of this code:

Imported Libraries:

PySide2: A library for creating user interfaces.
cryptosteganography: Used for encoding and decoding secret messages within images.
secure_delete: Used for secure file deletion.
PIL: A library for image processing.
numpy: A library for array and data manipulation.
shutil: Used for file manipulation operations.
telepot: A library for interacting with the Telegram API (for sending files).
Random Image Generation:

The generate_random_image function generates a random image with dimensions 128x128 pixels and saves it as "base.jpg."
App Class:

This class represents the graphical user interface of the application.
Widgets such as buttons, text areas, etc., are created and configured within this class.
Buttons labeled "Encrypt," "Decrypt," "Clean," "Quit," and "minimise" are configured to respond to user clicks.
The setup_css method defines CSS styles for the widgets.
The mousePressEvent, mouseMoveEvent, and mouseReleaseEvent methods allow the window to be moved by dragging the mouse.
Processing Methods:

The bouton_enc_clic, bouton_dec_clic, bouton_clean, and bouton_quit methods are called in response to user actions.
bouton_enc_clic: This method takes the content from the text area, encodes it into the "base.jpg" image, and then sends it to Telegram.
bouton_dec_clic: This method decodes a secret message from a PNG image downloaded from Telegram.
bouton_clean: This method deletes temporary files and clears the text area.
bouton_quit: This method deletes temporary files, clears the text area, and closes the application.
Tray System Configuration (system tray icon) to minimize the application.

The application is run by creating an instance of the App class and calling app.exec_() to start the main graphical user interface loop.

Ensure that you have the required libraries installed and replace specific values such as Telegram API keys before running the code. This application allows you to encode secret messages within images and decode them later. It also provides cleaning features to remove temporary files generated during the process.

https://user-images.githubusercontent.com/85953451/147551387-33cf4d83-da8b-4db8-bdff-572cf8a1a1d6.mp4


How to work:

in C:/  create a telesec folder
add TelSec.py and secplus.ico in this folder
and run!
