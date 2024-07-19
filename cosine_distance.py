def cosine_distance(d1, d2):
    unit1 = d1 / np.linalg.norm(d1, keepdims=True)
    unit2 = d2 / np.linalg.norm(d2, keepdims=True)
    
    cosine = np.dot(unit1, unit2)
    
    cosine_distance = 1 - cosine
    
    return cosine_distance
