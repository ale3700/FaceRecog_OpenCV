import face_recognition as fr

def reconhece_face(url_foto):
    foto = fr.load_image_file(url_foto)
    rostos = fr.face_encodings(foto)
    if(len(rostos) > 0):
        return True, rostos
    
    return False, []

def get_rostos():
    rostos_conhecidos = []
    nomes_dos_rostos = []

    avril = reconhece_face("./Imagens_RF/avril1.jpg") #nome da pasta img
    if(avril[0]):
        rostos_conhecidos.append(avril[1][0])
        nomes_dos_rostos.append("Avril")

    hayley = reconhece_face("./Imagens_RF/hayley.jpg")
    if(hayley[0]):
        rostos_conhecidos.append(hayley[1][0])
        nomes_dos_rostos.append("Hayley")
    
    return rostos_conhecidos, nomes_dos_rostos