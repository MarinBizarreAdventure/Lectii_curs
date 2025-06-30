# 2. Decorator pentru limitarea adâncimii recursivității
def limiteaza_recursivitate(max_depth=50):
    """Decorator care limitează adâncimea recursivității"""
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Obținem adâncimea curentă din call stack
            import inspect
            current_depth = len([frame for frame in inspect.stack() 
                               if frame.function == func.__name__])
            
            if current_depth > max_depth:
                raise RecursionError(
                    f"Recursivitate prea adâncă pentru {func.__name__}: "
                    f"{current_depth} > {max_depth}"
                )
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

@limiteaza_recursivitate(max_depth=10)
def factorial_limitat(n):
    """Factorial cu limitare de adâncime"""
    if n <= 1:
        return 1
    return n * factorial_limitat(n - 1)

print("🛡️ Testarea limitării recursivității:")
try:
    rezultat_ok = factorial_limitat(5)
    print(f"✅ factorial_limitat(5) = {rezultat_ok}")
    
    rezultat_problematic = factorial_limitat(15)  # Va depăși limita
    
except RecursionError as e:
    print(f"🛡️ Protecție activată: {e}")

print("\n" + "="*50)