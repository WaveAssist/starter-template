
<h1 align="center">WaveAssist Starter Template</h1>
<p align="center">
  <img src="https://img.shields.io/badge/WaveAssist-Starter_Template-007F3B" alt="WaveAssist Starter Template" />
  <a href="https://waveassist.io/templates/starter-template">
    <img src="https://img.shields.io/badge/Deploy_with-WaveAssist-007F3B" alt="Deploy with WaveAssist" />
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License" />
  </a>
</p>

---

## 🚀 Overview

The **WaveAssist Starter Template** is a lightweight, three-node ETL (Extract, Transform, Load) pipeline demonstrating the core power of the [WaveAssist](https://waveassist.io) automation platform. Use this template as a springboard to build and deploy your own data workflows in minutes.

---

## 🔗 Pipeline Flow

```text
IngestData → TransformData → LoadData
```

1. **IngestData** (`ingest_data.py`)
   Initializes WaveAssist and writes sample records:

   * A greeting message
   * A basic customer object

2. **TransformData** (`transform_data.py`)
   Reads stored data, enriches it by:

   * Converting `city` to uppercase
   * Calculating `name_length`
   * Building a personalized greeting combining the greeting and customer name

3. **LoadData** (`load_data.py`)
   Retrieves and displays:

   * Original greeting
   * Transformed customer object
   * Personalized greeting

---

## 🧰 Features

* **Zero-Infrastructure**: Deploy with one click on WaveAssist—no servers required.
* **Modular Nodes**: Clear separation of ingestion, transformation, and loading logic.
* **Hands-On Learning**: Perfect for getting started with pipelines on WaveAssist.
* **Customizable**: Plug in real data sources, add more nodes, or route outputs anywhere.

---

## 🎯 Getting Started

### 1. One-Click Deploy (Recommended)

<p align="center">
  <a href="https://waveassist.io/templates/starter-template" target="_blank">
    <img src="https://waveassistapps.s3.us-east-1.amazonaws.com/public/Button.png" alt="Deploy on WaveAssist" width="230" />
  </a>
</p>

1. Sign in or sign up at [WaveAssist](https://waveassist.io).
2. Go to **Templates** → **Starter Template**.
3. Click **Deploy**—WaveAssist will import nodes and variables automatically.
4. Run the `IngestData` node, then `TransformData`, and finally `LoadData`.

---

### 2. Local Setup

Clone and run locally if you prefer your own infrastructure:

```bash
git clone https://github.com/WaveAssist/starter-template.git
cd starter-template
pip install waveassist
```

Set your WaveAssist credentials as environment variables:

```bash
export WAVEASSIST_API_KEY="your_api_key_here"
```

Execute each node in order:

```bash
python ingest_data.py
python transform_data.py
python load_data.py
```

---

## ⚙️ Customization

* **Data Sources**: Swap `ingest_data.py` for a connector to your database or API.
* **Transform Logic**: Add or modify enrichments inside `transform_data.py`.
* **Destinations**: Send results to dashboards, data lakes, or third-party services.

---

## 📖 Learn More

* Full docs: [waveassist.io/docs](https://waveassist.io/docs)
* Report issues: [github.com/WaveAssist/starter-template/issues](https://github.com/WaveAssist/starter-template/issues)

---

Built with ❤️ by the WaveAssist team.
