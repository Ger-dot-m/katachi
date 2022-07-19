# katachi
Este proyecto analiza el impacto de las noticias sobre el Bitcoin sobre los precios de esta criptomoneda.
## Estructura
- Extracción de datos.ipynb.

  Se extraen datos de internet mediante web scrapping: se obtienen los enlaces y de estos se extrae el cuerpo de la página
- Preparación de datos.ipynb.

  En un mismo día se publican varias noticias sobre el Bitcoin, entonces hay dos opciones: Elegir sólo una noticia por día o mezclar las noticias de todo un
  día en una sola entrada. Ambas con ventajas y desventajas, sin embargo, se realiza la segunda opción.
- Modelos.

  Con los datos listos para ser trabajados, en este archivo se estandarizan las entradas y se prueban diferentes modelos, exportando únicamente el de mejores
  resultados
<br>

## Resultados y observaciones
Finalmente, se obtuvo un modelo con precisión del 55%, es de esperarse un resultado así no sólo por todos los factores inherentes al cambio de valor en el Bitcoin,
si no también por la escaces de datos.

### Sobre la escaces de los datos.
Ciertamente, conseguir una fuente para obtener información puede llegar a ser complicado, en esto se ve involucrado la fiabilidad del sitio, su seguridad y 
la estructura de su página web. Teniendo en cuenta lo anterior, el algoritmo recopiló más de 1,000 noticias diferentes, la cual tras la preparación de los 
datos se redujo aproximadamente a 100 entradas, luego, en la separación de datos de prueba y entrenamiento, el modelo fue entrenado con cerca de 80 entradas.

## Automatización y acomulación de datos
Por el punto anterior, se implementa un escucha que obtenga datos de forma pasiva y más selectiva, la cual servirá para mejorar la cantidad y calidad de los 
datos, caso que conducirá a mejores resultados y una mayor precisión.
