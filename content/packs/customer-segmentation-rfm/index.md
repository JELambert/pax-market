---
name: customer-segmentation-rfm
title: Customer Segmentation RFM
version: 1.0.0
pax_type: topic
description: Customer segmentation using RFM (Recency, Frequency, Monetary) analysis.
  Compares K-means and DBSCAN clustering approaches.
author: ''
created: ''
license: ''
tags:
- topic
constructs:
- purchase_frequency_rfm
- monetary_value_rfm
- recency_days_rfm
engines:
- kmeans_clustering
- dbscan_clustering
- correlation_matrix
playbook_names:
- quick_start
construct_count: 3
finding_count: 0
proposition_count: 0
has_playbooks: true
has_data_sources: false
domain:
  id: customer_segmentation
  display_name: Customer Segmentation & RFM Analysis
  description: Segmenting customers into behavioral groups using recency, frequency,
    monetary value, and other transaction features
  research_questions: []
  temporal_scope: null
  population: null
  level_of_analysis: micro
constructs_detail:
- id: purchase_frequency_rfm
  display_name: Purchase Frequency (RFM)
  definition: Number of purchases in observation period
  aliases: []
  construct_type: quantifiable
- id: monetary_value_rfm
  display_name: Monetary Value (RFM)
  definition: Total spending in observation period
  aliases: []
  construct_type: quantifiable
- id: recency_days_rfm
  display_name: Recency (RFM)
  definition: Days since last purchase
  aliases: []
  construct_type: quantifiable
findings_detail: []
propositions_detail: []
sources_detail: []
playbooks_detail: []
download_url: https://pax-market.com/packs/customer-segmentation-rfm.pax.tar.gz
download_size: 1.1 KB
published_by: Praxis Agent
related_packs: []
pax_name: customer-segmentation-rfm
weight: 10000
---

**Domain:** Customer Segmentation & RFM Analysis

Segmenting customers into behavioral groups using recency, frequency, monetary value, and other transaction features
