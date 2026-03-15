from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List


BREACH_TYPES = {
    "credential_compromise": "Credential Compromise (Email / SaaS)",
    "pos_payment_exposure": "POS / Payment Data Exposure",
    "lost_stolen_device": "Lost or Stolen Device",
    "vendor_saas_breach": "Vendor / SaaS Data Breach",
}

DATA_TYPES = {
    "pii_customers": "Customer PII",
    "payment": "Payment Data",
    "employee": "Employee Data",
    "business": "Business Records",
}

TOOLS = {
    "email_o365_gsuite": "Email (Microsoft 365 / Google Workspace)",
    "pos_system": "POS / Payment System",
    "saas_crm": "SaaS Tools",
    "shared_spreadsheets": "Shared Spreadsheets / Drives",
    "personal_devices": "Personal Devices (BYOD)",
    "no_it_support": "No IT Support",
}

BUSINESS_TYPES = [
    "Retail",
    "Restaurant",
    "Clinic",
    "Nonprofit",
    "Professional Services",
    "Other",
]


@dataclass
class BusinessProfile:
    business_name: str
    business_type: str
    employee_count: int
    data_types: List[str]
    tools_used: List[str]
    breach_type: str
    city: str = "Chicago"


def assess_risk(profile: BusinessProfile):
    score = 0
    reasons = []

    if profile.employee_count > 20:
        score += 25
        reasons.append("Larger workforce increases exposure.")
    elif profile.employee_count > 5:
        score += 15
        reasons.append("Moderate workforce size.")

    if "payment" in profile.data_types:
        score += 25
        reasons.append("Handles payment data.")
    if "pii_customers" in profile.data_types:
        score += 15
        reasons.append("Stores customer PII.")
    if "personal_devices" in profile.tools_used:
        score += 15
        reasons.append("Uses personal devices for work.")
    if "no_it_support" in profile.tools_used:
        score += 20
        reasons.append("No dedicated IT support.")

    if score < 35:
        level = "Low"
    elif score < 70:
        level = "Medium"
    else:
        level = "High"

    return {"score": score, "level": level, "reasons": reasons}


def generate_plan(profile: BusinessProfile, risk):
    return {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "business": profile,
        "scenario": BREACH_TYPES.get(profile.breach_type),
        "risk": risk,
        "first_24_hours": [
            "Identify the incident",
            "Contain affected systems",
            "Preserve evidence",
            "Reset passwords",
            "Notify internal contacts",
        ],
        "disclaimer": "This tool provides preparedness guidance only and is not legal advice.",
    }
