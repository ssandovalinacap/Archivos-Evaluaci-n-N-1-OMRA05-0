 
# Crear directorio para alojar los scripts
mkdir /home/devasc/scripts_evaluacion
cp /home/devasc/*.py /home/devasc/scripts_evaluacion/
# Inicializar el directorio como repositorio Git
cd /home/devasc/scripts_evaluacion
git init

# Generar un commit con el título "Evaluación N°1 OMRA05"
git add .
git commit -m "Evaluacion N°1 OMRA05"

# Crear repositorio público en GitHub
# Subir los archivos al repositorio
# Clonar el repositorio en la máquina virtual para demostrar que los archivos se descargan y ejecutan sin errores
