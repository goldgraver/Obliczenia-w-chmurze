import numpy as np
import matplotlib.pyplot as plt

def calculate_stresses():
    print("\nObliczanie naprężeń normalnych od rozciągania i zginania belki prostokątnej.")
	#Pozioma belka o prostokątnym przekroju utwierdzona jest z jednej strony,
	#natomiast drugi jej koniec jest swobodny. Na swobodnym końcu wprowadzona zostaje
	#siła normalna, siła poprzeczna i moment gnący z konwencją zgodną z wytrzymałością konstrukcji.

    # Dane wejściowe
    try:
        b = float(input("Podaj szerokość przekroju prostokątnego (b) [m]: "))
        h = float(input("Podaj wysokość przekroju prostokątnego (h) [m]: "))
        if b <= 0 or h <= 0:
            raise ValueError("Wymiary przekroju muszą być dodatnie!")
        L = float(input("Podaj długość belki (L) [m]: "))
        if L <= 0:
            raise ValueError("Długość belki musi być dodatnia!")

        N = float(input("Podaj wartość siły normalnej na swobodnym końcu belki(N) [N]: "))
        T = float(input("Podaj wartość siły poprzecznej na swobodnym końcu belki(T) [N]: "))
        M = float(input("Podaj wartosć momentu gnącego na swobodnym końcu belki (M) [Nm]: "))

        # Wyznaczanie momentu gnącego w utwierdzonym końcu belki
        M_max = M + T * L
        print(f"\nMoment gnący w utwierdzeniu belki (M_max): {M_max:.6f} Nm")

        # Pole przekroju
        A = b * h
        print(f"Pole przekroju (A): {A:.6f} m^2")

        # Moment bezwładności przekroju względem osi zginania
        I = (b * h**3) / 12
        print(f"Moment bezwładności przekroju (I): {I:.6f} m^4")

        # Naprężenie normalne od rozciągania/ściskania
        sigma_normal = N / A
        print(f"Naprężenie normalne od rozciągania/ściskania (\u03C3_n): {sigma_normal:.6f} Pa")

        # Maksymalne naprężenie od zginania
        sigma_bending = (M_max * h / 2) / I
        print(f"Maksymalne naprężenie od zginania (\u03C3_b): {sigma_bending:.6f} Pa")

        # Naprężenie całkowite w najniekorzystniejszym punkcie przekroju
        sigma_total_top = sigma_normal - sigma_bending  # Górne włókno
        sigma_total_bottom = sigma_normal + sigma_bending  # Dolne włókno

        print("\n--- Wyniki ---")
        print(f"Naprężenie całkowite w górnym włóknie: {sigma_total_top:.6f} Pa")
        print(f"Naprężenie całkowite w dolnym włóknie: {sigma_total_bottom:.6f} Pa")

        # Rysowanie wykresu momentu gnącego na długości belki
        x = np.linspace(0, L, 500)
        M = M + T * x

        plt.figure(figsize=(10, 6))
        plt.plot(x, M, label="Moment gnący M(x)", color="blue")
        plt.xlabel("Długość belki (x) [m]")
        plt.ylabel("Moment gnący (M) [Nm]")
        plt.title("Wykres momentu gnącego na długości belki")
        plt.grid()
        plt.legend()
        plt.show()

    except ValueError as e:
        print(f"Błąd: {e}")
    except Exception as e:
        print(f"Nieoczekiwany błąd: {e}")

if __name__ == "__main__":
    calculate_stresses()
