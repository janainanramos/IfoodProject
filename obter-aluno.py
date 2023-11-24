def getValue(msg='', func=float):
    while True:
        valor = input(msg)
        try:
            return list(map(func, [valor]))[0]
        except ValueError:
            msg = f'Entrada Inválida! {msg}'


def getMatricula() -> int:
    return getValue('Entre com a Matricula:', func=int)


def getName() -> str:
    return input('Entre com Nome:').title()


def getCurso() -> int:
    return input('Entre com Curso: ').upper()


def getTurno() -> str:
    return input('Entre com Turno: ').title()


# Insere aluno
def insertStudent(students: list[dict]) -> bool:
    newStudent = {
        'Matricula': getMatricula(),
        'Nome': getName(),
        'Curso': getCurso(),
        'Turno': getTurno(),
        'Notas': []
    }
    students.append(newStudent)
    return newStudent


# Obter Aluno especifico
def findStudent(students: list[dict]) -> list[dict]:
    name = getName()
    student = list(filter(lambda students: name.title() in students["Nome"], students))
    if len(student) == 0:
        return 'Student Not Found!'

    return student
