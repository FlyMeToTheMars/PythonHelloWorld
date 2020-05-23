
class StringReplace:
    """

    """

    def strreplace(self, str):
        output = str.replace(" ", "%20")
        return output

    def strreplace2(self, str):
        s = list(str)
        count = len(s)
        for i in range(0, count):
            if s[i] == ' ':
                s[i] = '%20'
        return ''.join(s)

    def strreplace3(self,str):
        r = []
        for c in str:
            if c == ' ':
                r.append('%20')
            else:
                r.append(c)
        return ''.join(r)
