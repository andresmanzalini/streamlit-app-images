# genAI streamlit App

simple genAI streamlit app de creacion de imagenes

app consiste en 2 partes>
    . text-to-image > crear imagenes a partir de texto con stable diffusion base xl
    . image-to-image > refina imagenes a partir de una imagen base. se agregan detalles con el prompt. en realidad es image+text-to-image

una vez hecho estos dos funciones, hacer que se combinen


### Construir imagen

docker build -t streamlit-app .


### Ejecutar contenedor

docker run -p 8501:8501 streamlit-app




#### Caracteristicas faltantes

. descargar la imagen

. memoria para tener mas contexto

. seleccionar estilo para fine tunear

