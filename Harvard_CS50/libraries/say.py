# import cowsay
# import sys

# if len(sys.argv) == 2:
#     cowsay.cow("hello, " + sys.argv[1])

# Packages -> third-party libraries, implemented as a folder, that add functionality
# PyPI is a repository or directory of all third-party packages currently available
# cowsay -> a well-known package that allows a cow to talk to the user
# pip -> package manager in Python that allows a quick installation of packages onto your system
# Install it by typing pip install cowsay in the terminal

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])
