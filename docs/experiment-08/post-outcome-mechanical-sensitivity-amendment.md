# Experiment 08 — Post-Outcome Mechanical Sensitivity Amendment

## Status

This document defines a post-outcome diagnostic sensitivity analysis for Experiment 08.

It does **not** revise, replace, or rescue the original frozen mechanical-validity gate.

The original mechanical result remains failed:

- `ra14_mechanical_pass = false`
- `magnitude_gate_pass = false`
- raster magnitude P95 relative error = 21.33%

The purpose of this amendment is only to diagnose why the frozen raster magnitude gate failed.

No predictive analysis is part of this amendment.

---

## Diagnostic Question

Why did the frozen raster magnitude-validity gate fail?

The analysis will distinguish among three possible mechanisms:

1. denominator conditioning at low second-harmonic magnitude;
2. support/sampling instability;
3. genuine raster/interpolation instability.

---

## 1. Denominator-Conditioning Hypothesis

Let the original second-harmonic magnitude be

\[
R_2
\]

and the corresponding magnitude after raster rotation be

\[
R_2'.
\]

The original relative magnitude error is

\[
E_{\mathrm{rel}}
=
\frac{|R_2'-R_2|}{R_2}.
\]

Under a bounded raster perturbation, relative error may scale approximately as

\[
E_{\mathrm{rel}}
\sim
\frac{1}{R_2}.
\]

Therefore the prespecified diagnostic prediction is

\[
R_2 \uparrow
\Longrightarrow
E_{\mathrm{rel}} \downarrow.
\]

Large relative errors concentrated at small \(R_2\), while absolute errors remain small, will be interpreted as evidence of denominator conditioning rather than global mechanical instability.

---

## 2. Small-Absolute-Error Hypothesis

Define absolute magnitude error as

\[
E_{\mathrm{abs}}
=
|R_2'-R_2|.
\]

The analysis will test whether observations with large relative error, particularly at low \(R_2\), nevertheless show small absolute magnitude perturbations.

---

## 3. Support/Sampling Hypothesis

Let shell mass or shell support be denoted by

\[
m.
\]

The analysis will test whether low shell support is associated with greater raster error independently of \(R_2\).

The diagnostic question is whether

\[
m \downarrow
\Longrightarrow
E_{\mathrm{rel}} \uparrow
\]

and/or

\[
m \downarrow
\Longrightarrow
E_{\mathrm{abs}} \uparrow.
\]

---

## Error Measures

Three measures are frozen for the sensitivity analysis.

### Absolute error

\[
E_{\mathrm{abs}}
=
|R_2'-R_2|.
\]

### Relative error

\[
E_{\mathrm{rel}}
=
\frac{|R_2'-R_2|}{R_2}.
\]

### Symmetric relative diagnostic

\[
E_{\mathrm{sym}}
=
\frac{2|R_2'-R_2|}
{R_2'+R_2}.
\]

`E_sym` is a sensitivity diagnostic only.

It does **not** replace the original frozen relative-error gate and must not be used to retroactively change the original mechanical PASS/FAIL decision.

---

## Population

Use the full available Experiment 08 raster mechanical-validation population.

The following are prohibited:

- filtering observations on the basis of error magnitude;
- excluding low-\(R_2\) cases;
- removing inconvenient raster failures;
- modifying RA14;
- changing the frozen mechanical threshold;
- conducting classifier or predictive analyses as part of this sensitivity analysis.

All available mechanical-validation observations remain in scope.

---

## Prespecified \(R_2\) Strata

The original \(R_2\) magnitude will be stratified using the following fixed bins:

- `[0, 0.05)`
- `[0.05, 0.10)`
- `[0.10, 0.20)`
- `[0.20, 0.40)`
- `[0.40, 0.60)`
- `[0.60, 0.80)`
- `[0.80, 1.00]`

These strata are diagnostic and must not be used to exclude observations from the full-population summary.

For every stratum report:

- number of shell-rotation observations;
- median `E_abs`;
- P95 `E_abs`;
- median `E_rel`;
- P95 `E_rel`;
- median `E_sym`;
- P95 `E_sym`;
- median shell mass/support;
- proportion exceeding the original 15% relative-error threshold.

---

## Zero-\(R_2\) Domain Rule

The full mechanical-validation population remains in scope, including observations with \(R_2=0\).

The diagnostic measures are defined as follows:

\[
E_{\mathrm{abs}}
=
|R_2'-R_2|
\]

for all observations.

\[
E_{\mathrm{sym}}
=
\frac{2|R_2'-R_2|}
{R_2'+R_2}
\]

is used when \(R_2'+R_2>0\). If \(R_2'=R_2=0\), define

\[
E_{\mathrm{sym}}=0.
\]

The original relative error

\[
E_{\mathrm{rel}}
=
\frac{|R_2'-R_2|}{R_2}
\]

is mathematically defined only where \(R_2>0\).

For observations with \(R_2=0\):

- retain the observation in the full-population count;
- report `E_abs`;
- report `E_sym`;
- record `E_rel` as undefined / NA;
- do not replace the denominator with an epsilon;
- do not delete the observation.

All summaries involving `E_rel` must report both:

- the total number of observations in the relevant population/stratum; and
- the number of observations for which `E_rel` is defined.

Spearman analyses involving `E_rel` use only observations where `E_rel` is mathematically defined. This is a domain restriction of the ratio, not outcome-based filtering.

---

## Association Analyses

Two descriptive Spearman associations are prespecified:

\[
\rho_s(R_2,E_{\mathrm{rel}})
\]

and

\[
\rho_s(m,E_{\mathrm{rel}}).
\]

Spearman associations are computed on the untransformed values. This preserves zero-valued observations and avoids arbitrary logarithmic zero-handling rules.

---

## Descriptive Model

The following descriptive model is prespecified:

\[
\log(1+E_{\mathrm{rel}})
=
\beta_0
+
\beta_1 \log(1+R_2)
+
\beta_2 \log(1+m)
+
\gamma_\phi
+
\epsilon,
\]

where rotation angle \(\phi\) is treated categorically.

This model is descriptive only.

It is not intended to establish causal effects.

---

## Interpretation Firewall

Interpretation is frozen as follows.

### Denominator conditioning

A strong negative dependence of relative error on \(R_2\), together with small absolute error at low \(R_2\), supports denominator conditioning.

### Support/sampling instability

An independent association between shell support and raster error after accounting for \(R_2\) supports a support/sampling contribution.

### Genuine raster instability

Substantial absolute error that persists at moderate or high \(R_2\) supports genuine raster/interpolation instability rather than a denominator-only explanation.

### Rotation-angle dependence

Strong rotation-angle effects support interpolation/operator dependence.

---

## Confirmatory Status

The original mechanical gate remains failed.

This post-outcome sensitivity analysis is explanatory and diagnostic only.

It does not retroactively convert the original mechanical result from FAIL to PASS.

Any Experiment 08 predictive analyses that crossed the predictive boundary despite the failed frozen mechanical gate must retain their appropriately qualified post-outcome/exploratory interpretation.

---

## Execution Boundary

At the time this amendment is committed:

- no sensitivity-analysis outcome may have been computed;
- no diagnostic result may have been inspected;
- no frozen mechanical evidence may have been altered;
- no predictive result may be recomputed as part of this amendment.

Implementation and execution must occur only after this amendment is committed.
