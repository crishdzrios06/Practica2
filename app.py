import flet as ft
import xml.etree.ElementTree as ET
from itertools import product


# =========================
# AFD
# =========================
class AFD:
    def __init__(self, estados, alfabeto, inicial, finales, transiciones):
        self.estados = estados
        self.alfabeto = alfabeto
        self.inicial = inicial
        self.finales = finales
        self.transiciones = transiciones

    def validar(self, cadena):
        estado = self.inicial
        recorrido = [estado]

        for c in cadena:
            if c not in self.alfabeto:
                return False, recorrido, f"Símbolo inválido: {c}"

            if (estado, c) not in self.transiciones:
                return False, recorrido, "Transición no definida"

            estado = self.transiciones[(estado, c)]
            recorrido.append(estado)

        return estado in self.finales, recorrido, "OK"


# =========================
# LEER JFF
# =========================
def leer_jff(ruta):
    tree = ET.parse(ruta)
    root = tree.getroot()

    estados = {}
    inicial = None
    finales = set()
    transiciones = {}
    alfabeto = set()

    for s in root.iter("state"):
        sid = s.get("id")
        nombre = "q" + sid
        estados[sid] = nombre

        if s.find("initial") is not None:
            inicial = nombre

        if s.find("final") is not None:
            finales.add(nombre)

    for t in root.iter("transition"):
        o = estados[t.find("from").text]
        d = estados[t.find("to").text]
        simbolo = t.find("read").text

        if simbolo is None:
            continue

        alfabeto.add(simbolo)
        transiciones[(o, simbolo)] = d

    return set(estados.values()), alfabeto, inicial, finales, transiciones


# =========================
# EXTRAS
# =========================
def subcadenas(c):
    return sorted({c[i:j] for i in range(len(c)) for j in range(i+1, len(c)+1)})

def prefijos(c):
    return sorted({c[:i] for i in range(len(c)+1)})

def sufijos(c):
    return sorted({c[i:] for i in range(len(c)+1)})

def kleene(alfabeto, n=3):
    res = [""]
    for i in range(1, n+1):
        for p in product(alfabeto, repeat=i):
            res.append("".join(p))
    return res


# =========================
# UI
# =========================
def main(page: ft.Page):
    page.title = "Simulador AFD"
    page.scroll = "auto"

    estados = ft.TextField(label="Estados (q0,q1,q2)")
    alfabeto = ft.TextField(label="Alfabeto (0,1)")
    inicial = ft.TextField(label="Estado inicial")
    finales = ft.TextField(label="Estados finales")
    transiciones = ft.TextField(label="Transiciones", multiline=True)

    ruta_archivo = ft.TextField(label="Ruta archivo .jff (ej: C:/carpeta/automata.jff)")

    cadena = ft.TextField(label="Cadena")

    resultado = ft.Text()
    recorrido = ft.Text()
    salida = ft.Text()

    # =====================
    # VALIDAR
    # =====================
    def validar(e):
        try:
            est = set(estados.value.split(","))
            alf = set(alfabeto.value.split(","))
            fin = set(finales.value.split(","))

            trans = {}
            for r in transiciones.value.split(";"):
                if not r.strip():
                    continue
                izq, der = r.split("->")
                s, c = izq.split(",")
                trans[(s.strip(), c.strip())] = der.strip()

            afd = AFD(est, alf, inicial.value.strip(), fin, trans)

            ok, rec, _ = afd.validar(cadena.value)

            resultado.value = "ACEPTADA" if ok else "RECHAZADA"
            recorrido.value = " → ".join(rec)

        except Exception as ex:
            resultado.value = f"Error: {ex}"

        page.update()

    # =====================
    # CARGAR JFF
    # =====================
    def cargar(e):
        try:
            ruta = ruta_archivo.value.strip()

            est, alf, ini, fin, trans = leer_jff(ruta)

            estados.value = ",".join(est)
            alfabeto.value = ",".join(alf)
            inicial.value = ini
            finales.value = ",".join(fin)

            reglas = []
            for (o, s), d in trans.items():
                reglas.append(f"{o},{s}->{d}")

            transiciones.value = " ; ".join(reglas)

            resultado.value = "Archivo cargado correctamente"

        except Exception as ex:
            resultado.value = f"Error al cargar: {ex}"

        page.update()

    # =====================
    # EXTRAS
    # =====================
    def ver_sub(e):
        salida.value = "Subcadenas:\n" + ", ".join(subcadenas(cadena.value))
        page.update()

    def ver_pref(e):
        salida.value = "Prefijos:\n" + ", ".join(prefijos(cadena.value))
        page.update()

    def ver_suf(e):
        salida.value = "Sufijos:\n" + ", ".join(sufijos(cadena.value))
        page.update()

    def ver_kleene(e):
        salida.value = "Kleene (n<=3):\n" + ", ".join(kleene(alfabeto.value.split(",")))
        page.update()

    # =====================
    # UI
    # =====================
    page.add(
        ft.Text("Simulador de AFD", size=22, weight="bold"),

        estados,
        alfabeto,
        inicial,
        finales,
        transiciones,

        ruta_archivo,
        ft.ElevatedButton("Cargar JFF", on_click=cargar),

        cadena,
        ft.ElevatedButton("Validar", on_click=validar),

        resultado,
        recorrido,

        ft.Divider(),

        ft.Text("Funciones adicionales"),

        ft.Row([
            ft.ElevatedButton("Subcadenas", on_click=ver_sub),
            ft.ElevatedButton("Prefijos", on_click=ver_pref),
            ft.ElevatedButton("Sufijos", on_click=ver_suf),
            ft.ElevatedButton("Kleene", on_click=ver_kleene),
        ]),

        salida
    )


ft.app(target=main)
