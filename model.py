def set_path(edcl: str):
    # global path
    if edcl == '5А':
        p = 'Lesson8_Homework\\5А.txt'
    if edcl == '5Б':
        p = 'Lesson8_Homework\\5Б.txt'
    return p


def call_jornal(pa: str):
    with open(pa, 'r', encoding='UTF-8') as file:
        cl_jorn = file.readlines()
        cl_jorn = [item.strip() for item in cl_jorn]
    return cl_jorn


def write_marks(jor: list, pa: str):
    jor = [item + '\n' for item in jor]
    with open(pa, 'w', encoding='UTF-8') as file:
        file.writelines(jor)


def add_mark(jor: list, sub: str, pers: str, ma: str):
    new_jor = []
    for el in jor:
        a = el.split('|')
        if a[0] == sub:
            b = a[1].split(';')
            new_line = a[0] + '|'
            for i in range(0, len(b) - 1, 2):
                if b[i] == pers:
                    b[i + 1] = b[i + 1][:-1] + ',' + ma + ')'
            for item in b:
                new_line += item + ';'
            new_line = new_line[:-1]
            new_jor.append(new_line)
        else:
            new_jor.append(el)
        
    return new_jor   