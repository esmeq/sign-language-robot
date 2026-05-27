print("Project started!")


import cv2

def main():
    cap=cv2.VideoCapture(0)  #con 0 attiva la fotocamera del portatile

    while True:    #ciclo infinito per continuare a raccogliere dati dalla fotocamera
        ret, frame = cap.read()   #ret è True/False a seconda se legge bene o meno l'immagine
    
        if not ret:
            break
    
        cv2.imshow("Sign Language Robot", frame)   #nome finestra e fra= immagine della webcam presa prima
        if cv2.waitKey(1) & 0xFF== ord('q'):    #se premi q esce dal programma manualmente
            break
    cv2.release()   #libera la webcam
    cv2.destroyAllWindows()   #chiude la finestra

if __name__ == "__main__":
    main()
