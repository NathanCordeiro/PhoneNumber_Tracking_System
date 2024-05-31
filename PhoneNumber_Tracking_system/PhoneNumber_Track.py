
import json
import tkinter as tk
from tkinter import messagebox

# Load the country codes JSON file
def load_country_codes(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", "Country codes JSON file not found")
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Unable to decode country codes JSON file")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    return {}

# Get the country name from the phone number
def get_country_from_number(phone_number, country_codes):
    for code in country_codes:
        if phone_number.startswith(code):
            return country_codes[code]
    return "Unknown Country"

# Function to show custom error message dialog
def show_error_dialog(message):
    error_dialog = tk.Toplevel(root)
    error_dialog.title("Error")
    error_dialog.geometry("250x100")
    error_dialog.configure(bg='black')

    tk.Label(error_dialog, text=message, fg="coral", bg="black", font=("Courier", 10)).pack(pady=10)
    tk.Button(error_dialog, text="OK", command=error_dialog.destroy, bg="coral", fg="black", font=("Courier", 10)).pack(pady=5)

# Function to handle the button click
def on_check_button_click():
    phone_number = entry.get()
    if phone_number.isdigit():  # Check if the input is a valid phone number
        country_name = get_country_from_number(phone_number, country_codes)
        result_label.config(text=f"Country: {country_name}")
    else:
        show_error_dialog("Invalid phone number format")



# Function to handle the clear button click
def on_clear_button_click():
    entry.delete(0, tk.END)  # Clear the entry widget
    result_label.config(text="Country: ")  # Reset the result label

# Load country codes
country_codes = load_country_codes('country_codes.json')

# Create the GUI
root = tk.Tk()
root.title("Phone Number Tracker")
root.geometry("300x200")
root.configure(bg='black')

tk.Label(root, text="Enter phone number:", fg="coral", bg="black", font=("Courier", 12,'bold')).pack(pady=5)
entry = tk.Entry(root, bg="coral", fg="black", width=30)
entry.pack(pady=5)

check_button = tk.Button(root, text="Check", command=on_check_button_click, bg="coral", fg="black", font=("Courier", 12,'bold'), width=10)
check_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear", command=on_clear_button_click, bg="coral", fg="black", font=("Courier", 12,'bold'), width=10)
clear_button.pack(pady=5)

result_label = tk.Label(root, text="Country: ", fg="coral", bg="black", font=("Courier", 12,'bold'))
result_label.pack(pady=5)

root.mainloop()
