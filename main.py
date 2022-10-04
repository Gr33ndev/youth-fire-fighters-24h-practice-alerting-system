# importing the required modules
import json
import time
from datetime import datetime
from tkinter import *

import pygame

blink_time_in_minutes = 1
length_of_sound_in_seconds = 30
default_operation_description = "Derzeit kein Alarm"
default_address = "Ihr könnt ja Knoten & Stiche üben :-)"

root = Tk()

root.title("Youth Fire Fighters 24h Practise Alerting System by Gilian Rehm")

root.geometry("1080x720")

root.grid()

# Config column rows and cols
Grid.rowconfigure(root, 0, weight=0)
Grid.rowconfigure(root, 1, weight=0)
Grid.rowconfigure(root, 2, weight=1)
Grid.rowconfigure(root, 3, weight=1)
Grid.columnconfigure(root, 1, weight=1)
Grid.columnconfigure(root, 2, weight=1)
Grid.columnconfigure(root, 3, weight=1)
Grid.columnconfigure(root, 4, weight=1)

# Add description text
description_frame = Frame(root, width=775, height=50, borderwidth=1, relief="solid", bg="lightgrey")
description_frame.grid(row=0, column=1, columnspan=4, sticky="nsew")
description_label = Label(description_frame, text="Description", font=("Arial", 24), width=80, bg="lightgrey")
description_label.pack()

# Add address text
address_frame = Frame(root, width=775, height=50, borderwidth=1, relief="solid", bg="lightgrey")
address_frame.grid(row=1, column=1, columnspan=4, sticky="nsew")
address_label = Label(address_frame, text="Address", font=("Arial", 20), width=100, bg="lightgrey")
address_label.pack()

# Add 1/19 label
one_nineteen_frame = Frame(root, width=100, height=100, borderwidth=1, relief="solid")
one_nineteen_frame.grid(row=2, column=1, sticky="nsew")
one_nineteen_label = Label(one_nineteen_frame, text="1-19", width=20, height=10, font=("Arial", 20))
one_nineteen_label.pack()

# Add 1/42 label
one_forty_two_frame = Frame(root, width=100, height=100, borderwidth=1, relief="solid")
one_forty_two_frame.grid(row=2, column=2, sticky="nsew")
one_forty_two_label = Label(one_forty_two_frame, text="1-42", width=20, height=10, font=("Arial", 20))
one_forty_two_label.pack()

# Add 2/42 label
two_forty_two_frame = Frame(root, width=100, height=100, borderwidth=1, relief="solid")
two_forty_two_frame.grid(row=2, column=3, sticky="nsew")
two_forty_two_label = Label(two_forty_two_frame, text="2-42", width=20, height=10, font=("Arial", 20))
two_forty_two_label.pack()

# Add 3/48 label
three_forty_eight_frame = Frame(root, width=100, height=100, borderwidth=1, relief="solid")
three_forty_eight_frame.grid(row=2, column=4, sticky="nsew")
three_forty_eight_label = Label(three_forty_eight_frame, text="3-48", width=20, height=10, font=("Arial", 20))
three_forty_eight_label.pack()

# Add oil label
oil_frame = Frame(root, width=100, height=100, borderwidth=1, relief="solid")
oil_frame.grid(row=3, column=1, sticky="nsew")
oil_label = Label(oil_frame, text="ÖL-A", width=20, height=10, font=("Arial", 20))
oil_label.pack()

# Add hose cart label
hose_cart_frame = Frame(root, width=100, height=100, borderwidth=1, relief="solid")
hose_cart_frame.grid(row=3, column=2, sticky="nsew")
hose_cart_label = Label(hose_cart_frame, text="SW-A", width=20, height=10, font=("Arial", 20))
hose_cart_label.pack()

# Add unit 1 label
unit_one_frame = Frame(root, width=100, height=100, borderwidth=1, relief="solid")
unit_one_frame.grid(row=3, column=3, sticky="nsew")
unit_one_label = Label(unit_one_frame, text="Zug 1", width=20, height=10, font=("Arial", 20))
unit_one_label.pack()

# Add unit 2 label
unit_two_frame = Frame(root, width=100, height=100, borderwidth=1, relief="solid")
unit_two_frame.grid(row=3, column=4, sticky="nsew")
unit_two_label = Label(unit_two_frame, text="Zug 2", width=20, height=10, font=("Arial", 20))
unit_two_label.pack()

root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)

root.update()


def one_nineteen_on():
    one_nineteen_frame.config(bg="red")
    one_nineteen_label.config(bg="red")


def one_nineteen_off():
    one_nineteen_frame.config(bg="SystemButtonFace")
    one_nineteen_label.config(bg="SystemButtonFace")


def one_forty_two_on():
    one_forty_two_frame.config(bg="red")
    one_forty_two_label.config(bg="red")


def one_forty_two_off():
    one_forty_two_frame.config(bg="SystemButtonFace")
    one_forty_two_label.config(bg="SystemButtonFace")


def two_forty_two_on():
    two_forty_two_frame.config(bg="red")
    two_forty_two_label.config(bg="red")


def two_forty_two_off():
    two_forty_two_frame.config(bg="SystemButtonFace")
    two_forty_two_label.config(bg="SystemButtonFace")


def three_forty_eight_on():
    three_forty_eight_frame.config(bg="red")
    three_forty_eight_label.config(bg="red")


def three_forty_eight_off():
    three_forty_eight_frame.config(bg="SystemButtonFace")
    three_forty_eight_label.config(bg="SystemButtonFace")


def oil_on():
    oil_frame.config(bg="red")
    oil_label.config(bg="red")


def oil_off():
    oil_frame.config(bg="SystemButtonFace")
    oil_label.config(bg="SystemButtonFace")


def hose_cart_on():
    hose_cart_frame.config(bg="red")
    hose_cart_label.config(bg="red")


def hose_cart_off():
    hose_cart_frame.config(bg="SystemButtonFace")
    hose_cart_label.config(bg="SystemButtonFace")


def unit_one_on():
    unit_one_frame.config(bg="red")
    unit_one_label.config(bg="red")


def unit_one_off():
    unit_one_frame.config(bg="SystemButtonFace")
    unit_one_label.config(bg="SystemButtonFace")


def unit_two_on():
    unit_two_frame.config(bg="red")
    unit_two_label.config(bg="red")


def unit_two_off():
    unit_two_frame.config(bg="SystemButtonFace")
    unit_two_label.config(bg="SystemButtonFace")


def blink(one_nineteen, one_forty_two, two_forty_two, three_forty_eight, oil, hose_cart, unit_one, unit_two):
    for i in range(blink_time_in_minutes * 60):
        if one_nineteen:
            one_nineteen_on()
            root.update()

        if one_forty_two:
            one_forty_two_on()
            root.update()

        if two_forty_two:
            two_forty_two_on()
            root.update()

        if three_forty_eight:
            three_forty_eight_on()
            root.update()

        if oil:
            oil_on()
            root.update()

        if hose_cart:
            hose_cart_on()
            root.update()

        if unit_one:
            unit_one_on()
            root.update()

        if unit_two:
            unit_two_on()
            root.update()

        time.sleep(0.5)

        if one_nineteen:
            one_nineteen_off()
            root.update()

        if one_forty_two:
            one_forty_two_off()
            root.update()

        if two_forty_two:
            two_forty_two_off()
            root.update()

        if three_forty_eight:
            three_forty_eight_off()
            root.update()

        if oil:
            oil_off()
            root.update()

        if hose_cart:
            hose_cart_off()
            root.update()

        if unit_one:
            unit_one_off()
            root.update()

        if unit_two:
            unit_two_off()
            root.update()

        time.sleep(0.5)


def setDescription(description):
    description_label.config(text=description)


def setAddress(address):
    address_label.config(text=address)


def on_off_to_bool(on_off):
    if on_off == "on":
        return True
    else:
        return False


def init():
    setAddress(default_address)
    setDescription(default_operation_description)
    one_nineteen_off()
    root.update()
    one_forty_two_off()
    root.update()
    two_forty_two_off()
    root.update()
    three_forty_eight_off()
    root.update()
    oil_off()
    root.update()
    hose_cart_off()
    root.update()
    unit_one_off()
    root.update()
    unit_two_off()
    root.update()


init()


def alarm(date_time, operation_description, address, one_nineteen, one_forty_two, two_forty_two, three_forty_eight, oil,
          hose_cart, unit_one, unit_two):
    if datetime.strptime(date_time, "%Y-%m-%d, %H:%M") < datetime.now():
        print(date_time + " < " + str(datetime.now()))
        return

    while True:
        root.update()

        if date_time == datetime.now().strftime("%Y-%m-%d, %H:%M"):
            print("Alarm is ringing")

            setDescription(operation_description)
            setAddress(address)

            try:
                pygame.mixer.init()
                pygame.mixer.music.load("audio.mp3")
                pygame.mixer.music.play(int(blink_time_in_minutes * 60 / length_of_sound_in_seconds))
            except:
                print("Error playing audio")

            blink(one_nineteen, one_forty_two, two_forty_two, three_forty_eight, oil, hose_cart, unit_one, unit_two)

            setDescription(default_operation_description)
            setAddress(default_address)

            print("Alarm is off")

            break


def set_alarm(operation_description, address, operation_date, operation_time, one_nineteen, one_forty_two,
              two_forty_two, three_forty_eight, oil, hose_cart, unit_one, unit_two):
    if "-" not in operation_date or ":" not in operation_time:
        print("ERROR")
        return

    one_nineteen = on_off_to_bool(one_nineteen)
    one_forty_two = on_off_to_bool(one_forty_two)
    two_forty_two = on_off_to_bool(two_forty_two)
    three_forty_eight = on_off_to_bool(three_forty_eight)
    oil = on_off_to_bool(oil)
    hose_cart = on_off_to_bool(hose_cart)
    unit_one = on_off_to_bool(unit_one)
    unit_two = on_off_to_bool(unit_two)

    print("Operation Description: " + operation_description)
    print("Address: " + address)
    print("operationDate, operationTime: " + operation_date + " - " + operation_time)
    print("1-19: " + str(one_nineteen))
    print("1-42: " + str(one_forty_two))
    print("2-42: " + str(two_forty_two))
    print("3-48: " + str(three_forty_eight))
    print("Oil: " + str(oil))
    print("Hose Cart: " + str(hose_cart))
    print("Zug 1: " + str(unit_one))
    print("Zug 2: " + str(unit_two))

    alarm(operation_date + ", " + operation_time, operation_description, address, one_nineteen, one_forty_two,
          two_forty_two, three_forty_eight, oil, hose_cart, unit_one, unit_two)


config_data = json.load(open("config.json"))

numberOfOperations = int(config_data[0]["numberOfOperations"])
print(numberOfOperations)

sorted_config_data = config_data[1:]

sorted_config_data.sort(key=lambda x: x["operationDate"] + x["operationTime"])

print("Sorted")

for i in range(numberOfOperations):
    print(sorted_config_data[i])
    set_alarm(sorted_config_data[i]["operationDescription"], sorted_config_data[i]["address"],
              sorted_config_data[i]["operationDate"], sorted_config_data[i]["operationTime"],
              sorted_config_data[i]["1-19"], sorted_config_data[i]["1-42"], sorted_config_data[i]["2-42"],
              sorted_config_data[i]["3-48"], sorted_config_data[i]["oil"], sorted_config_data[i]["hoseCart"],
              sorted_config_data[i]["unitOne"], sorted_config_data[i]["unitTwo"])

# keep alive
while True:
    root.update()
