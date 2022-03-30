import re
from bs4 import BeautifulSoup
import requests

from constants import FIELDS


def fetchInternships(debug=True) -> list:

    if debug:
        try:
            with open("pasantias.html", "r", encoding="ISO-8859-1") as f:
                page = BeautifulSoup(f, "html.parser")
        except:
            print("\npasantias.html does not exist, please add it to debug.\n\n")
    else:
        result = requests.get("https://seu.frc.utn.edu.ar/?pIs=1286")
        page = BeautifulSoup(result.text, "html.parser")

    page = str(page.find(class_="show-hide")).split("\n")[1:-1]

    internships = []

    for line in page:

        if re.search(".*FORMULARIO DE SOLICITUD DE SERVICIO.*", line):
            internships.append({})
            continue

        for field in FIELDS:
            data = ""
            for pattern in field[1]:
                found = re.findall(f".*{pattern}: (.*)<.*", line)
                if found:
                    data = found[0]
                    break
            if data:
                internships[-1][field[0]] = data
                break

    n = len(internships)
    for i in range(n):
        internships[i]['iid'] = n - i

    return internships


if __name__ == "__main__":
    fetchInternships()
