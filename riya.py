class RiyaAssistant:
    def __init__(self):
        self.name = "Riya"
        self.owner = "Boss"
        self.call_mode = False

    def start(self):
        print(f"{self.name} AI Voice Call Assistant ready hai 🤖📞")
        print(f"Hello {self.owner} 💖")

    def listen_for_owner_command(self):
        command = input("Boss 🎙️: ")
        return command

    def handle_command(self, command):
        command = command.lower()

        if "call karo" in command:
            person = command.replace("riya", "").replace("call karo", "").replace(" ko", "").strip()
            print("📞 Riya: Boss, call command samajh gayi.")
            print(f"👤 Person: {person}")

        elif "baat karo" in command:
            print("🗣️ Riya: Boss, conversation mode samajh gayi.")

        elif "call band" in command:
            print("🔴 Riya: Boss, call end command samajh gayi.")

        else:
            print("🤔 Riya: Boss, command abhi samajh nahi aayi.")


riya = RiyaAssistant()
riya.start()

while True:
    command = riya.listen_for_owner_command()

    if command.lower() in ["exit", "quit", "bye", "band ho jao"]:
        print("Riya: Theek hai Boss, main standby mode me ja rahi hoon 💖")
        break

    riya.handle_command(command)
