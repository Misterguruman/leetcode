class Solution:
    def romanToInt(self, s: str) -> int:
        value_guide = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50, 
            "C": 100,
            "D": 500,
            "M": 1000
        }

        serialized = [value_guide[x] for x in s]

        total = 0
        previous_value = 0
        group_reset = False

        for value in serialized:
            if value > previous_value:
                if group_reset:
                    total += value - previous_value
                previous_value = value
                group_reset = True
                continue


            total += value
            previous_value = value

            if group_reset:
                group_reset = False

        return total

            
