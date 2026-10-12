# 📚 RAG Local para mis Apuntes (con IBM Granite)

Este es mi primer proyecto montando un sistema RAG (Retrieval-Augmented Generation) en Python. Básicamente, es un script que te permite "chatear" con tus propios apuntes de clase en local, sin necesidad de internet y manteniendo la privacidad a tope. 

Lo he pensado específicamente para que funcione bien en ordenadores portátiles que no tienen una gráfica de la NASA (yo lo muevo en un MSI con 4GB de VRAM).

## 🚧 Estado actual: Fase Alpha

El programa funciona y responde bastante rápido, pero ten en cuenta un par de cosillas:
- A veces se hace un poco de lío si mezclamos idiomas, porque el modelo que convierte el texto a números (`nomic-embed-text`) está más pensado para el inglés. Más adelante probaré a meterle uno multilingüe.
- Lee sin problemas `.txt`, `.pdf`, `.docx` y `.odt`, pero si el archivo tiene un formato súper complejo (tablas raras, imágenes), le puede costar leerlo bien.

## 🛠️ Con qué está hecho
- **Python** (aprendiendo sobre la marcha, vengo de C/Java 😅)
- **LlamaIndex**: Para organizar la lectura de documentos y las búsquedas.
- **Ollama**: Para correr los modelos en local sin depender de APIs de pago.
- **Modelos**: 
  - Para pensar/hablar: `granite3.1-dense:2b` (va súper fluido).
  - Para los vectores: `nomic-embed-text`.

---

## ⚙️ Cómo descargarlo y hacerlo funcionar

Si quieres probarlo, sigue estos pasos:

### 1. Preparar el motor (Ollama)
Primero necesitas descargarte [Ollama](https://ollama.com/) e instalarlo. 
Abre una terminal y bájate los dos modelos que usa el código:
```bash
ollama pull granite3.1-dense:2b
ollama pull nomic-embed-text
```

### 2. Descargar este proyecto
Copia este repositorio en tu ordenador:
```bash
git clone https://github.com/DevLeonJA/RAG_Estudio.git   
cd mi-rag-estudios
```

### 3. Crear el entorno de Python
Para no ensuciar tu ordenador con librerías, creamos un entorno virtual:
```bash
python -m venv entorno
```
Actívalo:
- **En Windows:** `entorno\Scripts\activate`
- **En Mac/Linux:** `source entorno/bin/activate`

Instala las librerías necesarias:
```bash
pip install -r requirements.txt
```

### 4. ¡A estudiar!
1. Crea una carpeta llamada `datos` dentro del proyecto (si no está creada ya).
2. Mete ahí tus apuntes en PDF, Word, ODT o TXT.
3. Con el entorno activado, ejecuta:
```bash
python app.py
```
La primera vez puede tardar un pelín en cargar el modelo en la tarjeta gráfica, pero luego vuela. ¡Escribe "salir" cuando termines de estudiar!