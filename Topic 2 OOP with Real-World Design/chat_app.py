from datetime import datetime

class Message:
    def __init__(self, sender, receiver, content):
        self._sender = sender
        self._receiver = receiver
        self._content = content
        self._timestamp = datetime.now()

    @property
    def sender(self):
        return self._sender

    @property
    def receiver(self):
        return self._receiver

    @property
    def content(self):
        return self._content

    @property
    def timestamp(self):
        return self._timestamp

    def __str__(self):
        time_str = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        return f"[{time_str}] {self.sender.name} -> {self.receiver.name}: {self.content}"


class User:
    def __init__(self, name, manager):
        self.name = name
        self.manager = manager
        self._inbox = []

    def compose_message(self, receiver_name):
        return f"Hello {receiver_name}, this is {self.name}!"

    def send_message(self, receiver_name):
        receiver = self.manager.get_user(receiver_name)
        if receiver:
            content = self.compose_message(receiver_name)
            msg = Message(self, receiver, content)
            self.manager.store_message(msg)
            receiver.receive_message(msg)
        else:
            print(f"User '{receiver_name}' not found.")

    def receive_message(self, message):
        self._inbox.append(message)

    def get_inbox(self):
        return self._inbox

    def __str__(self):
        return f"User({self.name})"


class Manager:
    def __init__(self):
        self._users = {}
        self._messages = []

    def register_user(self, name):
        if name in self._users:
            print(f"User '{name}' already exists.")
            return None
        user = User(name, self)
        self._users[name] = user
        return user

    def get_user(self, name):
        return self._users.get(name)

    def store_message(self, message):
        self._messages.append(message)

    def get_all_messages(self):
        return self._messages

    def __str__(self):
        return f"Manager({len(self._users)} users, {len(self._messages)} messages)"


if __name__ == "__main__":
    manager = Manager()

    alice = manager.register_user("Alice")
    bob = manager.register_user("Bob")

    alice.send_message("Bob")
    bob.send_message("Alice")

    print("\n--- Inbox for Alice ---")
    for msg in alice.get_inbox():
        print(msg)

    print("\n--- Inbox for Bob ---")
    for msg in bob.get_inbox():
        print(msg)
