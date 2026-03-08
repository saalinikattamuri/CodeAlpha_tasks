import os
import shutil
import re
import requests

# folders
IMAGE_FOLDER = "images"
OUTPUT_FOLDER = "output"

os.makedirs(IMAGE_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


# -----------------------------
# Move JPG Files
# -----------------------------
def move_jpg_files():
    source_folder = "."

    count = 0
    for file in os.listdir(source_folder):
        if file.lower().endswith(".jpg"):
            shutil.move(file, os.path.join(IMAGE_FOLDER, file))
            count += 1
            print(f"Moved: {file}")

    print(f"\nTotal JPG files moved: {count}")


# -----------------------------
# Extract Emails
# -----------------------------
def extract_emails():
    file_name = input("Enter text file name: ")

    try:
        with open(file_name, "r") as file:
            text = file.read()

        pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+'
        emails = re.findall(pattern, text)

        output_path = os.path.join(OUTPUT_FOLDER, "emails.txt")

        with open(output_path, "w") as file:
            for email in emails:
                file.write(email + "\n")

        print(f"\nEmails extracted: {len(emails)}")
        print(f"Saved to: {output_path}")

    except FileNotFoundError:
        print("File not found!")


# -----------------------------
# Scrape Webpage Title
# -----------------------------
def scrape_title():
    url = input("Enter webpage URL: ")

    try:
        response = requests.get(url)
        html = response.text

        title = re.search(r"<title>(.*?)</title>", html)

        if title:
            webpage_title = title.group(1)

            output_path = os.path.join(OUTPUT_FOLDER, "webpage_title.txt")

            with open(output_path, "w") as file:
                file.write(webpage_title)

            print("\nWebpage Title:", webpage_title)
            print("Saved to:", output_path)

        else:
            print("Title not found.")

    except requests.exceptions.RequestException:
        print("Invalid URL or connection problem.")


# -----------------------------
# Main Menu
# -----------------------------
def menu():
    while True:
        print("\n===== Python Task Automation Tool =====")
        print("1. Move JPG files to images folder")
        print("2. Extract emails from text file")
        print("3. Scrape webpage title")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            move_jpg_files()

        elif choice == "2":
            extract_emails()

        elif choice == "3":
            scrape_title()

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")


menu()