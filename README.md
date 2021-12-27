# Bot simple ML

## Run

Crear ambiente virtual:

```bash
python -m venv env
```

Activar ambiente:

```bash
. env/scripts/activate
```

Instalar requerimientos:

```bash
pip install numpy pydantic torch python-dotenv nltk
```

O tambien utilizando:

```bash
pip install requirements.txt
```

Entrenar modelo:

```bash
python src/models/train_model.py
```

El modelo se entrena solo una vez o bien cada vez que se actualiza el archivo de ***data/intents.json***

Ejecutar app de chat:

```bash
python src/app.py
```

## Intents

```file
data/intents.json
```
