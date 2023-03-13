KEYS = ["log(", "var", "func", "call"]
VARIABLES = {}
FUNCTIONS = {}
FUNCTIONS_ARGS = {}

with open("Script.zc", "r") as f:
    Script = (f.read()).split("\n")
    for i in range(len(Script)):
        Script[i] = Script[i].lstrip()


def Main(Program):

    global FunctionScript
    global func
    global functionScripting
    FunctionScript = 0
    func = ""
    functionScripting = []

    for i in range(len(Program)):

        if FunctionScript != 1:
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

            # variables
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

            # Functions
            if KEYS[2] in Program[i]:
                func = (Program[i].split("func")[1]).split("(")
                funcArgs = func[1].split(")")[0].split(',')
                FUNCTIONS_ARGS[func[0].lstrip() + "("] = funcArgs
                FUNCTIONS[func[0].lstrip() + "("] = functionScripting
                FunctionScript = 1

            # Calling a function
            if KEYS[3] in Program[i]:
                FunctionTarget = Program[i].split("call")[1].split(")")[0]
                function(FUNCTIONS[FunctionTarget.lstrip()])


        else:

            if Program[i] != "}":
                FUNCTIONS[func[0].lstrip()+"("].append(Program[i])
            else:
                FunctionScript = 0

# Reinterpreter For Functions
def function(Program1):

    for i in range(len(Program1)):

        if KEYS[0] in Program1[i]:
            if "'" in Program1[i]:
                printv = ((Program1[i].split("("))[1].split("'"))
                print(printv[1])
            else:
                printv = (Program1[i].split("("))[1].split(")")
                if '+' in printv[0].lstrip() or '-' in printv[0].lstrip() or '*' in printv[0].lstrip() or '/' in \
                    printv[0].lstrip():
                    print(var_math(printv[0]))
                else:
                    print(VARIABLES[printv[0]])

            # variables
        if KEYS[1] in Program1[i]:
            variable = Program1[i].split(" ")

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