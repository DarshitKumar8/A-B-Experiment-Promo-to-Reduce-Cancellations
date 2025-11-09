# ✅ A/B Test to Reduce 7-Day Cancellations

This project demonstrates a complete **end-to-end A/B experiment**:  
✅ experiment design  
✅ statistical analysis  
✅ business impact estimation  
✅ deployed production API  
✅ automated weekly updates

---

## 🎯 Objective
- Reduce **7-day cancellation rate**
- Ensure no drop in core experience (guardrails: completion rate, refunds, support volume)

---

## 📦 Dataset
- **60,000 users** (30K control, 30K treatment)
- Columns: `user_id`, `group`, `cancelled_7d`, `revenue`
- Simulated for realistic behavior (avg revenue ₹150)

---

## 🧪 Experiment Design
| Parameter | Value |
|----------|-------|
| Randomization unit | User |
| Primary metric | Cancellation rate in 7 days |
| Significance | 0.05 |
| Power | 0.8 |
| MDE | 2.8 pp |
| Test used | Two-sample proportions z-test |

---

## ✅ Sample Size
- Sufficient sample for detecting **2.8 percentage points** difference
- Calculated using `statsmodels.stats.power`

---

## 📊 Key Results
| Metric | Control | Treatment |
|--------|---------|-----------|
| Cancel Rate | 9.90% | 7.08% |
| **Absolute Reduction** | **2.82 pp** |
| **Relative Reduction** | **28.5%** |

✅ Statistically significant improvement  
✅ Passes guardrails

---

## 💰 Business Impact (At 1M MAU)
| Component | Estimate |
|-----------|----------|
| Prevented churn | ~28,200 users |
| Revenue preserved | **₹2.1M / month** |
| Operational savings | ₹1.4M / month (support cost avoided) |
| Rollout recommendation | 10% → 30% → 70% → 100% |

---

## 🛠️ Tech Stack
- **Python** — pandas, numpy, matplotlib, statsmodels
- **Papermill** — automated notebook execution
- **Docker** — containerized app
- **FastAPI / Uvicorn** — production endpoints
- **Hugging Face Spaces** — deployment
- **GitHub Actions** — weekly metrics refresh + uptime checks

---

## 🗂️ Files
- `AB_Test.ipynb` — full experiment & analysis
- `metrics.json` — latest live stats
- `server.py` — HTTP API
- `Dockerfile` — production container

---

## 🚀 Production Signals

![Refresh metrics weekly](https://github.com/DarshitKumar8/A-B-Experiment-Promo-to-Reduce-Cancellations/actions/workflows/refresh-metrics.yml/badge.svg)

- ✅ Dockerized app
- ✅ `/` → health check
- ✅ `/metrics` → JSON API with live results
- ✅ Deployed publicly
- ✅ Notebook runs weekly → regenerates `metrics.json`

### ✅ Live API
| Endpoint | Description |
|----------|-------------|
| **https://darshitkumar-ab-metrics.hf.space/** | Health check → `{"status":"ok"}` |
| **https://darshitkumar-ab-metrics.hf.space/metrics** | Live cancel rates |

---

## ✅ Skills Demonstrated
- Product experimentation & statistics
- A/B testing with z-test + confidence intervals
- Dashboard-style live API
- CI/CD with GitHub Actions
- Containerized deployment (Docker)
- Business impact & rollout strategy
