#comandos para levantar el docker

#crear imagen con:
    > docker build -t mi-api-rest .

# correr la imagen como contenedor
    > docker run -p 4000:4000 mi-api-rest

# eliminar todas las imagenes:
    > docker rmi -f $(docker images -a -q)

# eliminar todos los procesos
    > docker rm -fv $(docker ps -aq)