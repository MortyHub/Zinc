KEYS = ["log(", "var"]
VARIABLES = {}

with open("Script.zc", "r") as f:
    Script = (f.read()).split("\n")
    for i in range(len(Script)):
        Script[i] = Script[i].lstrip()

def Main(Program):

    for i in range(len(Program)):

        # Prints value of log()
        if KEYS[0] in Program[i]:
            if "'" in Program[i]:
                printv = ((Program[i].split("("))[1].split("'"))
                print(printv[1])
            else:
                printv = (Program[i].split("("))[1].split(")")
                if '+' in printv[0].lstrip() or '-' in printv[0].lstrip() or '*' in printv[0].lstrip() or '/' in printv[0].lstrip():
                    print(var_math(printv[0]))
                else:
                    print(VARIABLES[printv[0]])

        if KEYS[1] in Program[i]:
            variable = Program[i].split(" ")

            if variable[1] == "int":
                VARIABLES[variable[2]] = int(variable[4])

            elif variable[1] == "str":
                VARIABLES[variable[2]] = str(variable[4])

            elif variable[1] == "bool":
                VARIABLES[variable[2]] = bool(variable[4])

            elif variable[1] == "float":
                VARIABLES[variable[2]] = float(variable[4])

def var_math(eq):
    if '+' in eq:
        eq = eq.split('+')
        return int(VARIABLES[eq[0].lstrip()]) + int(eq[1].lstrip())
    if '-' in eq:
        eq = eq.split('-')
        return int(VARIABLES[eq[0].lstrip()]) - int(eq[1].lstrip())
    if '*' in eq:
        eq = eq.split('*')
        return int(VARIABLES[eq[0].lstrip()]) * int(eq[1].lstrip())
    if '/' in eq:
        eq = eq.split('/')
        return int(VARIABLES[eq[0].lstrip()]) / int(eq[1].lstrip())




Main(Script)