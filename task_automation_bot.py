import pyautogui
import time
import webbrowser

def open_application(app_name):
    """Opens an application using the Start menu."""
    pyautogui.hotkey("win", "s")
    time.sleep(1)
    pyautogui.write(app_name, interval=0.1)
    time.sleep(1)
    pyautogui.press("enter")

def open_website(url):
    """Opens a website in the default web browser."""
    webbrowser.open(url)

def type_message(message):
    """Types a message automatically."""
    time.sleep(2)  # Wait for cursor focus
    pyautogui.write(message, interval=0.1)
    pyautogui.press("enter")

def take_screenshot(filename="screenshot.png"):
    """Takes a screenshot and saves it to a file."""
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)

def main():
    print("Starting Automation Bot...")
    time.sleep(2)
    
    # Open Notepad and type a message
    open_application("Notepad")
    time.sleep(2)
    type_message("Hello! This message is typed by an automation bot.")
    
    # Open a website
    open_website("https://www.google.com")
    
    # Take a screenshot
    time.sleep(3)  # Wait for the page to load
    take_screenshot("google_home.png")
    
    print("Automation completed.")

if __name__ == "__main__":
    main()
