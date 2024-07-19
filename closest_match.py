def find_min_distance(d, database, prob_threshold, cosine_threshold, probability):

    distances=[]
    if (probability>prob_thresh):
        
        #find the minimum cosine distance
        for i in range(len(database)):
            distances.append(cosine_distance(d, list(database.values())[i]))
        minimum_distance = min(distances)
    
        if minimum_distance <= cosine_threshold:
            return list(database.values())[distances.index(minimum_distance)]
        
        return "Person is not found"
        
    return "Probability too low"
