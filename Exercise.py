from dataclasses import dataclass


@dataclass
class Set:
    weight: float = 0
    reps: int = 1

    def __str__(self) -> str:
        return f"{self.weight} lbs for {self.reps} reps"


class Exercise:
    def __init__(self):
        self.name = ""
        self.sets = []

    def add_set(self, number):
        if number < 0:
            raise ValueError("Number must be positive")

        current = len(self.sets)
        if number > current:
            for i in range(number - current):
                self.sets.append(Set())
        elif number < current:
            self.sets = self.sets[:number]

    def change_name(self, name):
        self.name = name

    @property
    def number_of_sets(self):
        return len(self.sets)

    def change_set_weight(self, position, weight):
        if not 0 <= position < len(self.sets):
            raise IndexError(f"Invalid set position: {position}")
        self.sets[position].weight = weight

    def change_set_rep(self, position, reps):
        if not 0 <= position < len(self.sets):
            raise IndexError(f"Invalid set position: {position}")
        self.sets[position].reps = reps

    def __str__(self):
        sets_str = "\n\t".join(
            f"Set {i + 1}: {specific}"
            for i, specific in enumerate(self.sets)
        )
        return f"Exercise: {self.name}\nSets: {self.number_of_sets}\n\t{sets_str}"

    def __repr__(self) -> str:
        return f"Exercise(name='{self.name}', sets={self.sets})"

    def __len__(self):
        return len(self.sets)
