# Technical Debt – File Upload Validator

## Overview
This document lists technical debt items identified in the File Upload Validator project. These items represent areas where the code or project structure can be improved for maintainability, clarity, and long-term quality.

## Technical Debt Items

### TD-01: Validation logic is concentrated in one function
The `validate_file()` function handles too many responsibilities in one block, making it harder to maintain and extend.

### TD-02: File validation rules are hard-coded
Allowed and blocked extensions are defined directly in the function instead of being centralized as constants or configuration values.

### TD-03: Warning threshold logic is mixed with core validation logic
The size warning feature is embedded directly in the same function, reducing readability.

### TD-04: Python cache files were previously tracked in Git
Generated files like `.pyc` created unnecessary noise and merge conflicts.

### TD-05: Validation messages are duplicated as raw strings
Messages such as "Blocked file type" and "Upload allowed" are directly embedded in the code, making future updates less consistent.

## Selected Debt to Fix
**TD-01: Validation logic is concentrated in one function**

## Reason for Selection
This item has the highest impact on maintainability. Refactoring it into smaller helper functions will make the validator easier to understand, test, and improve in future iterations.