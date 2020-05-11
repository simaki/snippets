#!bin/sh
git clone https://github.com/yosupo06/library-checker-problems.git tests/library-checker-problems/
pip3 install toml markdown
cd tests/library-checker-problems
./generate.py $(find . -name "info.toml" -not -path "./test/*")
