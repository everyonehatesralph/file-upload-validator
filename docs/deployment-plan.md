# Deployment Plan – File Upload Validator

## Target Environment
- Platform: Streamlit Community Cloud
- Runtime: Python 3.x
- Source Repository: GitHub
- Entry File: `app.py`

## Deployment Strategy
### Selected Strategy: Development deployment using Streamlit Community Cloud
The application will be deployed first in a development environment to verify that the online version behaves the same as the local version.

## Deployment Steps
1. Push the latest project files to GitHub.
2. Ensure `app.py` and `requirements.txt` are present in the repository.
3. Connect the GitHub repository to Streamlit Community Cloud.
4. Select the correct repository, branch, and file path.
5. Deploy the application using `app.py`.
6. Verify the system works online.

## Verification Steps
- Open the deployed app URL
- Enter valid and invalid file inputs
- Confirm that validation results are correct
- Check that the warning message appears for near-limit files

## Rollback Steps
1. Identify the last stable commit in GitHub.
2. Revert the deployment source to that commit.
3. Redeploy the previous working version.
4. Re-test the deployed application.
5. Notify team members if rollback was required.

## Risks
- Missing dependency in `requirements.txt`
- Wrong main file path
- Source code pushed incompletely
- Online behavior differs from local testing