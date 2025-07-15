#!/usr/bin/python3

def generate_invitations(template, attendees):
    # Vérification des types d'entrée
    invalid_template = not isinstance(template, str)
    invalid_list = not isinstance(attendees, list)
    invalid_elements = not all(isinstance(attendee, dict)
                               for attendee in attendees)

    if invalid_template or invalid_list or invalid_elements:
        # Si les types sont invalides,
        # on affiche un message et on arrête la fonction
        print("Invalid input types.")
        return

    # Vérification du contenu vide du template
    # strip() créer un copie de la string et delete les espaces
    if template.strip() == "":
        print("Template is empty.")
        return

    # Vérification si la liste d'invités est vide
    if not attendees:
        print("No data provided.")
        return

    # Parcours de chaque invité avec un index à partir de 1
    for index, attendee in enumerate(attendees, start=1):

        # On commence avec une copie du template original
        personalized = template

        # Remplacement des champs avec les données de l'invité
        # ou "N/A" si absente ou None
        name = attendee.get("name") or "N/A"
        personalized = personalized.replace("{name}", name)

        event_title = attendee.get("event_title") or "N/A"
        personalized = personalized.replace("{event_title}", event_title)

        event_date = attendee.get("event_date") or "N/A"
        personalized = personalized.replace("{event_date}", event_date)

        event_location = attendee.get("event_location") or "N/A"
        personalized = personalized.replace("{event_location}", event_location)

        # Génération du nom de fichier de sortie (ex: output_1.txt)
        filename = f"output_{index}.txt"

        # Écriture du message personnalisé dans le fichier
        with open(filename, "w") as file:
            file.write(personalized)
