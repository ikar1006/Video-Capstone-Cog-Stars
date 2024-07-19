def find_min_distance(d, database, prob_threshold, cosine_threshold, probability):

    distances=[]
    if (probability>prob_thresh):
        
        #find the minimum cosine distance
        for i in database:
            distances.append(cosine_distance(d, i.descriptor))
        minimum_distance = min(distances)
    
        if minimum_distance <= cosine_threshold:
            return database[distances.index(minimum_distance)].name
        
        return "Person is not found"
        
    return "Probability too low"
