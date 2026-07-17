class RiyaAssistant:
    def __init__(self):
        self.name = "Riya"
        self.owner = "Boss"
        self.call_mode = False
        self.active_person = None

    def start(self):
        print(f"{self.name} AI Voice Call Assistant ready hai 🤖📞")
        print(f"Hello {self.owner} 💖")

    def listen_for_owner_command(self):
        return input("Boss 🎙️: ")

    def listen_for_caller(self):
        return input("Caller 🗣️: ")

    def handle_caller(self, message):
        message = message.lower()

        if "hello" in message or "hi" in message:
            return "Hello 😊 Kaise ho?"

        elif "kaise ho" in message:
            return "Main bilkul theek hoon 😊 Aap batao?"

        elif "naam" in message:
            return "Mera naam Riya hai 🤖"

        else:
            return "Ji, main samajh rahi hoon 😊 Aap boliye."

    def handle_command(self, command):
        command = command.lower()

        if "call karo" in command:
            person = (
                command
                .replace("riya", "")
                .replace("call karo", "")
                .replace(" ko", "")
                .strip()
            )

            self.active_person = person
            print("📞 Riya: Boss, call command samajh gayi.")
            print(f"👤 Person: {person}")

        elif "baat karo" in command:
            if self.active_person:
                self.call_mode = True
                print(
                    f"🗣️ Riya: Boss, main {self.active_person} se baat kar rahi hoon."
                )
            else:
                print("⚠️ Riya: Boss, pehle kisi ko call karna hoga.")

        elif "call band" in command:
            self.call_mode = False
            self.active_person = None
            print("🔴 Riya: Boss, call end command samajh gayi.")

        else:
            print("🤔 Riya: Boss, command abhi samajh nahi aayi.")

    def run(self):
        self.start()

        while True:
            if self.call_mode:
                caller_message = self.listen_for_caller()

                if caller_message.lower() == "call band":
                    self.call_mode = False
                    self.active_person = None
                    print("🔴 Riya: Call end ho gayi.")
                    continue

                reply = self.handle_caller(caller_message)
                print(f"🗣️ Riya: {reply}")

            else:
                command = self.listen_for_owner_command()

                if command.lower() in ["exit", "quit", "bye", "band ho jao"]:
                    print(
                        "Riya: Theek hai Boss, main standby mode me ja rahi hoon 💖"
                    )
                    break

                self.handle_command(command)


riya = RiyaAssistant()
riya.run()
