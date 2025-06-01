class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    # Encapsulation: private attribute with property and validation
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if '@' not in value or '.' not in value:
            raise ValueError("Invalid email address.")
        self._email = value

    def __str__(self):
        return f"User(name={self.name}, email={self.email})"

    def __len__(self):
        # Length could mean length of the name for User
        return len(self.name)


class Intern(User):
    def __init__(self, name, email, duration_months):
        super().__init__(name, email)
        self.duration_months = duration_months  # Duration of internship

    @property
    def duration_months(self):
        return self._duration_months

    @duration_months.setter
    def duration_months(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Duration must be a positive integer.")
        self._duration_months = value

    def __str__(self):
        return (f"Intern(name={self.name}, email={self.email}, "
                f"duration={self.duration_months} months)")

    def __len__(self):
        # Length could mean duration of internship in months
        return self.duration_months


class Mentor(User):
    def __init__(self, name, email, expertise):
        super().__init__(name, email)
        self.expertise = expertise  # List or string of skills/expertise

    @property
    def expertise(self):
        return self._expertise

    @expertise.setter
    def expertise(self, value):
        if not value or (isinstance(value, str) and value.strip() == ""):
            raise ValueError("Expertise cannot be empty.")
        self._expertise = value

    def __str__(self):
        return f"Mentor(name={self.name}, email={self.email}, expertise={self.expertise})"

    def __len__(self):
        # Length could mean number of expertise areas
        if isinstance(self.expertise, list):
            return len(self.expertise)
        return 1  # If expertise is a string, count as 1


# Example usage:
if __name__ == "__main__":
    user = User("Alice", "alice@example.com")
    intern = Intern("Bob", "bob@interns.com", 6)
    mentor = Mentor("Carol", "carol@mentors.com", ["Python", "Machine Learning"])

    print(user)     # User(name=Alice, email=alice@example.com)
    print(len(user))  # 5 (length of "Alice")

    print(intern)   # Intern(name=Bob, email=bob@interns.com, duration=6 months)
    print(len(intern))  # 6 (internship duration)

    print(mentor)   # Mentor(name=Carol, email=carol@mentors.com, expertise=['Python', 'Machine Learning'])
    print(len(mentor))  # 2 (number of expertise areas)
