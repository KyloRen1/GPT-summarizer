# Simple OPEN AI GPT summarizer
I didn't like opensource versions, so I did my own
## Installation
```console
python3 -m venv venv
source venv/bin/activate
python -m pip install pip setuptools wheel
python -m pip install -e .
```

## Usage
Enter your [OPEN AI API KEY](https://platform.openai.com/account/api-keys) top `config.py` file

```python
python main.py --filepath=PDF_FILE_PATH
```
If input text is long than the maximum number of tokens the model can handle, text is slitted into multiple chucks and the results are concatenated. Final text is saved to `cache` folder (unless configured otherwise) with postfix `_summary`
