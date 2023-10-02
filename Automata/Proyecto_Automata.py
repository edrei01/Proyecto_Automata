import tkinter as tk
from PIL import Image, ImageTk

class AFD:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12','q13','q14'}
        self.alphabet = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                         'A', 'B', 'C', 'D', 'E', 'F', 'G','H', 'I', 'J',
                         'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
                         'U', 'V', 'W', 'X', 'Y', 'Z', '-'}
        
        self.transitions = {
            'q0': {'A': 'q1', 'B': 'q2', 'C':'q3'},
            'q1': {'G': 'q4', 'H': 'q4', 'I': 'q4', 'J': 'q4','K': 'q4', 'L': 'q4', 'M': 'q4', 'N': 'q4', 'O': 'q4',
                   'P': 'q4', 'Q' : 'q4', 'R': 'q4','S': 'q4', 'T': 'q4', 'U': 'q4', 'V': 'q4', 'W': 'q4', 'X': 'q4', 
                   'Y' : 'q4', 'Z': 'q4'},
            'q2': {'A': 'q4', 'B': 'q4', 'C': 'q4', 'D': 'q4', 'E' : 'q4', 'F': 'q4', 'G': 'q4', 'H': 'q4', 'I': 'q4',
                   'J': 'q4','K': 'q4', 'L': 'q4', 'M': 'q4', 'N': 'q4', 'O': 'q4','P': 'q4', 'Q' : 'q4', 'R': 'q4','S': 'q4',
                   'T': 'q4', 'U': 'q4', 'V': 'q4', 'W': 'q4', 'X': 'q4', 'Y' : 'q4', 'Z': 'q4'},
            'q3': {'A': 'q4', 'B': 'q4', 'C': 'q4', 'D': 'q4'},
            'q4': {'-': 'q5'},
            'q5': {'0': 'q6' ,'1': 'q10', '2': 'q10', '3': 'q10', '4': 'q10', '5': 'q10', '6': 'q10', '7': 'q10', '8': 'q10', '9' : 'q10'},
            'q6': {'0': 'q7' ,'1': 'q11', '2': 'q11', '3': 'q11', '4': 'q11', '5': 'q11', '6': 'q11', '7': 'q11', '8': 'q11', '9' : 'q11'},
            'q7': {'0': 'q8' ,'1': 'q12', '2': 'q12', '3': 'q12', '4': 'q12', '5': 'q12', '6': 'q12', '7': 'q12', '8': 'q12', '9' : 'q12'},
            'q8': {'1': 'q9'},
            'q9': {'-': 'q13'},
            'q10': {'0': 'q11' ,'1': 'q11', '2': 'q11', '3': 'q11', '4': 'q11', '5': 'q11', '6': 'q11', '7': 'q11', '8': 'q11', '9' : 'q11'},
            'q11': {'0': 'q12','1': 'q12', '2': 'q12', '3': 'q12', '4': 'q12', '5': 'q12', '6': 'q12', '7': 'q12', '8': 'q12', '9' : 'q12'},
            'q12': {'0': 'q9', '1': 'q9', '2': 'q9', '3': 'q9', '4': 'q9', '5': 'q9', '6': 'q9', '7': 'q9', '8': 'q9', '9' : 'q9'},
            'q13': {'A': 'q14', 'B': 'q14', 'C': 'q14', 'D': 'q14', 'E' : 'q14', 'F': 'q14', 'G': 'q14', 'H': 'q14', 'I': 'q14', 'J': 'q14', 
                   'K': 'q14', 'L': 'q14', 'M': 'q14', 'N': 'q14', 'O': 'q14', 'P': 'q14', 'Q' : 'q14', 'R': 'q14', 'S': 'q14', 'T': 'q14', 
                   'U': 'q14', 'V': 'q14', 'W': 'q14', 'X': 'q14', 'Y' : 'q14', 'Z': 'q14'},
            'q14': {},
           
        }
        self.start_state = 'q0'
        self.accept_states = {'q14'}
        
    def validar(self, input_string):
        current_state = self.start_state
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False 
            if current_state not in self.states:
                return False 
            current_state = self.transitions[current_state].get(symbol, None)
            if current_state is None:
                return False  
        return current_state in self.accept_states
    
automata = AFD()
def verificarCadena():
    input_string = entrada.get()
    transiciones = []
    current_state = automata.start_state
    for symbol in input_string:
        transiciones.append(f"{current_state} --({symbol})--> {automata.transitions[current_state].get(symbol)}")
        next_state = automata.transitions[current_state].get(symbol)
        if next_state is None:
            break  # La cadena no es válida
        current_state = next_state
    
    if current_state in automata.accept_states:
        resultado.config(text=f"La Cadena es válida: {input_string}")
    else:
        resultado.config(text=f"La Cadena no es válida: {input_string}")
    
    transiciones_label.config(text='\n'.join(transiciones))

ventana = tk.Tk()
ventana.title("Automata Rangos")
ventana.geometry("400x400")  # Aumenté la altura de la ventana para dar espacio a las transiciones
ventana.configure(bg="lightblue")  

etiqueta = tk.Label(ventana, text="Ingrese una cadena:")
etiqueta.pack()

entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="Verificar", command=verificarCadena)
boton.pack()

resultado = tk.Label(ventana, text="")
resultado.pack()

# Etiqueta para mostrar las transiciones
transiciones_label = tk.Label(ventana, text="", justify="left")
transiciones_label.pack()

# Ejecutar la ventana
ventana.mainloop()
