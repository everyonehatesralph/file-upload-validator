# CI/CD Diagram – File Upload Validator

## Overview
This document describes the CI/CD pipeline used for the File Upload Validator project.

## Trigger
- Push to `main`

## Pipeline Stages
1. **Checkout**
   - GitHub Actions checks out the latest repository code.

2. **Setup**
   - Python is installed in the runner environment.
   - Dependencies are installed from `requirements.txt`.

3. **Test**
   - Unit tests are executed using `pytest`.

4. **Build Check**
   - Python files are compiled to verify syntax and build readiness.

5. **Deploy**
   - Streamlit Community Cloud automatically redeploys the application when changes are pushed to the connected GitHub repository.

6. **Smoke Test**
   - GitHub Actions sends a request to the deployed app URL.
   - The pipeline passes if the deployed system returns HTTP 200.

## Diagram

```mermaid
flowchart TD
    A[Push to main] --> B[Checkout repository]
    B --> C[Set up Python]
    C --> D[Install dependencies]
    D --> E[Run unit tests]
    E --> F[Build check]
    F --> G[Streamlit Cloud auto-deploy]
    G --> H[Smoke test deployed app]
    H --> I[Pipeline success]