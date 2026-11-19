
def format_bib_name(name):
    if not isinstance(name, str):
        return ""
    return name.strip().upper()[:12]


def parse_finish_time(text):
    if not isinstance(text, str):
        return None

    try:
        parts = text.split(":")

        if len(parts) != 3:
            return None

        hours, minutes, seconds = map(int, parts)

        if hours < 0 or not (0 <= minutes < 60):
            return None

        if not (0 <= seconds < 60):
            return None

        return hours * 3600 + minutes * 60 + seconds

    except (ValueError, TypeError):
        return None


def average_split(text):
    if not isinstance(text, str):
        return None

    try:
        splits = [int(s) for s in text.split()]

        if not splits:
            return None

        if any(s < 0 for s in splits):
            return None

        return sum(splits) / len(splits)

    except (ValueError, TypeError):
        return None


def main():
    print("==== Running format_bib_name ====")
    value = input("Enter the name to print on the bib: ")
    print("Bib name:", format_bib_name(value))

    print("\n==== Running parse_finish_time ====")
    value = input("Enter a finish time as H:MM:SS (e.g. 3:45:10): ")
    print("Finish time in seconds:", parse_finish_time(value))

    print("\n==== Running average_split ====")
    value = input("Enter your 5 km split times in minutes separated by spaces (e.g. 25 26 24): ")
    print("Average split (minutes):", average_split(value))

if __name__ == "__main__":
    main()
