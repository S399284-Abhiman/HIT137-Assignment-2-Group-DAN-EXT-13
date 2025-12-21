The Encryption method used in this program applies fixed shift values to characters and wraps them within a limited alphabet range using modulo arithmetic. Because the number of possible characters input is larger than the number of unique encrypted outputs, the encryption process is not one-to-one. As a result, the encryption function maps multiple possible inputs into same output space.

This can be expressed using equation below:

                                                  E (x) = (x + k) mod N

where x is a character index,
k is constant derived from shift1 and shift2 and,
N is the size of the alphabet.

Due to the modulo operation, different input charcters can produce the same encrypted character. This results in collisions, meaning the original character cannot always be uniquely determined during  decryption. These collisions are a limitation of the encryption rules provided and are not caused by implementation errors.
Despite this, some texts ( for example: " Ace Bag Fed Cab" ) can still be encrypted and decrypted correctly for specific shift values (i.e shift1 = 1, and shift2 = 2, for this example). This occurs when all characters in the text transform uniquely do not overlap with possible mappings.

In conclusion, collisions are mathematically unavoidable with this encryption design, but correct encryption and decryption sre still possible for certain inputs that do not trigger overlapping character mappings.
