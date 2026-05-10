class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score, counter = 0, 0
        for ev in events:
            if counter == 10: break
            match ev:
                case "W": counter += 1
                case "WD" | "NB": score += 1
                case val: score += int(val)

        return [score, counter]