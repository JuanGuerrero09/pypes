# Current structure

```bash
src/
└── pypes/
├── __init__.py
├── liquids.py # Liquid class
├── materials.py # Material class
├── pipelines/ # Folder for pipeline-related logic
│ ├── __init__.py
│ ├── pipeline.py # Pipeline class
│ ├── calculations.py # Functions like Reynolds number, head loss
│ ├── utils.py # Helper functions (e.g., unit conversions)
├── head_loss.py
├── reynolds.py
├── py.typed
```
