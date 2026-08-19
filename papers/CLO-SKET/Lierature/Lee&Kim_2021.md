# Lee & Kim (2021) — Feature-based Fashion Flat Sketch Design Using Automatic Module Alignment Algorithm

## Citation

**Lee, Y.-J., & Kim, S. (2021)**

*Feature-based Fashion Flat Sketch Design Using Automatic Module Alignment Algorithm*

*International Journal of Clothing Science and Technology*, 33(5), 824–837.

### Role in CLO-SKET Literature Review

This paper represents a **feature-based geometric / modular fashion-flat representation approach**.

Its central contribution is not to learn a latent garment morphology space, but to organize **2D fashion flat sketches into reusable geometric garment modules** and automatically assemble those modules to generate new flat sketches.

The paper therefore provides an important precedent for:

\[
\boxed{
\text{fashion flat geometry}
\rightarrow
\text{explicit garment modules}
\rightarrow
\text{automatic design assembly}
}
\]

---

# 1. Scientific Question

The central question is:

> **How can fashion flat sketches be represented as reusable geometric modules so that new flat sketches can be generated efficiently through automatic module assembly?**

The overall direction is:

\[
\boxed{
\text{Fashion flat sketches}
\rightarrow
\text{morphological analysis}
\rightarrow
\text{module database}
\rightarrow
\text{automatic assembly}
}
\]

The paper therefore treats the **fashion flat as a structured design object**, rather than simply as an image.

---

# 2. Input

The input consists of **2D fashion flat sketches**.

The authors analyze existing fashion-flat designs and identify recurring garment components.

The resulting module database contains components such as:

- bodices,
- sleeves,
- collars,
- cuffs,
- pockets.

Thus the input representation can be conceptualized as:

\[
\boxed{
\text{fashion flat}
\rightarrow
\{\text{garment modules}\}
}
\]

The representation is explicitly geometric and design-oriented.

---

# 3. The Core Problem

Creating fashion flats manually can require repeatedly redrawing garment components that already occur across many designs.

The authors therefore seek to make garment-flat design more reusable.

Instead of:

\[
\text{draw complete garment from scratch}
\]

the system aims for:

\[
\boxed{
\text{select existing modules}
\rightarrow
\text{align modules}
\rightarrow
\text{assemble new flat}
}
\]

The key computational problem is therefore **geometric module alignment and assembly**.

---

# 4. Morphological Analysis as Used in the Paper

The paper describes the construction of a sample fashion-flat module database using:

\[
\boxed{
\text{sketch modularization}
+
\text{morphological analysis}
}
\]

The important point for our literature review is that the term **morphological analysis** is used in the context of identifying useful garment modules and their variations.

Therefore:

\[
\boxed{
\text{morphological analysis}
\rightarrow
\text{module vocabulary}
}
\]

rather than:

\[
\boxed{
\text{morphological analysis}
\rightarrow
\text{continuous population shape space}
}
\]

This distinction is important for CLO-SKET.

---

# 5. Module Representation

The resulting representation is feature/module-based.

A garment can be described through combinations of components such as:

\[
G =
\{
B,S,C,F,P,\ldots
\}
\]

where, conceptually:

- \(B\) = bodice,
- \(S\) = sleeve,
- \(C\) = collar,
- \(F\) = cuff,
- \(P\) = pocket.

The representation therefore captures **which geometric garment components are present and how they can be assembled**.

---

# 6. Automatic Module Alignment

The central computational operation is to align a selected module with the target garment structure.

Conceptually:

\[
\boxed{
\text{source module}
\rightarrow
\text{geometric transformation}
\rightarrow
\text{target module position}
}
\]

The transformation can involve operations such as:

- translation,
- rotation,
- scaling.

The objective is to place the selected component correctly relative to the target garment structure.

---

# 7. Important Distinction: Alignment vs PCA

The geometric transformation should not be confused with PCA.

### Module alignment

\[
\boxed{
\text{rotate / translate / scale the geometric object}
}
\]

The garment component itself changes position or orientation.

### PCA

\[
\boxed{
\text{rotate the coordinate basis of the data}
}
\]

The observations are not physically rotated.

PCA instead finds new orthogonal directions describing variation in the dataset.

Therefore:

\[
\boxed{
\text{Lee & Kim: object-space transformation}
}
\]

versus

\[
\boxed{
\text{PCA: feature-space transformation}
}
\]

This distinction is important when positioning the paper relative to quantitative morphology.

---

# 8. Automatic Assembly

After identifying and aligning appropriate modules, the system assembles them into a new fashion flat.

The overall process is:

\[
\boxed{
\text{module selection}
\rightarrow
\text{module alignment}
\rightarrow
\text{module assembly}
\rightarrow
\text{new fashion flat}
}
\]

The contribution is therefore primarily a **feature-based CAD workflow for fashion-flat design**.

---

# 9. What Is Learned?

The paper should not be interpreted as a neural representation-learning approach.

There is no demonstrated:

\[
\boxed{
\text{fashion sketch}
\rightarrow
\text{neural latent morphology space}
}
\]

Instead, the representation is explicitly constructed from garment components and their geometric relationships.

Conceptually:

\[
\boxed{
\text{fashion-flat geometry}
\rightarrow
\text{explicit modules}
\rightarrow
\text{geometric assembly}
}
\]

Thus the representation is **explicit and design-oriented**.

---

# 10. What the Paper Actually Represents

The final object of representation is essentially a **structured collection of garment design modules**.

Its information content can be viewed as:

\[
\boxed{
\text{garment components}
+
\text{component geometry}
+
\text{component relationships}
}
\]

The representation is useful because modules can be reused and recombined.

This makes the paper relevant to the broader question of whether fashion sketches contain structured geometric information.

---

# 11. What They Demonstrate

The paper demonstrates that:

1. fashion flats can be decomposed into reusable garment modules;
2. those modules can be stored in a database;
3. modules can be automatically aligned;
4. modules can be recombined;
5. new fashion-flat designs can therefore be generated computationally.

The central demonstrated capability is:

\[
\boxed{
\text{existing garment geometry}
\rightarrow
\text{reusable representation}
\rightarrow
\text{new design}
}
\]

---

# 12. Important Limitation for CLO-SKET

The representation is **module-based rather than population-statistical**.

The paper does not establish that:

\[
\boxed{
\text{many fashion flats}
\rightarrow
\text{continuous morphology space}
}
\]

Instead, it establishes:

\[
\boxed{
\text{many fashion flats}
\rightarrow
\text{reusable component vocabulary}
}
\]

This means that the word **morphological** in this paper should not automatically be interpreted in the same sense as geometric morphometrics.

---

# 13. What the Paper Does NOT Study

The paper does not primarily ask:

- How is whole-garment morphology distributed across a population?
- Can garment sketches be represented in a continuous statistical shape space?
- What are the principal directions of geometric garment variation?
- Can population-level shape clusters be discovered without predefined categories?
- Do different geometric representations recover the same morphology?
- Can morphological dimensions be independently validated?
- Does a learned representation correspond to interpretable garment morphology?
- Does the geometry of a sketch population reveal an underlying semantic organization?

These questions are outside the primary objective of the work.

The paper concerns **feature-based garment design and module recombination**, rather than population-level statistical morphology.

---

# 14. Lee & Kim vs. CLO-SKET

## Lee & Kim

The central question is:

\[
\boxed{
\text{How can garment components be reused to construct new fashion flats?}
}
\]

Pipeline:

\[
\boxed{
\text{fashion flats}
\rightarrow
\text{modules}
\rightarrow
\text{alignment}
\rightarrow
\text{assembly}
}
\]

---

## CLO-SKET

The central question is:

\[
\boxed{
\text{How is garment morphology organized across a population of sketches?}
}
\]

Conceptually:

\[
\boxed{
\text{sketch population}
\rightarrow
\text{explicit geometry}
\rightarrow
\text{morphological variation}
\rightarrow
\text{shape space}
}
\]

The scientific objectives are therefore different.

---

# 15. Scientific Positioning

Lee & Kim represents a **feature-based geometric representation of fashion flats**.

Its principal concern is:

\[
\boxed{
\text{fashion-flat geometry}
\rightarrow
\text{modular design representation}
}
\]

CLO-SKET instead treats the **sketch population itself** as the object of quantitative study:

\[
\boxed{
\text{fashion-sketch population}
\rightarrow
\text{morphology representation}
}
\]

The distinction can therefore be summarized as:

\[
\boxed{
\text{Lee & Kim: garment modules}
\rightarrow
\text{design assembly}
}
\]

versus

\[
\boxed{
\text{CLO-SKET: sketch population}
\rightarrow
\text{morphological organization}
}
\]

They therefore operate at different scientific levels rather than being direct methodological competitors.

---

# 16. FOMO Takeaway

### What this paper means for CLO-SKET

Lee & Kim prevents us from making an overly broad claim such as:

> "Previous work has not represented fashion flats as structured geometric objects."

That would be incorrect.

The paper demonstrates that fashion flats can be decomposed into **explicit geometric garment modules** and computationally recombined.

However, the paper does not establish:

\[
\boxed{
\text{population}
\rightarrow
\text{statistical shape space}
\rightarrow
\text{garment morphology}
}
\]

A more defensible positioning is:

> Prior work has represented fashion flats as explicit geometric garment modules for computational design and automatic recombination. CLO-SKET addresses a different level of analysis by asking whether explicit geometric measurements across a population of 2D fashion sketches reveal a statistically organized morphology space.

---

# 17. Reviewer-Proof Classification

### **Literature category:**

\[
\boxed{
\text{Feature-based geometric fashion-flat representation}
}
\]

### **Primary task:**

\[
\boxed{
\text{Fashion flats}
\rightarrow
\text{modules}
\rightarrow
\text{alignment}
\rightarrow
\text{assembly}
}
\]

### **Representation type:**

\[
\boxed{
\text{Explicit modular geometric representation}
}
\]

### **Mathematical basis:**

\[
\boxed{
\text{geometric module alignment}
}
\]

### **Learning type:**

\[
\boxed{
\text{No neural latent representation for the core module-assembly framework}
}
\]

### **Population-level fashion-sketch morphology analysis:**

\[
\boxed{\text{No}}
\]

### **Direct CLO-SKET competitor:**

\[
\boxed{\text{No}}
\]

### **Relevance to CLO-SKET:**

\[
\boxed{
\text{High — establishes explicit geometric/module representation of fashion flats}
}
\]

---

# 18. Final One-Sentence Understanding

> **Lee and Kim organize fashion flat sketches into reusable geometric garment modules and develop automatic alignment and assembly for computational flat-sketch design; while this establishes explicit geometric representation and manipulation of fashion flats, it does not investigate whether a population of 2D fashion sketches exhibits a statistically organized morphological shape space.**

---

## 🔒 Final Status

\[
\boxed{
\textbf{KEEP — ADJACENT GEOMETRIC PRECEDENT}
}
\]

**FOMO role:** Important boundary paper.

**What it establishes:** Explicit modular geometry of fashion flats.

**What remains open:** Population-level statistical morphology of 2D fashion sketches.