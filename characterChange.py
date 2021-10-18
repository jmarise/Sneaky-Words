
class cc:
  def __init__(self, chars):
    self.chars = chars

  def getchars(self):
    return self.chars

  def characters(self, c):
    self.chars = {
      "a" : "c01",
      "b" : "c02",
      "c" : "c03",
      "d" : "c04",
      "e" : "c05",
      "f" : "c06",
      "g" : "c07",
      "h" : "c08",
      "i" : "c09",
      "j" : "c10",
      "k" : "c11",
      "l" : "c12",
      "m" : "c13",
      "n" : "c14",
      "o" : "c15",
      "p" : "c16",
      "q" : "c17",
      "r" : "c18",
      "s" : "c19",
      "t" : "c20",
      "u" : "c21",
      "v" : "c22",
      "w" : "c23",
      "x" : "c24",
      "y" : "c25",
      "z" : "c26",
      "0" : "n00",
      "1" : "n01",
      "2" : "n02",
      "3" : "n03",
      "4" : "n04",
      "5" : "n05",
      "6" : "n06",
      "7" : "n07",
      "8" : "n08",
      "9" : "n09",
      "_" : "s01",
      "-" : "s02",
      "$" : "s03",
      "@" : "s04",
      "!" : "s05",
      "." : "s06",
      "&" : "s07",
      " " : "s08",
      "," : "s09",
      "(" : "s10",
      ")" : "s11", 
    }

    return self.chars[c]
