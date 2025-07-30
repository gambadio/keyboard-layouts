# Keyboard Layout Manager

A simple graphical tool for managing keyboard layouts on Windows.  
Easily add or remove input languages using a convenient GUI.

## Features

- View currently installed keyboard layouts.
- Add new layouts from a comprehensive list of supported languages.
- Remove existing layouts with one click.
- Built-in mapping of layout codes to human-readable names.

## Supported Layouts

Supports all major keyboard layouts recognized by Windows, including:
- English (US, UK, Dvorak, International)
- Arabic, Bulgarian, Chinese (Traditional/Simplified), Czech, Danish,
  German, Greek, Spanish, French, Hebrew, Hungarian, Italian,
  Japanese, Korean, Dutch, Norwegian, Polish, Portuguese,
  Russian, Turkish ... and many more!

*(See `keyboard_layout_manager.py` for the full list.)*

## Requirements

- **Platform:** Windows only
- **Python:** 3.x
- **Dependencies:**
    - `tkinter` (standard library)
    - `pywin32` (`win32api`, `win32con`)
    - Administrator privileges may be required to change system input settings.

Install dependencies with:

```sh
pip install pywin32
```

## Usage

1. Run the application:
   ```sh
   python keyboard_layout_manager.py
   ```
2. The GUI will show your current keyboard layouts.
3. Use the dropdown to select a layout to add; click "Add Layout".
4. Select an installed layout in the list and click "Remove Selected Layout" to uninstall it.
5. Click "Refresh List" if changes do not appear immediately.
> **Note:** Changes may require you to log out or restart certain applications to take effect.

## File Structure
```
keyboard-layouts/
└── keyboard_layout_manager.py   # Main application script and layout data
```
## Contributing
Pull requests are welcome!  
If you want to contribute additional features or bugfixes:
1. Fork this repository.
2. Create a new branch (`git checkout -b feature/my-feature`)
3. Commit your changes and push your branch.
4. Open a pull request describing your changes.
## License
This project is licensed for private/personal use only (see LICENSE file).
If you wish to use this project commercially please contact ricardo.kupper@adalala.com .
---
**Repository:** https://github.com/gambadio/keyboard-layouts
