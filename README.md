# Obf | The faggot onion  
## Algorithm:  
```py
import base64, codecs
magic = "Mujeeb"
love = "is"
god = "big"
destiny = "skid"
joy = '\x72\x6f\x74\x31\x33'		
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')		
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
```
## Deobfuscation:  
+ replace `eval(compile())` with `print()`
```py
print(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec')
```
I've attached a script to do the next part automatically  
```
- Run the script and pipe the output to a new file
- Chop off the b" in the beginning of the file and the stuff behind the last "
- Then replace the followings:
    + \\ with \
    + \t with 
    + \n with newline
- Then run the script and pipe the output to a new file again
- Repeat the following steps from 16 - 19 times```

This should result in a oneliner containing the original code. doing the 3rd and 4th step again should give you the original code.

Credits: Kernal.eu - giving me the outlines to explain in this read.me
