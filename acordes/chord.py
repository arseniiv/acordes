import re
from .note import Note, note_regex


# intervals in semitones:
P1, m2, M2, m3, M3, P4, A4, P5, m6, M6, m7, M7 = range(12)


suffix_meanings = {
    "5":      (P1,     P5),
    "m(no5)": (P1, m3),
    "(no5)":  (P1, M3),
    "m":      (P1, m3, P5),
    "":       (P1, M3, P5),
    "m7":     (P1, m3, P5, m7),
    "mM7":    (P1, m3, P5, M7),
    "7":      (P1, M3, P5, m7),
    "M7":     (P1, M3, P5, M7)
}


chord_regex = re.compile(fr"({note_regex})(.*)$")


class Chord:
    def __init__(self, name: str):
        self.name, self.notes = name, []

        if match := chord_regex.match(name):
            root_name, suffix = match.groups()
        else:
            raise ValueError(f"Can't parse {name}")

        root = Note(root_name)
        for interval in suffix_meanings[suffix]:
            self.notes.append(root + interval)

    def __repr__(self) -> str:
        return f"{self.name} = <{' '.join(f'{n}' for n in self.notes)}>"
