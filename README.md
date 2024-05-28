# pqc-proyecto2
Archivos del proyecto 2 de criptografia

## Instalación

---

Para poder hacer la ejecución del proyecto, se requiere hacer la instalación del programa CMAKE, para lo cual se debe ir a la página: https://cmake.org/download/. 
Elegir el sistema operativo en donde se vaya a revisar el código e instalar el programa.

Posteriormente se tiene que construir la biblioteca **liboqs** en nuestro entorno, el cual se realiza con los siguientes comandos en la línea de comandos o CMD como administrador:

```
git clone --depth=1 https://github.com/open-quantum-safe/liboqs
cmake -S liboqs -B liboqs/build -DBUILD_SHARED_LIBS=ON
cmake --build liboqs/build --parallel 8
cmake --build liboqs/build --target install
```
La última línea puede requerir ```sudo``` antes en los sistemas basados en UNIX. La bandera ```--parallel 8``` tiene que ser modificado el 8 para que coincida con el número de núcleos disponibles en su computadora.

En plataformas basadas en UNIX es posible que se tenga que configurar la variable de entorno ```LD_LIBRARY_PATH``` (```DYLD_LIBRARY_PATH``` en MacOS) para dirigir a la ruta del directorio de la biblioteca liboqs.

```
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
```

En plataformas de Windows, también tenemos que configurar el path, esto dentro del panel de control usando la herramienta "Editar las variables de entorno del sistema", damos click en el botón que dice "Variables de entorno", dentro del apartado de "Variables del sistema" hay que encontrar el que dice "Path" y seleccionar "Editar". En la nueva ventana que se abre, tenemos que agregar la ruta hacia la carpeta bin dentro de liboqs. Usualmente esta es la ruta predeterminada ```C:\Program Files (x86)\liboqs\bin```.

Además se tiene que agregar la siguiente línea en las plataformas Windows.

```
cmake -S liboqs -B liboqs/build -DCMAKE_INSTALL_PREFIX="C:ruta/a/liboqs" -DCMAKE_WINDOWS_EXPORT_ALL_SYMBOLS=TRUE -DBUILD_SHARED_LIBS=ON
```

---

Requerimos ahora crear y activar un ambiente virtual de Python para tener mejor contenido el programa, de nuevo en la línea de comando o CMD como Administrador ejecutamos las siguientes líneas:

```
python3 -m venv venv
. venv/bin/activate
python3 -m ensurepip --upgrade
```

En caso de utilizar una plataforma Windows, la línea ```. venv/bin/activate``` se sustituye por ```venv\Scripts\activate.bat```.

---

Una vez instalado y activado el entorno virtual, el archivo **main.py** tiene que encontrarse dentro de nuestra carpeta del proyecto, no necesariamente dentro de la carpeta del ambiente virtual.

Ahora se procede a ejecutar el archivo con la instrucción

```python main.py```

En la salida que se obtiene, se observa que se ejecuta primero una función en donde está implementado el esquema ML-KEM, posteriormente viene la ejecución de una función que implementa el esquema de firma ML-DSA, y finalmente se hace la ejecución de la función que implementa el esquema de firma SLH-DSA.

Al final se muestra el tiempo de ejecución de cada uno de las funciones, para poder visualizar cuanto tiempo se están tardando en ejecutar y posteriormente hacer una comparación entre estos algoritmos.
