class Course:
    def __init__(self, title="Test is broken", schedule="Test is broken", description="Test is broken"):
        self.title = title
        self.schedule = schedule
        self.description = description

    def __str__(self):
        output = ""
        output += f"Title: {self.title}\nSchedule: {self.schedule}\nDescription: {self.description}\n"
        output += "------------------"

        return output