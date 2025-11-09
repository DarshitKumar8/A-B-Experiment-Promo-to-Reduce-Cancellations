# A/B Test to Reduce 7-Day Cancellations

## Project Overview
This project demonstrates an end-to-end A/B test designed to reduce 7-day cancellations in a product/service context. It covers experiment design, statistical analysis, visualization, and business impact estimation using a simulated dataset.

## Objective
- Reduce 7-day cancellation rate per user.
- Monitor guardrail metrics such as completion rate and refund rate to ensure no unintended negative effects.

## Dataset
- Simulated dataset with 60,000 users (30,000 control, 30,000 treatment).
- Each user has `user_id`, `group` (control/treatment), `cancelled_7d` (0/1), and `revenue` (₹150 avg).

## Methodology

### Experiment Design
- Unit of randomization: User
- Treatment vs Control: Random assignment
- Primary metric: 7-day cancellation rate per user  
  `cancel_rate_7d = (# users who cancel within 7 days) / (# users in cohort)`
- Null hypothesis: `H0: μ_treatment = μ_control`
- Alternative hypothesis: `H1: μ_treatment ≠ μ_control`
- Statistical test: Two-sample proportions z-test
- Significance level (α): 0.05
- Power: 0.8
- Minimum Detectable Effect (MDE): 2.8 pp absolute

### Sample Size Calculation
- Calculated using `statsmodels` to ensure sufficient power for detecting the MDE.

### Analysis
- Sanity/randomization checks for balanced groups.
- Z-test for proportions to compare control vs treatment cancellation rates.
- Calculation of absolute and relative uplift.
- 95% confidence intervals for cancel rates and difference.
- Visualization of results with error bars.

### Business Impact
- MAU = 1,000,000
- Average order value = ₹150
- Orders per user in 7 days = 0.5
- Operations cost per contact = ₹50
- Estimated prevented cancellations, revenue preserved, and operational savings calculated based on observed uplift.
- Phased rollout recommendation: 10% → 30% → 70% → 100%, with guardrails monitored at each stage.

## Files
- `AB_Test.ipynb` — Jupyter notebook with full analysis
- `Control_vs_Treatment.png` — Visualization of control vs treatment cancellation rates

## Key Results
- Absolute reduction in cancellations: 2.82 pp
- Relative reduction: 28.5%
- Estimated revenue preserved: ₹2.1M/month
- Recommended phased rollout with guardrails.

## Skills Demonstrated
- A/B testing and experiment design
- SQL and Python (Pandas, NumPy, Matplotlib)
- Statistical analysis (z-test, confidence intervals)
- Business impact calculation and product metric interpretation

# A/B Experiment – Promo to Reduce Cancellations

![Refresh metrics weekly](https://github.com/DarshitKumar8/A-B-Experiment-Promo-to-Reduce-Cancellations/actions/workflows/refresh-metrics.yml/badge.svg)

**Production signals**
- Containerized (Dockerfile), health `/` and metrics `/metrics`
- Public deployment on Hugging Face Space
- Weekly notebook run via GitHub Actions → updates `metrics.json`
- Logs visible in Space; basic monitoring via uptime check (below)

**Live API**
- Health: https://darshitkumar-ab-metrics.hf.space/
- Metrics: https://darshitkumar-ab-metrics.hf.space/metrics
