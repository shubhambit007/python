import calendar
import datetime
import json
import os
import sys

class CalendarApp:
    def __init__(self):
        self.today = datetime.date.today()
        self.current_year = self.today.year
        self.current_month = self.today.month
        self.events_file = 'events.json'
        self.events = self.load_events()

    def load_events(self):
        if os.path.exists(self.events_file):
            with open(self.events_file, 'r') as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return {}
        return {}

    def save_events(self):
        with open(self.events_file, 'w') as f:
            json.dump(self.events, f, indent=4)

    def add_event(self):
        try:
            date_str = input("Enter date for the event (YYYY-MM-DD): ")
            event_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            event_desc = input("Enter event description: ")
            self.events.setdefault(event_date.isoformat(), []).append(event_desc)
            self.save_events()
            print(f"Event added on {event_date.isoformat()}")
        except ValueError:
            print("Invalid date format. Please try again.")

    def view_events(self):
        date_str = input("Enter date to view events (YYYY-MM-DD): ")
        try:
            event_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            events = self.events.get(event_date.isoformat(), [])
            if events:
                print(f"Events on {event_date.isoformat()}:")
                for idx, event in enumerate(events, 1):
                    print(f"  {idx}. {event}")
            else:
                print(f"No events found on {event_date.isoformat()}.")
        except ValueError:
            print("Invalid date format. Please try again.")

    def display_calendar(self, year, month):
        cal = calendar.TextCalendar(calendar.SUNDAY)
        month_str = cal.formatmonth(year, month)
        rows = month_str.splitlines()

        # Header
        header = rows[0]
        print(header)

        # Days of the week
        print(rows[1])

        # Dates
        for row in rows[2:]:
            formatted_row = ""
            for day in row.split():
                if day.isdigit():
                    day_int = int(day)
                    date_obj = datetime.date(year, month, day_int)
                    day_str = f"{day:2}"
                    if date_obj == self.today:
                        # Highlight today's date
                        day_str = f"[{day:2}]"
                    elif date_obj.isoformat() in self.events:
                        # Mark days with events
                        day_str = f"*{day:2}*"
                    else:
                        day_str = f" {day:2} "
                    formatted_row += day_str + " "
                else:
                    formatted_row += "    "
            print(formatted_row)

        # List events for the month
        print("\nEvents this month:")
        for date_str, events in self.events.items():
            date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            if date_obj.year == year and date_obj.month == month:
                print(f"  {date_str}:")
                for event in events:
                    print(f"    - {event}")

    def navigate(self):
        while True:
            self.display_calendar(self.current_year, self.current_month)
            print("\nOptions:")
            print("  [N] Next month")
            print("  [P] Previous month")
            print("  [Y] Next year")
            print("  [B] Previous year")
            print("  [A] Add event")
            print("  [V] View events")
            print("  [Q] Quit")

            choice = input("Choose an option: ").strip().upper()

            if choice == 'N':
                self.next_month()
            elif choice == 'P':
                self.previous_month()
            elif choice == 'Y':
                self.next_year()
            elif choice == 'B':
                self.previous_year()
            elif choice == 'A':
                self.add_event()
            elif choice == 'V':
                self.view_events()
            elif choice == 'Q':
                print("Exiting Calendar App. Goodbye!")
                sys.exit()
            else:
                print("Invalid option. Please try again.")

    def next_month(self):
        if self.current_month == 12:
            self.current_month = 1
            self.current_year += 1
        else:
            self.current_month += 1

    def previous_month(self):
        if self.current_month == 1:
            self.current_month = 12
            self.current_year -= 1
        else:
            self.current_month -= 1

    def next_year(self):
        self.current_year += 1

    def previous_year(self):
        self.current_year -= 1

def main():
    app = CalendarApp()
    app.navigate()

if __name__ == "__main__":
    main()

