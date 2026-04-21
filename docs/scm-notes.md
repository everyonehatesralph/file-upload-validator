# SCM Notes – Merge Conflict Resolution

## Conflict Summary
A rebase conflict occurred while synchronizing local changes with the updated `dev` branch.

## Files Involved
- `src/validator.py`
- Python cache files inside `__pycache__`

## Cause
Both branches had changes in the same validator logic, and generated cache files were also tracked in Git.

## Resolution
The conflict in `src/validator.py` was resolved manually by keeping the final warning-threshold logic. The `.pyc` files were removed from version control, and a `.gitignore` file was added to prevent them from being tracked again.

## Lesson Learned
Only source files should be tracked in Git. Auto-generated files like `.pyc` can create unnecessary conflicts and should be ignored.