# CI/CD Diagram – File Upload Validator

## Overview
This document describes the automated CI/CD pipeline for the File Upload Validator project.

## Trigger
- Push to `main`

## Pipeline Stages
1. **Checkout**
   - GitHub Actions checks out the latest repository code.

2. **Setup**
   - Python environment is prepared.
   - Dependencies are installed from `requirements.txt`.

3. **Test**
   - Unit tests are executed using `pytest`.

4. **Build Check**
   - Python files are compiled to verify syntax and basic build readiness.

5. **Deploy**
   - Streamlit Community Cloud automatically redeploys the application after a push to the connected GitHub repository.

6. **Smoke Test**
   - GitHub Actions sends a request to the deployed application URL.
   - The pipeline passes if the deployed app returns HTTP 200.

## Mermaid Diagram

```mermaid
flowchart TD
    A[Push to main] --> B[GitHub Actions: Checkout]
    B --> C[Set up Python]
    C --> D[Install dependencies]
    D --> E[Run pytest]
    E --> F[Build check]
    F --> G[Streamlit Cloud auto-deploy]
    G --> H[Smoke test deployed URL]
    H --> I[Pipeline success]