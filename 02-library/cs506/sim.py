def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += abs(x[i] - y[i])
    return res

# intersection set of s1 and s2 
def intersection(s1, s2) :
  
    # Find the intersection of the two sets 
    intersect = s1 & s2 
  
    return intersect; 

def jaccard_dist(x, y)  :

    size_s1 = len(x); 
    size_s2 = len(y); 
  
    # Get the intersection set 
    intersect = intersection(x, y); 
  
    # Size of the intersection set 
    size_in = len(intersect); 
  
    # Calculate the Jaccard index 
    # using the formula 
    jaccard_in = size_in  / (size_s1 + size_s2 - size_in)
  
    # Calculate the Jaccard distance 
    # using the formula 
    jaccard_dist = 1 - jaccard_in; 
  
    # Return the Jaccard distance 
    return jaccard_dist; 

def cosine_sim(x, y):
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(x)):
        x = x[i]; y = y[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/(sumxx*sumyy)**1/2

# Feel free to add more
