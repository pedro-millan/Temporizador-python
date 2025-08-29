# ⏱️ Temporizador en Python

Este proyecto implementa una clase `Timer` en Python que simula el comportamiento de un reloj digital. Permite avanzar o retroceder el tiempo en segundos, y mantiene un formato legible (hh:mm:ss) en todo momento.

## 🚀 Características

- Inicialización con horas, minutos y segundos.
- Método `next_second()` para avanzar un segundo.
- Método `prev_second()` para retroceder un segundo.
- Representación formateada con `__str__()`.
- Control de desbordamientos (60 seg → 1 min, 60 min → 1 h, etc.).
- Control de ciclos (23:59:59 → 00:00:00 y viceversa).

## 📦 Uso

```python
timer = Timer(23, 59, 59)
print(timer)           # 23:59:59
timer.next_second()
print(timer)           # 00:00:00
timer.prev_second()
print(timer)           # 23:59:59
```

## 🧠 Aprendizajes

Este proyecto pone en práctica:

- Programación orientada a objetos (POO).
- Encapsulamiento con atributos privados.
- Métodos especiales (`__str__()`).
- Buenas prácticas para construir clases reutilizables.

## 🛠️ Autor

Este repositorio fue creado como parte del proceso de aprendizaje de Python, y representa una muestra de conocimientos sobre clases, métodos y control del tiempo.

---

> Si te ha sido útil o inspirador, siéntete libre de darle una ⭐️ al repo o dejarme tu feedback.
