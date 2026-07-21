---
theme: seriph
background: https://cover.sli.dev
title: AI Data Analytics for Transportation Sector
info: |
  ## AI Data Analytics for Transportation Sector
  A module within "AI-Driven Transformation in Public Governance"

  Faculty of Engineering, KMUTNB
class: text-center text-white
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
presenterName: Asst. Prof. Dr. Ruslee Sutthaweekul
program: AI-Driven Transformation in Public Governance
module: AI Data Analytics for Transportation Sector
organizer: Faculty of Engineering, KMUTNB
cohort: Department of Rail Transport, Ministry of Transport
---

# {{ $slidev.configs.module }}

## {{ $slidev.configs.program }}

Presented by {{ $slidev.configs.presenterName }}

<div class="pt-8 opacity-70">
{{ $slidev.configs.organizer }} — for {{ $slidev.configs.cohort }}
</div>

<div @click="$slidev.nav.next" class="mt-12 py-1" hover:bg="white op-10">
  Press Space for next page <carbon:arrow-right />
</div>

---
hideInToc: true
---

# Today's Agenda

1.  **Why AI for Transportation & Rail**
2.  AI/ML Fundamentals Recap
3.  What is NDT & Where AI Fits
4.  Hands-On Lab 1 — Cargo Fill-Level Estimation
5.  Hands-On Lab 2 — Railway Defect Detection
6.  Wrap-Up & Your Own Pilot AI Idea

<div class="text-sm opacity-70 mt-8">
Items 1–3 are today's lecture (~60 minutes). Items 4–5 are hands-on, no-code labs.
</div>

---

# Your Instructor Today

<div class="grid grid-cols-5 gap-6 mt-2 items-center">
<div class="col-span-3">

### **Asst. Prof. Dr. Ruslee Sutthaweekul**

Dept. of Electrical and Computer Engineering  
Faculty of Engineering, KMUTNB

<div class="mt-4 text-sm">

- **Ph.D.** Electrical & Electronic Engineering — Newcastle University, UK
- **M.Eng** Electrical Eng. & IT — Rosenheim, Germany
- **B.Eng** Electrical Engineering — KMUTNB

</div>

<div class="mt-4 text-sm font-semibold text-blue-600 dark:text-blue-400">

26 years across **AI & Machine Learning** and **Rail Inspection Engineering**

</div>

</div>

<div class="col-span-2 text-center">
  <img src="/img/ruslee-lecture-live.jpg" class="rounded-xl shadow-lg border border-gray-500/20" style="max-height: 250px; width: 100%; object-fit: cover;">
  <div class="text-[11px] opacity-70 mt-2">Lecturing on Railway Signalling & AI</div>
</div>
</div>

---

# Relevant Experience

<div class="grid grid-cols-2 gap-6 text-sm">
<div>

### Industry

- **Bombardier Transportation** — Automatic Train Control (ATC) department
- **Project's Advisory, Thailand Post** — fleet optimization (ทุน บพข) 

<div class="grid grid-cols-2 gap-3 mt-4 text-center">
  <div>
    <img src="/img/bombardier-atc.png" class="rounded-lg shadow border border-gray-500/20" style="height:145px; width:100%; object-fit:cover;">
    <div class="text-[11px] font-semibold mt-1">Bombardier Transportation</div>
    <div class="text-[10px] opacity-75">Automatic Train Control (ATC)</div>
  </div>
  <div>
    <img src="/img/thailand-post-fleet.png" class="rounded-lg shadow border border-gray-500/20" style="height:145px; width:100%; object-fit:cover;">
    <div class="text-[11px] font-semibold mt-1">Thailand Post (ไปรษณีย์ไทย)</div>
    <div class="text-[10px] opacity-75">Fleet Optimization (ทุน บพข)</div>
  </div>
</div>

</div>
<div>

### Rail NDT & AI Research

- Eddy Current Testing for Railway
- Digital twin-driven design for the railway industry (British Council, UK)
- Predictive maintenance for lightweight wagons — INNOWAG (Shift2Rail, EU)
- Rail surface defect detection with neural networks; 3D rail reconstruction with Mask R-CNN 

<div class="grid grid-cols-2 gap-3 mt-4 text-center">
  <div>
    <img src="/img/uk-railway-digital-twin.png" class="rounded-lg shadow border border-gray-500/20" style="height:145px; width:100%; object-fit:cover;">
    <div class="text-[11px] font-semibold mt-1">UK Railway Digital Twin</div>
    <div class="text-[10px] opacity-75">British Council & Shift2Rail (UK)</div>
  </div>
  <div>
    <img src="/img/ruslee-ndt-field.png" class="rounded-lg shadow border border-gray-500/20" style="height:145px; width:100%; object-fit:cover;">
    <div class="text-[11px] font-semibold mt-1">UK Field Inspection</div>
    <div class="text-[10px] opacity-75">Newcastle University, UK</div>
  </div>
</div>

</div>
</div>

---

# In the Field & Global Research

<div class="grid grid-cols-4 gap-3 mt-4 text-center">
<div>
  <img src="/img/ruslee-ndt-field.png" class="rounded-lg shadow border border-gray-500/20" style="height:145px; width:100%; object-fit:cover;">
  <div class="text-xs font-bold mt-2">Field NDT Inspection</div>
  <div class="text-[11px] opacity-75">Non-destructive testing (RFID Sensors), Barrow Hill, Newcastle, UK</div>
</div>

<div>
  <img src="/img/ruslee-lecture-live.jpg" class="rounded-lg shadow border border-gray-500/20" style="height:145px; width:100%; object-fit:cover;">
  <div class="text-xs font-bold mt-2">Railway Training</div>
  <div class="text-[11px] opacity-75">Railway signalling & summer school lecture, Southwest JiaoTong University, Chengdu, China</div>
</div>

<div>
  <img src="/img/ruslee-ieee-award.jpg" class="rounded-lg shadow border border-gray-500/20" style="height:145px; width:100%; object-fit:cover;">
  <div class="text-xs font-bold mt-2">IEEE Sensors Award</div>
  <div class="text-[11px] opacity-75">2nd Place Student Contest, Glasgow, UK</div>
</div>

<div>
  <img src="/img/railway-digital-twin-workshop.jpg" class="rounded-lg shadow border border-gray-500/20" style="height:145px; width:100%; object-fit:cover;">
  <div class="text-xs font-bold mt-2">Digital Twin Workshop</div>
  <div class="text-[11px] opacity-75">British Council & international railway workshop, Bangkok, Thailand</div>
</div>
</div>

<div class="grid grid-cols-2 gap-3 mt-3 text-center">
<div>
  <img src="/img/ruslee-ect-rail-setup.jpg" class="rounded-lg shadow border border-gray-500/20" style="height:130px; width:100%; object-fit:cover;">
  <div class="text-xs font-bold mt-2">Eddy Current Testing Rig</div>
  <div class="text-[11px] opacity-75">Rail specimen with seeded defects, automated probe scanning &amp; oscilloscope acquisition</div>
</div>

<div>
  <img src="/img/ruslee-rail-3d-reconstruction.jpg" class="rounded-lg shadow border border-gray-500/20" style="height:130px; margin:auto; object-fit:contain;">
  <div class="text-xs font-bold mt-2">3D Rail Defect Reconstruction</div>
  <div class="text-[11px] opacity-75">Reconstructed rail-head surface vs. ground truth across 4 seeded defects</div>
</div>
</div>

---
layout: section
---

# Part 1
## NDT & AI Fundamentals

---
layout: two-cols-header
---

# Where You Are in the Program

::left::

### Already covered (Days 1–5)

- Introduction to AI: Everyday & Transportation
- How AI Learns: Basic Machine Learning
- Data Management for Smart AI
- AI for Communication: Chatbots & Voice Assistants
- AI Project Ideation for Transportation

::right::

### Today (Days 6–8)

- Going deep on **one domain**: transportation & rail
  infrastructure
- Two real, hands-on case studies
- Building toward **your own pilot AI project idea**
  for your unit

<div class="mt-4">
  <img src="/img/deep-engineering-ai.png" class="rounded-xl shadow-lg border border-gray-500/20" style="height: 180px; width: 100%; object-fit: cover;">
  <div class="text-[11px] opacity-75 mt-1.5 text-center font-medium">Deep Engineering AI & ML Research for Transportation Infrastructure</div>
</div>

---

# Fundamentals of Transportation Maintenance

<div class="grid grid-cols-2 gap-6 items-center">
<div>

### Evolution of Maintenance Paradigms

<div class="text-xs space-y-3 mt-2">

- **1. Reactive Maintenance (Run-to-Failure)**  
  Repair *after* breakdown occurs — high downtime, emergency costs & safety hazards.
- **2. Preventive Maintenance (Time / Mileage-Based)**  
  Scheduled interval servicing — leads to premature component replacement or undetected early flaws.
- **3. Condition-Based Maintenance (CBM) & NDT**  
  Assess internal & structural health **without damaging assets** using Non-Destructive Testing (NDT).
- **4. AI Predictive Maintenance (PdM)**  
  Combine continuous NDT data streams with **AI/ML prognostics** to forecast failure before it happens.

</div>

<div class="mt-4 p-3 bg-blue-500/10 rounded-lg border border-blue-500/30 text-xs">
💡 <strong>The Bridge to NDT:</strong> NDT provides the essential high-fidelity sensory data required to move from rigid calendar schedules to intelligent AI prognostics.
</div>

</div>

<div class="text-center">
  <img src="/img/maintenance-evolution.png" class="rounded-xl shadow-lg border border-gray-500/20" style="max-height: 330px; width: 100%; object-fit: contain;">
  <div class="text-[11px] opacity-70 mt-2">4 Generations of Transportation Asset Maintenance</div>
</div>
</div>

---

# Why Rail Specifically Needs NDT

<div class="grid grid-cols-4 gap-3 my-3">
<div class="text-center">
  <img src="/img/defect-head-checks.png" class="rounded shadow" style="height:120px; width:100%; object-fit:cover;">
  <div class="text-xs font-bold mt-1.5">Head Checks / RCF</div>
  <div class="text-[11px] opacity-75">Fine surface micro-cracks</div>
</div>
<div class="text-center">
  <img src="/img/defect-spalling.png" class="rounded shadow" style="height:120px; width:100%; object-fit:cover;">
  <div class="text-xs font-bold mt-1.5">Spalling / Squats</div>
  <div class="text-[11px] opacity-75">Surface pitting & metal loss</div>
</div>
<div class="text-center">
  <img src="/img/defect-corrugation.png" class="rounded shadow" style="height:120px; width:100%; object-fit:cover;">
  <div class="text-xs font-bold mt-1.5">Corrugation</div>
  <div class="text-[11px] opacity-75">Periodic wave-like wear</div>
</div>
<div class="text-center">
  <img src="/img/defect-break.png" class="rounded shadow" style="height:120px; width:100%; object-fit:cover;">
  <div class="text-xs font-bold mt-1.5">Rail Break</div>
  <div class="text-[11px] opacity-75">Severe transverse fracture</div>
</div>
</div>

<v-clicks>

- Surface defects like **head checks** and **spalling** can propagate internally into catastrophic **rail breaks**
- Continuous traffic loading means rail defects accumulate constantly — inspection is an **ongoing process**

</v-clicks>

---

# What is Non-Destructive Testing (NDT)?

**Definition:** inspecting or evaluating a material, component, or
structure's condition **without damaging it or removing it from
service**.

<v-click>

**Contrast with destructive testing** — e.g. pulling a sample to
failure to find its breaking strength. That tells you about *one
sample*, and destroys it. You obviously can't test 100% of a rail
network that way.

</v-click>

<v-click>

NDT lets you inspect the **actual asset in service**, repeatedly, over
its entire operating life.

</v-click>

---

# Common NDT Methods

<div class="grid grid-cols-3 gap-3 my-2 text-xs">
<div class="rounded-lg p-2.5 bg-gray-500/10 border border-gray-500/20 shadow-sm flex flex-col">
  <img src="/img/ndt-visual.png" class="rounded h-24 w-full object-cover mb-2">
  <div class="font-bold text-sm text-blue-600 dark:text-blue-400">Visual (VT)</div>
  <div class="opacity-90 font-medium mt-0.5">Camera / Optical examination</div>
  <div class="opacity-70 text-[11px] mt-1">First line of defense — automated in Lab 2</div>
</div>

<div class="rounded-lg p-2.5 bg-gray-500/10 border border-gray-500/20 shadow-sm flex flex-col">
  <img src="/img/ndt-ultrasonic.png" class="rounded h-24 w-full object-cover mb-2">
  <div class="font-bold text-sm text-amber-600 dark:text-amber-400">Ultrasonic (UT)</div>
  <div class="opacity-90 font-medium mt-0.5">High-frequency sound waves</div>
  <div class="opacity-70 text-[11px] mt-1">Internal cracks & internal rail defects</div>
</div>

<div class="rounded-lg p-2.5 bg-gray-500/10 border border-gray-500/20 shadow-sm flex flex-col">
  <img src="/img/ndt-magnetic-particle.png" class="rounded h-24 w-full object-cover mb-2">
  <div class="font-bold text-sm text-emerald-600 dark:text-emerald-400">Magnetic Particle (MPI)</div>
  <div class="opacity-90 font-medium mt-0.5">Magnetic field + iron particles</div>
  <div class="opacity-70 text-[11px] mt-1">Ferromagnetic surface/near-surface cracks</div>
</div>

<div class="rounded-lg p-2.5 bg-gray-500/10 border border-gray-500/20 shadow-sm flex flex-col">
  <img src="/img/ndt-eddy-current.png" class="rounded h-24 w-full object-cover mb-2">
  <div class="font-bold text-sm text-purple-600 dark:text-purple-400">Eddy Current (ECT)</div>
  <div class="opacity-90 font-medium mt-0.5">Induced electromagnetic fields</div>
  <div class="opacity-70 text-[11px] mt-1">Shallow surface micro-flaws & head checks</div>
</div>

<div class="rounded-lg p-2.5 bg-gray-500/10 border border-gray-500/20 shadow-sm flex flex-col">
  <img src="/img/ndt-radiography.png" class="rounded h-24 w-full object-cover mb-2">
  <div class="font-bold text-sm text-red-600 dark:text-red-400">Radiographic (RT)</div>
  <div class="opacity-90 font-medium mt-0.5">Industrial X-rays / Gamma rays</div>
  <div class="opacity-70 text-[11px] mt-1">Internal weld porosity & cast structure</div>
</div>

<div class="rounded-lg p-2.5 bg-gray-500/10 border border-gray-500/20 shadow-sm flex flex-col">
  <img src="/img/ndt-thermography.png" class="rounded h-24 w-full object-cover mb-2">
  <div class="font-bold text-sm text-cyan-600 dark:text-cyan-400">Thermography (IRT)</div>
  <div class="opacity-90 font-medium mt-0.5">Infrared heat signature mapping</div>
  <div class="opacity-70 text-[11px] mt-1">Thermal anomalies & friction hot spots</div>
</div>
</div>

---

# Traditional Rail Inspection: The Bottleneck

<div class="grid grid-cols-5 gap-6 mt-4 items-center">
<div class="col-span-3">

<v-clicks>

- **Manual walking inspection** — thorough, but slow, subjective, fatigue-prone, and dependent on weather & heat
- **Specialized inspection trains** — fast and objective, but expensive and limited in availability/scheduling
- **The coverage gap** — thousands of track-km vs limited inspector-hours and vehicle-hours to cover them

</v-clicks>

</div>

<div class="col-span-2 text-center">
  <img src="/img/manual-walking-inspector.png" class="rounded-xl shadow-lg border border-gray-500/20" style="max-height: 240px; width: 100%; object-fit: cover;">
  <div class="text-[11px] opacity-70 mt-2">Manual track walking inspection under harsh weather</div>
</div>
</div>

---
layout: center
class: text-center
---

# From NDT to AI Fundamentals

We've covered what NDT is, why rail needs it, and where traditional
inspection struggles to keep up. Now: the AI concepts today's labs are
built on.

---

# AI/ML Recap: Supervised Learning in One Picture

<div class="flex items-center justify-center gap-4 my-8 px-4">
  <div class="flex-1 max-w-xs p-5 rounded-2xl bg-blue-500/10 border-2 border-blue-500/30 shadow-lg text-center">
    <div class="text-4xl mb-2">🖼️</div>
    <div class="font-bold text-lg">Input</div>
    <div class="text-sm opacity-80 mt-1">Photo / Sensor Data</div>
  </div>

  <div class="text-3xl opacity-60 flex-shrink-0">➔</div>

  <div class="flex-1 max-w-xs p-5 rounded-2xl bg-amber-500/10 border-2 border-amber-500/30 shadow-lg text-center">
    <div class="text-4xl mb-2">🧠</div>
    <div class="font-bold text-lg">Model</div>
    <div class="text-sm opacity-80 mt-1">Learned Patterns</div>
  </div>

  <div class="text-3xl opacity-60 flex-shrink-0">➔</div>

  <div class="flex-1 max-w-xs p-5 rounded-2xl bg-emerald-500/10 border-2 border-emerald-500/30 shadow-lg text-center">
    <div class="text-4xl mb-2">🎯</div>
    <div class="font-bold text-lg">Output</div>
    <div class="text-sm opacity-80 mt-1">Prediction / Answer</div>
  </div>
</div>

<v-click>

The model doesn't know the answer on day one — it **learns from
labeled examples**. Give it enough correctly-labeled photos, and it
learns the pattern well enough to guess on a *new* photo it has never
seen.

Both of today's labs are examples of exactly this: **supervised
learning**.

</v-click>

---
layout: two-cols-header
---

# Two Flavors of AI Output You'll See Today

<div class="text-xs opacity-75 mb-3 -mt-1">
Understanding how Machine Learning models solve different engineering problems in transportation
</div>

::left::

<div class="flex flex-col justify-between bg-gradient-to-b from-blue-950/40 via-slate-900/60 to-slate-950/80 border border-blue-500/30 rounded-2xl p-4 shadow-xl relative overflow-hidden group hover:border-blue-400/60 transition-all duration-300">
  <div class="absolute -top-10 -right-10 w-24 h-24 bg-blue-500/10 rounded-full blur-xl pointer-events-none"></div>

  <div>
    <div class="flex items-center justify-between mb-2">
      <span class="text-[11px] font-bold uppercase tracking-wider text-blue-400 bg-blue-500/15 px-2.5 py-0.5 rounded-full border border-blue-500/30">
        Flavor 1 — Regression
      </span>
      <span class="text-[10px] opacity-60 font-mono">Continuous Value</span>
    </div>
    <h3 class="text-base font-bold text-white mb-1">
      Output = A <span class="text-blue-400 underline decoration-blue-500/40 underline-offset-4">Continuous Number</span>
    </h3>
    <p class="text-[11px] opacity-70 mb-3">Predicts single quantitative measurements like percentage, weight, or speed.</p>
    <!-- Visual Flow -->
    <div class="flex items-center justify-between bg-slate-950/80 rounded-xl p-3 border border-white/5 my-2">
      <div class="text-center">
        <img src="/img/cargo-front-later.jpg" class="h-20 w-24 object-cover rounded-lg shadow-md border border-white/10 group-hover:scale-105 transition-transform duration-300">
        <div class="text-[10px] opacity-60 mt-1">Input Image</div>
      </div>
      <div class="flex flex-col items-center justify-center px-1">
        <carbon:arrow-right class="text-xl text-blue-400" />
        <span class="text-[9px] text-blue-300/80 font-mono mt-0.5">CNN Model</span>
      </div>
      <div class="text-center flex flex-col items-center justify-center">
        <div class="bg-gradient-to-br from-blue-600 to-indigo-700 text-white font-extrabold text-2xl px-3 py-1.5 rounded-xl shadow-lg shadow-blue-500/20 border border-blue-400/40">
          72%
        </div>
        <div class="text-[10px] font-medium text-blue-300 mt-1">Cargo Fill Level</div>
      </div>
    </div>
  </div>

  <div class="mt-3 pt-2.5 border-t border-white/5 flex items-center justify-between text-xs">
    <span class="font-semibold text-blue-300 text-[11px]">Lab 1 Context:</span>
    <span class="text-[10px] opacity-90 bg-blue-950 px-2 py-0.5 rounded border border-blue-800/60 text-blue-200">Cargo Volume Estimation</span>
  </div>
</div>

::right::

<div class="flex flex-col justify-between bg-gradient-to-b from-emerald-950/40 via-slate-900/60 to-slate-950/80 border border-emerald-500/30 rounded-2xl p-4 shadow-xl relative overflow-hidden group hover:border-emerald-400/60 transition-all duration-300">
  <div class="absolute -top-10 -right-10 w-24 h-24 bg-emerald-500/10 rounded-full blur-xl pointer-events-none"></div>

  <div>
    <div class="flex items-center justify-between mb-2">
      <span class="text-[11px] font-bold uppercase tracking-wider text-emerald-400 bg-emerald-500/15 px-2.5 py-0.5 rounded-full border border-emerald-500/30">
        Flavor 2 — Segmentation
      </span>
      <span class="text-[10px] opacity-60 font-mono">Pixel-Level Mask</span>
    </div>
    <h3 class="text-base font-bold text-white mb-1">
      Output = A <span class="text-emerald-400 underline decoration-emerald-500/40 underline-offset-4">Pixel Defect Map</span>
    </h3>
    <p class="text-[11px] opacity-70 mb-3">Classifies every pixel to isolate precise defect boundaries & locations.</p>
    <!-- Visual Flow -->
    <div class="flex items-center justify-between bg-slate-950/80 rounded-xl p-3 border border-white/5 my-2">
      <div class="text-center">
        <img src="/img/rail-sample.jpg" class="h-20 w-24 object-cover rounded-lg shadow-md border border-white/10 group-hover:scale-105 transition-transform duration-300">
        <div class="text-[10px] opacity-60 mt-1">Raw Rail Photo</div>
      </div>
      <div class="flex flex-col items-center justify-center px-1">
        <carbon:arrow-right class="text-xl text-emerald-400" />
        <span class="text-[9px] text-emerald-300/80 font-mono mt-0.5">U-Net Model</span>
      </div>
      <div class="text-center">
        <img src="/img/rail-sample-mask.png" class="h-20 w-24 object-cover rounded-lg shadow-md border border-emerald-500/40 group-hover:scale-105 transition-transform duration-300">
        <div class="text-[10px] font-medium text-emerald-300 mt-1">Defect Mask Map</div>
      </div>
    </div>
  </div>

  <div class="mt-3 pt-2.5 border-t border-white/5 flex items-center justify-between text-xs">
    <span class="font-semibold text-emerald-300 text-[11px]">Lab 2 Context:</span>
    <span class="text-[10px] opacity-90 bg-emerald-950 px-2 py-0.5 rounded border border-emerald-800/60 text-emerald-200">Railway Defect Segmentation</span>
  </div>
</div>

---

# Train / Validation / Test Split

<div class="grid grid-cols-2 gap-6 items-center">
<div>

<h3 class="text-sm font-semibold text-blue-400 mb-2">Why Hide Data from the Model?</h3>

<p class="text-xs opacity-80 leading-relaxed mb-3">
Testing a model on training data causes <strong>memorization (overfitting)</strong>. To ensure true real-world reliability, every dataset is split into 3 distinct subsets:
</p>

<div class="space-y-2.5 text-xs">
  <div class="p-2.5 bg-blue-950/40 border border-blue-500/30 rounded-xl flex items-start gap-2.5">
    <div class="bg-blue-500/20 text-blue-300 font-bold px-2 py-0.5 rounded text-[11px] mt-0.5">70%</div>
    <div>
      <div class="font-bold text-blue-300">1. Train Set</div>
      <div class="text-[11px] opacity-75">Used by the model to adjust weights and learn underlying feature patterns.</div>
    </div>
  </div>

  <div class="p-2.5 bg-purple-950/40 border border-purple-500/30 rounded-xl flex items-start gap-2.5">
    <div class="bg-purple-500/20 text-purple-300 font-bold px-2 py-0.5 rounded text-[11px] mt-0.5">15%</div>
    <div>
      <div class="font-bold text-purple-300">2. Validation Set</div>
      <div class="text-[11px] opacity-75">Used during training to tune hyperparameters & prevent overfitting.</div>
    </div>
  </div>

  <div class="p-2.5 bg-emerald-950/40 border border-emerald-500/30 rounded-xl flex items-start gap-2.5">
    <div class="bg-emerald-500/20 text-emerald-300 font-bold px-2 py-0.5 rounded text-[11px] mt-0.5">15%</div>
    <div>
      <div class="font-bold text-emerald-300">3. Test Set (Locked)</div>
      <div class="text-[11px] opacity-75">Held back completely until the end to give an honest, final accuracy score.</div>
    </div>
  </div>
</div>

<div class="mt-3 p-2.5 bg-amber-500/10 rounded-lg border border-amber-500/30 text-[11px] flex items-center gap-2">
  <span>💡</span>
  <span><strong>Lab Note:</strong> Today's hands-on scripts perform this 3-way split automatically!</span>
</div>

</div>

<div class="text-center">
  <img src="/img/dataset-split-diagram.png" class="rounded-2xl shadow-2xl border border-gray-500/30" style="max-height: 370px; width: 100%; object-fit: contain;">
  <div class="text-[11px] opacity-70 mt-2 font-medium">Dataset Partitioning Architecture for Machine Learning</div>
</div>
</div>

---

# Hyperparameters: What YOU Control

Every model has two kinds of numbers inside it:

<v-clicks>

- **Learned automatically** — adjusted during training, you never
  touch these directly
- **Hyperparameters** — chosen by *you*, before training even starts
  (e.g. how many decision trees, what confidence threshold to use)

</v-clicks>

<v-click>

Today's labs are "no code" precisely because we've isolated the
hyperparameters into a plain settings file you edit. Everything else
is already written.

</v-click>

---

# How Do We Know If a Model Is Good?

## Two scorecards you'll use today

| Lab | Task | Metric | A good score looks like |
|---|---|---|---|
| **Lab 1: Cargo** | Regression | MAE (Mean Absolute Error) | **Low** — close to 0 |
| **Lab 2: Rail** | Segmentation | IoU / Dice | **High** — close to 1 |

<div class="text-sm opacity-70 mt-4">
Different tasks need different scorecards — there's no single
universal "accuracy" number that works for both.
</div>

---

# Garbage In, Garbage Out

A model can only be as good as the labels it learns from.

<div class="grid grid-cols-5 gap-6 mt-4 items-center">
<div class="col-span-3">

<v-click>

In **Lab 1**, *you* are the label source — there is no automatic "correct answer key." You decide, by eye, how full each truck looks.

</v-click>

<v-click>

<div class="mt-4">
This mirrors a crucial issue in government AI projects: <strong>is your agency's data trustworthy enough to build AI on?</strong> Often the hardest, most valuable work is data quality — not the model.
</div>

</v-click>

</div>

<div class="col-span-2 text-center">
  <img src="/img/data-labeling-workstation.png" class="rounded-xl shadow-lg border border-gray-500/20" style="max-height: 240px; width: 100%; object-fit: cover;">
  <div class="text-[11px] opacity-70 mt-2">Human-in-the-loop data labeling & validation</div>
</div>
</div>

---

# The Class Imbalance Problem

In a rail defect photo, maybe **2%** of pixels are the actual defect —
the other 98% are normal rail surface.

<v-click>

A lazy model could say *"no defect anywhere"* and still be 98%
"accurate."

</v-click>

<v-click>

That's exactly why **Lab 2 uses IoU, not accuracy** — and why the
model has to be specifically built to avoid falling into this trap.
Watch for this same trap in your own agency's data: rare events (fraud,
failures, accidents) are almost always a tiny minority of the records.

</v-click>

---

# Why Transportation & Rail Need AI

Thailand's transport network is huge, aging, and safety-critical — exactly where AI pays off.

<div class="grid grid-cols-5 gap-6 mt-4 items-center">
<div class="col-span-3 text-base">

<v-clicks>

- **Coverage Gap**: Track-km to inspect vastly exceed available inspector-hours
- **Rare Anomalies**: Defects are rare events hidden inside huge volumes of routine data — ideal for AI
- **Consistency**: Repeatable judgment vs. human fatigue and subjectivity
- **Human-in-the-Loop**: Frees skilled staff for critical decisions AI can't make

</v-clicks>

</div>

<div class="col-span-2 text-center">
  <img src="/img/rail-inspection-train.png" class="rounded-xl shadow-lg border border-gray-500/20" style="max-height: 240px; width: 100%; object-fit: cover;">
  <div class="text-[11px] opacity-70 mt-2">Automated high-speed rail scanning vehicle</div>
</div>
</div>

---

# Where AI Fits in the NDT Workflow

AI doesn't replace certified inspectors — it **augments** them.

<div class="flex items-center justify-between gap-2 my-6">
  <div class="flex-1 p-4 rounded-xl bg-blue-500/10 border-2 border-blue-500/30 shadow text-center">
    <div class="text-3xl mb-1">📷</div>
    <div class="font-bold text-base">Camera / Sensor</div>
    <div class="text-xs opacity-75 mt-1">Automated data capture</div>
  </div>

  <div class="text-2xl opacity-60 flex-shrink-0">➔</div>

  <div class="flex-1 p-4 rounded-xl bg-amber-500/10 border-2 border-amber-500/30 shadow text-center">
    <div class="text-3xl mb-1">🤖</div>
    <div class="font-bold text-base">AI Screening</div>
    <div class="text-xs opacity-75 mt-1">Flags candidate defects</div>
  </div>

  <div class="text-2xl opacity-60 flex-shrink-0">➔</div>

  <div class="flex-1 p-4 rounded-xl bg-emerald-500/10 border-2 border-emerald-500/30 shadow text-center">
    <div class="text-3xl mb-1">🔍</div>
    <div class="font-bold text-base">Human Inspector</div>
    <div class="text-xs opacity-75 mt-1">Verifies & prioritizes</div>
  </div>

  <div class="text-2xl opacity-60 flex-shrink-0">➔</div>

  <div class="flex-1 p-4 rounded-xl bg-purple-500/10 border-2 border-purple-500/30 shadow text-center">
    <div class="text-3xl mb-1">🛠️</div>
    <div class="font-bold text-base">Decision</div>
    <div class="text-xs opacity-75 mt-1">Maintenance action</div>
  </div>
</div>

<v-click>

<div class="mt-4">

**What AI is good at:** scanning huge volumes of images tirelessly,
consistently, flagging the same pattern every single time.

**What stays human:** final judgment, operational context,
safety-critical sign-off.

</div>

</v-click>

---

# Today's Two Case Studies

|  | Lab 1: Cargo | Lab 2: Rail |
|---|---|---|
| **Domain** | Logistics / transportation | NDT / rail infrastructure |
| **AI task** | Regression | Segmentation |
| **Metric** | MAE (lower is better) | IoU (higher is better) |
| **What you do** | Label the data | Tune the threshold |

---
layout: default
---

# Part 1 Summary

<div class="text-sm">

- **Supervised learning** — a model learns from labeled examples, not
  hard-coded rules
- **Regression vs. segmentation** — predicting a number vs. predicting
  a pixel map
- **Train / validation / test split** — why held-out data makes a
  score trustworthy
- **Hyperparameters** — the settings you choose, not what the model
  learns on its own
- **MAE** (lower is better) and **IoU / Dice** (higher is better) — two
  different scorecards for two different tasks
- **Garbage in, garbage out** — label quality determines model quality
- **Class imbalance** — why accuracy alone can be a deceptive metric
- **NDT** — inspecting without damaging, and where AI fits alongside
  human inspectors

</div>

---
hideInToc: true
---

# Today's Agenda

1.  Why AI for Transportation & Rail
2.  AI/ML Fundamentals Recap
3.  What is NDT & Where AI Fits
4.  **Hands-On Lab 1 — Cargo Fill-Level Estimation**
5.  Hands-On Lab 2 — Railway Defect Detection
6.  Wrap-Up & Your Own Pilot AI Idea

---

# Why These Labs Exist

Most of the effort in a real AI project isn't writing code — it's:

<v-clicks>

- Organizing raw data
- Deciding what the "correct answer" even is
- Choosing sensible settings
- Honestly measuring how good the result is

</v-clicks>

<br>

<v-click>

These two labs isolate exactly that experience. **All the code is
already written** — you label data and/or tweak settings, and see how
the results change.

</v-click>

---
layout: section
---

# Part 2
## Hands-On Lab 1
### Estimating Truck Cargo Space with AI

---

# Lab 1: The Big Picture

Cameras bolted inside a delivery truck's cargo box (front + rear) take photos
as the truck gets loaded through the day.

**Goal:** given a new photo, guess what percentage of the cargo space is used.

<div class="grid grid-cols-3 gap-3 mt-2">
<div class="text-center">
<img src="/img/cargo-front-early.jpg" class="rounded shadow" style="max-height:150px; margin:auto">
<div class="text-sm opacity-70 mt-1">Front camera, early</div>
</div>
<div class="text-center">
<img src="/img/cargo-front-later.jpg" class="rounded shadow" style="max-height:150px; margin:auto">
<div class="text-sm opacity-70 mt-1">Front camera, later</div>
</div>
<div class="text-center">
<img src="/img/cargo-rear-later.jpg" class="rounded shadow" style="max-height:150px; margin:auto">
<div class="text-sm opacity-70 mt-1">Rear camera, later</div>
</div>
</div>

<div class="mt-2">

- 0% = empty &nbsp;&nbsp;→&nbsp;&nbsp; 100% = completely full
- **No automatic ground truth exists** — a human has to look and decide
- That's the main task: label 42 photos by eye

</div>

---

# Lab 1: How It All Fits Together

<div class="grid grid-cols-4 gap-2.5 my-3 text-xs">
  <div class="p-3 rounded-lg bg-gray-500/10 border border-gray-500/20 flex flex-col justify-between">
    <div>
      <span class="px-2 py-0.5 rounded text-[10px] font-semibold bg-gray-500/20 text-gray-700 dark:text-gray-300">Done for you</span>
      <div class="font-bold text-sm mt-2">1. Raw Photos</div>
      <div class="opacity-75 text-[11px] mt-0.5">Organize photos</div>
    </div>
    <div class="text-right text-base opacity-40 mt-1">➔</div>
  </div>

  <div class="p-3 rounded-lg bg-orange-500/15 border-2 border-orange-500/40 shadow-sm flex flex-col justify-between">
    <div>
      <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-orange-500 text-white">YOUR ACTION</span>
      <div class="font-bold text-sm mt-2">2. Label Data</div>
      <div class="opacity-75 text-[11px] mt-0.5">Label fill_level</div>
    </div>
    <div class="text-right text-base opacity-40 mt-1">➔</div>
  </div>

  <div class="p-3 rounded-lg bg-gray-500/10 border border-gray-500/20 flex flex-col justify-between">
    <div>
      <span class="px-2 py-0.5 rounded text-[10px] font-semibold bg-gray-500/20 text-gray-700 dark:text-gray-300">Done for you</span>
      <div class="font-bold text-sm mt-2">3. Split Dataset</div>
      <div class="opacity-75 text-[11px] mt-0.5">Train / Val / Test</div>
    </div>
    <div class="text-right text-base opacity-40 mt-1">➔</div>
  </div>

  <div class="p-3 rounded-lg bg-orange-500/15 border-2 border-orange-500/40 shadow-sm flex flex-col justify-between">
    <div>
      <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-orange-500 text-white">YOUR ACTION</span>
      <div class="font-bold text-sm mt-2">4. Edit Config</div>
      <div class="opacity-75 text-[11px] mt-0.5">cargo_config.yaml</div>
    </div>
    <div class="text-right text-base opacity-40 mt-1">➔</div>
  </div>
</div>

<div class="grid grid-cols-3 gap-3 my-2 text-xs">
  <div class="p-3 rounded-lg bg-gray-500/10 border border-gray-500/20 flex flex-col justify-between">
    <div>
      <span class="px-2 py-0.5 rounded text-[10px] font-semibold bg-gray-500/20 text-gray-700 dark:text-gray-300">Done for you</span>
      <div class="font-bold text-sm mt-1">5. Train Model</div>
      <div class="opacity-75 text-[11px] mt-0.5">cargo_train.py</div>
    </div>
    <div class="text-right text-base opacity-40 mt-1">➔</div>
  </div>

  <div class="p-3 rounded-lg bg-gray-500/10 border border-gray-500/20 flex flex-col justify-between">
    <div>
      <span class="px-2 py-0.5 rounded text-[10px] font-semibold bg-gray-500/20 text-gray-700 dark:text-gray-300">Done for you</span>
      <div class="font-bold text-sm mt-1">6. Evaluate</div>
      <div class="opacity-75 text-[11px] mt-0.5">cargo_evaluate.py</div>
    </div>
    <div class="text-right text-base opacity-40 mt-1">➔</div>
  </div>

  <div class="p-3 rounded-lg bg-blue-500/15 border-2 border-blue-500/40 shadow-sm flex flex-col justify-between">
    <div>
      <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-blue-600 text-white">SCORE</span>
      <div class="font-bold text-sm mt-1">7. Your Score</div>
      <div class="opacity-90 font-medium text-[11px] mt-0.5">Mean Absolute Error (MAE)</div>
    </div>
    <div class="text-xs text-blue-600 dark:text-blue-400 font-semibold mt-1">🔄 Tweak settings & repeat</div>
  </div>
</div>

---

# Lab 1: Three Models to Try

<div class="grid grid-cols-3 gap-4 mt-6 text-sm">
<div>

### 🌳 Random Forest

Many simple "decision trees" each guess an answer, and the guesses
get averaged. A good default — handles messy patterns well.

</div>
<div>

### 👥 KNN

*(k-nearest neighbors)*

Finds the most visually similar training photos and averages
their fill %. Simple and intuitive.

</div>
<div>

### 📈 Linear Regression

The simplest possible model: fits one straight-line relationship
between the photo and the fill %.

</div>
</div>

<div class="mt-8 text-sm opacity-70 text-center">
Set with <code>model_type</code> in <code>cargo_config.yaml</code> — try all three and compare.
</div>

---

# Deep Dive: Random Forest

<div class="text-sm opacity-80 mt-1">An ensemble of decision trees, trained on randomized subsets of the data, whose predictions are averaged.</div>

<div class="grid grid-cols-2 gap-4 mt-3 text-xs leading-snug">
<div>

**How it works**

- Each tree trains on a **bootstrap sample** (*bagging*, Breiman 1996) and each split considers only a **random subset of features** (Breiman 2001) — this decorrelates the trees
- Every split greedily picks the feature/threshold that most reduces variance in the target ($\Delta = \mathrm{Var}(y_{\text{parent}}) - \text{weighted child variance}$)
- Final prediction is the plain average across all $T$ trees:

$$\hat y = \frac{1}{T}\sum_{t=1}^{T} f_t(x)$$

</div>
<div>

<div class="p-2.5 rounded-lg bg-amber-500/10 border border-amber-500/30">

**Hyperparameters:** `n_estimators` ($T$) — error shrinks ~$1/\sqrt{T}$, diminishing returns past a point. `max_depth` — caps one tree's capacity.

</div>

<div class="mt-2 p-2.5 rounded-lg bg-blue-500/10 border border-blue-500/30">

**Bias/variance:** one deep tree is low-bias/high-variance; averaging many *decorrelated* high-variance trees cancels noise without raising bias.

</div>

<div class="mt-2 p-2.5 rounded-lg bg-gray-500/10 border border-gray-500/20">

✅ nonlinear patterns & interactions, robust to noise &nbsp;&nbsp; ❌ costs memory/time, less interpretable

</div>

</div>
</div>

<div class="mt-2 text-xs opacity-70">
In Lab 1: the default <code>model_type</code> — a strong general-purpose choice when you don't know the shape of the relationship in advance.
</div>

---

# Deep Dive: K-Nearest Neighbors

<div class="text-sm opacity-80 mt-1">An instance-based, "lazy" learner — there is no training step, the stored training data <strong>is</strong> the model.</div>

<div class="grid grid-cols-2 gap-4 mt-3 text-xs leading-snug">
<div>

**How it works**

- To predict for photo $x$, compute its distance to every training photo in feature space: $d(x, x_i) = \lVert x - x_i \rVert_2$ (typically Euclidean)
- Take the $k$ closest photos (`n_neighbors`) and average their labels:

$$\hat y = \frac{1}{k}\sum_{i \,\in\, N_k(x)} y_i$$

- **Curse of dimensionality**: our feature vector has ~83 numbers (brightness stats + histogram + 8×8 coarse grid) — in high dimensions, distances between points get less discriminative, a known weak spot for KNN

</div>
<div>

<div class="p-2.5 rounded-lg bg-amber-500/10 border border-amber-500/30">

**Hyperparameter:** `n_neighbors` ($k$) is the bias/variance dial in one number.

</div>

<div class="mt-2 p-2.5 rounded-lg bg-blue-500/10 border border-blue-500/30">

**Bias/variance:** small $k$ follows local noise closely (low bias/high variance, overfits). Large $k$ averages over a big neighborhood (high bias/low variance), trending toward the global mean as $k \to n$.

</div>

<div class="mt-2 p-2.5 rounded-lg bg-gray-500/10 border border-gray-500/20">

✅ zero training cost, adapts to local structure &nbsp;&nbsp; ❌ slow at prediction, sensitive to scaling, weak in high-dim

</div>

</div>
</div>

<div class="mt-2 text-xs opacity-70">

In Lab 1: with only ~30 training photos, $k$ is literally how many labeled examples get blended into each guess — try `n_neighbors=1` vs. `10`.

</div>

---

# Deep Dive: Linear Regression

<div class="text-sm opacity-80 mt-1">Assumes the target is a straight-line (affine) function of the input features — the simplest possible model, and this lab's only "settings-free" one.</div>

<div class="grid grid-cols-2 gap-4 mt-3 text-xs leading-snug">
<div>

**How it works**

$$\hat y = w^\top x + b$$

- Fit by **Ordinary Least Squares**: choose $w, b$ to minimize the sum of squared residuals over the training photos:

$$(w^*, b^*) = \arg\min_{w,\,b} \sum_{i=1}^{n} \left(y_i - w^\top x_i - b\right)^2$$

- Solved in closed form via the normal equations — no iteration, no hyperparameters to tune

</div>
<div>

<div class="p-2.5 rounded-lg bg-amber-500/10 border border-amber-500/30">

**Hyperparameters:** none — `random_seed` is the only setting that still applies (it only affects the train/val/test split, not the fit itself).

</div>

<div class="mt-2 p-2.5 rounded-lg bg-blue-500/10 border border-blue-500/30">

**Bias/variance:** high bias (hard-assumes linearity), low variance — stable and reproducible, but systematically wrong whenever the true relationship curves.

</div>

<div class="mt-2 p-2.5 rounded-lg bg-gray-500/10 border border-gray-500/20">

✅ fully interpretable, fast, no overfitting risk &nbsp;&nbsp; ❌ can't capture nonlinearity/interactions, sensitive to outliers

</div>

</div>
</div>

<div class="mt-2 text-xs opacity-70">
In Lab 1: this is why <code>linear_regression</code> usually scores worst (MAE ≈13 vs. ≈2–3) — fill % isn't a straight-line function of brightness/edge features.
</div>

---

# Lab 1: What Do the Other Settings Mean?

<div class="text-sm">

| Setting | Used by | What it controls |
|---|---|---|
| `n_estimators` | Random Forest | How many trees vote. More = steadier, but slower. |
| `max_depth` | Random Forest | How deep/detailed each tree's questions get. Too deep = memorizes noise ("overfitting"). |
| `n_neighbors` | KNN | How many similar photos to average together. |
| `random_seed` | All models | Controls internal randomness (tie-breaking, etc). Same seed = reproducible result. |

</div>

<div class="mt-6 opacity-70 text-sm">
Only the settings for your chosen <code>model_type</code> actually do
anything — the rest are ignored.
</div>

---

# Lab 1: Compete With Each Other

Once labeled, edit `configs/cargo_config.yaml` — no code, just values:

```yaml
model_type: random_forest   # or: knn, linear_regression
n_estimators: 100
max_depth: 5
random_seed: 42
```

<v-click>

Re-run training + evaluation, track your **Mean Absolute Error** (lower is
better) on a shared scoreboard.

<div class="text-sm opacity-70 mt-4">
Did the best score come from the best settings — or the most careful labeling?
</div>

</v-click>

---

# Lab 1: Example Run — What to Expect

<div class="text-sm">

| model_type | key settings | MAE (percentage points) |
|---|---|---|
| random_forest (default) | n_estimators=100, max_depth=5 | 2.9 |
| knn | n_neighbors=3 | 2.4 |
| random_forest | n_estimators=300, max_depth=15 | 2.7 |
| random_forest | n_estimators=20, max_depth=2 (shallow/few trees) | 5.0 |
| linear_regression | (default) | 13.1 |

</div>

<div class="mt-4 text-sm opacity-70">

- This dry run used placeholder photos with a clean fill gradient — a pipeline
  smoke test, not real fleet data. Expect your own MAE to be **higher and more
  variable**, since real photos are messier and labeling is subjective.
- The pattern to expect still holds: `linear_regression` underfits badly,
  very shallow/few-tree forests underfit, and `knn`/well-tuned forests land
  closest to the pack.

</div>

---

# Lab 1: Real Output Example

<div class="text-center">
<img src="/img/cargo-eval-example.png" style="max-height:150px; margin:auto">
</div>

<div class="text-center mt-2">
<img src="/img/cargo-eval-scatter-example.png" style="max-height:150px; margin:auto">
</div>

<div class="text-xs opacity-70 text-center mt-1">
Actual output from this pipeline's default settings — the photo strip (top) and scatter plot (bottom) it saves after every <code>cargo_evaluate.py</code> run.
</div>

---
layout: center
class: text-center
---

# 🛠 Lab 1 Time

## Estimating Truck Cargo Space with AI

<div class="mt-6 text-lg">
Follow <code>docs/labsheets/cargo_labsheet.pdf</code>
</div>

<div class="mt-8 opacity-70">
Label the photos → split → edit the settings → train → evaluate
</div>

<div class="mt-12 text-sm opacity-60">
I'll circulate to help — flag me down anytime.<br>
When you're done, note your Mean Absolute Error on the scoreboard.
</div>

---
hideInToc: true
---

# Today's Agenda

1.  Why AI for Transportation & Rail
2.  AI/ML Fundamentals Recap
3.  What is NDT & Where AI Fits
4.  Hands-On Lab 1 — Cargo Fill-Level Estimation
5.  **Hands-On Lab 2 — Railway Defect Detection**
6.  Wrap-Up & Your Own Pilot AI Idea

---
layout: section
---

# Part 3
## Hands-On Lab 2
### Detecting Rail Defects with AI

---

# Lab 2: The Big Picture

113 real rail photos from the RSDDs research dataset, each with a hand-drawn
**ground-truth defect map** already provided.

<div class="grid grid-cols-2 gap-4 mt-4">
<div class="text-center">
<img src="/img/rail-sample.jpg" class="rounded shadow" style="max-height:220px; margin:auto">
<div class="text-sm opacity-70 mt-1">Rail surface photo</div>
</div>
<div class="text-center">
<img src="/img/rail-sample-mask.png" class="rounded shadow" style="max-height:220px; margin:auto">
<div class="text-sm opacity-70 mt-1">Hand-drawn defect map (white = defect)</div>
</div>
</div>

<v-clicks>

- No labeling needed this time — the answer key already exists
- **Goal:** train a model that draws its own defect map on a new photo
- This is *segmentation* — exactly the concept from Part 1, applied to
  a real NDT problem

</v-clicks>

---

# Lab 2: How It All Fits Together

<div class="grid grid-cols-5 gap-2 my-3 text-xs">
  <div class="p-3 rounded-lg bg-gray-500/10 border border-gray-500/20 flex flex-col justify-between">
    <div>
      <span class="px-2 py-0.5 rounded text-[9px] font-semibold bg-gray-500/20 text-gray-700 dark:text-gray-300">Done for you</span>
      <div class="font-bold text-xs mt-2">1. Dataset</div>
      <div class="opacity-75 text-[10px] mt-0.5">RSDDs & ground truth</div>
    </div>
    <div class="text-right text-sm opacity-40 mt-1">➔</div>
  </div>

  <div class="p-3 rounded-lg bg-orange-500/15 border-2 border-orange-500/40 shadow-sm flex flex-col justify-between">
    <div>
      <span class="px-2 py-0.5 rounded text-[9px] font-bold bg-orange-500 text-white">YOUR ACTION</span>
      <div class="font-bold text-xs mt-2">2. Edit Config</div>
      <div class="opacity-75 text-[10px] mt-0.5">rail_ndt_config.yaml</div>
    </div>
    <div class="text-right text-sm opacity-40 mt-1">➔</div>
  </div>

  <div class="p-3 rounded-lg bg-gray-500/10 border border-gray-500/20 flex flex-col justify-between">
    <div>
      <span class="px-2 py-0.5 rounded text-[9px] font-semibold bg-gray-500/20 text-gray-700 dark:text-gray-300">Done for you</span>
      <div class="font-bold text-xs mt-2">3. Train Model</div>
      <div class="opacity-75 text-[10px] mt-0.5">rail_train.py</div>
    </div>
    <div class="text-right text-sm opacity-40 mt-1">➔</div>
  </div>

  <div class="p-3 rounded-lg bg-gray-500/10 border border-gray-500/20 flex flex-col justify-between">
    <div>
      <span class="px-2 py-0.5 rounded text-[9px] font-semibold bg-gray-500/20 text-gray-700 dark:text-gray-300">Done for you</span>
      <div class="font-bold text-xs mt-2">4. Evaluate</div>
      <div class="opacity-75 text-[10px] mt-0.5">rail_evaluate.py</div>
    </div>
    <div class="text-right text-sm opacity-40 mt-1">➔</div>
  </div>

  <div class="p-3 rounded-lg bg-blue-500/15 border-2 border-blue-500/40 shadow-sm flex flex-col justify-between">
    <div>
      <span class="px-2 py-0.5 rounded text-[9px] font-bold bg-blue-600 text-white">SCORE</span>
      <div class="font-bold text-xs mt-2">5. Your Score</div>
      <div class="opacity-90 font-medium text-[10px] mt-0.5">Mean IoU Metric</div>
    </div>
    <div class="text-right text-sm opacity-40 mt-1">✓</div>
  </div>
</div>

<div class="grid grid-cols-2 gap-3 my-2 text-xs">
  <div class="p-3 rounded-lg bg-emerald-500/10 border border-emerald-500/30 flex items-start gap-2">
    <div class="text-xl">⚡</div>
    <div>
      <div class="font-bold text-emerald-600 dark:text-emerald-400">Fast Loop (No Retrain)</div>
      <div class="opacity-80 text-[11px] mt-0.5">Tweak threshold in config ➔ re-run <code>rail_evaluate.py</code> (takes seconds)</div>
    </div>
  </div>

  <div class="p-3 rounded-lg bg-purple-500/10 border border-purple-500/30 flex items-start gap-2">
    <div class="text-xl">🔄</div>
    <div>
      <div class="font-bold text-purple-600 dark:text-purple-400">Full Retrain Loop</div>
      <div class="opacity-80 text-[11px] mt-0.5">Change model architecture/settings in config ➔ re-run <code>rail_train.py</code></div>
    </div>
  </div>
</div>

---

# A Real Example of What You'll Produce

<div class="flex justify-center mt-2">
<img src="/img/rail-eval-example-compact.png" style="max-height:340px">
</div>

<div class="text-sm opacity-70 text-center mt-2">
Actual output from this pipeline: true and predicted defect areas overlaid on the rail photo — <strong>yellow</strong> = correctly caught, <strong>green</strong> = missed, <strong>red</strong> = false alarm. See all that red? That's exactly what threshold tuning fixes.
</div>

---

# Lab 2: Compete With Each Other

The main lever needs **no retraining at all** — just the confidence
threshold from Part 1's discussion:

| threshold | Effect |
|---|---|
| Low (e.g. 0.2) | Flags more pixels — more defects caught, more false alarms |
| High (e.g. 0.8) | Flags fewer pixels — fewer false alarms, more missed defects |

<v-click>

Re-run `rail_evaluate.py` after each change, track your best **Mean IoU**
(higher is better) — each check takes only seconds.

</v-click>

---

# Lab 2: Example Run — What to Expect

<div class="text-sm">
Default settings (<code>random_forest</code>, 100 trees, max_depth=8, threshold=0.5):
&nbsp; <strong>Mean IoU: 0.248 · Mean Dice: 0.379</strong>
</div>

<div class="grid grid-cols-2 gap-6 mt-3">
<div class="text-xs leading-tight">

Threshold sweep, same trained model (no retrain):

| threshold | Mean IoU | Mean Dice |
|---|---|---|
| 0.2 | 0.157 | 0.253 |
| 0.3 | 0.187 | 0.294 |
| 0.4 | 0.207 | 0.322 |
| 0.5 (default) | 0.248 | 0.379 |
| 0.6 | 0.299 | 0.443 |
| **0.7–0.8** | **0.33–0.34** | **0.46–0.48** |
| 0.9–0.95 | 0.15–0.25 | 0.23–0.36 |

</div>
<div class="text-xs opacity-80 leading-snug">

- This is a real run on the actual RSDDs data, done as a full dry run of this
  lab before class.
- IoU rises smoothly as threshold increases, **peaks around 0.7–0.8**, then
  drops off — the classic precision/recall trade-off from Part 1.
- Retraining with `logistic_regression` or a bigger forest (300 trees,
  max_depth=15) only moved Mean IoU to ~0.255 — tuning `threshold` mattered
  far more here than model choice.

</div>
</div>

---

# Lab 2: Real Output Example

<div class="text-center">
<img src="/img/rail-eval-example.png" style="max-height:150px; margin:auto">
</div>

<div class="text-center mt-2">
<img src="/img/rail-eval-threshold-curve-example.png" style="max-height:150px; margin:auto">
</div>

<div class="text-xs opacity-70 text-center mt-1">
Actual output from this pipeline — the true/predicted overlay (top) and the
threshold sweep curve (bottom) it saves after every <code>rail_evaluate.py</code> run.
</div>

---
layout: center
class: text-center
---

# 🛠 Lab 2 Time

## Detecting Rail Defects with AI

<div class="mt-6 text-lg">
Follow <code>docs/labsheets/rail_ndt_labsheet.pdf</code>
</div>

<div class="mt-8 opacity-70">
Train → evaluate → tune the threshold → re-evaluate (no retrain needed)
</div>

<div class="mt-12 text-sm opacity-60">
I'll circulate to help — flag me down anytime.<br>
When you're done, note your best Mean IoU on the scoreboard.
</div>

---
hideInToc: true
---

# Today's Agenda

1.  Why AI for Transportation & Rail
2.  AI/ML Fundamentals Recap
3.  What is NDT & Where AI Fits
4.  Hands-On Lab 1 — Cargo Fill-Level Estimation
5.  Hands-On Lab 2 — Railway Defect Detection
6.  **Wrap-Up & Your Own Pilot AI Idea**

---

# Getting Set Up

Both labs share the same one-time setup:

```bash
cd AI-training
python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

<div class="mt-6">

Full step-by-step instructions (PDF or Markdown):

- `docs/labsheets/cargo_labsheet.pdf`
- `docs/labsheets/rail_ndt_labsheet.pdf`

</div>

---

# From Today's Labs to Your Pilot Project

Later in this program, you'll propose an **MVP pilot AI project** for
your own unit. Today's two labs are templates for the two most common
shapes that project could take:

<v-clicks>

- **A regression problem** — predicting a number from data you already
  collect (occupancy, delay minutes, demand, risk score...)
- **A segmentation/detection problem** — finding *where* something is
  in an image (defects, obstructions, congestion, violations...)

</v-clicks>

<v-click>

<div class="mt-4">
Ask yourself: what does <strong>your</strong> agency already photograph,
scan, or measure — that nobody has systematically labeled yet?
</div>

</v-click>

---
layout: center
class: text-center
---

# Questions?

Discuss: why might two people with identical settings still get
different scores?

<div class="opacity-60 mt-4">
docs/labsheets/ · scripts/ · configs/
</div>
