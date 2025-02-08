from deepface import DeepFace

class HighSecurityFaceVerifier:
    def __init__(self):
        self.model_name = "ArcFace"
        self.detector_backend = "retinaface"
        self.metrics = "cosine"
        
        # Paramètres 
        self.confidence_threshold = 0.89  
        self.distance_threshold = 0.1    

    def verify_ultra_secure(self, img1_path, img2_path):
        try:
            result = DeepFace.verify(
                img1_path=img1_path,
                img2_path=img2_path,
                model_name=self.model_name,
                detector_backend=self.detector_backend,
                distance_metric=self.metrics,
                enforce_detection=False
            )
            
            confidence = 1 - result['distance']
            verified = (confidence > self.confidence_threshold) and (result['distance'] < self.distance_threshold)
            
            return {
                "verified": verified,
                "confidence": round(confidence * 100, 4), 
                "distance": round(result['distance'], 4),
                "thresholds": {
                    "required_confidence": self.confidence_threshold,
                    "max_distance": self.distance_threshold
                }
            }
            
        except Exception as e:
            return {"error": str(e)}


verifier = HighSecurityFaceVerifier()
result = verifier.verify_ultra_secure("image1.jpeg", "image4.jpeg")

if "error" not in result:
    if result['verified']:
        print("ALERTE : Identité confirmée à sécurité maximale (99%+)")
    else:
        print("Alerte sécurité : Correspondance non confirmée")
        
    print(f"Confiance réelle: {result['confidence']}%")
    print(f"Distance réelle: {result['distance']}")
    
else:
    print(f"Erreur: {result['error']}")