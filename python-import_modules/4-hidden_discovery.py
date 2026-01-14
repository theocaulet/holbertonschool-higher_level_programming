#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for hidden in sorted(dir(hidden_4)):
        if not hidden.startswith("__"):
            print(hidden)