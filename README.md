# 📚 RAG para Estudios con IBM Granite

Este es un proyecto personal para crear un sistema **RAG (Retrieval-Augmented Generation)** que funciona 100% en local. Permite "chatear" con mis propios apuntes de clase garantizando la máxima privacidad y adaptado a ordenadores con recursos limitados (4GB de VRAM).

## 🚀 Características
- **100% Local y Privado**: No requiere conexión a internet y tus documentos no se envían a la nube.
- **Multiformato**: Lee automáticamente archivos `.txt`, `.pdf`, `.docx` (Word) y `.odt` (LibreOffice).
- **Ligero**: Utiliza modelos optimizados como **IBM Granite** para un rendimiento fluido en equipos estándar.

## 🛠️ Tecnologías utilizadas
- **Python** 
- **LlamaIndex**: Framework principal para orquestar el RAG.
- **Ollama**: Motor local para ejecutar los modelos de Inteligencia Artificial.
- **Modelos:**
  - LLM: `granite3.1-dense:2b` (o `granite-code:3b`)
  - Embeddings: `nomic-embed-text`

## ⚙️ Instalación y Uso

1. **Instalar Ollama** desde [ollama.com](https://ollama.com/) y descargar los modelos en la terminal:
   ```bash
   ollama pull granite3.1-dense:2b
   ollama pull nomic-embed-text