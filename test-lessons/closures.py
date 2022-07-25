

def derivative(f, epsilon):
    return lambda x: (f(x + epsilon) - f(x)) / epsilon