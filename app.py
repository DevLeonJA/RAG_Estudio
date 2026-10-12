# Mi primer proyecto RAG para chatear con mis apuntes en local
# Usando LlamaIndex y los modelos de IBM Granite por Ollama

import os

# Importo las piezas principales de LlamaIndex para montar el RAG
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.core.readers.base import BaseReader
from llama_index.core.schema import Document

# Conectores para que LlamaIndex se hable con el Ollama que tengo instalado
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding

# Librerías para leer los .odt (los apuntes de LibreOffice)
import odf.opendocument
import odf.teletype
from odf.text import P


# Como LlamaIndex no sabe leer los .odt de base, me he creado esta clase
# heredando de BaseReader para explicárselo.
class ODTReader(BaseReader):
    def load_data(self, file, extra_info=None):
        # Cargamos el archivo físico
        doc = odf.opendocument.load(str(file))
        text_nodes = []
        
        # Buscamos todos los párrafos (P) y sacamos el texto limpio
        for paragraph in doc.getElementsByType(P):
            text_nodes.append(odf.teletype.extractText(paragraph))
            
        # Lo juntamos todo con saltos de línea para que quede legible
        content = "\n".join(text_nodes)
        
        # LlamaIndex necesita que le devuelva un objeto tipo "Document"
        return [Document(text=content, extra_info=extra_info or {})]


# Lo meto todo en un main() porque dicen que es buena práctica en Python
def main():
    print("Arrancando el sistema RAG... ten paciencia si tarda la primera vez.")

    # --- 1. Configurar los modelos ---
    # Uso Granite 2B porque mi gráfica MSI solo tiene 4GB de VRAM y si meto uno más grande explota.
    # Le pongo un timeout de 120s porque al cargar el modelo por primera vez el portátil se queda pensando un buen rato.
    Settings.llm = Ollama(model="granite3.1-dense:2b", request_timeout=120.0)

    # El modelo que convierte el texto en vectores matemáticos
    Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text")
    print("Modelos de IA configurados.")

    # --- 2. Leer los apuntes ---
    print("Buscando archivos en la carpeta 'datos'...")
    
    # Le digo que cuando vea un .odt, use la clase que programé arriba
    mis_extractores = {
        ".odt": ODTReader(),
    }

    # El lector principal. Le paso la carpeta y los formatos que quiero que pille.
    reader = SimpleDirectoryReader(
        input_dir="datos",
        required_exts=[".odt", ".pdf", ".docx", ".txt"],
        file_extractor=mis_extractores
    )

    documents = reader.load_data()
    print(f"He cargado {len(documents)} trozos de archivos.")

    # --- 3. Crear el cerebro (Índice Vectorial) ---
    print("Vectorizando los aarchivos...")
    
    # Aquí es donde coge el texto y lo guarda como números en memoria para buscar luego
    index = VectorStoreIndex.from_documents(documents)

    # Preparo el buscador. streaming=True es para que escriba palabra por palabra como ChatGPT
    query_engine = index.as_query_engine(streaming=True)
    print("¡Índice creado!")

    # --- 4. El Chat ---
    print("\n" + "=" * 50)
    print("Todo listo. Ya puedes preguntarle a Granite sobre los temas.")
    print("Escribe 'salir' para cerrar el programa.")
    print("=" * 50)

    # Bucle infinito para poder hacer más de una pregunta
    while True:
        try:
            question = input("\nPregunta: ")
            
            # Por si escribo salir en mayúsculas o minúsculas
            if question.lower() in ['exit', 'salir']:
                print("Cerrando el RAG.")
                break
                
            print("\nGranite: ", end="")
            
            # Hacemos la consulta y mostramos la respuesta en directo
            response = query_engine.query(question)
            response.print_response_stream()
            print("\n")
            
        except Exception as e:
            # Pongo el try-except para que si Ollama peta no se me cierre la consola de golpe
            print(f"\nHa dado un error: {e}")

# Esto es para que ejecute el main solo si arranco el archivo directamente
if __name__ == "__main__":
    main()