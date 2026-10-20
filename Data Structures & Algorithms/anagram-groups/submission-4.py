from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[int]) -> List[List[str]]:
        # Usamos un defaultdict para no tener que verificar si la clave ya existe
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Creamos un contador de caracteres inmutable para 26 letras (a-z)
            count = [0] * 26
            for char in s:
                # Calculamos el índice en el alfabeto restando el valor ASCII
                count[ord(char) - ord('a')] += 1
            
            # Convertimos la lista a una tupla porque las listas no pueden ser claves de diccionario
            # Esta tupla es tu "decodificador posicional" de frecuencias
            anagram_map[tuple(count)].append(s)
            
        # Devolvemos solo las sublistas agrupadas
        return list(anagram_map.values())
