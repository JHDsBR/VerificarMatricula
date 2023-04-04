from flask import Flask
from util import StartNgrok, VerificarMatricula, RetornarNome


app     = Flask(__name__)
port    = 8080


@app.get("/")
def index():
    return "<h1>Online</h1>"


@app.get("/verificar_matricula/<matricula>")
def verificar(matricula):
    existe = VerificarMatricula(matricula, 'ecologia')
    return 'aluno encontrado' if existe else 'aluno não encontrado'

@app.get("/busca_aluno/curso=<curso>&matricula=<matricula>")
def buscaAluno(curso, matricula):
    nomeAluno = RetornarNome(curso, matricula)
    return "aluno não encontrado" if nomeAluno == None else nomeAluno
    


if __name__ == "__main__":
    # StartNgrok(port)
    app.run(port=port, debug=True)


