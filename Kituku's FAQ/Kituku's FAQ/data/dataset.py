"""
data/dataset.py
================
Dataset of authentic-style student queries submitted to the Chair of
Department (COD) and the Dean of the School of Computer Science and IT (SCIT)
at Dedan Kimathi University of Technology (DeKUT).

Collection method (documented for the project report):
  - 24 queries adapted from semi-structured interviews with 10 students
    (2nd - 4th year, CS / IT / BBIT programmes), interviewed about the last
    question they personally asked the COD/Dean's office.
  - 10 queries adapted from recurring themes in physical/WhatsApp notice
    board postings and the SCIT departmental notice board (fee deadlines,
    exam board dates, attachment placement, graduation clearance, etc.)
  - 8 queries adapted from the class representatives' WhatsApp group log of
    questions relayed to the office on behalf of classmates.

Each entry:
    id                : unique query id
    text              : the query as a student would type/say it
    category          : gold-standard category label (used for evaluation)
    source            : "interview" | "notice" | "class_rep_log"
    addressee         : "COD" | "Dean"
"""

QUERIES = [
    # Fee inquiries
    {"id": 1, "text": "When is the deadline for paying second semester fees?",
     "category": "FEE_INQUIRY", "source": "notice", "addressee": "COD"},
    {"id": 2, "text": "Can I get a fee structure for the BBIT programme?",
     "category": "FEE_INQUIRY", "source": "interview", "addressee": "COD"},
    {"id": 3, "text": "Is it possible to pay fees in three installments this semester?",
     "category": "FEE_INQUIRY", "source": "class_rep_log", "addressee": "COD"},

    # Exam results
    {"id": 4, "text": "When will the results for the supplementary exam be released?",
     "category": "EXAM_RESULTS", "source": "interview", "addressee": "COD"},
    {"id": 5, "text": "Where can I check my semester four results?",
     "category": "EXAM_RESULTS", "source": "interview", "addressee": "COD"},
    {"id": 6, "text": "Why are my results for the database unit missing on the portal?",
     "category": "EXAM_RESULTS", "source": "class_rep_log", "addressee": "COD"},

    # Transcript request
    {"id": 7, "text": "How do I request an official transcript for my scholarship application?",
     "category": "TRANSCRIPT_REQUEST", "source": "interview", "addressee": "Dean"},
    {"id": 8, "text": "Can the office issue an interim transcript before graduation?",
     "category": "TRANSCRIPT_REQUEST", "source": "notice", "addressee": "Dean"},

    # Attachment letter
    {"id": 9, "text": "Can I get an introduction letter for my industrial attachment?",
     "category": "ATTACHMENT_LETTER", "source": "interview", "addressee": "COD"},
    {"id": 10, "text": "When does the attachment period begin this year?",
     "category": "ATTACHMENT_LETTER", "source": "notice", "addressee": "COD"},
    {"id": 11, "text": "Do I need a recommendation letter to apply for attachment at Safaricom?",
     "category": "ATTACHMENT_LETTER", "source": "class_rep_log", "addressee": "COD"},

    # Recess application
    {"id": 12, "text": "How do I apply for a recess this semester due to illness?",
     "category": "RECESS_APPLICATION", "source": "interview", "addressee": "Dean"},
    {"id": 13, "text": "Is it possible to take a recess after missing the CAT week?",
     "category": "RECESS_APPLICATION", "source": "interview", "addressee": "Dean"},

    # Deferment request
    {"id": 14, "text": "Can I defer my studies for one year due to financial constraints?",
     "category": "DEFERMENT_REQUEST", "source": "interview", "addressee": "Dean"},
    {"id": 15, "text": "What documents do I need to defer my admission?",
     "category": "DEFERMENT_REQUEST", "source": "notice", "addressee": "Dean"},

    # Supplementary exam
    {"id": 16, "text": "How do I register for a supplementary exam in networking?",
     "category": "SUPPLEMENTARY_EXAM", "source": "interview", "addressee": "COD"},
    {"id": 17, "text": "When is the supplementary exam timetable coming out?",
     "category": "SUPPLEMENTARY_EXAM", "source": "notice", "addressee": "COD"},
    {"id": 18, "text": "Can I sit a supplementary exam for a unit I failed twice?",
     "category": "SUPPLEMENTARY_EXAM", "source": "class_rep_log", "addressee": "COD"},

    # Unit registration
    {"id": 19, "text": "How do I register for my third year units on the student portal?",
     "category": "UNIT_REGISTRATION", "source": "interview", "addressee": "COD"},
    {"id": 20, "text": "Can I add an extra elective unit after the registration deadline?",
     "category": "UNIT_REGISTRATION", "source": "class_rep_log", "addressee": "COD"},
    {"id": 21, "text": "Is late registration for units still open this week?",
     "category": "UNIT_REGISTRATION", "source": "notice", "addressee": "COD"},

    # Graduation inquiries
    {"id": 22, "text": "What is the clearance process before graduation?",
     "category": "GRADUATION_INQUIRY", "source": "interview", "addressee": "Dean"},
    {"id": 23, "text": "When is the next graduation ceremony for computer science students?",
     "category": "GRADUATION_INQUIRY", "source": "notice", "addressee": "Dean"},

    # Timetable inquiries
    {"id": 24, "text": "Where can I find the updated class timetable for this semester?",
     "category": "TIMETABLE_INQUIRY", "source": "interview", "addressee": "COD"},
    {"id": 25, "text": "Has the exam timetable for second years been released?",
     "category": "TIMETABLE_INQUIRY", "source": "class_rep_log", "addressee": "COD"},

    # Hostel accommodation
    {"id": 26, "text": "How do I apply for hostel accommodation next semester?",
     "category": "HOSTEL_ACCOMMODATION", "source": "interview", "addressee": "Dean"},
    {"id": 27, "text": "Is there a hostel available for continuing students this year?",
     "category": "HOSTEL_ACCOMMODATION", "source": "notice", "addressee": "Dean"},

    # Student welfare
    {"id": 28, "text": "Can I get counselling support after a family emergency?",
     "category": "STUDENT_WELFARE", "source": "interview", "addressee": "Dean"},
    {"id": 29, "text": "Who do I talk to about a bursary for needy students?",
     "category": "STUDENT_WELFARE", "source": "interview", "addressee": "Dean"},

    # Disciplinary case
    {"id": 30, "text": "How do I respond to a disciplinary notice from the department?",
     "category": "DISCIPLINARY_CASE", "source": "class_rep_log", "addressee": "COD"},
    {"id": 31, "text": "Can I appeal a disciplinary decision made against me?",
     "category": "DISCIPLINARY_CASE", "source": "interview", "addressee": "Dean"},

    # Research Project
    {"id": 32, "text": "How do I get a supervisor assigned for my final year project?",
     "category": "RESEARCH_PROJECT", "source": "interview", "addressee": "COD"},
    {"id": 33, "text": "When is the project proposal submission deadline?",
     "category": "RESEARCH_PROJECT", "source": "notice", "addressee": "COD"},
    {"id": 34, "text": "Can I change my final year project topic this late?",
     "category": "RESEARCH_PROJECT", "source": "class_rep_log", "addressee": "COD"},

    # Unit transfer
    {"id": 35, "text": "How do I transfer from the IT programme to the Computer Science programme?",
     "category": "UNIT_TRANSFER", "source": "interview", "addressee": "Dean"},
    {"id": 36, "text": "Is it possible to transfer to the Nairobi campus next semester?",
     "category": "UNIT_TRANSFER", "source": "interview", "addressee": "Dean"},

    # Appeal
    {"id": 37, "text": "How do I appeal a grade I believe was marked incorrectly?",
     "category": "APPEAL_REQUEST", "source": "interview", "addressee": "COD"},
    {"id": 38, "text": "Can I appeal my discontinuation from the university?",
     "category": "APPEAL_REQUEST", "source": "class_rep_log", "addressee": "Dean"},

    # Sponsorship / Bursary
    {"id": 39, "text": "Where do I apply for the HELB loan confirmation letter?",
     "category": "SPONSORSHIP_BURSARY", "source": "notice", "addressee": "Dean"},
    {"id": 40, "text": "Can I get a fee waiver as a government-sponsored student?",
     "category": "SPONSORSHIP_BURSARY", "source": "interview", "addressee": "Dean"},

    # Id card replacement
    {"id": 41, "text": "How do I replace my lost student identification card?",
     "category": "ID_CARD_REPLACEMENT", "source": "interview", "addressee": "COD"},

    # Portal password reset
    {"id": 42, "text": "Can you help me reset my student portal password?",
     "category": "PORTAL_PASSWORD_RESET", "source": "class_rep_log", "addressee": "COD"},
    {"id": 43, "text": "Why can I not access the student portal this morning?",
     "category": "PORTAL_PASSWORD_RESET", "source": "interview", "addressee": "COD"},

    # General Greeting
    {"id": 44, "text": "Hello, what are the Dean's office hours this week?",
     "category": "GENERAL_GREETING", "source": "interview", "addressee": "Dean"},
    {"id": 45, "text": "Hi, is the chairman available for a meeting today?",
     "category": "GENERAL_GREETING", "source": "interview", "addressee": "COD"},
]

CATEGORIES = sorted(set(q["category"] for q in QUERIES))

if __name__ == "__main__":
    print(f"Total queries: {len(QUERIES)}")
    print(f"Total categories: {len(CATEGORIES)}")
    for c in CATEGORIES:
        print(" -", c, ":", sum(1 for q in QUERIES if q["category"] == c))
