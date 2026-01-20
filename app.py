from __future__ import annotations

from flask import Flask, render_template, request
from planner import (
    BusinessProfile,
    BUSINESS_TYPES,
    BREACH_TYPES,
    DATA_TYPES,
    TOOLS,
    assess_risk,
    generate_plan,
)

app = Flask(__name__)


@app.get("/")
def index():
    return render_template(
        "index.html",
        business_types=BUSINESS_TYPES,
        breach_types=BREACH_TYPES,
        data_types=DATA_TYPES,
        tools=TOOLS,
    )


@app.post("/generate")
def generate():
    business_name = request.form.get("business_name", "").strip() or "Unnamed Business"
    business_type = request.form.get("business_type", "Other")
    employee_count = int(request.form.get("employee_count", "1"))

    data_types = request.form.getlist("data_types")
    tools_used = request.form.getlist("tools_used")
    breach_type = request.form.get("breach_type", "credential_compromise")

    profile = BusinessProfile(
        business_name=business_name,
        business_type=business_type,
        employee_count=employee_count,
        data_types=data_types,
        tools_used=tools_used,
        breach_type=breach_type,
        city="Chicago",
    )

    risk = assess_risk(profile)
    plan = generate_plan(profile, risk)

    return render_template("result.html", plan=plan)


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
