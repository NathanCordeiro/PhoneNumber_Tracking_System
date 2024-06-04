# PhoneNumber_Tracking_System 📱🌐
---

The Phone Number Tracker is a Python application that allows you to determine the country associated with a given phone number. 
It uses a JSON file containing country codes to perform the lookup.

## Features 
- **Input Field:** Enter a phone number in the provided input field.
- **Check Button:** Click the `“Check”` button to retrieve the associated country name.
- **Clear Button:** Use the `“Clear”` button to reset the input field and result label.

## How it works
- The application loads country codes from a JSON file `country_codes.json.`
- When a valid phone number is entered, the app identifies the corresponding country.
- Invalid phone numbers trigger an error message.

## Usage
- Make sure you have the `country_codes.json` file in the same directory as your script.
- Run the script, and the GUI window will appear.
  ```sh
   python PhoneNumber_Track.py
   ```
- Enter a phone number and click `“Check”` to see the associated country.

## Dependencies
- Python 3
- tkinter

## Contributions
- Contributions are welcome! If you find any issues or have suggestions, feel free to open an issue or submit a pull request.

## License
- This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

> [!NOTE]
> Feel free to customize and enhance this project as needed! 😊
