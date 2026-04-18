# QA Plan – File Upload Validator

## Project Overview
The File Upload Validator checks whether an uploaded file is valid based on filename, file type, and file size rules.

## Test Levels
- **Unit Testing**: Tests individual validation rules such as allowed file types, blocked file types, empty filename, invalid format, and file size limit.
- **Integration Testing**: Confirms that multiple validation rules work together correctly in the upload validation flow.
- **System Testing**: Verifies that the overall validator behaves according to the project requirements.

## Entry Criteria
- Validation logic is implemented in the source code.
- Testing framework is installed and working.
- Test cases are prepared.

## Exit Criteria
- All planned unit tests are executed.
- Failed tests are investigated.
- High-severity bugs are fixed.
- Final results are documented.

## Severity Levels
- **S1 – Critical**: Major failure or security issue that prevents safe use of the system.
- **S2 – High**: Important functionality fails and needs immediate correction.
- **S3 – Medium**: A feature works incorrectly but has a workaround.
- **S4 – Low**: Minor issue with limited impact on functionality.