## Tipizzazione dinamica

Per dichiarare una variabile in python facciamo:

```python
a = 3
```

<p align="justify">
In pratica, <b>in python dichiariamo la variabile senza specificare che tipo di dato essa dovrà contenere</b> (un numero intero, un numero reale, un carattere o un'intera stringa di testo).
Questo è molto diverso rispetto ad altri linguaggi che studierai già dal prossimo anno (C, C++, Java) dove per dichiarare una variabile si deve specificare il suo tipo: per esempio in C avremmo fatto:
</p>

```c
int a = 3
```

Quando scriviamo <code>a = 3</code> come fa python a sapere che è sarà un intero?

<p align="justify">
La risposta è che <b>python è un linguaggio a tipizzazione dinamica</b>: cioè i tipi vengono determinati dinamicamente durante l'esecuzione e non a seguito di dichiarazione esplicite contenute nel codice sorgente.
</p>

> [!IMPORTANT]
> In python non bisogna preoccuparsi di dichiarare le variabili prima di usarle

<p align="justify">
Una variabile viene creata la prima volta che le viene assegnato un valore. Assegnamenti successivi modificano il valore associato al nome (identificatore) precedentemente creato. Si può pensare dunque che l'inizializzazione di una variabile crea la variabile stessa quindi tutte le variabili devono essere esplicitamente assegnate prima di poter essere utilizzate. L'uso di variabili non assegnate genera sempre un errore.
</p>

<p align="justify">
<b>I tipi non sono associati alle variabili (agli identificatori) ma agli oggetti</b> (l'effettiva locazione di memoria che contiene il dato) a cui l'identificatore punta (o si riferisce). Esiste dunque una differenza tra i nomi e gli oggetti; quando scriviamo:
</p>

```python
a = 3
```

1. Crea l'oggetto (spazio in memoria) per contenere il valore <code>3</code>
2. Crea la variabile (il nome o identificare) <code>a</code> (se non esiste già)
3. Collega la variabile <code>a</code> all'oggetto che contiene il valore <code>3</code>. Questo collegamento è detto <b>refence</b>


<p align=center>
<img src="https://github.com/TheBitPoets/friedpython/blob/main/images/tipizzazione_dinamica/1.png"></img>
</p>

Un oggetto ha due campi:
1. <b>Un designatore di tipo</b> (usato per memorizzare il tipo)
2. <b>Un contatore di reference</b> (usato per determinare quando si può eliminare dalla memoria un oggetto non referenziato)
   
