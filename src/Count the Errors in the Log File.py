from collections import Counter

def map_errors():
    error_counts = Counter()
    
    # Open the file exactly as specified in the constraints
    with open("server.log", "r") as file:
        for line in file:
            # Strip trailing newlines and whitespace from the right
            clean_line = line.rstrip("\n")
            
            # Check for exact, uppercase prefix matching
            if clean_line.startswith("ERROR: "):
                # Extract everything after "ERROR: " and normalize to lowercase
                error_msg = clean_line[7:].lower()
                error_counts[error_msg] += 1
                
    # Sort by frequency (the dict values) in descending order
    # item[1] targets the count value in the (key, value) tuple
    sorted_errors = dict(
        sorted(error_counts.items(), key=lambda item: item[1], reverse=True)
    )
    
    return sorted_errors
