# Cambiar al directorio link_bio
Set-Location -Path link_bio

# Crear un entorno virtual de Python
python -m venv .venv

# Activar el entorno virtual
& .\.venv\Scripts\Activate.ps1

# Actualizar pip
pip install --upgrade pip

# Instalar las dependencias del archivo requirements.txt
pip install -r requirements.txt

# Eliminar el directorio 'public' si existe
Remove-Item -Recurse -Force public

# Inicializar Reflex
reflex init

# Exportar el frontend de Reflex
$env:API_URL = "https://devsdav-web.up.railway.app"
reflex export --frontend-only

# Descomprimir frontend.zip en el directorio 'public'
Expand-Archive -Path frontend.zip -DestinationPath public

# Eliminar el archivo frontend.zip
Remove-Item -Force frontend.zip

# Desactivar el entorno virtual
deactivate