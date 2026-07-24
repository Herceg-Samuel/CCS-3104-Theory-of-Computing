"""
grammar/responses.py

Simulated Dean / COD office responses, one per query category. These are
placeholder responses written in a realistic administrative tone,
as required by "Simulate office responses" task. They are
templated with {addressee} so the same bank works whether the query was
directed at the Dean or the COD.

"""

RESPONSES = {
    "FEE_INQUIRY": (
        "Thank you for reaching out to the {addressee}'s office. Fee "
        "structures and payment deadlines are published on the university "
        "student portal under 'Finance'. Installment payment plans require "
        "a written request to the Finance Office copied to the {addressee}. "
        "For your specific balance, please visit the office during working "
        "hours (Mon-Fri, 9:00am-4:00pm) with your admission number."
    ),
    "EXAM_RESULTS": (
        "Examination results are released via the student portal after "
        "moderation by the Examinations Board, typically within 3 weeks of "
        "the exam period ending. If a result is missing or you suspect an "
        "error, please submit a written query to the {addressee}'s office "
        "with the unit code and your registration number for verification."
    ),
    "TRANSCRIPT_REQUEST": (
        "Official transcripts are processed by the Academic Registrar's "
        "office upon written application and payment of the transcript fee. "
        "Interim transcripts before graduation may be issued by the "
        "{addressee} for scholarship or attachment purposes -- please "
        "submit a formal request stating the purpose."
    ),
    "ATTACHMENT_LETTER": (
        "Introduction letters for industrial attachment are issued by the "
        "{addressee}'s office once you have identified a host organisation "
        "and completed the attachment briefing. Bring your student ID and "
        "the host organisation's name and address to the office."
    ),
    "RECESS_APPLICATION": (
        "Applications for recess must be made in writing to the {addressee}, "
        "accompanied by supporting documents (e.g. a medical certificate for "
        "health-related recess). Applications should be submitted as soon as "
        "possible and, where feasible, before the end of the semester in "
        "question."
    ),
    "DEFERMENT_REQUEST": (
        "Deferment of studies requires a written application to the "
        "{addressee}, stating the reason and proposed return date, along "
        "with any supporting documentation (financial, medical, etc.). "
        "Approved deferments are recorded by the Registrar and will affect "
        "your expected completion date."
    ),
    "SUPPLEMENTARY_EXAM": (
        "Supplementary examinations are available to students who fail a "
        "unit within the allowed number of attempts, subject to Senate "
        "regulations. Registration for supplementary exams opens after "
        "results are released watch the notice board and student portal "
        "for the timetable, or confirm directly with the {addressee}."
    ),
    "UNIT_REGISTRATION": (
        "Unit registration is done via the student portal within the dates "
        "set by the Academic Registrar. Late registration or unit changes "
        "after the deadline require written approval from the {addressee}, "
        "typically with a late-registration fee."
    ),
    "GRADUATION_INQUIRY": (
        "Graduation clearance requires fee clearance, library clearance, "
        "hostel clearance (if applicable) and departmental clearance signed "
        "by the {addressee}. Graduation ceremony dates are announced by the "
        "Registrar (Academic) and posted on the university website."
    ),
    "TIMETABLE_INQUIRY": (
        "Class and exam timetables are published on the student portal and "
        "on the departmental notice board. If your timetable has a clash or "
        "you cannot locate it, please notify the {addressee}'s office with "
        "your year of study and programme."
    ),
    "HOSTEL_ACCOMMODATION": (
        "Hostel accommodation applications are handled by the Dean of "
        "Students' office, with allocation priority typically given to "
        "first-year and continuing needy students. Please check the housing "
        "portal for the current application window."
    ),
    "STUDENT_WELFARE": (
        "The {addressee}'s office works closely with the Dean of Students "
        "and university counselling unit to support students facing "
        "personal or family difficulties. Please visit the office in person "
        "or request a confidential appointment so we can direct you to the "
        "right support."
    ),
    "DISCIPLINARY_CASE": (
        "If you have received a disciplinary notice, you are required to "
        "respond in writing within the timeframe stated in the notice. You "
        "have the right to be heard by the disciplinary committee, and may "
        "appeal a decision through the {addressee} in line with the "
        "university's student disciplinary procedure."
    ),
    "RESEARCH_PROJECT": (
        "Final year project supervisors are allocated by the department "
        "based on your area of interest -- please submit your top three "
        "topic preferences to the {addressee}'s office. Proposal submission "
        "deadlines are announced at the start of the project unit; topic "
        "changes after supervisor allocation require the supervisor's and "
        "{addressee}'s written approval."
    ),
    "UNIT_TRANSFER": (
        "Programme or campus transfer requests are considered on a "
        "case-by-case basis, subject to available capacity and meeting the "
        "minimum entry requirements of the destination programme/campus. "
        "Please submit a written application to the {addressee} stating "
        "your reasons for the transfer."
    ),
    "APPEAL_REQUEST": (
        "Academic appeals (grades, discontinuation, etc.) must be submitted "
        "in writing to the {addressee} within 14 days of the decision being "
        "communicated, together with any supporting evidence. Appeals are "
        "reviewed by the relevant academic board."
    ),
    "SPONSORSHIP_BURSARY": (
        "HELB loan confirmation letters and bursary/sponsorship "
        "verification letters are issued by the {addressee}'s office on "
        "request. Please bring your admission letter and national ID/HELB "
        "reference number."
    ),
    "ID_CARD_REPLACEMENT": (
        "Lost student ID cards should first be reported to campus security, "
        "then a replacement can be processed at the Registrar's office on "
        "payment of the replacement fee. The {addressee}'s office can issue "
        "a temporary access note in the meantime if needed."
    ),
    "PORTAL_PASSWORD_RESET": (
        "Student portal password resets are handled by the ICT Helpdesk. "
        "If the self-service reset option does not work, please visit the "
        "ICT office with your student ID, or notify the {addressee}'s "
        "office and we will escalate it on your behalf."
    ),
    "GENERAL_GREETING": (
        "Hello! The {addressee}'s office is open Monday-Friday, "
        "9:00am-4:00pm. For a specific meeting, please book a slot with the "
        "office administrator or state your query and we will guide you."
    ),
    "UNRECOGNISED": (
        "I'm not yet able to confidently classify that query. Could you "
        "rephrase it, or would you like it forwarded directly to the "
        "{addressee}'s office for a personal response?"
    ),
}

NEEDS_REVIEW = {category: False for category in RESPONSES}


def get_response(category: str, addressee: str = "Dean/COD") -> str:
    template = RESPONSES.get(category, RESPONSES["UNRECOGNISED"])
    return template.format(addressee=addressee)
