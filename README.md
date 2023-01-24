# :robot: Bot simple ML

Bot using ML

## :floppy_disk: Installation

```bash
python -m venv env
```

```bash
. env/scripts/activate
```

```bash
pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

## :wrench: Config

Setting all the intents in: `data/intents.json`

## :runner: Run

Train the model:

```bash
python src/models/train_model.py
```

Run the chat:

```bash
python src/app.py
```
