# vulneroReposnsable

Este proyecto tiene como objetivo educar sobre la importancia de la seguridad informática mediante la simulación de una alerta de seguridad.

## Instrucciones

1. Instalar Python desde [python.org](https://www.python.org/downloads/).
2. Instalar `pip` y `PyInstaller`:
    ```bash
    python -m ensurepip --upgrade
    pip install pyinstaller
    ```
3. Crear el ejecutable:
    ```bash
    cd \Users\MacBook\Proyectos_web\vulneroReposnsable\
    pyinstaller --onefile alerta.py
    ```
4. Renombrar el ejecutable para que parezca un documento legítimo:
    ```bash
    mv dist/alerta.exe dist/documento_importante.pdf.exe
    ```
5. El ejecutable se encontrará en el directorio `dist`. Ejecuta el archivo para ver la alerta de seguridad.

## Distribución

Para distribuir el ejecutable a otros usuarios:

1. Copia el archivo ejecutable del directorio `dist` a la computadora del usuario.
2. Asegúrate de incluir cualquier archivo adicional necesario, como imágenes, en el mismo directorio que el ejecutable.
3. Los usuarios pueden ejecutar el archivo haciendo doble clic en `documento_importante.pdf.exe`.

## Nota de Seguridad

Este proyecto debe ser utilizado únicamente con fines educativos y en un entorno controlado. No intentes engañar a los usuarios para que ejecuten archivos sin su conocimiento, ya que esto puede ser considerado malicioso y es una violación de las políticas de seguridad y ética.


Windows: 

pip install pyinstaller

cd /Users/MacBook/Proyectos_web/vulneroReposnsable/
pyinstaller --onefile alerta.py

mv dist/alerta.exe dist/documento_importante.pdf.exe

