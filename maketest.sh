#!bin/sh
git clone https://github.com/yosupo06/library-checker-problems.git
pip3 install toml markdown
cd library-checker-problems
./generate.py $(find . -name "info.toml" -not -path "./test/*")
