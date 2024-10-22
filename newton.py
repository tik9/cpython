
import math

def main():
    x0 = 1.0
    x0 = 1961
    
    # print(f)
    # newton(x0)
    nullstelle,it = newton_method(f, df, x0)
    print(f"Gefundene Nullstelle: {nullstelle}")

def newton(x0):

    x1=x0-(f(x0))/df(x0)
    x2=x1-(f(x1))/df(x1)

    print(x1,x2)

    # for i in range(3):
        # print(i)

def newton_method(f, df, x0, tolerance=1e-7, max_iterations=10):
    """
    Implementiert das Newton-Verfahren zur Lösung von f(x) = 0.    
    :param f: Funktion f(x)
    :param df: Ableitung der Funktion f(x)
    :param x0: Startwert für die Iteration
    :param tolerance: Toleranz für die Konvergenzbedingung
    :param max_iterations: Maximale Anzahl von Iterationen
    :return: Die angenäherte Nullstelle und die Anzahl der Iterationen
    """
    
    xn = x0
    for n in range(max_iterations):
        fxn = f(xn)
        dfxn = df(xn)
        
        if dfxn == 0:
            print("Die Ableitung ist 0. Kein Newton-Verfahren möglich.")
            return None
        
        # Aktualisiere x-Wert gemäß Newton-Verfahren
        xn_next = xn - fxn / dfxn
        
        # Prüfen, ob die Toleranz erreicht wurde
        if abs(xn_next - xn) < tolerance:
            print(f"Nullstelle gefunden nach {n+1} Iterationen: x = {xn_next}")
            return xn_next, n+1
        
        xn = xn_next
    
    print("Max. Anzahl von Iterationen erreicht.")
    return None

# def f(x):
#     return x**2 - 2

# def df(x):
#     return 2*x

def f(x):
    return (9.8606/(1+1.1085*10**25*math.exp(-0.029*x)))-9
    
def df(x):
    return -9.8606*-1.1085*10**25*math.exp(-0.029*x)*0.029/(1+1.1085*10**25*math.exp(-0.029*x))**2


if __name__=='__main__':
    main()

