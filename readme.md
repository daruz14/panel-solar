# ¿Cuántos paneles caben?

## 🎯 Objetivo

El objetivo de este ejercicio es poder entender tus habilidades como programador/a, la forma en que planteas un problema, cómo los resuelves y finalmente cómo comunicas tu forma de razonar y resultados.

<aside>
🙂 **¿Qué esperamos?** La idea es simular de la forma más simple y completa una tarea dentro del equipo técnico de Ruuf. El ejercicio está enfocado en desarrollar un algoritmo que reciba inputs, resuelva un problema matemático y entrega la respuesta.

</aside>

---

## 🛠️ Problema

El problema a resolver consiste en encontrar la máxima cantidad de rectángulos de dimensiones “a” y “b” (paneles solares) que caben dentro de un rectángulo de dimensiones “x” e “y” (techo), según se muestra en la siguiente figura:

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/5fd840ef-599c-4be1-aeef-1ea8a114fce5/9dd7880a-77cd-4127-984b-00d26d5549bd/Untitled.png)

Por ejemplo, podríamos decir que en el siguiente ejemplo caben 5 rectángulos de dimensiones 1 y 2, en un rectángulo de dimensiones 3 y 5.

![               ¿O caben más? 👀](https://prod-files-secure.s3.us-west-2.amazonaws.com/5fd840ef-599c-4be1-aeef-1ea8a114fce5/f2217992-2d65-47e2-9865-087d5dbbb978/Untitled.png)

               ¿O caben más? 👀

## 📜 Instrucciones

- Usa el lenguaje/framework que más te acomode. No hay una solución única al problema, por lo que puedes hacer lo que prefieras.
- El algoritmo debe ser una sola función que reciba las dimensiones y retorne un solo integer con la cantidad de paneles que caben.
- No hay restricciones de orientación. Pon todos los rectángulos que puedas en la posición y sentido que prefieras.
- No se pide nada gráfico.

## ✅ Algunos ejemplos para que revises tu código:

- Paneles 1x2 y techo 2x4 ⇒ Caben 4
- Paneles 1x2 y techo 3x5 ⇒ Caben 7
- Paneles 2x2 y techo 1x10 ⇒ Caben 0

---

## 💰 Bonus Opcional

¿Te pareció demasiado fácil? ¿Te entretuviste y quieres resolver algo un poco más complejo?

Te dejamos dos alternativas que puedes intentar resolver también. Pero ojo que con resolver el problema base bien ya es suficiente para entrar al proceso 🙂 Si haces el bonus, puedes explicarlo o no en el video. Solo recuerda que no debes pasarte de los 3 minutos de duración.

**Opción 1**

Repetir el ejercicio base, considerando un techo triangular, isóceles.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/5fd840ef-599c-4be1-aeef-1ea8a114fce5/bf1e4651-277b-4a42-b9ea-b59fe177793b/Untitled.png)

**Opción 2**

Repetir el ejercicio base considerando dos rectángulos iguales superpuestos. Puedes parametrizar la superposición entre ambos rectángulos.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2db5592c-1f8d-4fd4-abeb-09f3f856b429/Untitled.png)