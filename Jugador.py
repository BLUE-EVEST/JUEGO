import cv2

class Jugador:
    def __init__(self, W, H):
        self.x = 50
        self.y = 50
        self.W = W
        self.H = H
        self.speed = 5
        self.image = None
    
    def cambiar_imagen(self, img_path):
        logo = cv2.imread("aruco_0.png")
        if logo is None:
            raise FileNotFoundError("No se encontró aruco_0.png")
        logo = cv2.resize(logo, (50, 50))
        self.image = logo
        self.lh, self.lw = logo.shape[:2]
        
    def actualizar_posicion(self, key):
        vx, vy = 0, 0
        if key == ord('w'):
            vy = -self.speed
        elif key == ord('s'):
            vy = self.speed
        elif key == ord('a'):
            vx = -self.speed
        elif key == ord('d'):
            vx = self.speed
            
        if key != 255:
            if key in [ord('w'), ord('s')]:
                self.y += vy
            elif key in [ord('a'), ord('d')]:
                self.x += vx
                
        self.x = max(0, min(self.W - self.lw, self.x))
        self.y = max(0, min(self.H - self.lh, self.y))
        print(self.x, self.y)
        return self.x, self.y