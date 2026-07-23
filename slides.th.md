---
theme: seriph
background: https://cover.sli.dev
title: AI Data Analytics for Transportation Sector (ภาษาไทย)
info: |
  ## AI Data Analytics for Transportation Sector
  โมดูลหนึ่งในหลักสูตร "AI-Driven Transformation in Public Governance"

  คณะวิศวกรรมศาสตร์ มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าพระนครเหนือ (มจพ.)

  24 กรกฎาคม 2569
class: text-center text-white
highlighter: shiki
drawings:
  persist: false
transition: slide-left
mdc: true
fonts:
  sans: Sarabun
  weights: '400,500,600,700'
presenterName: ผศ. ดร. Ruslee Sutthaweekul
program: AI-Driven Transformation in Public Governance
module: AI Data Analytics for Transportation Sector
organizer: คณะวิศวกรรมศาสตร์ มจพ.
cohort: นักเรียนทุนกระทรวงคมนาคม
presentationDate: 24 กรกฎาคม 2569
---

# {{ $slidev.configs.module }}

## {{ $slidev.configs.program }}

บรรยายโดย {{ $slidev.configs.presenterName }}

<div class="pt-8 opacity-70">
{{ $slidev.configs.organizer }} — จัดให้กับ {{ $slidev.configs.cohort }}
</div>

<div class="pt-2 opacity-70">
{{ $slidev.configs.presentationDate }}
</div>

<div @click="$slidev.nav.next" class="mt-12 py-1" hover:bg="white op-10">
  กด Space เพื่อไปหน้าถัดไป <carbon:arrow-right />
</div>

---
hideInToc: true
---

# กำหนดการวันนี้

1.  **ทำไม AI ถึงสำคัญกับงานคมนาคมและรางรถไฟ**
2.  ทบทวนพื้นฐาน AI/ML
3.  NDT คืออะไร และ AI เข้ามาช่วยตรงไหน
4.  ลงมือทำแล็บ 1 — ประเมินระดับความเต็มของสินค้าในตู้บรรทุก
5.  ลงมือทำแล็บ 2 — ตรวจจับข้อบกพร่องของรางรถไฟ
6.  สรุปและไอเดียโครงการนำร่อง AI ของคุณเอง

<div class="text-sm opacity-70 mt-8">
หัวข้อ 1–3 คือการบรรยายของวันนี้ (~60 นาที) หัวข้อ 4–5 คือแล็บลงมือทำจริง ไม่ต้องเขียนโค้ด
</div>

---

# วิทยากรของวันนี้

<div class="grid grid-cols-5 gap-6 mt-2 items-center">
<div class="col-span-3">

### **ผศ. ดร. Ruslee Sutthaweekul**

ภาควิชาวิศวกรรมไฟฟ้าและคอมพิวเตอร์
คณะวิศวกรรมศาสตร์ มจพ.

<div class="mt-4 text-sm">

- **ปริญญาเอก** วิศวกรรมไฟฟ้าและอิเล็กทรอนิกส์ — Newcastle University, สหราชอาณาจักร
- **ปริญญาโท** วิศวกรรมไฟฟ้าและเทคโนโลยีสารสนเทศ — Rosenheim, เยอรมนี
- **ปริญญาตรี** วิศวกรรมไฟฟ้า — มจพ.

</div>

<div class="mt-4 text-sm font-semibold text-blue-600 dark:text-blue-400">
ประสบการณ์ 26 ปี ทั้งด้าน **AI & Machine Learning** และ **วิศวกรรมตรวจสอบรางรถไฟ**
</div>

</div>

<div class="col-span-2 text-center">
  <img src="/img/newcastle-isg-collage.png" class="rounded-xl shadow-lg border border-gray-500/20" style="max-height: 265px; width: 100%; object-fit: contain;">
  <div class="text-[11px] opacity-75 mt-2 font-medium">Intelligent Sensing Group — Newcastle University (พร้อมภาพสถานที่สำคัญของเมือง Newcastle)</div>
</div>
</div>

---

# ประสบการณ์ที่เกี่ยวข้อง

<div class="grid grid-cols-2 gap-6 text-sm">
<div>

### ภาคอุตสาหกรรม

- **Bombardier Transportation** — แผนก Automatic Train Control (ATC)
- **ที่ปรึกษาโครงการ ไปรษณีย์ไทย** — เพิ่มประสิทธิภาพการบริหารจัดการยานพาหนะ (ทุน บพข)

<div class="grid grid-cols-2 gap-3 mt-4 text-center">
  <div>
    <img src="/img/bombardier-atc.png" class="rounded-lg shadow border border-gray-500/20" style="height:145px; width:100%; object-fit:cover;">
    <div class="text-[11px] font-semibold mt-1">Bombardier Transportation</div>
    <div class="text-[10px] opacity-75">Automatic Train Control (ATC)</div>
  </div>
  <div>
    <img src="/img/thailand-post-fleet.png" class="rounded-lg shadow border border-gray-500/20" style="height:145px; width:100%; object-fit:cover;">
    <div class="text-[11px] font-semibold mt-1">ไปรษณีย์ไทย</div>
    <div class="text-[10px] opacity-75">เพิ่มประสิทธิภาพยานพาหนะ (ทุน บพข)</div>
  </div>
</div>

</div>
<div>

### งานวิจัยด้าน NDT และ AI สำหรับรางรถไฟ

- การตรวจสอบรางรถไฟด้วย Eddy Current Testing
- การออกแบบด้วย Digital Twin สำหรับอุตสาหกรรมรางรถไฟ (British Council, สหราชอาณาจักร)
- การซ่อมบำรุงเชิงพยากรณ์สำหรับตู้สินค้าน้ำหนักเบา — โครงการ INNOWAG (Shift2Rail, สหภาพยุโรป)
- การตรวจจับข้อบกพร่องบนผิวรางด้วยโครงข่ายประสาทเทียม และการสร้างแบบจำลอง 3 มิติของรางด้วย Mask R-CNN

<div class="grid grid-cols-2 gap-3 mt-4 text-center">
  <div>
    <img src="/img/uk-railway-digital-twin.png" class="rounded-lg shadow border border-gray-500/20" style="height:145px; width:100%; object-fit:cover;">
    <div class="text-[11px] font-semibold mt-1">UK Railway Digital Twin</div>
    <div class="text-[10px] opacity-75">British Council & Shift2Rail (สหราชอาณาจักร)</div>
  </div>
  <div>
    <img src="/img/ruslee-ndt-field.png" class="rounded-lg shadow border border-gray-500/20" style="height:145px; width:100%; object-fit:cover;">
    <div class="text-[11px] font-semibold mt-1">การตรวจสอบภาคสนามในสหราชอาณาจักร</div>
    <div class="text-[10px] opacity-75">Newcastle University, สหราชอาณาจักร</div>
  </div>
</div>

</div>
</div>

---

# ภาคสนามและงานวิจัยระดับนานาชาติ

<div class="grid grid-cols-4 gap-3 mt-4 text-center">
<div>
  <img src="/img/ruslee-ndt-field.png" class="rounded-lg shadow border border-gray-500/20" style="height:145px; width:100%; object-fit:cover;">
  <div class="text-xs font-bold mt-2">การตรวจสอบ NDT ภาคสนาม</div>
  <div class="text-[11px] opacity-75">การทดสอบแบบไม่ทำลาย (เซนเซอร์ RFID), Barrow Hill, Newcastle, สหราชอาณาจักร</div>
</div>

<div>
  <img src="/img/ruslee-lecture-live.jpg" class="rounded-lg shadow border border-gray-500/20" style="height:145px; width:100%; object-fit:cover;">
  <div class="text-xs font-bold mt-2">การอบรมด้านรางรถไฟ</div>
  <div class="text-[11px] opacity-75">บรรยายระบบอาณัติสัญญาณรถไฟและ summer school ที่ Southwest JiaoTong University, เมืองเฉิงตู ประเทศจีน</div>
</div>

<div>
  <img src="/img/ruslee-ieee-award.jpg" class="rounded-lg shadow border border-gray-500/20" style="height:145px; width:100%; object-fit:cover;">
  <div class="text-xs font-bold mt-2">รางวัล IEEE Sensors</div>
  <div class="text-[11px] opacity-75">รางวัลรองชนะเลิศอันดับ 1 การประกวดระดับนักศึกษา เมือง Glasgow สหราชอาณาจักร</div>
  <a href="https://www.youtube.com/watch?v=e2A9Jfn78JU" target="_blank" class="text-[10px] text-blue-600 dark:text-blue-400 hover:underline">▶ ชมวิดีโอ: Sounnatic 1.0</a>
</div>

<div>
  <img src="/img/railway-digital-twin-workshop.jpg" class="rounded-lg shadow border border-gray-500/20" style="height:145px; width:100%; object-fit:cover;">
  <div class="text-xs font-bold mt-2">Workshop Digital Twin</div>
  <div class="text-[11px] opacity-75">Workshop รางรถไฟนานาชาติ ร่วมกับ British Council กรุงเทพฯ ประเทศไทย</div>
</div>
</div>

<div class="grid grid-cols-2 gap-3 mt-3 text-center">
<div>
  <img src="/img/ruslee-ect-rail-setup.jpg" class="rounded-lg shadow border border-gray-500/20" style="height:130px; width:100%; object-fit:cover;">
  <div class="text-xs font-bold mt-2">ชุดทดสอบ Eddy Current</div>
  <div class="text-[11px] opacity-75">ชิ้นทดสอบรางที่ฝังข้อบกพร่องไว้ พร้อมระบบสแกนหัวโพรบอัตโนมัติและบันทึกผลด้วยออสซิลโลสโคป</div>
</div>

<div>
  <img src="/img/ruslee-rail-3d-reconstruction.jpg" class="rounded-lg shadow border border-gray-500/20" style="height:130px; margin:auto; object-fit:contain;">
  <div class="text-xs font-bold mt-2">การสร้างแบบจำลอง 3 มิติของข้อบกพร่องราง</div>
  <div class="text-[11px] opacity-75">ผิวหัวรางที่สร้างขึ้นใหม่เทียบกับค่าอ้างอิงจริงใน 4 ตำแหน่งข้อบกพร่องที่ฝังไว้</div>
</div>
</div>

---
layout: section
---

# ตอนที่ 1
## พื้นฐาน NDT และ AI

---
layout: two-cols-header
---

# ตำแหน่งของคุณในหลักสูตรนี้

::left::

### ที่ผ่านมาแล้ว (วันที่ 1–5)

- แนะนำ AI: ในชีวิตประจำวันและงานคมนาคม
- AI เรียนรู้ได้อย่างไร: พื้นฐานแมชชีนเลิร์นนิง
- การบริหารจัดการข้อมูลเพื่อ AI ที่ชาญฉลาด
- AI เพื่อการสื่อสาร: แชทบอทและผู้ช่วยเสียง
- การคิดไอเดียโครงการ AI สำหรับงานคมนาคม

::right::

### วันนี้ (วันที่ 6–8)

- เจาะลึก**หนึ่งสาขา**: โครงสร้างพื้นฐานด้านคมนาคมและรางรถไฟ
- กรณีศึกษาจริงแบบลงมือทำ 2 เรื่อง
- ก้าวสู่**ไอเดียโครงการ AI นำร่องของคุณเอง** สำหรับหน่วยงานของคุณ

<div class="mt-4">
  <img src="/img/deep-engineering-ai.png" class="rounded-xl shadow-lg border border-gray-500/20" style="height: 180px; width: 100%; object-fit: cover;">
  <div class="text-[11px] opacity-75 mt-1.5 text-center font-medium">งานวิจัยเชิงลึกด้าน AI & ML สำหรับโครงสร้างพื้นฐานคมนาคม</div>
</div>

---

# พื้นฐานการซ่อมบำรุงระบบคมนาคม

<div class="grid grid-cols-2 gap-6 items-center">
<div>

### วิวัฒนาการของแนวทางการซ่อมบำรุง

<div class="text-xs space-y-3 mt-2">

- **1. การซ่อมบำรุงเชิงรับ (ใช้จนเสียแล้วซ่อม)**
  ซ่อม*หลังจาก*เกิดความเสียหายแล้ว — เวลาหยุดทำงานสูง ค่าใช้จ่ายฉุกเฉิน และความเสี่ยงด้านความปลอดภัย
- **2. การซ่อมบำรุงเชิงป้องกัน (ตามระยะเวลา/ระยะทาง)**
  บำรุงรักษาตามรอบเวลาที่กำหนด — อาจเปลี่ยนชิ้นส่วนเร็วเกินจำเป็น หรือพลาดข้อบกพร่องระยะแรกที่ยังตรวจไม่พบ
- **3. การซ่อมบำรุงตามสภาพ (CBM) และ NDT**
  ประเมินสภาพภายในและโครงสร้าง**โดยไม่ทำลายทรัพย์สิน** ด้วยการทดสอบแบบไม่ทำลาย (NDT)
- **4. การซ่อมบำรุงเชิงพยากรณ์ด้วย AI (PdM)**
  ผสานข้อมูล NDT แบบต่อเนื่องเข้ากับ **การพยากรณ์ด้วย AI/ML** เพื่อคาดการณ์ความเสียหายก่อนเกิดขึ้นจริง

</div>

<div class="mt-4 p-3 bg-blue-500/10 rounded-lg border border-blue-500/30 text-xs">
💡 <strong>สะพานเชื่อมสู่ NDT:</strong> NDT คือแหล่งข้อมูลเซนเซอร์ความละเอียดสูงที่จำเป็น ในการก้าวจากตารางซ่อมบำรุงตายตัวไปสู่การพยากรณ์อัจฉริยะด้วย AI
</div>

</div>

<div class="text-center">
  <img src="/img/maintenance-evolution.png" class="rounded-xl shadow-lg border border-gray-500/20" style="max-height: 330px; width: 100%; object-fit: contain;">
  <div class="text-[11px] opacity-70 mt-2">4 ยุคของการซ่อมบำรุงทรัพย์สินด้านคมนาคม</div>
</div>
</div>

---

# ทำไมรางรถไฟจึงต้องการ NDT โดยเฉพาะ

<div class="grid grid-cols-4 gap-3 my-3">
<div class="text-center">
  <img src="/img/defect-head-checks.png" class="rounded shadow" style="height:120px; width:100%; object-fit:cover;">
  <div class="text-xs font-bold mt-1.5">Head Checks / RCF</div>
  <div class="text-[11px] opacity-75">รอยแตกร้าวขนาดเล็กบนผิวราง</div>
</div>
<div class="text-center">
  <img src="/img/defect-spalling.png" class="rounded shadow" style="height:120px; width:100%; object-fit:cover;">
  <div class="text-xs font-bold mt-1.5">Spalling / Squats</div>
  <div class="text-[11px] opacity-75">ผิวเป็นหลุมและเนื้อโลหะหลุดล่อน</div>
</div>
<div class="text-center">
  <img src="/img/defect-corrugation.png" class="rounded shadow" style="height:120px; width:100%; object-fit:cover;">
  <div class="text-xs font-bold mt-1.5">Corrugation (รางลูกคลื่น)</div>
  <div class="text-[11px] opacity-75">การสึกหรอเป็นคลื่นซ้ำ ๆ</div>
</div>
<div class="text-center">
  <img src="/img/defect-break.png" class="rounded shadow" style="height:120px; width:100%; object-fit:cover;">
  <div class="text-xs font-bold mt-1.5">รางหัก</div>
  <div class="text-[11px] opacity-75">การแตกหักตามขวางขั้นรุนแรง</div>
</div>
</div>

<v-clicks>

- ข้อบกพร่องบนผิว เช่น **head checks** และ **spalling** สามารถลุกลามเข้าสู่ภายในจนกลายเป็น**รางหัก**ขั้นร้ายแรงได้
- การรับน้ำหนักจากขบวนรถอย่างต่อเนื่อง ทำให้ข้อบกพร่องของรางสะสมตัวตลอดเวลา — การตรวจสอบจึงเป็น**กระบวนการต่อเนื่อง**

</v-clicks>

---

# Non-Destructive Testing (NDT) คืออะไร?

**นิยาม:** การตรวจสอบหรือประเมินสภาพของวัสดุ ชิ้นส่วน หรือโครงสร้าง
**โดยไม่ทำให้เสียหายหรือต้องถอดออกจากการใช้งาน**

<v-click>

**เปรียบเทียบกับการทดสอบแบบทำลาย** — เช่น การดึงชิ้นตัวอย่างจนขาดเพื่อหาค่าความแข็งแรง
วิธีนี้บอกข้อมูลได้แค่*ชิ้นตัวอย่างชิ้นเดียว* และทำลายมันไปด้วย แน่นอนว่าคุณไม่สามารถทดสอบ
รางรถไฟทั้งเครือข่าย 100% ด้วยวิธีนี้ได้

</v-click>

<v-click>

NDT ทำให้คุณตรวจสอบ**ทรัพย์สินจริงที่กำลังใช้งานอยู่**ซ้ำ ๆ ได้ตลอดอายุการใช้งานทั้งหมด

</v-click>

---

# วิธี NDT ที่ใช้กันทั่วไป

<div class="grid grid-cols-3 gap-3 my-2 text-xs">
<div class="rounded-lg p-2.5 bg-gray-500/10 border border-gray-500/20 shadow-sm flex flex-col">
  <img src="/img/ndt-visual.png" class="rounded h-24 w-full object-cover mb-2">
  <div class="font-bold text-sm text-blue-600 dark:text-blue-400">Visual (VT) — การตรวจด้วยสายตา</div>
  <div class="opacity-90 font-medium mt-0.5">กล้อง / การตรวจสอบด้วยแสง</div>
  <div class="opacity-70 text-[11px] mt-1">ด่านแรกของการตรวจสอบ — ระบบอัตโนมัติในแล็บ 2</div>
</div>

<div class="rounded-lg p-2.5 bg-gray-500/10 border border-gray-500/20 shadow-sm flex flex-col">
  <img src="/img/ndt-ultrasonic.png" class="rounded h-24 w-full object-cover mb-2">
  <div class="font-bold text-sm text-amber-600 dark:text-amber-400">Ultrasonic (UT) — คลื่นเสียงความถี่สูง</div>
  <div class="opacity-90 font-medium mt-0.5">คลื่นเสียงความถี่สูง</div>
  <div class="opacity-70 text-[11px] mt-1">รอยแตกภายในและข้อบกพร่องภายในราง</div>
</div>

<div class="rounded-lg p-2.5 bg-gray-500/10 border border-gray-500/20 shadow-sm flex flex-col">
  <img src="/img/ndt-magnetic-particle.png" class="rounded h-24 w-full object-cover mb-2">
  <div class="font-bold text-sm text-emerald-600 dark:text-emerald-400">Magnetic Particle (MPI) — อนุภาคแม่เหล็ก</div>
  <div class="opacity-90 font-medium mt-0.5">สนามแม่เหล็ก + ผงเหล็ก</div>
  <div class="opacity-70 text-[11px] mt-1">รอยแตกบนผิวและใกล้ผิวของวัสดุเฟอร์โรแมกเนติก</div>
</div>

<div class="rounded-lg p-2.5 bg-gray-500/10 border border-gray-500/20 shadow-sm flex flex-col">
  <img src="/img/ndt-eddy-current.png" class="rounded h-24 w-full object-cover mb-2">
  <div class="font-bold text-sm text-purple-600 dark:text-purple-400">Eddy Current (ECT) — กระแสไหลวน</div>
  <div class="opacity-90 font-medium mt-0.5">สนามแม่เหล็กไฟฟ้าเหนี่ยวนำ</div>
  <div class="opacity-70 text-[11px] mt-1">รอยแตกขนาดเล็กที่ผิวตื้นและ head checks</div>
</div>

<div class="rounded-lg p-2.5 bg-gray-500/10 border border-gray-500/20 shadow-sm flex flex-col">
  <img src="/img/ndt-radiography.png" class="rounded h-24 w-full object-cover mb-2">
  <div class="font-bold text-sm text-red-600 dark:text-red-400">Radiographic (RT) — ภาพถ่ายรังสี</div>
  <div class="opacity-90 font-medium mt-0.5">รังสีเอกซ์ / รังสีแกมมาทางอุตสาหกรรม</div>
  <div class="opacity-70 text-[11px] mt-1">รูพรุนในรอยเชื่อมภายในและโครงสร้างงานหล่อ</div>
</div>

<div class="rounded-lg p-2.5 bg-gray-500/10 border border-gray-500/20 shadow-sm flex flex-col">
  <img src="/img/ndt-thermography.png" class="rounded h-24 w-full object-cover mb-2">
  <div class="font-bold text-sm text-cyan-600 dark:text-cyan-400">Thermography (IRT) — ภาพถ่ายความร้อน</div>
  <div class="opacity-90 font-medium mt-0.5">การทำแผนที่รังสีความร้อนอินฟราเรด</div>
  <div class="opacity-70 text-[11px] mt-1">ความผิดปกติทางความร้อนและจุดที่เกิดแรงเสียดทานสูง</div>
</div>
</div>

---

# การตรวจสอบรางแบบดั้งเดิม: จุดคอขวด

<div class="grid grid-cols-5 gap-6 mt-4 items-center">
<div class="col-span-3">

<v-clicks>

- **การตรวจสอบเดินเท้าด้วยคน** — ละเอียด แต่ช้า มีความคลาดเคลื่อนตามดุลยพินิจ เหนื่อยล้าได้ง่าย และขึ้นกับสภาพอากาศ/ความร้อน
- **รถไฟตรวจสอบเฉพาะทาง** — รวดเร็วและเป็นกลาง แต่ราคาแพงและมีจำกัดทั้งด้านความพร้อมใช้งานและตารางเวลา
- **ช่องว่างด้านการครอบคลุมพื้นที่** — รางยาวนับพันกิโลเมตร เทียบกับชั่วโมงทำงานของผู้ตรวจสอบและยานพาหนะที่มีจำกัด

</v-clicks>

</div>

<div class="col-span-2 text-center">
  <img src="/img/manual-walking-inspector.png" class="rounded-xl shadow-lg border border-gray-500/20" style="max-height: 240px; width: 100%; object-fit: cover;">
  <div class="text-[11px] opacity-70 mt-2">การตรวจสอบรางด้วยการเดินเท้าท่ามกลางสภาพอากาศเลวร้าย</div>
</div>
</div>

---
layout: center
class: text-center
---

# จาก NDT สู่พื้นฐาน AI

เราได้เรียนรู้แล้วว่า NDT คืออะไร เหตุใดรางรถไฟจึงต้องการ และการตรวจสอบแบบดั้งเดิมมีข้อจำกัด
ตรงไหน ต่อไปนี้คือแนวคิด AI ที่แล็บของวันนี้ถูกสร้างขึ้นบนพื้นฐานนี้

---

# ทบทวน AI/ML: Supervised Learning ในภาพเดียว

<div class="flex items-center justify-center gap-4 my-8 px-4">
  <div class="flex-1 max-w-xs p-5 rounded-2xl bg-blue-500/10 border-2 border-blue-500/30 shadow-lg text-center">
    <div class="text-4xl mb-2">🖼️</div>
    <div class="font-bold text-lg">ข้อมูลนำเข้า</div>
    <div class="text-sm opacity-80 mt-1">ภาพถ่าย / ข้อมูลเซนเซอร์</div>
  </div>

  <div class="text-3xl opacity-60 flex-shrink-0">➔</div>

  <div class="flex-1 max-w-xs p-5 rounded-2xl bg-amber-500/10 border-2 border-amber-500/30 shadow-lg text-center">
    <div class="text-4xl mb-2">🧠</div>
    <div class="font-bold text-lg">โมเดล</div>
    <div class="text-sm opacity-80 mt-1">รูปแบบที่เรียนรู้แล้ว</div>
  </div>

  <div class="text-3xl opacity-60 flex-shrink-0">➔</div>

  <div class="flex-1 max-w-xs p-5 rounded-2xl bg-emerald-500/10 border-2 border-emerald-500/30 shadow-lg text-center">
    <div class="text-4xl mb-2">🎯</div>
    <div class="font-bold text-lg">ผลลัพธ์</div>
    <div class="text-sm opacity-80 mt-1">คำทาย / คำตอบ</div>
  </div>
</div>

<v-click>

โมเดลไม่รู้คำตอบตั้งแต่วันแรก — มัน**เรียนรู้จากตัวอย่างที่ติดป้ายกำกับ** ป้อนภาพที่ติดป้ายกำกับ
ถูกต้องให้มากพอ มันก็จะเรียนรู้รูปแบบได้ดีพอที่จะทายภาพ*ใหม่*ที่ไม่เคยเห็นมาก่อนได้

แล็บทั้งสองของวันนี้คือตัวอย่างของสิ่งนี้โดยตรง: **supervised learning (การเรียนรู้แบบมีผู้สอน)**

</v-click>

---
layout: two-cols-header
---

# ผลลัพธ์ AI สองรูปแบบที่คุณจะได้เห็นวันนี้

<div class="text-xs opacity-75 mb-3 -mt-1">
ทำความเข้าใจว่าโมเดลแมชชีนเลิร์นนิงแก้ปัญหาทางวิศวกรรมด้านคมนาคมที่แตกต่างกันอย่างไร
</div>

::left::

<div class="flex flex-col justify-between bg-gradient-to-b from-blue-950/40 via-slate-900/60 to-slate-950/80 border border-blue-500/30 rounded-2xl p-4 shadow-xl relative overflow-hidden group hover:border-blue-400/60 transition-all duration-300">
  <div class="absolute -top-10 -right-10 w-24 h-24 bg-blue-500/10 rounded-full blur-xl pointer-events-none"></div>

  <div>
    <div class="flex items-center justify-between mb-2">
      <span class="text-[11px] font-bold uppercase tracking-wider text-blue-400 bg-blue-500/15 px-2.5 py-0.5 rounded-full border border-blue-500/30">
        รูปแบบที่ 1 — Regression
      </span>
      <span class="text-[10px] opacity-60 font-mono">ค่าต่อเนื่อง</span>
    </div>
    <h3 class="text-base font-bold text-white mb-1">
      ผลลัพธ์ = <span class="text-blue-400 underline decoration-blue-500/40 underline-offset-4">ตัวเลขค่าต่อเนื่อง</span>
    </h3>
    <p class="text-[11px] opacity-70 mb-3">ทายค่าวัดเชิงปริมาณค่าเดียว เช่น เปอร์เซ็นต์ น้ำหนัก หรือความเร็ว</p>
    <!-- Visual Flow -->
    <div class="flex items-center justify-between bg-slate-950/80 rounded-xl p-3 border border-white/5 my-2">
      <div class="text-center">
        <img src="/img/cargo-front-later.jpg" class="h-20 w-24 object-cover rounded-lg shadow-md border border-white/10 group-hover:scale-105 transition-transform duration-300">
        <div class="text-[10px] opacity-60 mt-1">ภาพนำเข้า</div>
      </div>
      <div class="flex flex-col items-center justify-center px-1">
        <carbon:arrow-right class="text-xl text-blue-400" />
        <span class="text-[9px] text-blue-300/80 font-mono mt-0.5">โมเดล CNN</span>
      </div>
      <div class="text-center flex flex-col items-center justify-center">
        <div class="bg-gradient-to-br from-blue-600 to-indigo-700 text-white font-extrabold text-2xl px-3 py-1.5 rounded-xl shadow-lg shadow-blue-500/20 border border-blue-400/40">
          72%
        </div>
        <div class="text-[10px] font-medium text-blue-300 mt-1">ระดับความเต็มของสินค้า</div>
      </div>
    </div>
  </div>

  <div class="mt-3 pt-2.5 border-t border-white/5 flex items-center justify-between text-xs">
    <span class="font-semibold text-blue-300 text-[11px]">บริบทแล็บ 1:</span>
    <span class="text-[10px] opacity-90 bg-blue-950 px-2 py-0.5 rounded border border-blue-800/60 text-blue-200">ประเมินปริมาตรสินค้า</span>
  </div>
</div>

::right::

<div class="flex flex-col justify-between bg-gradient-to-b from-emerald-950/40 via-slate-900/60 to-slate-950/80 border border-emerald-500/30 rounded-2xl p-4 shadow-xl relative overflow-hidden group hover:border-emerald-400/60 transition-all duration-300">
  <div class="absolute -top-10 -right-10 w-24 h-24 bg-emerald-500/10 rounded-full blur-xl pointer-events-none"></div>

  <div>
    <div class="flex items-center justify-between mb-2">
      <span class="text-[11px] font-bold uppercase tracking-wider text-emerald-400 bg-emerald-500/15 px-2.5 py-0.5 rounded-full border border-emerald-500/30">
        รูปแบบที่ 2 — Segmentation
      </span>
      <span class="text-[10px] opacity-60 font-mono">Mask ระดับพิกเซล</span>
    </div>
    <h3 class="text-base font-bold text-white mb-1">
      ผลลัพธ์ = <span class="text-emerald-400 underline decoration-emerald-500/40 underline-offset-4">แผนที่ข้อบกพร่องระดับพิกเซล</span>
    </h3>
    <p class="text-[11px] opacity-70 mb-3">จำแนกทุกพิกเซลเพื่อระบุขอบเขตและตำแหน่งข้อบกพร่องอย่างแม่นยำ</p>
    <!-- Visual Flow -->
    <div class="flex items-center justify-between bg-slate-950/80 rounded-xl p-3 border border-white/5 my-2">
      <div class="text-center">
        <img src="/img/rail-sample.jpg" class="h-20 w-24 object-cover rounded-lg shadow-md border border-white/10 group-hover:scale-105 transition-transform duration-300">
        <div class="text-[10px] opacity-60 mt-1">ภาพรางถ่ายดิบ</div>
      </div>
      <div class="flex flex-col items-center justify-center px-1">
        <carbon:arrow-right class="text-xl text-emerald-400" />
        <span class="text-[9px] text-emerald-300/80 font-mono mt-0.5">โมเดล U-Net</span>
      </div>
      <div class="text-center">
        <img src="/img/rail-sample-mask.png" class="h-20 w-24 object-cover rounded-lg shadow-md border border-emerald-500/40 group-hover:scale-105 transition-transform duration-300">
        <div class="text-[10px] font-medium text-emerald-300 mt-1">แผนที่ Mask ข้อบกพร่อง</div>
      </div>
    </div>
  </div>

  <div class="mt-3 pt-2.5 border-t border-white/5 flex items-center justify-between text-xs">
    <span class="font-semibold text-emerald-300 text-[11px]">บริบทแล็บ 2:</span>
    <span class="text-[10px] opacity-90 bg-emerald-950 px-2 py-0.5 rounded border border-emerald-800/60 text-emerald-200">แบ่งส่วนข้อบกพร่องของราง</span>
  </div>
</div>

---

# การแบ่งชุดข้อมูล Train / Validation / Test

<div class="grid grid-cols-2 gap-6 items-center">
<div>

<h3 class="text-sm font-semibold text-blue-400 mb-2">ทำไมต้องกันข้อมูลไว้ไม่ให้โมเดลเห็น?</h3>

<p class="text-xs opacity-80 leading-relaxed mb-3">
การทดสอบโมเดลด้วยข้อมูลชุดฝึกเดิมจะทำให้เกิด<strong>การจดจำ (overfitting)</strong> เพื่อให้แน่ใจ
ว่าน่าเชื่อถือในโลกจริง ชุดข้อมูลทุกชุดจะถูกแบ่งออกเป็น 3 ส่วน:
</p>

<div class="space-y-2.5 text-xs">
  <div class="p-2.5 bg-blue-950/40 border border-blue-500/30 rounded-xl flex items-start gap-2.5">
    <div class="bg-blue-500/20 text-blue-300 font-bold px-2 py-0.5 rounded text-[11px] mt-0.5">70%</div>
    <div>
      <div class="font-bold text-blue-300">1. ชุด Train (ฝึก)</div>
      <div class="text-[11px] opacity-75">ใช้โดยโมเดลในการปรับค่าน้ำหนักและเรียนรู้รูปแบบพื้นฐานของฟีเจอร์</div>
    </div>
  </div>

  <div class="p-2.5 bg-purple-950/40 border border-purple-500/30 rounded-xl flex items-start gap-2.5">
    <div class="bg-purple-500/20 text-purple-300 font-bold px-2 py-0.5 rounded text-[11px] mt-0.5">15%</div>
    <div>
      <div class="font-bold text-purple-300">2. ชุด Validation (ตรวจสอบ)</div>
      <div class="text-[11px] opacity-75">ใช้ระหว่างการฝึกเพื่อปรับ hyperparameter และป้องกัน overfitting</div>
    </div>
  </div>

  <div class="p-2.5 bg-emerald-950/40 border border-emerald-500/30 rounded-xl flex items-start gap-2.5">
    <div class="bg-emerald-500/20 text-emerald-300 font-bold px-2 py-0.5 rounded text-[11px] mt-0.5">15%</div>
    <div>
      <div class="font-bold text-emerald-300">3. ชุด Test (ทดสอบ, ปิดผนึกไว้)</div>
      <div class="text-[11px] opacity-75">กันไว้ทั้งหมดจนถึงขั้นตอนสุดท้าย เพื่อให้ได้คะแนนความแม่นยำที่ตรงไปตรงมาและเป็นทางการ</div>
    </div>
  </div>
</div>

<div class="mt-3 p-2.5 bg-amber-500/10 rounded-lg border border-amber-500/30 text-[11px] flex items-center gap-2">
  <span>💡</span>
  <span><strong>หมายเหตุแล็บ:</strong> สคริปต์ในแล็บวันนี้แบ่งข้อมูล 3 ส่วนนี้ให้โดยอัตโนมัติ!</span>
</div>

</div>

<div class="text-center">
  <img src="/img/dataset-split-diagram.png" class="rounded-2xl shadow-2xl border border-gray-500/30" style="max-height: 370px; width: 100%; object-fit: contain;">
  <div class="text-[11px] opacity-70 mt-2 font-medium">โครงสร้างการแบ่งชุดข้อมูลสำหรับแมชชีนเลิร์นนิง</div>
</div>
</div>

---

# Hyperparameter: สิ่งที่ตัว**คุณ**ควบคุมได้

ทุกโมเดลมีตัวเลขอยู่ภายในสองประเภท:

<v-clicks>

- **เรียนรู้เองโดยอัตโนมัติ** — ปรับค่าระหว่างการฝึก คุณไม่ต้องแตะต้องโดยตรง
- **Hyperparameter** — เลือกโดย*คุณ*ก่อนเริ่มการฝึกด้วยซ้ำ (เช่น จำนวนต้นไม้ตัดสินใจ
  หรือค่าเกณฑ์ความมั่นใจที่จะใช้)

</v-clicks>

<v-click>

แล็บวันนี้เป็นแบบ "ไม่ต้องเขียนโค้ด" ก็เพราะเราแยก hyperparameter ออกมาไว้ในไฟล์ตั้งค่าแบบ
ข้อความล้วนที่คุณแก้ไขได้ ส่วนที่เหลือทั้งหมดถูกเขียนไว้ให้แล้ว

</v-click>

---

# เรารู้ได้อย่างไรว่าโมเดลดีหรือไม่?

## สองแบบวัดผลที่คุณจะใช้วันนี้

| แล็บ | งาน | ตัวชี้วัด | คะแนนที่ดีมีลักษณะอย่างไร |
|---|---|---|---|
| **แล็บ 1: Cargo** | Regression | MAE (Mean Absolute Error) | **ต่ำ** — ใกล้ 0 |
| **แล็บ 2: Rail** | Segmentation | IoU / Dice | **สูง** — ใกล้ 1 |

<div class="text-sm opacity-70 mt-4">
งานที่ต่างกันต้องการแบบวัดผลที่ต่างกัน — ไม่มีตัวเลข "ความแม่นยำ" สากลตัวเดียวที่ใช้ได้กับทั้งสองงาน
</div>

---

# Garbage In, Garbage Out (ข้อมูลแย่ ผลลัพธ์ก็แย่)

โมเดลจะดีได้มากที่สุดเท่ากับป้ายกำกับที่มันเรียนรู้จากเท่านั้น

<div class="grid grid-cols-5 gap-6 mt-4 items-center">
<div class="col-span-3">

<v-click>

ใน **แล็บ 1** *คุณ*คือแหล่งที่มาของป้ายกำกับ — ไม่มี "เฉลยที่ถูกต้อง" อัตโนมัติ คุณเป็นผู้ตัดสิน
ด้วยสายตาว่ารถบรรทุกแต่ละคันดูเต็มแค่ไหน

</v-click>

<v-click>

<div class="mt-4">
สิ่งนี้สะท้อนประเด็นสำคัญในโครงการ AI ภาครัฐ: <strong>ข้อมูลของหน่วยงานคุณน่าเชื่อถือพอที่จะสร้าง
AI ได้หรือไม่?</strong> บ่อยครั้งงานที่ยากและมีคุณค่าที่สุดคือคุณภาพของข้อมูล ไม่ใช่ตัวโมเดล
</div>

</v-click>

</div>

<div class="col-span-2 text-center">
  <img src="/img/data-labeling-workstation.png" class="rounded-xl shadow-lg border border-gray-500/20" style="max-height: 240px; width: 100%; object-fit: cover;">
  <div class="text-[11px] opacity-70 mt-2">การติดป้ายกำกับและตรวจสอบข้อมูลโดยมีมนุษย์ร่วมในกระบวนการ (human-in-the-loop)</div>
</div>
</div>

---

# ปัญหาความไม่สมดุลของคลาส (Class Imbalance)

ในภาพข้อบกพร่องของราง อาจมีเพียง **2%** ของพิกเซลเท่านั้นที่เป็นข้อบกพร่องจริง —
อีก 98% ที่เหลือคือพื้นผิวรางปกติ

<v-click>

โมเดลที่ขี้เกียจอาจตอบว่า *"ไม่มีข้อบกพร่องเลย"* แล้วยังได้ความ "แม่นยำ" ถึง 98%

</v-click>

<v-click>

นี่คือเหตุผลที่ **แล็บ 2 ใช้ IoU แทนความแม่นยำ (accuracy)** — และเหตุผลที่โมเดลต้องถูกออกแบบมา
โดยเฉพาะเพื่อไม่ให้ติดกับดักนี้ ระวังกับดักแบบเดียวกันนี้ในข้อมูลของหน่วยงานคุณเอง: เหตุการณ์ที่
พบได้น้อย (การทุจริต, ความล้มเหลว, อุบัติเหตุ) มักเป็นสัดส่วนเล็กน้อยมากของข้อมูลทั้งหมดเสมอ

</v-click>

---

# ทำไมงานคมนาคมและรางรถไฟจึงต้องการ AI

เครือข่ายคมนาคมของไทยมีขนาดใหญ่ อายุการใช้งานนาน และเกี่ยวข้องกับความปลอดภัยโดยตรง —
จุดที่ AI สร้างคุณค่าได้มากที่สุดพอดี

<div class="grid grid-cols-5 gap-6 mt-4 items-center">
<div class="col-span-3 text-base">

<v-clicks>

- **ช่องว่างด้านการครอบคลุม**: ระยะทางรางที่ต้องตรวจมีมากกว่าชั่วโมงทำงานของผู้ตรวจสอบที่มีอยู่มาก
- **ความผิดปกติที่พบได้น้อย**: ข้อบกพร่องเป็นเหตุการณ์ที่หายากซ่อนอยู่ในข้อมูลปกติจำนวนมหาศาล — เหมาะกับ AI อย่างยิ่ง
- **ความสม่ำเสมอ**: การตัดสินใจที่ทำซ้ำได้ เทียบกับความเหนื่อยล้าและความคลาดเคลื่อนตามดุลยพินิจของมนุษย์
- **มนุษย์ร่วมในกระบวนการ**: ปลดปล่อยเจ้าหน้าที่ผู้เชี่ยวชาญให้ไปทำการตัดสินใจสำคัญที่ AI ทำแทนไม่ได้

</v-clicks>

</div>

<div class="col-span-2 text-center">
  <img src="/img/rail-inspection-train.png" class="rounded-xl shadow-lg border border-gray-500/20" style="max-height: 240px; width: 100%; object-fit: cover;">
  <div class="text-[11px] opacity-70 mt-2">รถสแกนตรวจสอบรางความเร็วสูงแบบอัตโนมัติ</div>
</div>
</div>

---

# AI เข้ามาอยู่ตรงไหนในกระบวนการ NDT

AI ไม่ได้มาแทนที่ผู้ตรวจสอบที่ได้รับการรับรอง — แต่**เสริมประสิทธิภาพ**ให้พวกเขา

<div class="flex items-center justify-between gap-2 my-6">
  <div class="flex-1 p-4 rounded-xl bg-blue-500/10 border-2 border-blue-500/30 shadow text-center">
    <div class="text-3xl mb-1">📷</div>
    <div class="font-bold text-base">กล้อง / เซนเซอร์</div>
    <div class="text-xs opacity-75 mt-1">เก็บข้อมูลอัตโนมัติ</div>
  </div>

  <div class="text-2xl opacity-60 flex-shrink-0">➔</div>

  <div class="flex-1 p-4 rounded-xl bg-amber-500/10 border-2 border-amber-500/30 shadow text-center">
    <div class="text-3xl mb-1">🤖</div>
    <div class="font-bold text-base">AI คัดกรอง</div>
    <div class="text-xs opacity-75 mt-1">ทำเครื่องหมายข้อบกพร่องที่น่าสงสัย</div>
  </div>

  <div class="text-2xl opacity-60 flex-shrink-0">➔</div>

  <div class="flex-1 p-4 rounded-xl bg-emerald-500/10 border-2 border-emerald-500/30 shadow text-center">
    <div class="text-3xl mb-1">🔍</div>
    <div class="font-bold text-base">ผู้ตรวจสอบ (มนุษย์)</div>
    <div class="text-xs opacity-75 mt-1">ตรวจยืนยันและจัดลำดับความสำคัญ</div>
  </div>

  <div class="text-2xl opacity-60 flex-shrink-0">➔</div>

  <div class="flex-1 p-4 rounded-xl bg-purple-500/10 border-2 border-purple-500/30 shadow text-center">
    <div class="text-3xl mb-1">🛠️</div>
    <div class="font-bold text-base">การตัดสินใจ</div>
    <div class="text-xs opacity-75 mt-1">ดำเนินการซ่อมบำรุง</div>
  </div>
</div>

<v-click>

<div class="mt-4">

**สิ่งที่ AI ทำได้ดี:** สแกนภาพจำนวนมหาศาลอย่างไม่รู้จักเหนื่อย ด้วยความสม่ำเสมอ
ทำเครื่องหมายรูปแบบเดิมได้ทุกครั้ง

**สิ่งที่ยังต้องเป็นหน้าที่มนุษย์:** การตัดสินใจขั้นสุดท้าย บริบทเชิงปฏิบัติการ
และการอนุมัติในประเด็นที่เกี่ยวกับความปลอดภัย

</div>

</v-click>

---

# กรณีศึกษาสองเรื่องของวันนี้

|  | แล็บ 1: Cargo | แล็บ 2: Rail |
|---|---|---|
| **สาขา** | โลจิสติกส์ / คมนาคม | NDT / โครงสร้างพื้นฐานรางรถไฟ |
| **งาน AI** | Regression | Segmentation |
| **ตัวชี้วัด** | MAE (ยิ่งน้อยยิ่งดี) | IoU (ยิ่งสูงยิ่งดี) |
| **สิ่งที่คุณทำ** | ติดป้ายกำกับข้อมูล | ปรับค่าเกณฑ์ |

---
layout: default
---

# สรุปตอนที่ 1

<div class="text-sm">

- **Supervised learning** — โมเดลเรียนรู้จากตัวอย่างที่ติดป้ายกำกับ ไม่ใช่กฎที่เขียนไว้ตายตัว
- **Regression เทียบกับ Segmentation** — การทายตัวเลขหนึ่งค่า เทียบกับการทายแผนที่ระดับพิกเซล
- **การแบ่งชุด Train / Validation / Test** — เหตุใดข้อมูลที่กันไว้จึงทำให้คะแนนน่าเชื่อถือ
- **Hyperparameter** — ค่าตั้งค่าที่คุณเลือกเอง ไม่ใช่สิ่งที่โมเดลเรียนรู้ได้เอง
- **MAE** (ยิ่งน้อยยิ่งดี) และ **IoU / Dice** (ยิ่งสูงยิ่งดี) — แบบวัดผลสองแบบสำหรับสองงานที่ต่างกัน
- **Garbage in, garbage out** — คุณภาพของป้ายกำกับกำหนดคุณภาพของโมเดล
- **Class imbalance** — เหตุใดความแม่นยำ (accuracy) เพียงอย่างเดียวจึงอาจให้ค่าที่หลอกลวงได้
- **NDT** — การตรวจสอบโดยไม่ทำลาย และตำแหน่งที่ AI เข้ามาช่วยเสริมผู้ตรวจสอบมนุษย์

</div>

---
hideInToc: true
---

# กำหนดการวันนี้

1.  ทำไม AI ถึงสำคัญกับงานคมนาคมและรางรถไฟ
2.  ทบทวนพื้นฐาน AI/ML
3.  NDT คืออะไร และ AI เข้ามาช่วยตรงไหน
4.  **ลงมือทำแล็บ 1 — ประเมินระดับความเต็มของสินค้าในตู้บรรทุก**
5.  ลงมือทำแล็บ 2 — ตรวจจับข้อบกพร่องของรางรถไฟ
6.  สรุปและไอเดียโครงการนำร่อง AI ของคุณเอง

---

# ทำไมแล็บเหล่านี้จึงมีอยู่

ความพยายามส่วนใหญ่ในโครงการ AI จริงไม่ใช่การเขียนโค้ด แต่คือ:

<v-clicks>

- การจัดระเบียบข้อมูลดิบ
- การตัดสินใจว่า "คำตอบที่ถูกต้อง" คืออะไรกันแน่
- การเลือกค่าตั้งค่าที่สมเหตุสมผล
- การวัดผลอย่างตรงไปตรงมาว่าผลลัพธ์ดีแค่ไหน

</v-clicks>

<br>

<v-click>

แล็บทั้งสองนี้แยกเอาประสบการณ์นั้นออกมาให้เห็นชัด ๆ **โค้ดทั้งหมดถูกเขียนไว้แล้ว** —
คุณแค่ติดป้ายกำกับข้อมูลและ/หรือปรับค่าตั้งค่า แล้วดูว่าผลลัพธ์เปลี่ยนไปอย่างไร

</v-click>

---
layout: section
---

# ตอนที่ 2
## ลงมือทำแล็บ 1
### ประเมินพื้นที่ว่างในตู้บรรทุกด้วย AI

---

# แล็บ 1: ภาพรวมของงาน

กล้องที่ติดตั้งอยู่ภายในตู้บรรทุกของรถขนส่ง (ด้านหน้า + ด้านท้าย) ถ่ายภาพขณะที่รถถูกขนสินค้า
ขึ้นตลอดทั้งวัน

**เป้าหมาย:** เมื่อได้รับภาพใหม่ ให้ทายว่าพื้นที่ตู้บรรทุกถูกใช้ไปกี่เปอร์เซ็นต์

<div class="grid grid-cols-3 gap-3 mt-2">
<div class="text-center">
<img src="/img/cargo-front-early.jpg" class="rounded shadow" style="max-height:150px; margin:auto">
<div class="text-sm opacity-70 mt-1">กล้องหน้า ช่วงแรก</div>
</div>
<div class="text-center">
<img src="/img/cargo-front-later.jpg" class="rounded shadow" style="max-height:150px; margin:auto">
<div class="text-sm opacity-70 mt-1">กล้องหน้า ช่วงหลัง</div>
</div>
<div class="text-center">
<img src="/img/cargo-rear-later.jpg" class="rounded shadow" style="max-height:150px; margin:auto">
<div class="text-sm opacity-70 mt-1">กล้องหลัง ช่วงหลัง</div>
</div>
</div>

<div class="mt-2">

- 0% = ว่างเปล่า &nbsp;&nbsp;→&nbsp;&nbsp; 100% = เต็มพื้นที่ทั้งหมด
- **ไม่มีค่าอ้างอิงจริงอัตโนมัติ** — ต้องให้มนุษย์ดูแล้วตัดสินใจ
- นี่คืองานหลัก: ติดป้ายกำกับภาพ 42 ภาพด้วยสายตา

</div>

---

# แล็บ 1: ภาพรวมขั้นตอนการทำงานทั้งหมด

<div class="grid grid-cols-4 gap-2.5 my-3 text-xs">
  <div class="p-3 rounded-lg bg-gray-500/10 border border-gray-500/20 flex flex-col justify-between">
    <div>
      <span class="px-2 py-0.5 rounded text-[10px] font-semibold bg-gray-500/20 text-gray-700 dark:text-gray-300">ทำไว้ให้แล้ว</span>
      <div class="font-bold text-sm mt-2">1. ภาพถ่ายดิบ</div>
      <div class="opacity-75 text-[11px] mt-0.5">จัดเรียงภาพ</div>
    </div>
    <div class="text-right text-base opacity-40 mt-1">➔</div>
  </div>

  <div class="p-3 rounded-lg bg-orange-500/15 border-2 border-orange-500/40 shadow-sm flex flex-col justify-between">
    <div>
      <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-orange-500 text-white">ขั้นตอนของคุณ</span>
      <div class="font-bold text-sm mt-2">2. ติดป้ายกำกับข้อมูล</div>
      <div class="opacity-75 text-[11px] mt-0.5">ติดป้ายกำกับ fill_level</div>
    </div>
    <div class="text-right text-base opacity-40 mt-1">➔</div>
  </div>

  <div class="p-3 rounded-lg bg-gray-500/10 border border-gray-500/20 flex flex-col justify-between">
    <div>
      <span class="px-2 py-0.5 rounded text-[10px] font-semibold bg-gray-500/20 text-gray-700 dark:text-gray-300">ทำไว้ให้แล้ว</span>
      <div class="font-bold text-sm mt-2">3. แบ่งชุดข้อมูล</div>
      <div class="opacity-75 text-[11px] mt-0.5">Train / Val / Test</div>
    </div>
    <div class="text-right text-base opacity-40 mt-1">➔</div>
  </div>

  <div class="p-3 rounded-lg bg-orange-500/15 border-2 border-orange-500/40 shadow-sm flex flex-col justify-between">
    <div>
      <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-orange-500 text-white">ขั้นตอนของคุณ</span>
      <div class="font-bold text-sm mt-2">4. แก้ไขค่าตั้งค่า</div>
      <div class="opacity-75 text-[11px] mt-0.5">cargo_config.yaml</div>
    </div>
    <div class="text-right text-base opacity-40 mt-1">➔</div>
  </div>
</div>

<div class="grid grid-cols-3 gap-3 my-2 text-xs">
  <div class="p-3 rounded-lg bg-gray-500/10 border border-gray-500/20 flex flex-col justify-between">
    <div>
      <span class="px-2 py-0.5 rounded text-[10px] font-semibold bg-gray-500/20 text-gray-700 dark:text-gray-300">ทำไว้ให้แล้ว</span>
      <div class="font-bold text-sm mt-1">5. ฝึกโมเดล</div>
      <div class="opacity-75 text-[11px] mt-0.5">cargo_train.py</div>
    </div>
    <div class="text-right text-base opacity-40 mt-1">➔</div>
  </div>

  <div class="p-3 rounded-lg bg-gray-500/10 border border-gray-500/20 flex flex-col justify-between">
    <div>
      <span class="px-2 py-0.5 rounded text-[10px] font-semibold bg-gray-500/20 text-gray-700 dark:text-gray-300">ทำไว้ให้แล้ว</span>
      <div class="font-bold text-sm mt-1">6. ประเมินผล</div>
      <div class="opacity-75 text-[11px] mt-0.5">cargo_evaluate.py</div>
    </div>
    <div class="text-right text-base opacity-40 mt-1">➔</div>
  </div>

  <div class="p-3 rounded-lg bg-blue-500/15 border-2 border-blue-500/40 shadow-sm flex flex-col justify-between">
    <div>
      <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-blue-600 text-white">คะแนน</span>
      <div class="font-bold text-sm mt-1">7. คะแนนของคุณ</div>
      <div class="opacity-90 font-medium text-[11px] mt-0.5">Mean Absolute Error (MAE)</div>
    </div>
    <div class="text-xs text-blue-600 dark:text-blue-400 font-semibold mt-1">🔄 ปรับค่าตั้งค่าแล้วทำซ้ำ</div>
  </div>
</div>

---

# แล็บ 1: สามโมเดลให้ลองใช้

<div class="grid grid-cols-3 gap-4 mt-6 text-sm">
<div>

### 🌳 Random Forest

"ต้นไม้ตัดสินใจ" แบบง่าย ๆ จำนวนมากต่างทายคำตอบ แล้วนำผลมาเฉลี่ยกัน
ตัวเลือกที่ดีเป็นค่าเริ่มต้น — รับมือกับรูปแบบข้อมูลที่ยุ่งเหยิงได้ดี

</div>
<div>

### 👥 KNN

*(k-nearest neighbors — เพื่อนบ้านใกล้ที่สุด k ตัว)*

หาภาพฝึกที่คล้ายคลึงกันในเชิงภาพมากที่สุด แล้วเฉลี่ยเปอร์เซ็นต์ความเต็มของภาพเหล่านั้น
เรียบง่ายและเข้าใจง่าย

</div>
<div>

### 📈 Linear Regression

โมเดลที่ง่ายที่สุดเท่าที่จะเป็นไปได้: ปรับความสัมพันธ์แบบเส้นตรงเส้นเดียวระหว่างภาพกับเปอร์เซ็นต์
ความเต็ม

</div>
</div>

<div class="mt-8 text-sm opacity-70 text-center">
ตั้งค่าได้ด้วย <code>model_type</code> ใน <code>cargo_config.yaml</code> — ลองทั้งสามแบบแล้วเปรียบเทียบกัน
</div>

---

# เจาะลึก: Random Forest

<div class="text-sm opacity-80 mt-1">กลุ่มของต้นไม้ตัดสินใจ (ensemble) ที่ฝึกบนชุดข้อมูลย่อยแบบสุ่ม แล้วนำผลการทายมาเฉลี่ยกัน</div>

<div class="grid grid-cols-2 gap-4 mt-3 text-xs leading-snug">
<div>

**หลักการทำงาน**

- แต่ละต้นฝึกบน **bootstrap sample** (*bagging*, Breiman 1996) และแต่ละจุดแบ่งกิ่งพิจารณาเพียง
  **กลุ่มย่อยของฟีเจอร์แบบสุ่ม** เท่านั้น (Breiman 2001) — วิธีนี้ลดความสัมพันธ์ระหว่างต้นไม้แต่ละต้น
- ทุกจุดแบ่งกิ่งเลือกฟีเจอร์/ค่าเกณฑ์ที่ลดความแปรปรวนของค่าเป้าหมายได้มากที่สุดแบบโลภ (greedy)
  ($\Delta = \mathrm{Var}(y_{\text{parent}}) - \text{ความแปรปรวนถ่วงน้ำหนักของกิ่งลูก}$)
- ผลการทายสุดท้ายคือค่าเฉลี่ยธรรมดาของต้นไม้ทั้ง $T$ ต้น:

$$\hat y = \frac{1}{T}\sum_{t=1}^{T} f_t(x)$$

</div>
<div>

<div class="p-2.5 rounded-lg bg-amber-500/10 border border-amber-500/30">

**Hyperparameter:** `n_estimators` ($T$) — ค่าความผิดพลาดลดลงตามอัตรา ~$1/\sqrt{T}$ และผลตอบแทน
ลดลงเรื่อย ๆ เมื่อเกินจุดหนึ่ง `max_depth` — จำกัดขีดความสามารถของต้นไม้แต่ละต้น

</div>

<div class="mt-2 p-2.5 rounded-lg bg-blue-500/10 border border-blue-500/30">

**Bias/Variance:** ต้นไม้ลึกต้นเดียว มี bias ต่ำ/variance สูง; การเฉลี่ยต้นไม้ variance สูงจำนวน
มากที่*ไม่สัมพันธ์กัน*จะหักล้าง noise โดยไม่เพิ่ม bias

</div>

<div class="mt-2 p-2.5 rounded-lg bg-gray-500/10 border border-gray-500/20">

✅ รูปแบบไม่เป็นเส้นตรงและปฏิสัมพันธ์ระหว่างตัวแปร ทนต่อ noise &nbsp;&nbsp; ❌ ใช้หน่วยความจำ/เวลามาก อธิบายผลได้ยากกว่า

</div>

</div>
</div>

<div class="mt-2 text-xs opacity-70">
ในแล็บ 1: เป็นค่าเริ่มต้นของ <code>model_type</code> — ตัวเลือกอเนกประสงค์ที่แข็งแกร่งเมื่อคุณยังไม่รู้รูปแบบความสัมพันธ์ล่วงหน้า
</div>

---

# เจาะลึก: K-Nearest Neighbors

<div class="text-sm opacity-80 mt-1">โมเดลแบบอิงตัวอย่าง (instance-based) หรือ "lazy" learner — ไม่มีขั้นตอนการฝึก ข้อมูลฝึกที่เก็บไว้<strong>คือ</strong>ตัวโมเดลเอง</div>

<div class="grid grid-cols-2 gap-4 mt-3 text-xs leading-snug">
<div>

**หลักการทำงาน**

- เมื่อจะทายภาพ $x$ ให้คำนวณระยะห่างของมันกับภาพฝึกทุกภาพในปริภูมิฟีเจอร์:
  $d(x, x_i) = \lVert x - x_i \rVert_2$ (โดยทั่วไปใช้ระยะแบบยุคลิด)
- นำภาพที่ใกล้ที่สุด $k$ ภาพ (`n_neighbors`) มาเฉลี่ยค่าป้ายกำกับ:

$$\hat y = \frac{1}{k}\sum_{i \,\in\, N_k(x)} y_i$$

- **Curse of dimensionality (คำสาปของมิติสูง)**: เวกเตอร์ฟีเจอร์ของเรามีประมาณ 83 ค่า
  (สถิติความสว่าง + ฮิสโตแกรม + กริดหยาบ 8×8) — ในมิติที่สูง ระยะห่างระหว่างจุดต่าง ๆ จะแยกแยะ
  ได้น้อยลง ซึ่งเป็นจุดอ่อนที่รู้กันดีของ KNN

</div>
<div>

<div class="p-2.5 rounded-lg bg-amber-500/10 border border-amber-500/30">

**Hyperparameter:** `n_neighbors` ($k$) คือปุ่มปรับ bias/variance ในตัวเลขเดียว

</div>

<div class="mt-2 p-2.5 rounded-lg bg-blue-500/10 border border-blue-500/30">

**Bias/Variance:** $k$ น้อยจะตาม noise เฉพาะจุดอย่างใกล้ชิด (bias ต่ำ/variance สูง, overfit ง่าย)
$k$ มากจะเฉลี่ยพื้นที่ใกล้เคียงขนาดใหญ่ (bias สูง/variance ต่ำ) และเข้าใกล้ค่าเฉลี่ยรวมเมื่อ
$k \to n$

</div>

<div class="mt-2 p-2.5 rounded-lg bg-gray-500/10 border border-gray-500/20">

✅ ไม่มีต้นทุนการฝึก ปรับตามโครงสร้างเฉพาะจุดได้ &nbsp;&nbsp; ❌ ทายช้า อ่อนไหวต่อการปรับสเกล อ่อนแอในมิติสูง

</div>

</div>
</div>

<div class="mt-2 text-xs opacity-70">

ในแล็บ 1: ด้วยภาพฝึกเพียง ~30 ภาพ $k$ คือจำนวนตัวอย่างที่ติดป้ายกำกับที่จะถูกผสมเข้าไปในการทาย
แต่ละครั้งโดยตรง — ลองเทียบ `n_neighbors=1` กับ `10`

</div>

---

# เจาะลึก: Linear Regression

<div class="text-sm opacity-80 mt-1">สมมติว่าค่าเป้าหมายเป็นฟังก์ชันเส้นตรง (affine) ของฟีเจอร์นำเข้า — โมเดลที่ง่ายที่สุดเท่าที่จะเป็นไปได้ และเป็นโมเดลเดียวในแล็บนี้ที่ "ไม่มีค่าตั้งค่าให้ปรับ"</div>

<div class="grid grid-cols-2 gap-4 mt-3 text-xs leading-snug">
<div>

**หลักการทำงาน**

$$\hat y = w^\top x + b$$

- ปรับค่าด้วย **Ordinary Least Squares**: เลือก $w, b$ เพื่อลดผลรวมของค่าคลาดเคลื่อนกำลังสอง
  บนภาพฝึกให้น้อยที่สุด:

$$(w^*, b^*) = \arg\min_{w,\,b} \sum_{i=1}^{n} \left(y_i - w^\top x_i - b\right)^2$$

- แก้สมการได้ในรูปแบบปิด (closed form) ผ่าน normal equations — ไม่ต้องวนซ้ำ ไม่มี hyperparameter
  ให้ปรับ

</div>
<div>

<div class="p-2.5 rounded-lg bg-amber-500/10 border border-amber-500/30">

**Hyperparameter:** ไม่มี — `random_seed` เป็นค่าตั้งค่าเดียวที่ยังมีผล (มีผลแค่กับการแบ่งชุด
train/val/test ไม่ใช่ตัวการปรับค่าโมเดลเอง)

</div>

<div class="mt-2 p-2.5 rounded-lg bg-blue-500/10 border border-blue-500/30">

**Bias/Variance:** bias สูง (สมมติความเป็นเส้นตรงตายตัว) variance ต่ำ — เสถียรและทำซ้ำได้
แต่ผิดพลาดอย่างเป็นระบบเมื่อใดก็ตามที่ความสัมพันธ์จริงเป็นเส้นโค้ง

</div>

<div class="mt-2 p-2.5 rounded-lg bg-gray-500/10 border border-gray-500/20">

✅ อธิบายผลได้เต็มที่ รวดเร็ว ไม่มีความเสี่ยง overfitting &nbsp;&nbsp; ❌ จับความสัมพันธ์แบบไม่เป็นเส้นตรง/ปฏิสัมพันธ์ไม่ได้ อ่อนไหวต่อค่าผิดปกติ

</div>

</div>
</div>

<div class="mt-2 text-xs opacity-70">
ในแล็บ 1: นี่คือเหตุผลที่ <code>linear_regression</code> มักได้คะแนนแย่ที่สุด (MAE ≈13 เทียบกับ ≈2–3) — เปอร์เซ็นต์ความเต็มไม่ใช่ฟังก์ชันเส้นตรงของฟีเจอร์ความสว่าง/ขอบภาพ
</div>

---

# แล็บ 1: ค่าตั้งค่าอื่น ๆ หมายความว่าอย่างไร?

<div class="text-sm">

| ค่าตั้งค่า | ใช้โดย | สิ่งที่ควบคุม |
|---|---|---|
| `n_estimators` | Random Forest | จำนวนต้นไม้ที่ร่วมโหวต ยิ่งมากยิ่งนิ่ง แต่ช้าลง |
| `max_depth` | Random Forest | ความลึก/ความละเอียดของคำถามในแต่ละต้น ลึกเกินไป = จดจำ noise ("overfitting") |
| `n_neighbors` | KNN | จำนวนภาพที่คล้ายกันที่นำมาเฉลี่ยรวมกัน |
| `random_seed` | ทุกโมเดล | ควบคุมความสุ่มภายใน (การตัดสินกรณีเสมอ ฯลฯ) seed เดียวกัน = ผลลัพธ์ทำซ้ำได้ |

</div>

<div class="mt-6 opacity-70 text-sm">
มีเพียงค่าตั้งค่าของ <code>model_type</code> ที่คุณเลือกเท่านั้นที่มีผลจริง — ค่าที่เหลือจะถูกละเว้น
</div>

---

# แล็บ 1: แข่งขันกันเอง

เมื่อติดป้ายกำกับเสร็จแล้ว ให้แก้ไข `configs/cargo_config.yaml` — ไม่ต้องเขียนโค้ด แค่เปลี่ยนค่า:

```yaml
model_type: random_forest   # หรือ: knn, linear_regression
n_estimators: 100
max_depth: 5
random_seed: 42
```

<v-click>

รันขั้นตอนฝึก + ประเมินใหม่อีกครั้ง แล้วบันทึกค่า **Mean Absolute Error** ของคุณ (ยิ่งน้อยยิ่งดี)
ลงในกระดานคะแนนร่วมกัน

<div class="text-sm opacity-70 mt-4">
คะแนนที่ดีที่สุดมาจากค่าตั้งค่าที่ดีที่สุด — หรือมาจากการติดป้ายกำกับที่รอบคอบที่สุดกันแน่?
</div>

</v-click>

---

# แล็บ 1: ตัวอย่างการรัน — สิ่งที่ควรคาดหวัง

<div class="text-sm">

| model_type | ค่าตั้งค่าหลัก | MAE (จุดเปอร์เซ็นต์) |
|---|---|---|
| random_forest (ค่าเริ่มต้น) | n_estimators=100, max_depth=5 | 2.9 |
| knn | n_neighbors=3 | 2.4 |
| random_forest | n_estimators=300, max_depth=15 | 2.7 |
| random_forest | n_estimators=20, max_depth=2 (ต้นไม้น้อย/ตื้น) | 5.0 |
| linear_regression | (ค่าเริ่มต้น) | 13.1 |

</div>

<div class="mt-4 text-sm opacity-70">

- การรันทดสอบนี้ใช้ภาพตัวอย่างชั่วคราวที่มีความเต็มไล่ระดับอย่างชัดเจน — เป็นการทดสอบระบบ
  ไม่ใช่ข้อมูลรถบรรทุกจริง คาดว่า MAE ของคุณเองจะ**สูงกว่าและแปรปรวนมากกว่านี้** เพราะภาพจริง
  ยุ่งเหยิงกว่าและการติดป้ายกำกับก็เป็นเรื่องของดุลยพินิจส่วนบุคคล
- รูปแบบที่ควรคาดหวังยังคงเดิม: `linear_regression` underfit อย่างชัดเจน ป่าไม้ที่ตื้น/น้อยต้น
  เกินไปก็ underfit เช่นกัน ส่วน `knn` และป่าไม้ที่ปรับจูนดีแล้วมักได้คะแนนใกล้เคียงกันที่สุด

</div>

---

# แล็บ 1: ตัวอย่างผลลัพธ์จริง

<div class="text-center">
<img src="/img/cargo-eval-example.png" style="max-height:150px; margin:auto">
</div>

<div class="text-center mt-2">
<img src="/img/cargo-eval-scatter-example.png" style="max-height:150px; margin:auto">
</div>

<div class="text-xs opacity-70 text-center mt-1">
ผลลัพธ์จริงจากค่าตั้งค่าเริ่มต้นของ pipeline นี้ — แถบภาพ (บน) และกราฟกระจาย (ล่าง)
ที่ถูกบันทึกไว้ทุกครั้งหลังรัน <code>cargo_evaluate.py</code>
</div>

---

# แล็บ 1 (ทางเลือกเพิ่มเติม): เพิ่มจำนวนภาพให้โมเดลเรียนรู้

ด้วยภาพฝึกที่ติดป้ายกำกับแล้วเพียง ~30 ภาพ โมเดลมีความหลากหลายให้เรียนรู้น้อยมาก
**Data augmentation** ทำให้แต่ละภาพทำงานได้สองเท่า: บันทึกสำเนาที่ดัดแปลงแบบสุ่มไม่กี่ชุด —
พลิกภาพ หมุนเล็กน้อย ปรับความสว่าง/คอนทราสต์ — แล้วเพิ่มเข้าไปเป็นตัวอย่างฝึกเพิ่มเติม

```yaml
augment_per_image: 4   # ใน cargo_config.yaml, 0 = ปิดใช้งาน
```

```bash
python3 scripts/cargo_augment.py
```

<div class="grid grid-cols-2 gap-4 mt-4 text-sm">
<div class="p-2.5 rounded-lg bg-gray-500/10 border border-gray-500/20">

**สิ่งที่ถูกแตะต้อง**

- มีเพียงแถว `train` เท่านั้นที่ได้รับสำเนาที่ดัดแปลง
- ชุด `val`/`test` ยังคงเป็นภาพจริง ไม่ถูกแตะต้อง — คะแนนจึงไม่ถูกทำให้สูงเกินจริง
- ตั้งค่ากลับเป็น `0` แล้วรันใหม่เพื่อลบสำเนาเหล่านี้ออก

</div>
<div class="p-2.5 rounded-lg bg-blue-500/10 border border-blue-500/30">

**ลองคิดดู**

*มุมมอง*เพิ่มเติมของช่วงเวลาจริงชุดเดิมเพียงไม่กี่ช่วง ≠ ข้อมูลใหม่จริง ๆ สิ่งนี้เปลี่ยนสิ่งที่
โมเดลต้องการเพื่อใช้งานได้ดีกับรถบรรทุกคันอื่นหรือวันอื่นหรือไม่?

</div>
</div>

<div class="mt-3 text-xs opacity-70">
รัน Part 3 + Part 4 ใหม่หลังจากนั้นแล้วเปรียบเทียบ MAE กับก่อนหน้านี้ — ดูรายละเอียดใน labsheet Part 5.5
</div>

---
layout: center
class: text-center
---

# 🛠 ถึงเวลาทำแล็บ 1

## ประเมินพื้นที่ว่างในตู้บรรทุกด้วย AI

<div class="mt-6 text-lg">
ทำตาม <code>docs/labsheets/cargo_labsheet_th.pdf</code>
</div>

<div class="mt-8 opacity-70">
ติดป้ายกำกับภาพ → แบ่งชุดข้อมูล → แก้ไขค่าตั้งค่า → ฝึกโมเดล → ประเมินผล
</div>

<div class="mt-12 text-sm opacity-60">
วิทยากรจะเดินให้ความช่วยเหลือ — เรียกได้ตลอดเวลา<br>
เมื่อเสร็จแล้ว จดค่า Mean Absolute Error ของคุณลงในกระดานคะแนน
</div>

---
hideInToc: true
---

# กำหนดการวันนี้

1.  ทำไม AI ถึงสำคัญกับงานคมนาคมและรางรถไฟ
2.  ทบทวนพื้นฐาน AI/ML
3.  NDT คืออะไร และ AI เข้ามาช่วยตรงไหน
4.  ลงมือทำแล็บ 1 — ประเมินระดับความเต็มของสินค้าในตู้บรรทุก
5.  **ลงมือทำแล็บ 2 — ตรวจจับข้อบกพร่องของรางรถไฟ**
6.  สรุปและไอเดียโครงการนำร่อง AI ของคุณเอง

---
layout: section
---

# ตอนที่ 3
## ลงมือทำแล็บ 2
### ตรวจจับข้อบกพร่องของรางรถไฟด้วย AI

---

# แล็บ 2: ภาพรวมของงาน

ภาพรางรถไฟจริง 113 ภาพจากชุดข้อมูลวิจัย RSDDs แต่ละภาพมี**แผนที่ข้อบกพร่องอ้างอิงจริง**
ที่วาดด้วยมือมาให้อยู่แล้ว

<div class="grid grid-cols-2 gap-4 mt-4">
<div class="text-center">
<img src="/img/rail-sample.jpg" class="rounded shadow" style="max-height:220px; margin:auto">
<div class="text-sm opacity-70 mt-1">ภาพผิวรางรถไฟ</div>
</div>
<div class="text-center">
<img src="/img/rail-sample-mask.png" class="rounded shadow" style="max-height:220px; margin:auto">
<div class="text-sm opacity-70 mt-1">แผนที่ข้อบกพร่องที่วาดด้วยมือ (สีขาว = ข้อบกพร่อง)</div>
</div>
</div>

<v-clicks>

- ครั้งนี้ไม่ต้องติดป้ายกำกับ — เฉลยมีอยู่แล้ว
- **เป้าหมาย:** ฝึกโมเดลให้วาดแผนที่ข้อบกพร่องของตัวเองบนภาพใหม่
- นี่คือ *segmentation* — แนวคิดเดียวกับที่เรียนในตอนที่ 1 นำมาประยุกต์ใช้กับปัญหา NDT จริง

</v-clicks>

---

# แล็บ 2: ภาพรวมขั้นตอนการทำงานทั้งหมด

<div class="grid grid-cols-5 gap-2 my-3 text-xs">
  <div class="p-3 rounded-lg bg-gray-500/10 border border-gray-500/20 flex flex-col justify-between">
    <div>
      <span class="px-2 py-0.5 rounded text-[9px] font-semibold bg-gray-500/20 text-gray-700 dark:text-gray-300">ทำไว้ให้แล้ว</span>
      <div class="font-bold text-xs mt-2">1. ชุดข้อมูล</div>
      <div class="opacity-75 text-[10px] mt-0.5">RSDDs & ค่าอ้างอิงจริง</div>
    </div>
    <div class="text-right text-sm opacity-40 mt-1">➔</div>
  </div>

  <div class="p-3 rounded-lg bg-orange-500/15 border-2 border-orange-500/40 shadow-sm flex flex-col justify-between">
    <div>
      <span class="px-2 py-0.5 rounded text-[9px] font-bold bg-orange-500 text-white">ขั้นตอนของคุณ</span>
      <div class="font-bold text-xs mt-2">2. แก้ไขค่าตั้งค่า</div>
      <div class="opacity-75 text-[10px] mt-0.5">rail_ndt_config.yaml</div>
    </div>
    <div class="text-right text-sm opacity-40 mt-1">➔</div>
  </div>

  <div class="p-3 rounded-lg bg-gray-500/10 border border-gray-500/20 flex flex-col justify-between">
    <div>
      <span class="px-2 py-0.5 rounded text-[9px] font-semibold bg-gray-500/20 text-gray-700 dark:text-gray-300">ทำไว้ให้แล้ว</span>
      <div class="font-bold text-xs mt-2">3. ฝึกโมเดล</div>
      <div class="opacity-75 text-[10px] mt-0.5">rail_train.py</div>
    </div>
    <div class="text-right text-sm opacity-40 mt-1">➔</div>
  </div>

  <div class="p-3 rounded-lg bg-gray-500/10 border border-gray-500/20 flex flex-col justify-between">
    <div>
      <span class="px-2 py-0.5 rounded text-[9px] font-semibold bg-gray-500/20 text-gray-700 dark:text-gray-300">ทำไว้ให้แล้ว</span>
      <div class="font-bold text-xs mt-2">4. ประเมินผล</div>
      <div class="opacity-75 text-[10px] mt-0.5">rail_evaluate.py</div>
    </div>
    <div class="text-right text-sm opacity-40 mt-1">➔</div>
  </div>

  <div class="p-3 rounded-lg bg-blue-500/15 border-2 border-blue-500/40 shadow-sm flex flex-col justify-between">
    <div>
      <span class="px-2 py-0.5 rounded text-[9px] font-bold bg-blue-600 text-white">คะแนน</span>
      <div class="font-bold text-xs mt-2">5. คะแนนของคุณ</div>
      <div class="opacity-90 font-medium text-[10px] mt-0.5">ค่า Mean IoU</div>
    </div>
    <div class="text-right text-sm opacity-40 mt-1">✓</div>
  </div>
</div>

<div class="grid grid-cols-2 gap-3 my-2 text-xs">
  <div class="p-3 rounded-lg bg-emerald-500/10 border border-emerald-500/30 flex items-start gap-2">
    <div class="text-xl">⚡</div>
    <div>
      <div class="font-bold text-emerald-600 dark:text-emerald-400">ทางลัดที่รวดเร็ว (ไม่ต้องฝึกใหม่)</div>
      <div class="opacity-80 text-[11px] mt-0.5">ปรับค่าเกณฑ์ในไฟล์ตั้งค่า ➔ รัน <code>rail_evaluate.py</code> ใหม่ (ใช้เวลาไม่กี่วินาที)</div>
    </div>
  </div>

  <div class="p-3 rounded-lg bg-purple-500/10 border border-purple-500/30 flex items-start gap-2">
    <div class="text-xl">🔄</div>
    <div>
      <div class="font-bold text-purple-600 dark:text-purple-400">วงจรฝึกโมเดลใหม่แบบเต็มรูปแบบ</div>
      <div class="opacity-80 text-[11px] mt-0.5">เปลี่ยนโครงสร้าง/ค่าตั้งค่าโมเดลในไฟล์ตั้งค่า ➔ รัน <code>rail_train.py</code> ใหม่</div>
    </div>
  </div>
</div>

---

# ตัวอย่างจริงของสิ่งที่คุณจะได้ผลลัพธ์

<div class="flex justify-center mt-2">
<img src="/img/rail-eval-example-compact.png" style="max-height:340px">
</div>

<div class="text-sm opacity-70 text-center mt-2">
ผลลัพธ์จริงจาก pipeline นี้: พื้นที่ข้อบกพร่องจริงและที่ทายซ้อนทับลงบนภาพราง —
<strong>สีเหลือง</strong> = ตรวจจับถูกต้อง, <strong>สีเขียว</strong> = พลาดไป, <strong>สีแดง</strong> = แจ้งเตือนผิดพลาด
เห็นสีแดงเยอะขนาดนี้ไหม? นั่นแหละคือสิ่งที่การปรับค่าเกณฑ์จะช่วยแก้ไขได้พอดี
</div>

---

# แล็บ 2: แข่งขันกันเอง

เครื่องมือหลักไม่ต้อง**ฝึกโมเดลใหม่เลย** — แค่ปรับค่าเกณฑ์ความมั่นใจจากบทสนทนาในตอนที่ 1:

| threshold (ค่าเกณฑ์) | ผลลัพธ์ |
|---|---|
| ต่ำ (เช่น 0.2) | ทำเครื่องหมายพิกเซลมากขึ้น — จับข้อบกพร่องได้มากขึ้น แต่แจ้งเตือนผิดพลาดมากขึ้นด้วย |
| สูง (เช่น 0.8) | ทำเครื่องหมายพิกเซลน้อยลง — แจ้งเตือนผิดพลาดน้อยลง แต่พลาดข้อบกพร่องมากขึ้น |

<v-click>

รัน `rail_evaluate.py` ใหม่ทุกครั้งหลังเปลี่ยนค่า แล้วบันทึกค่า **Mean IoU** ที่ดีที่สุดของคุณ
(ยิ่งสูงยิ่งดี) — แต่ละครั้งใช้เวลาเพียงไม่กี่วินาที

</v-click>

---

# แล็บ 2: ตัวอย่างการรัน — สิ่งที่ควรคาดหวัง

<div class="text-sm">
ค่าตั้งค่าเริ่มต้น (<code>random_forest</code>, 100 ต้น, max_depth=8, threshold=0.5):
&nbsp; <strong>Mean IoU: 0.248 · Mean Dice: 0.379</strong>
</div>

<div class="grid grid-cols-2 gap-6 mt-3">
<div class="text-xs leading-tight">

การไล่ค่าเกณฑ์บนโมเดลที่ฝึกไว้ตัวเดียวกัน (ไม่ฝึกใหม่):

| threshold | Mean IoU | Mean Dice |
|---|---|---|
| 0.2 | 0.157 | 0.253 |
| 0.3 | 0.187 | 0.294 |
| 0.4 | 0.207 | 0.322 |
| 0.5 (ค่าเริ่มต้น) | 0.248 | 0.379 |
| 0.6 | 0.299 | 0.443 |
| **0.7–0.8** | **0.33–0.34** | **0.46–0.48** |
| 0.9–0.95 | 0.15–0.25 | 0.23–0.36 |

</div>
<div class="text-xs opacity-80 leading-snug">

- นี่คือการรันจริงบนข้อมูล RSDDs จริง ทำเป็นการทดสอบเต็มรูปแบบของแล็บนี้ก่อนสอน
- ค่า IoU เพิ่มขึ้นอย่างราบรื่นเมื่อค่าเกณฑ์สูงขึ้น **ขึ้นสูงสุดที่ประมาณ 0.7–0.8** แล้วจึงลดลง
  — จุดสมดุลแบบคลาสสิกระหว่าง precision/recall จากตอนที่ 1
- การฝึกใหม่ด้วย `logistic_regression` หรือป่าไม้ที่ใหญ่ขึ้น (300 ต้น, max_depth=15)
  ขยับ Mean IoU ได้แค่ราว 0.255 — การปรับ `threshold` สำคัญกว่าการเลือกโมเดลมากในกรณีนี้

</div>
</div>

---

# แล็บ 2: ตัวอย่างผลลัพธ์จริง

<div class="text-center">
<img src="/img/rail-eval-example.png" style="max-height:150px; margin:auto">
</div>

<div class="text-center mt-2">
<img src="/img/rail-eval-threshold-curve-example.png" style="max-height:150px; margin:auto">
</div>

<div class="text-xs opacity-70 text-center mt-1">
ผลลัพธ์จริงจาก pipeline นี้ — ภาพซ้อนทับจริง/ที่ทาย (บน) และกราฟไล่ค่าเกณฑ์ (ล่าง)
ที่ถูกบันทึกไว้ทุกครั้งหลังรัน <code>rail_evaluate.py</code>
</div>

---
layout: center
class: text-center
---

# 🛠 ถึงเวลาทำแล็บ 2

## ตรวจจับข้อบกพร่องของรางรถไฟด้วย AI

<div class="mt-6 text-lg">
ทำตาม <code>docs/labsheets/rail_ndt_labsheet_th.pdf</code>
</div>

<div class="mt-8 opacity-70">
ฝึกโมเดล → ประเมินผล → ปรับค่าเกณฑ์ → ประเมินผลใหม่ (ไม่ต้องฝึกใหม่)
</div>

<div class="mt-12 text-sm opacity-60">
วิทยากรจะเดินให้ความช่วยเหลือ — เรียกได้ตลอดเวลา<br>
เมื่อเสร็จแล้ว จดค่า Mean IoU ที่ดีที่สุดของคุณลงในกระดานคะแนน
</div>

---
hideInToc: true
---

# กำหนดการวันนี้

1.  ทำไม AI ถึงสำคัญกับงานคมนาคมและรางรถไฟ
2.  ทบทวนพื้นฐาน AI/ML
3.  NDT คืออะไร และ AI เข้ามาช่วยตรงไหน
4.  ลงมือทำแล็บ 1 — ประเมินระดับความเต็มของสินค้าในตู้บรรทุก
5.  ลงมือทำแล็บ 2 — ตรวจจับข้อบกพร่องของรางรถไฟ
6.  **สรุปและไอเดียโครงการนำร่อง AI ของคุณเอง**

---

# การตั้งค่าเริ่มต้น

ทั้งสองแล็บใช้การตั้งค่าเริ่มต้นแบบเดียวกัน (ทำครั้งเดียว):

```bash
cd AI-training
python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

<div class="mt-6">

คำแนะนำแบบละเอียดทีละขั้นตอน (PDF หรือ Markdown):

- `docs/labsheets/cargo_labsheet_th.pdf`
- `docs/labsheets/rail_ndt_labsheet_th.pdf`

</div>

---

# จากแล็บวันนี้ สู่โครงการนำร่องของคุณ

ในช่วงถัดไปของหลักสูตรนี้ คุณจะต้องเสนอ **โครงการ AI นำร่องแบบ MVP** สำหรับหน่วยงานของคุณเอง
แล็บทั้งสองของวันนี้คือต้นแบบของรูปแบบโครงการที่พบได้บ่อยที่สุดสองแบบ:

<v-clicks>

- **ปัญหาแบบ Regression** — ทายตัวเลขจากข้อมูลที่หน่วยงานของคุณเก็บอยู่แล้ว
  (อัตราการใช้พื้นที่, จำนวนนาทีที่ล่าช้า, ความต้องการ, คะแนนความเสี่ยง ...)
- **ปัญหาแบบ Segmentation/Detection** — หาว่า*สิ่งใดอยู่ตรงไหน*ในภาพ
  (ข้อบกพร่อง, สิ่งกีดขวาง, ความแออัด, การกระทำผิดกฎ ...)

</v-clicks>

<v-click>

<div class="mt-4">
ลองถามตัวเองดู: หน่วยงาน<strong>ของคุณ</strong>ถ่ายภาพ สแกน หรือวัดค่าอะไรอยู่แล้วบ้าง —
ที่ยังไม่มีใครนำมาติดป้ายกำกับอย่างเป็นระบบ?
</div>

</v-click>

---
layout: center
class: text-center
---

# มีคำถามไหม?

ลองคิดดู: เหตุใดคนสองคนที่ใช้ค่าตั้งค่าเหมือนกันทุกประการ จึงยังอาจได้คะแนนต่างกันได้?

<div class="opacity-60 mt-4">
docs/labsheets/ · scripts/ · configs/
</div>
