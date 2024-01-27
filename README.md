# La Bayeta de la Fortuna

Vamos a simular la creación de una aplicación web sencilla llamada “La
Bayeta de la Fortuna”. Cada vez que accedamos a la web, nos dirá un
texto auspicioso aleatorio. Para desarrollar y desplegar la aplicación
tendremos que asegurarnos de lo siguiente:

1.  No perdemos código (ni tiempo repitiendo dicho código) y
realizamos un mantenimiento del mismo. Además, trabajaremos
colaborativamente y queremos publicar distintas versiones de
nuestra aplicación conforme vayamos avanzando en su desarrollo.

2. El proyecto debe poder clonarse y compilarse/ejecutarse sin que
esto sea un problema de dependencias.

3.  Además, queremos asegurarnos de que el ecosistema en el que se ejecuta la aplicación se mantiene limpio y estable, de forma que no haya diferencias entre ejecutarlo en local o hacerlo en un servidor
Para ello vamos a utilizar (sí, lo has adivinado) Python (venv), Git y Docker

### Entorno virtual de Python
```
python3 -m venv venv
source venv/bin/activate
```


### Instalación

Para instalar las dependencias, ejecuta los siguientes comandos:
```
pip install -r requirements.txt
```

