import re
import coden as co
import base64 as b64

class Codings:
    def __init__(self, binary_length = 8):
        self.binary_length = binary_length
    
    def text_to_binary(self, text):
        return "".join(format(ord(i), "0{}b".format(self.binary_length)) for i in text)
    
    def binary_to_text(self, binary):
        return "".join(chr(int(binary[i:i+self.binary_length], 2)) for i in range(0, len(binary), self.binary_length))
    
    def text_to_hex(self, text):
        return self.binary_to_hex(self.text_to_binary(text))
    
    def hex_to_text(self, h):
        return self.binary_to_text(self.hex_to_binary(h))
    
    def text_to_base64(self, text):
        return self.hex_to_base64(self.text_to_hex(text))
    
    def base64_to_text(self, b):
        return self.hex_to_text(self.base64_to_hex(b))
    
    def text_to_base85(self, text):
        return self.hex_to_base85(self.text_to_hex(text))
    
    def base85_to_text(self, b):
        return self.hex_to_text(self.base85_to_hex(b))
    
    def binary_to_base64(self, binary):
        return self.hex_to_base64(self.binary_to_hex(binary))
    
    def base64_to_binary(self, b):
        return self.hex_to_binary(self.base64_to_hex(b))
    
    def binary_to_base85(self, binary):
        return self.hex_to_base85(self.binary_to_hex(binary))
    
    def base85_to_binary(self, b):
        return self.hex_to_binary(self.base85_to_hex(b))
    
    def base64_to_base85(self, b):
        return self.hex_to_base85(self.base64_to_hex(b))
    
    def base85_to_base64(self, b):
        return self.hex_to_base64(self.base85_to_hex(b))

    def binary_to_hex(self, binary):
        t, z = ("", re.search("^0+", binary))
        if not z is None: 
            t = "{}:".format(len(z.group()))
            binary = binary[len(z.group()):]
        s = co.bin_to_hex(binary) if binary != "" else ""
        if s != "" and len(s) % 2 != 0: s = "0" + s
        return t + s
    
    def hex_to_binary(self, h):
        t, z = ("", re.search("^(\d+):", h))
        if not z is None: 
            t = "0" * int(z.group(1))
            h = h[len(z.group()):]
        return t + (str(co.hex_to_bin(h)) if h != "" else "")
    
    def __extract_custom_bin(self, text):
        t, z = ("", re.search("^\d+:", text))
        if not z is None:
            t = z.group()
            text = text[len(z.group()):]
        return (t, text)
    
    def hex_to_base64(self, h):
        t, h = self.__extract_custom_bin(h)
        return t + (b64.b64encode(bytes.fromhex(h)).decode() if h != "" else "")
    
    def base64_to_hex(self, b):
        t, b = self.__extract_custom_bin(b) 
        return t + (b64.b64decode(b.encode()).hex() if b != "" else "")
    
    def hex_to_base85(self, h):
        t, h = self.__extract_custom_bin(h)
        return t + (b64.b85encode(bytes.fromhex(h)).decode() if h != "" else "")
    
    def base85_to_hex(self, b):
        t, b = self.__extract_custom_bin(b) 
        return t + (b64.b85decode(b.encode()).hex() if b != "" else "")