from typing import List


class Solution:

  def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
      return ""

    # Encontrar las palabras más alejadas alfabéticamente en O(S)
    min_str = min(strs)
    max_str = max(strs)

    # Solo necesitamos comparar los extremos
    for i, char in enumerate(min_str):
      if char != max_str[i]:
        return min_str[:i]

    return min_str
