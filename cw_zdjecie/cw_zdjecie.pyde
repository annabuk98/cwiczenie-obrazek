add_library("pdf")

def setup():
    global s
    global i
    global nazwa
    global ext
    nazwa = "dowod"
    ext = ".jpg"
    i = loadImage(nazwa+ext)
    size(198,255)
    beginRecord(PDF, "mojPDF.pdf")
    print(type(i))
    imageMode(CENTER)

def draw():
    background(0)
    image(i, width/2, height/2)
    s = loadShape("sunglasses.svg")  # brak pliku
    shape(s, 40, 95, 120, 80)
    # brak zapisu nagrania do pdf
    

    
