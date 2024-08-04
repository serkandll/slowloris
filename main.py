from importlib import import_module
from sys import path

path.insert(1, "./SDLL/")
main = import_module("SDLL.main")

main.run()
