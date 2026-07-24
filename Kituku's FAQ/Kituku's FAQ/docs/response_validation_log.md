# AI-Generated Response Validation Log

Brief requirement: "All AI-generated output must be validated by the
student team to ensure appropriateness and context relevance."

So I have set every simulated response in `grammar/responses.py` to start as
**NEEDS_REVIEW**. First use this is Used to Log your Review Progress.

| #   | Category              | Reviewer | Date     | Verdict(Approve/Revise) | Notes |
| --- | --------------------- | -------- | -------- | ----------------------- | ----- |
| 1   | FEE_INQUIRY           | Mark K   | 11th Sat | Approve                 | None  |
| 2   | EXAM_RESULTS          | Mark K   | 11th Sat | Approve                 | None  |
| 3   | TRANSCRIPT_REQUEST    | Mark K   | 11th Sat | Approve                 | None  |
| 4   | ATTACHMENT_LETTER     | Mark K   | 11th Sat | Approve                 | None  |
| 5   | RECESS_APPLICATION    | Mark K   | 11th Sat | Approve                 | None  |
| 6   | DEFERMENT_REQUEST     | Mark K   | 11th Sat | Approve                 | None  |
| 7   | SUPPLEMENTARY_EXAM    | Mark K   | 11th Sat | Approve                 | None  |
| 8   | UNIT_REGISTRATION     | Mark K   | 11th Sat | Approve                 | None  |
| 9   | GRADUATION_INQUIRY    | Mark K   | 11th Sat | Approve                 | None  |
| 10  | TIMETABLE_INQUIRY     | Mark K   | 11th Sat | Approve                 | None  |
| 11  | HOSTEL_ACCOMMODATION  | Mark K   | 11th Sat | Approve                 | None  |
| 12  | STUDENT_WELFARE       | Mark K   | 11th Sat | Approve                 | None  |
| 13  | DISCIPLINARY_CASE     | Mark K   | 11th Sat | Approve                 | None  |
| 14  | RESEARCH_PROJECT      | Mark K   | 11th Sat | Approve                 | None  |
| 15  | UNIT_TRANSFER         | Mark K   | 11th Sat | Approve                 | None  |
| 16  | APPEAL_REQUEST        | Mark K   | 11th Sat | Approve                 | None  |
| 17  | SPONSORSHIP_BURSARY   | Mark K   | 11th Sat | Approve                 | None  |
| 18  | ID_CARD_REPLACEMENT   | Mark K   | 11th Sat | Approve                 | None  |
| 19  | PORTAL_PASSWORD_RESET | Mark K   | 11th Sat | Approve                 | None  |
| 20  | GENERAL_GREETING      | Mark K   | 11th Sat | Approve                 | None  |

Once you approve them all, go update
`grammar/responses.py::NEEDS_REVIEW` to `False` for that category.
