#from io import open
filename = "a.txt"
try:
        with open(filename, encoding="utf-8") as f:
            for line in f:
                print(line)  # actually, I'd use "process_file(f)"
except IOError as e:
        print("Reading file %s failed: %s" % (filename, e))
except UnicodeDecodeError as e:
        print("Some error occurred decoding file %s: %s" % (filename, e))