# La Bayeta de la Fortuna
<div style="text-align: justify;">
<img src="icon.png"/>
Vamos a simular la creación de una aplicación web sencilla llamada “La
Bayeta de la Fortuna”. Cada vez que accedamos a la web, nos dirá un
texto auspicioso aleatorio. Para desarrollar y desplegar la aplicación
tendremos que asegurarnos de lo siguiente:

1.  No perdemos código (ni tiempo repitiendo dicho código) y
realizamos un mantenimiento del mismo. Además, trabajaremos
colaborativamente y queremos publicar distintas versiones de
nuestra aplicación conforme vayamos avanzando en su desarrollo.

1. El proyecto debe poder clonarse y compilarse/ejecutarse sin que
esto sea un problema de dependencias.

1.  Además, queremos asegurarnos de que el ecosistema en el que se ejecuta la aplicación se mantiene limpio y estable, de forma que no haya diferencias entre ejecutarlo en local o hacerlo en un servidor
Para ello vamos a utilizar (sí, lo has adivinado) Python (venv), Git y Docker


#### La app de bayeta se puede usar tanto sin DOCKER como con él.

## CON DOCKER

### Requisitos
Instalar Docker en el sistema, para ello podemos instalarlo.
```
sudo apt install docker-ce
```

Si quieres instalar de forma mas segura puedes hacerlo siguiendo estos pasos de **[Digitalocean](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04)**


### Ejecución
Para ejecutar la app hay que bajarse el repositorio y construir el docker.
```
git clone https://github.com/Andres1861083/1861083_pps_python_git_docker_.git

cd 1861083_pps_python_git_docker_

docker build -t app-bayeta .

docker pull mongo:latest
```

Una vez construido, ejecutamos los docker
```
docker run -p 5000:5000 --name app-bayeta app-bayeta:latest

docker run -p 27017:27017 --name mongodb -d mongo:latest 
```

Se crea una red y se meten dentro de la red.
```
docker network create bayeta-network 

docker network connect bayeta-network mongodb 

docker network connect bayeta-network app-bayeta

docker start app-bayeta
```

Por ultimo, en el navegador usamos la url **http://127.0.0.1:5000**

## SIN DOCKER

Para hacerlo sin docker hay que usar Python3 y virtualizarlo.

### Requisitos
Para usarlo hay que instalar python3.10 


```
sudo apt update && sudo apt upgrade -y && sudo apt autoremove -y

sudo apt install python3.10 -y && sudo apt install python3.11-venv -y
```
### ¡¡¡ATENCIÓN!!! 
***[depende de la distribucion cambiar el instalador y la version que puedas instalar]***


### Crear entorno virtual de Python
```
python3 -m venv venv

source venv/bin/activate

```

### Instalación y Ejecución

Para ejecutar el programa usa:
```
pip install -r requirements.txt

python3 app.py
```
Por ultimo ve al navegador y por la URL http://127.0.0.1:5000
</div>
