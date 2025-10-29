🚗 Proyecto Sprint 7 — Aplicación de Análisis de Vehículos
📘 Descripción general

Esta es una aplicación web interactiva desarrollada con Streamlit, Pandas y Plotly Express.
Permite visualizar y analizar datos de anuncios de venta de vehículos usados, mostrando información relevante sobre el kilometraje, precio y otras variables del conjunto de datos vehicles_us.csv.

⚙️ Funcionalidad principal

La aplicación ofrece dos visualizaciones interactivas que permiten explorar los datos fácilmente:

📊 Histograma: muestra la distribución del kilometraje (odometer) de los vehículos.

🔹 Gráfico de dispersión: representa la relación entre el precio (price) y el kilometraje, ayudando a detectar patrones o tendencias.

▶️ Cómo ejecutar la aplicación localmente

Clona este repositorio:

git clone https://github.com/Lilianampu/Sprint7-project.git
cd Sprint7-project


Crea y activa un entorno virtual (opcional pero recomendado):

python -m venv venv
source venv/bin/activate     # En macOS/Linux  
venv\Scripts\activate        # En Windows


Instala las dependencias necesarias:

pip install -r requirements.txt


Ejecuta la aplicación:

streamlit run app.py


Abre en tu navegador la URL local que se mostrará (por ejemplo, http://localhost:8501).

🌐 Despliegue en Render

El proyecto está listo para ser desplegado en Render.
Solo es necesario conectar el repositorio, definir el comando de inicio:

streamlit run app.py


y establecer el entorno de ejecución con las dependencias del archivo requirements.txt.

👩‍💻 Autor

Lilian Ampudia Pérez
Proyecto desarrollado como parte del Sprint 7 del programa de análisis de datos.
