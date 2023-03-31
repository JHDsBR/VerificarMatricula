import requests
from constants import URL 
from bs4 import BeautifulSoup as BS
from flask import Flask


def VerificarMatricula(matricula, curso):
    try:
        url = URL.CURSOS[curso.lower()]
        req = requests.get(url)
    except KeyError:
        print("Chave inválida")
        return
    except:
        print("Curso não cadastrado")
        return
    
    soup = BS(req.text, 'html.parser')

    table   = soup.find_all("table", class_="listagem")[0]
    tbody   = table.find("tbody")
    alunos  = tbody.find_all("tr")

    alunoExiste = False

    for aluno in alunos:
        mat = aluno.find(class_="colMatricula")
        if mat:
            if mat.text == matricula:
                alunoExiste = True
                break

    if alunoExiste:
        print("Aluno matriculado")
    else:
        print("Aluno morreu")

VerificarMatricula("23432423", "si")
