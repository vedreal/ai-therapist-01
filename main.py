"""Your AI therapist's diagnosis.

Entry for the make.fun bounty
u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41.

The diagnosis: chronic screenshot archiving. The human keeps
3,000 screenshots and has re-read none of them, and the
therapist's deadpan finding is that the memory is safe — the
human is not. A calm clinical voice, a turn the reader never
sees coming, and the laugh lands on the last three words.

The program writes the single diagnosis to /output/entry.txt.
"""

import os

ENTRY = (
    "Diagnosis: chronic screenshot archiving. You have 3,000 "
    "screenshots and have re-read none of them. The memory is "
    "safe. You are not."
)


def main() -> None:
    line = ENTRY.strip()
    if not line:
        raise ValueError("entry must not be empty or whitespace only")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(line)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
