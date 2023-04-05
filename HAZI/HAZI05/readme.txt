- load_csv: Az adatok beolvasása. Emellett egy shuffle is történik, ami segítségével megváltoztatjuk a sorok sorrendjét, hogy ha a bemenetei adatok valamilyen szabályszerűen jöttek be, akkor ezt a szabályt megbontsuk.

- train_test_spit: Létrehozzuk a train és a test adatsorokat. Ennek segítségével fogunk tanítani, illetve accuracy-t meghatározni.

- euclidean: Euklideszi távolságot nézünk a teszt adathalmazon, vagyis azt vizsgáljuk, hogy mekkora a távolság a mért és a tényleges ártákek között.

- predict: A távolságok függvényében sorba rendezi az elemet, és megvizsgálja, hogy melyik osztály fordul elő a leggyakrabban. 

- accuracy: Kiszámolja a true positive eredmények számát, vagyis azokat az értékeket, amiket helyesen vettünk helyesnek.

