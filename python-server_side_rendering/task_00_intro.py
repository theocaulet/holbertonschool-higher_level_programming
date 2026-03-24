#!/usr/bin/python3
def generate_invitations(template, attendees):
    """Generates a list of invitations based on a template and a list of attendees.

    Args:
        template (str): The invitation template containing a placeholder for the attendee's name.
        attendees (list): A list of attendee names.
    Returns:
        list: A list of personalized invitations for each attendee.
    """
    if not isinstance(template, str) or not isinstance(attendees, list):
        print("Invalid input: template must be a string"
              " and attendees must be a list")
        return
    if not template:
        print("Template is empty, no output files generated")
        return
    if not attendees:
        print("No data provided, no output files generated")
        return
    for index, attendee in enumerate(attendees, 1):
        invitation = template.replace("{name}", attendee.get("name") or "N/A")
        invitation = invitation.replace(
                "{event_title}", attendee.get("event_title") or "N/A")
        invitation = invitation.replace(
                "{event_date}", attendee.get("event_date") or "N/A")
        invitation = invitation.replace(
                "{event_location}", attendee.get("event_location") or "N/A")
        with open(f"output_{index}.txt", "w") as file:
            file.write(invitation)
