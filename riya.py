class RiyaAssistant:
    def __init__(self):
        self.name = "Riya"
        self.owner = "Boss"
        self.call_mode = False

    def start(self):
        print(f"{self.name} AI Voice Call Assistant ready hai 🤖📞")
        print(f"Hello {self.owner} 💖")

    def listen_for_owner_command(self):
        print("Riya tumhari command ka wait kar rahi hai 🎙️")

    def handle_call(self):
        print("Riya call handling mode me hai 📞")


riya = RiyaAssistant()
riya.start()
riya.listen_for_owner_command()
