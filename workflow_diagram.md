# AI Resume Analyzer — Workflow Diagram
```mermaid
flowchart TD
    A[Start Application] --> B[Upload PDF or DOCX Resume]
    B --> C{File Type and Size Valid?}
    C -->|No| D[Display Error]
    C -->|Yes| E[Extract Resume Text]
    E --> F[Clean Text]
    F --> G[Identify Skills]
    G --> H[Load Job Role Requirements]
    H --> I[Calculate TF-IDF and Cosine Similarity]
    I --> J[Rank Job Roles]
    J --> K[Display Top 3 Recommendations]
    K --> L[Select Target Job Role]
    L --> M[Identify Missing Skills]
    M --> N[Generate Learning Roadmap]
    N --> O[Display Chart and Results]
    O --> P[Download Analysis Report]
    P --> Q[End]
```
## Workflow Description
1. The user uploads a PDF or DOCX resume.
2. The application validates the file type and size.
3. Resume text is extracted and cleaned.
4. Skills are identified using the skill dictionary.
5. Extracted skills are compared with job-role requirements.
6. The application recommends the top three matching roles.
7. The user selects a target role to view missing skills.
8. A basic learning roadmap is generated.
9. Results are displayed and can be downloaded as a report.