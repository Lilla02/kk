character = "a"
vowels = "aáeéiíoóöőuúüűAÁEÉIÍOÓÖŐUÚÜŰ"
numbers = "0123456789"
ponctuation_marks = ",.;:?"
if vowels.find(character) >= 0:
    print("magánhangzó")
elif numbers.find(character) >= 0:
    print("számjegy")
elif ponctuation_marks.find(character) >= 0:
    print("írásjel")
