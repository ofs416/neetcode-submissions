class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = []
        for i, word in enumerate(strs):
            for letter in word:
                encoded.append(chr(ord(letter) << 1))

            encoded.append(chr(32 >> 1))

        print("".join(encoded))

        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        
        print(s)

        if s == "":
            return decoded


        for enc_word in s.split(chr(32 >> 1)):
            decoded.append([])
            for enc_letter in enc_word:
                decoded[-1].append(chr(ord(enc_letter) >> 1))
            decoded[-1] = "".join(decoded[-1])
        decoded.pop()

        return decoded