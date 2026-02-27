import numpy as np

def calculate(list_input):
    """
    Calculate mean, variance, standard deviation, max, min, and sum 
    of a 3x3 matrix along rows, columns, and flattened.
    
    Args:
        list_input: A list containing 9 digits
        
    Returns:
        A dictionary with statistical calculations
        
    Raises:
        ValueError: If the list doesn't contain exactly 9 elements
    """
    
    # Check if list contains exactly 9 elements
    if len(list_input) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert list to 3x3 numpy array
    matrix = np.array(list_input).reshape(3, 3)
    
    # Initialize result dictionary
    result = {
        'mean': [],
        'variance': [],
        'standard deviation': [],
        'max': [],
        'min': [],
        'sum': []
    }
    
    # Calculate for axis 0 (rows), axis 1 (columns), and flattened
    result['mean'] = [
        np.mean(matrix, axis=0).tolist(),
        np.mean(matrix, axis=1).tolist(),
        float(np.mean(matrix))
    ]
    
    result['variance'] = [
        np.var(matrix, axis=0).tolist(),
        np.var(matrix, axis=1).tolist(),
        float(np.var(matrix))
    ]
    
    result['standard deviation'] = [
        np.std(matrix, axis=0).tolist(),
        np.std(matrix, axis=1).tolist(),
        float(np.std(matrix))
    ]
    
    result['max'] = [
        np.max(matrix, axis=0).tolist(),
        np.max(matrix, axis=1).tolist(),
        int(np.max(matrix))
    ]
    
    result['min'] = [
        np.min(matrix, axis=0).tolist(),
        np.min(matrix, axis=1).tolist(),
        int(np.min(matrix))
    ]
    
    result['sum'] = [
        np.sum(matrix, axis=0).tolist(),
        np.sum(matrix, axis=1).tolist(),
        int(np.sum(matrix))
    ]
    
    return result