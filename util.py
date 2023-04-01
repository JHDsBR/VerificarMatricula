import requests
from constants import URL 
from bs4 import BeautifulSoup as BS
from pyngrok import ngrok, conf
from pyngrok.conf import PyngrokConfig
from pyngrok import ngrok


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

    for aluno in alunos:
        mat = aluno.find(class_="colMatricula")
        if mat:
            if mat.text == matricula:
                return True
    
    return
    

def LoadAuthToken():
    with open("authtoken.txt", "r") as file:
        return file.read()
    

def StartNgrok(port):

    """
        abre uma porta para a internet
    """

    config = PyngrokConfig(
        region      = "us",
        ngrok_path  = "ngrok/ngrok.exe",
        auth_token  = LoadAuthToken()
    )

    conf.set_default(config)

    public_url = ngrok.connect(port, "http").public_url

    print(public_url)


def EndNgrok():

    """
        fecha todas as portas abertas pelo ngrok para a internet
    """

    tunnels = ngrok.get_tunnels()

    for tunnel in tunnels:
        ngrok.disconnect(tunnel.public_url)
        ngrok.kill()


# StartNgrok(6756)
# EndNgrok()