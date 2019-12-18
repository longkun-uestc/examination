def simplify_path(path):
    stack = []
    for i in range(0, len(path)):
        if path[i] == "/":
            j = i+1
            while j < len(path) and path[j] != "/":
                j += 1
            if i < len(path)-1:
                str = path[i+1: j]
                if str == "..":
                    if len(stack) > 0:
                        stack.pop()
                elif str != "" and str != ".":
                    stack.append(str)
            i = j-1
    if len(stack) == 0:
        result = "/"
    else:
        result=""
        for s in stack:
            result += "/"+s
    return result


if __name__ == '__main__':
    # x = "/a/./b/../../c/"
    x = "/R/c/../"
    x = x.replace("/", "*")
    print(x)



