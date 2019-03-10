# Understanding_UnicodeDecodeError
This error arises when the file or string used in the program does not support the particular encoding type mentioned in the program. Default encoding in python is ASCII.  
Computer stores everything in its disk as a series of bytes which themseleves is meaningless and we need to give them meaning.
For text representation, ASCII codes are used where every byte is assigned one of 95 symbols. Extended version of ASCII is "ISO Latin 1 or 8859-1" which have 96 more symbols. Further extension was given by windows by adding 27 more symbols which produced  "CP1252". It is one of the best that can be used for representing text as single bytes. But still there are way more than 256 symbols in the world's text and single byte character codes such as ASCII can't solve this global text problem. Then, unicode came into picture to deal decisively with the issues with older character codes. It assigns integers, known as code points, to characters. It has room for 1.1 million code points, and only 110,000 are already assigned, so there’s plenty of room for future growth. It includes thousands of symbols. But still to represent them as bytes there needs a way. 
The Unicode standard defines a number of ways to represent code points as bytes. These are known as encodings & UTF-8 is the most popular encoding for storage and transmission of Unicode. It uses a variable number of bytes for each code point. The higher the code point value, the more bytes it needs in UTF-8. ASCII characters are one byte each, using the same values as ASCII, so ASCII is a subset of UTF-8.

Python 2.x provides a data type called a Unicode string for working with Unicode data using string encoding and decoding methods.
## Note:
When executing a Python script that contains Unicode characters, you must put the following line at the top of the script, to tell Python that the code is UTF-8/Unicode formatted.

    # -*- coding: utf-8 -*-

## Overview: Unicode
To understand encoding and decoding, let's take an example:
    
    >>> s = "Flügel"
    >>> s
    'Fl\xfcgel'
    >>> print(s)
    Flügel
         
We can see that the non-ASCII character ü was translated into a code phrase, i.e. “\xfc,“ by a set of rules behind-the-scenes. In other words,it can be concluded that it was encoded.
The simplest way to make a unicode string is to add "u" prefix in front of the string. Let's try this out.

    u = u"Flügel"
    >>> u
    u'Fl\xfcgel'
    >>> print(u)
    Flügel
We can see our “umlaut-u” is still “\xfc“. Let's try encode method.
   
    >>> u.encode('latin_1')
    'Fl\xfcgel'
    >>> s.encode('latin_1')
    Traceback (most recent call last):
     File "<pyshell#35>", line 1, in <module>
     s.encode('latin_1')
    UnicodeDecodeError: 'ascii' codec can't decode byte 0xfc in position 2: ordinal not in range(128)

We can see that encoding the Unicode string (with the ‘latin-1’ encoding) retuned the same value as string s, but the encode method didn’t work on string s. Let's try out the decoding.

    >>> s.decode('latin-1')
    u'Fl\xfcgel'
The difference that comes out is that s is an 8-bit string and u is a Unicode string. Unicode string u was using a code phrase that the Unicode standard defines for the character “umlaut-u,” and the 8-bit string s was using a code phrase that the "latin-1" codec (rule-set) defines for “umlaut-u.” To understand this more, let's consider another example. This time we will take only code phrases of string. It is an encoded string for an asian script character.

    new_s = '\xe5\xad\x97'
    >>>print new_s
The answer printed by print statement is not correct one as this is not an Asian script character and has more than one character. Now, we will do decoding as we did in our above example.

    >>> new_u = new_s.decode('latin_1')
    >>> new_u
    u'\xe5\xad\x97
let’s print our Unicode string and see what our script character is:
    
    >>> print(new_u)
    å
Let's decode with utf-8

    >>> new_u = new_s.decode('utf_8')
    >>> new_u
    u'\u5b57'
    >>> print(new_u)
    字

## Where to use UnicodeDecodeError
Suppose we have a text file named "a.txt" and we want to check whether it is utf encoded or not. We will use try-except for fulfilling this goal. We will open the file an print every line present in it. This condition will be executed only when the file will be utf-8 encoded otherwise UnicodeDecodeError will be raised. If file is not found in the directory, then IOError will be raised. The code is given below. 

    filename = "a.txt"
    try:
         with open(filename, encoding="utf-8") as f:
             for line in f:
                 print(line)  # actually, I'd use "process_file(f)"
    except IOError as e:
         print("Reading file %s failed: %s" % (filename, e))
    except UnicodeDecodeError as e:
         print("Some error occurred decoding file %s: %s" % (filename, e))

## References:
https://www.pythoncentral.io/python-unicode-encode-decode-strings-python-2x/  
https://nedbatchelder.com/text/unipain.html
