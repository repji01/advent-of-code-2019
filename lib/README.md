Intcode!
========

Some tools to work with Intcode programs.

Intcode VM & disassembler
-------------------------

The program `intcode.py` is a python script capable of disassembling and running
Intcode programs. It takes input from standard input and outputs to standard
output. Any disassembled code is printed to standard error.

Disassemble an Intcode program:

	./intcode.py dis prog.txt

Run an Intcode program:

	./intcode.py run prog.txt

Run an Intcode program in debug mode:

	./intcode.py debug prog.txt
