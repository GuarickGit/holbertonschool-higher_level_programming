#!/usr/bin/python3

def generate_invitations(template, attendees):

    invalid_template = not isinstance(template, str)
    invalid_list = not isinstance(attendees, list)
    invalid_elements = not all(isinstance(attendee, dict)
                               for attendee in attendees)

    if invalid_template or invalid_list or invalid_elements:
        print("Invalid input types.")
        return

    if template.strip() == "":
        print("Template is empty.")
        return
    if not attendees:
        print("No data provided.")
        return

    for index, attendee in enumerate(attendees, start=1):
        personalized = template

        name = attendee.get("name") or "N/A"
        personalized = personalized.replace("{name}", name)

        event_title = attendee.get("event_title") or "N/A"
        personalized = personalized.replace("{event_title}", event_title)

        event_date = attendee.get("event_date") or "N/A"
        personalized = personalized.replace("{event_date}", event_date)

        event_location = attendee.get("event_location") or "N/A"
        personalized = personalized.replace("{event_location}", event_location)

        filename = f"output_{index}.txt"

        with open(filename, "w") as file:
            file.write(personalized)
