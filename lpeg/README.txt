Der aktuelle Versuch, das bestehende LPEG-Modul insofern zu modifizieren, 
dass Bytecodes ausgebeben werden, die f�r weitere Verarbeitung verwendet werden k�nnen.

Bisherige Probleme beinhalten

1) In der C-Implementierung scheint es mehr Bytecodes zu geben als im Paper genannt werden

2) Die Ausgabe der Bytecodes erfolgt w�hrend sie ausgef�hrt werden, nicht wenn sie auf den Stack abgelegt werden (Performance)

3) Die Ausgabe erfolgt Parameterlos (ein Choice-Bytecode wird z.b. nicht mit dem zugeh�rigen Label ausgegeben)