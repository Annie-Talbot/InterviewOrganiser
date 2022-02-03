from enum import Enum


class InterviewerLevel(Enum):
    SENIOR = 0
    INTERN = 1
    EXTRA = 2

    @staticmethod
    def from_str(interviewer_type):
        if interviewer_type == 'senior':
            return InterviewerLevel.SENIOR
        elif interviewer_type == 'intern':
            return InterviewerLevel.INTERN
        elif interviewer_type == 'extra':
            return InterviewerLevel.EXTRA


class InterviewType(Enum):
    MANAGER = 0
    TECHNICAL = 1

    @staticmethod
    def from_str(interview_type):
        if interview_type == 'man':
            return InterviewType.MANAGER
        elif interview_type == "tech":
            return InterviewType.TECHNICAL


class Interviewer:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.slot1 = None
        self.slot2 = None


class Senior(Interviewer):
    def __init__(self, name, level, interview_type):
        Interviewer.__init__(self, name, level)
        self.type = interview_type

    def __repr__(self):
        return f"Name: {self.name}, Type: {self.type}"



class Junior(Interviewer):
    def __init__(self, name, level, preference, seniors):
        Interviewer.__init__(self, name, level)
        self.preference = next((i for i in seniors if i.name == preference),
                               None)
        if self.preference is None:
            print(f"Illegal value for preference in junior file for {name}")
            exit(1)

    def __repr__(self):
        return f"Name: {self.name}, Preference: {self.preference.name}"



class Candidate:
    def __init__(self, name, intern, interns):
        self.name = name
        # find intern in interns
        self.intern = next((i for i in interns if i.name == intern), None)
        if self.intern is None:
            print(f"Illegal value for intern in candidate file for {name}")
            exit(1)

    def __repr__(self):
        return f"Name: {self.name}, Intern: {self.intern.name}"


class Interview:
    def __init__(self, type, candidate, senior, junior, is_slot1):
        self.type = type
        self.candidate = candidate
        self.senior = senior
        self.junior = junior
        self.is_slot1 = is_slot1


def read_seniors(path):
    seniors = []
    with open(path, "r") as f:
        for line in f.readlines():
            raw = [line.strip() for line in line.split(",")]
            interview_type = InterviewType.from_str(raw[1])
            seniors.append(Senior(raw[0], InterviewerLevel.SENIOR,
                                  interview_type))

    return seniors


def read_juniors(path, seniors):
    juniors = []
    with open(path, "r") as f:
        for line in f.readlines():
            raw = [line.strip() for line in line.split(",")]
            level = InterviewerLevel.from_str(raw[1])
            juniors.append(Junior(raw[0], level, raw[2], seniors))
    return juniors


def read_candidates(path, interns):
    candidates = []
    with open(path, "r") as f:
        for line in f.readlines():
            raw = [line.strip() for line in line.split(",")]
            candidates.append(Candidate(raw[0], raw[1], interns))
    return candidates


def schedule(seniors, juniors, candidates):
    pass


def main():
    seniors = read_seniors("data/seniors")
    print("\nSeniors:")
    for s in seniors:
        print(s)
    juniors = read_juniors("data/juniors", seniors)
    print("\nJuniors")
    for j in juniors:
        print(j)
    candidates = read_candidates("data/candidates",
                                 [i for i in juniors
                                  if i.level == InterviewerLevel.INTERN])
    print("\nCandidates")
    for c in candidates:
        print(c)

    interviews = schedule(seniors, juniors, candidates)

    print("\nInterviews:")
    print(interviews)



if __name__ == "__main__":
    main()
