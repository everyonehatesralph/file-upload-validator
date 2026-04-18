# Product Backlog – File Upload Validator

## Project Overview
The File Upload Validator is a simple system that checks uploaded files based on rules such as allowed file type, blocked file type, file size limit, and filename validity. The goal is to help users safely upload files while preventing invalid or risky uploads.

---

## User Stories

### US-01
**As a user, I want to upload a valid file so that my file can be accepted by the system.**  
**Priority:** High  
**Story Points:** 3  

**Acceptance Criteria:**
- User can submit a file with a valid name
- File must have an allowed extension
- File must not exceed the size limit
- System displays “Upload allowed” for valid files

---

### US-02
**As a user, I want the system to reject blocked file types so that unsafe files cannot be uploaded.**  
**Priority:** High  
**Story Points:** 3  

**Acceptance Criteria:**
- System checks file extension before upload approval
- Files such as `.exe`, `.bat`, `.js`, and `.sh` are rejected
- System displays “Blocked file type” when blocked files are detected

---

### US-03
**As a user, I want the system to reject files that exceed the maximum size so that storage and security rules are followed.**  
**Priority:** High  
**Story Points:** 2  

**Acceptance Criteria:**
- System checks the file size before approval
- Files larger than the maximum allowed size are rejected
- System displays “File too large” for oversized files

---

### US-04
**As a user, I want the system to reject files with empty filenames so that invalid uploads are prevented.**  
**Priority:** High  
**Story Points:** 1  

**Acceptance Criteria:**
- System checks whether the filename is empty
- Blank or whitespace-only filenames are rejected
- System displays “Filename is empty” when detected

---

### US-05
**As a user, I want the system to reject files without a valid extension so that upload format rules are enforced.**  
**Priority:** Medium  
**Story Points:** 2  

**Acceptance Criteria:**
- System checks if the filename contains a valid extension
- Files without a dot extension are rejected
- System displays “Invalid file format” when no extension exists

---

### US-06
**As a user, I want the system to reject unsupported file types so that only approved file formats are accepted.**  
**Priority:** High  
**Story Points:** 3  

**Acceptance Criteria:**
- System checks whether the file extension is included in allowed file types
- Unsupported file types are rejected
- System displays “File type not allowed” when unsupported files are uploaded

---

### US-07
**As a developer, I want unit tests for the file validation rules so that the logic can be verified automatically.**  
**Priority:** High  
**Story Points:** 5  

**Acceptance Criteria:**
- At least 5 unit tests are created
- Tests cover valid and invalid file scenarios
- Tests can be executed using pytest
- Test results clearly show pass or fail status

---

### US-08
**As a QA lead, I want a QA plan document so that testing activities are clearly defined.**  
**Priority:** Medium  
**Story Points:** 2  

**Acceptance Criteria:**
- QA plan document is created in `/docs`
- Document includes test levels
- Document includes entry and exit criteria
- Document includes severity levels

---

### US-09
**As a QA lead, I want a defect log so that bugs can be documented and tracked properly.**  
**Priority:** Medium  
**Story Points:** 2  

**Acceptance Criteria:**
- Defect log is created in `/docs`
- Each defect entry contains bug ID, description, severity, and status
- Defect status can be updated from Open to Closed

---

### US-10
**As a team member, I want the project stored in GitHub so that the team can track changes and collaborate effectively.**  
**Priority:** High  
**Story Points:** 3  

**Acceptance Criteria:**
- Git repository is initialized
- Project is pushed to GitHub
- Team members can view the project files in the repository
- Commits reflect meaningful project progress

### US-11
**As a user, I want a warning when my file is near the size limit so that I can adjust before uploading.**  
Priority: Medium  
Story Points: 2  

Acceptance Criteria:
- System detects files above 80% of max size
- Displays warning message
- Does not block upload