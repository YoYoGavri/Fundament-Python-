class Parser:
    def __init__(self, initialString):
        self.initialString = initialString


    # Splits the input into pieces
    def parse_input(self):
        string = self.initialString
        args = []
        i = 0
        while i < len(string):
            arg = ""
            if string[i] == "\"":
                arg += "\""
                i += 1
                while i < len(string) and string[i] != "\"":
                    arg += string[i]
                    i += 1
                if i < len(string) and string[i] == "\"":
                    arg += "\""
            else:
                while i < len(string) and string[i] != " ":
                    arg += string[i]
                    i += 1
            if arg:
                if arg[0] == "\"" and arg[-1] == "\"":
                    args.append(arg)
                else:
                    args.append(arg)
            i += 1
        return args