# Health Risk Predictor

A Streamlit learning project that uses a trained scikit-learn Random Forest model to estimate a broad health-risk category from lifestyle and health inputs.

> **Educational demo only.** This model is not clinically validated and must not be used for diagnosis, treatment, or healthcare decisions.

## What it demonstrates

- A Streamlit form for structured input
- Categorical feature encoding and model inference
- A saved model and encoder loaded from pickle files
- A simple visualization of selected input factors

The training notebook documents the workflow and experiments. The checked-in application loads the model artifacts directly; it does not train the model at startup.

## Project files

| File | Purpose |
| --- | --- |
| `app.py` | Streamlit interface and prediction flow |
| `Health_RiskPredictor.ipynb` | Data exploration and model-training notebook |
| `Health_RiskPredictor.pkl` | Serialized model |
| `label_encoder.pkl` | Serialized label encoders |

## Run locally

Use Python 3 and install the packages used by the app:

```bash
git clone https://github.com/Sameer-ship-it/HEALTH_RISK_PREDICTOR.git
cd HEALTH_RISK_PREDICTOR
python -m venv .venv
```

Activate the environment, then install the dependencies:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS / Linux
source .venv/bin/activate
```

```bash
python -m pip install streamlit pandas numpy scikit-learn matplotlib plotly
streamlit run app.py
```

The application opens at the local URL printed by Streamlit.

## Model and data notes

The notebook uses a synthetic health dataset and records model experiments. Metrics in a notebook are not evidence of clinical performance; evaluate the final model on a documented, representative holdout set before making any performance claims. The repository does not include a separate CSV training dataset.

Only load pickle files from sources you trust. Pickle deserialization can execute code.

## Limitations

- Synthetic or limited training data may not represent real populations.
- The output is a model estimate, not a medical assessment.
- The feature set and thresholds are demonstration choices, not clinical guidance.

## Author

[Sameer Raza](https://github.com/Sameer-ship-it)
