"""Food picture entry: copy the ramen image to /output/entry.png."""

# Steaming ramen, noodles lifted high — the entry image lives next to this file.
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"), "/output/entry.png")


if __name__ == "__main__":
    main()
