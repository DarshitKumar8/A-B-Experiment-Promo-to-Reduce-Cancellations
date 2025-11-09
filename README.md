# ✅ A/B Test to Reduce 7-Day Cancellations

This project demonstrates an end-to-end A/B experiment designed to reduce 7-day cancellations, including experiment design, statistical analysis, production API, containerization, and weekly automation to refresh metrics.

---

## 🎯 Objective
Measure whether the treatment group shows a lower 7-day cancellation rate than control.

**Primary metric**
cancel_rate_7d = (# cancelled in 7 days) / (total users)

**Statistical test**
- Two-sample z-test for proportions  
- α = 0.05  
- Minimum Detectable Effect ≈ 2.8 pp

---

## ✅ Dataset
- Simulated dataset (60,000 users: 30k control, 30k treatment)
- Columns: `user_id`, `group`, `cancelled_7d`, `revenue`

---

## 📊 Key Results
| Group | Cancel Rate |
|--------|-------------|
| Control | 9.90% |
| Treatment | 7.08% |

✅ Absolute reduction: **2.82 pp**  
✅ Relative improvement: **28.5%**

---

## 📈 Business Impact Estimate (based on simulated numbers)
- 1,000,000 MAU  
- ₹150 avg revenue  
- 0.5 orders per user in 7 days  

Observed uplift → fewer cancellations and preserved revenue.

---

## 🧪 Repository Files
| File | Purpose |
|------|---------|
| `AB_Test.ipynb` | Full experiment analysis and plots |
| `server.py` | FastAPI app serving `/` and `/metrics` |
| `metrics.json` | Latest experiment metrics |
| `Dockerfile` | Container config used by Hugging Face |
| `.github/workflows/refresh-metrics.yml` | Weekly notebook run & metrics refresh |

---

## ✅ Live Production API

| Endpoint | Returns |
|----------|---------|
| `/` | `{"status": "ok"}` |
| `/metrics` | `{"cancel_rate_control": x, "cancel_rate_treatment": y}` |

Live Space: `https://darshitkumar-ab-metrics.hf.space`

---

## 🔁 Weekly Automation

![Refresh metrics weekly](https://github.com/DarshitKumar8/A-B-Experiment-Promo-to-Reduce-Cancellations/actions/workflows/refresh-metrics.yml/badge.svg)

Every Monday at 03:00 UTC:
1. Runs the notebook with Papermill  
2. Regenerates `metrics.json`  
3. Uploads it to the Space

---

## ✅ Skills Demonstrated
- A/B testing & experiment design
- Z-test for proportions, confidence intervals
- Pandas, NumPy, Matplotlib, Statsmodels
- FastAPI production endpoints
- Docker containerization
- Papermill for notebook automation
- GitHub Actions for scheduled CI/CD
- Cloud deployment (Hugging Face Spaces)

---

## ✅ Verification
curl https://darshitkumar-ab-metrics.hf.space/
curl https://darshitkumar-ab-metrics.hf.space/metrics
---
