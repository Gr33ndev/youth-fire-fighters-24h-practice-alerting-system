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

root.geometry("750x350")

root.grid()

description_frame = Frame(root, width=775, height=50, borderwidth=1, relief="solid", bg="lightgrey")
description_frame.grid(row=0, column=1, columnspan=4)
description_label = Label(description_frame, text="Description", font=("Arial", 24), width=80, bg="lightgrey")
description_label.pack()

address_frame = Frame(root, width=775, height=50, borderwidth=1, relief="solid", bg="lightgrey")
address_frame.grid(row=1, column=1, columnspan=4)
address_label = Label(address_frame, text="Address", font=("Arial", 20), width=100, bg="lightgrey")
address_label.pack()

one_nineteen_frame = Frame(root, width=100, height=100, borderwidth=1, relief="solid")
one_nineteen_frame.grid(row=2, column=1)
one_nineteen_label = Label(one_nineteen_frame, text="1-19", width=20, height=10, font=("Arial", 20))
one_nineteen_label.pack()

one_forty_two_frame = Frame(root, width=100, height=100, borderwidth=1, relief="solid")
one_forty_two_frame.grid(row=2, column=2)
one_forty_two_label = Label(one_forty_two_frame, text="1-42", width=20, height=10, font=("Arial", 20))
one_forty_two_label.pack()

two_forty_two_frame = Frame(root, width=100, height=100, borderwidth=1, relief="solid")
two_forty_two_frame.grid(row=2, column=3)
two_forty_two_label = Label(two_forty_two_frame, text="2-42", width=20, height=10, font=("Arial", 20))
two_forty_two_label.pack()

three_forty_eight_frame = Frame(root, width=100, height=100, borderwidth=1, relief="solid")
three_forty_eight_frame.grid(row=2, column=4)
three_forty_eight_label = Label(three_forty_eight_frame, text="3-48", width=20, height=10, font=("Arial", 20))
three_forty_eight_label.pack()

oil_frame = Frame(root, width=100, height=100, borderwidth=1, relief="solid")
oil_frame.grid(row=3, column=1)
oil_label = Label(oil_frame, text="ÖL-A", width=20, height=10, font=("Arial", 20))
oil_label.pack()

hose_cart_frame = Frame(root, width=100, height=100, borderwidth=1, relief="solid")
hose_cart_frame.grid(row=3, column=2)
hose_cart_label = Label(hose_cart_frame, text="SW-A", width=20, height=10, font=("Arial", 20))
hose_cart_label.pack()

drk_frame = Frame(root, width=100, height=100, borderwidth=1, relief="solid")
drk_frame.grid(row=3, column=3)
drk_label = Label(drk_frame, text="DRK", width=20, height=10, font=("Arial", 20))
drk_label.pack()

police_frame = Frame(root, width=100, height=100, borderwidth=1, relief="solid")
police_frame.grid(row=3, column=4)
police_label = Label(police_frame, text="POL", width=20, height=10, font=("Arial", 20))
police_label.pack()

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


def drk_on():
    drk_frame.config(bg="red")
    drk_label.config(bg="red")


def drk_off():
    drk_frame.config(bg="SystemButtonFace")
    drk_label.config(bg="SystemButtonFace")


def police_on():
    police_frame.config(bg="red")
    police_label.config(bg="red")


def police_off():
    police_frame.config(bg="SystemButtonFace")
    police_label.config(bg="SystemButtonFace")


def blink(one_nineteen, one_forty_two, two_forty_two, three_forty_eight, oil, hose_cart, drk, police):
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

        if drk:
            drk_on()
            root.update()

        if police:
            police_on()
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

        if drk:
            drk_off()
            root.update()

        if police:
            police_off()
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
    drk_off()
    root.update()
    police_off()
    root.update()


init()


def alarm(date_time, operation_description, address, one_nineteen, one_forty_two, two_forty_two, three_forty_eight, oil,
          hose_cart, drk, police):
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

            blink(one_nineteen, one_forty_two, two_forty_two, three_forty_eight, oil, hose_cart, drk, police)

            setDescription(default_operation_description)
            setAddress(default_address)

            print("Alarm is off")

            break


def set_alarm(operation_description, address, operation_date, operation_time, one_nineteen, one_forty_two,
              two_forty_two, three_forty_eight, oil, hose_cart, drk, police):
    if "-" not in operation_date or ":" not in operation_time:
        print("ERROR")
        return

    one_nineteen = on_off_to_bool(one_nineteen)
    one_forty_two = on_off_to_bool(one_forty_two)
    two_forty_two = on_off_to_bool(two_forty_two)
    three_forty_eight = on_off_to_bool(three_forty_eight)
    oil = on_off_to_bool(oil)
    hose_cart = on_off_to_bool(hose_cart)
    drk = on_off_to_bool(drk)
    police = on_off_to_bool(police)

    print("Operation Description: " + operation_description)
    print("Address: " + address)
    print("operationDate, operationTime: " + operation_date + " - " + operation_time)
    print("1-19: " + str(one_nineteen))
    print("1-42: " + str(one_forty_two))
    print("2-42: " + str(two_forty_two))
    print("3-48: " + str(three_forty_eight))
    print("Oil: " + str(oil))
    print("Hose Cart: " + str(hose_cart))
    print("DRK: " + str(drk))
    print("Police: " + str(police))

    alarm(operation_date + ", " + operation_time, operation_description, address, one_nineteen, one_forty_two,
          two_forty_two, three_forty_eight, oil, hose_cart, drk, police)


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
              sorted_config_data[i]["drk"], sorted_config_data[i]["police"])

# keep alive
while True:
    root.update()
