# Task to send "Hello World" on the radio

class Task:
    def __init__(self, satellite):
        self.cubesat = satellite

    async def main_task(self):
        print("Sending message from PyCubed....2")
        self.cubesat.radio2.send("Hello World 2!", keep_listening=True)
        print("Message sent from PyCubed 2")

    priority = 2
    frequency = 1
    task_id = 2

