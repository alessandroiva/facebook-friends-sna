# Facebook Friends Social Network Analysis (SNA)

This repository contains a modular implementation of Social Network Analysis (SNA) on Facebook friends data.

## Overview

This project analyzes social networks using various SNA techniques: centrality measures, community detection, PageRank, link prediction, and diffusion models.

## 📁 Repository Structure

- **`src/`**: Modular analysis components
  - `data_loader.py`: Graph loading and subgraph extraction
  - `metrics.py`: Basic metrics, transitivity, betweenness centrality
  - `pagerank.py`: Custom PageRank implementation
  - `communities.py`: Community detection algorithms
  - `link_prediction.py`: Similarity indices (CN, JI, PA, AA, RA)
  - `diffusion.py`: Independent Cascade Model (ICM)
- **`data/`**: Dataset files (`facebook_edges.txt`, description)
- **`notebooks/`**: Original Jupyter Notebook
- **`main.py`**: Main execution script

## 🚀 Usage

1. Install dependencies:
   ```bash
   pip install networkx pandas numpy matplotlib scikit-learn
   ```
2. Run the full analysis pipeline:
   ```bash
   python main.py
   ```

## 📊 Analysis Features

- Calculation of centrality measures (degree, betweenness, closeness)
- Community detection (Bridge Removal, Modularity Optimization, Label Propagation)
- Custom PageRank algorithm implementation
- Link prediction using topological similarity
- Information diffusion modeling (ICM)
