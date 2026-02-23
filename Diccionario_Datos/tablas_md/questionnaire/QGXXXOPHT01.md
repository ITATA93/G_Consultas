# questionnaire.QGXXXOPHT01

> Ophthalmology Examination

**Schema:** questionnaire
**Columnas:** 340
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ophthalmology Examination

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Sph-Rt |
| Q02 | varchar |  |  | SI | Sph-Lt |
| Q03 | varchar |  |  | SI | Axis-Rt |
| Q04 | varchar |  |  | SI | VA@Nr -OD |
| Q05 | varchar |  |  | SI | VA@Dt -OD |
| Q06 | varchar |  |  | SI | Sph-OD-WG |
| Q07 | varchar |  |  | SI | Cyl-Rt |
| Q08 | varchar |  |  | SI | Axis-Lt |
| Q09 | varchar |  |  | SI | VA@Nr -OS |
| Q10 | varchar |  |  | SI | VA@Dt -OS |
| Q100 | varchar |  |  | SI | Method 1 |
| Q101 | varchar |  |  | SI | Method 2 |
| Q102 | varchar |  |  | SI | Method 2 |
| Q103 | varchar |  |  | SI | Result |
| Q104 | varchar |  |  | SI | Result |
| Q105 | varchar |  |  | SI | Result |
| Q106 | varchar |  |  | SI | Method |
| Q107 | varchar |  |  | SI | OD |
| Q108 | varchar |  |  | SI | OS |
| Q109 | varchar |  |  | SI | OD |
| Q11 | varchar |  |  | SI | Sph-OS-WG |
| Q110 | varchar |  |  | SI | OS |
| Q111 | varchar |  |  | SI | Notes |
| Q112 | varchar |  |  | SI | Anesthetic used |
| Q113 | varchar |  |  | SI | OD |
| Q115 | varchar |  |  | SI | Cyl-OS-WG |
| Q116 | varchar |  |  | SI | OD Inferior Oblique |
| Q117 | varchar |  |  | SI | DRX-OD-Sph |
| Q118 | varchar |  |  | SI | DRX-OD-Cyl |
| Q119 | varchar |  |  | SI | VA-Nr-OSr |
| Q120 | varchar |  |  | SI | Notes |
| Q121 | varchar |  |  | SI | OS |
| Q125 | varchar |  |  | SI | Light & Accommodation |
| Q126 | varchar |  |  | SI | Notes |
| Q13 | varchar |  |  | SI | Cyl-Lt |
| Q131 | varchar |  |  | SI | Notes |
| Q133 | varchar |  |  | SI | Notes |
| Q137 | date |  |  | SI | Date |
| Q139 | varchar |  |  | SI | Cyl-OD-Wx |
| Q14 | varchar |  |  | SI | Cyl-OD-WG |
| Q140 | varchar |  |  | SI | Light & Accommodation |
| Q141 | varchar |  |  | SI | Reflex- Direct |
| Q142 | varchar |  |  | SI | Reflex- Direct |
| Q143 | varchar |  |  | SI | Reflex-Consensual |
| Q144 | varchar |  |  | SI | Reflex-Consensual |
| Q145 | varchar |  |  | SI | RAPD |
| Q146 | varchar |  |  | SI | RAPD |
| Q147 | varchar |  |  | SI | IOP-OD |
| Q147ObsDR | varchar |  | FK | SI | IOP-OD DR |
| Q148 | varchar |  |  | SI | IOP-OS |
| Q148ObsDR | varchar |  | FK | SI | IOP-OS DR |
| Q149 | varchar |  |  | SI | IOP-OD2 |
| Q149ObsDR | varchar |  | FK | SI | IOP-OD2 DR |
| Q15 | varchar |  |  | SI | VA@Dt-UA-Rt |
| Q150 | varchar |  |  | SI | IOP-OS2 |
| Q150ObsDR | varchar |  | FK | SI | IOP-OS2 DR |
| Q151 | varchar |  |  | SI | Gaze |
| Q152 | varchar |  |  | SI | OD |
| Q153 | varchar |  |  | SI | OS |
| Q154 | varchar |  |  | SI | Amsler Grid |
| Q155 | varchar |  |  | SI | Size |
| Q156 | varchar |  |  | SI | Axis-OD-WG |
| Q157 | varchar |  |  | SI | Axis-OS-WG |
| Q158 | varchar |  |  | SI | OD |
| Q159 | varchar |  |  | SI | OS |
| Q16 | varchar |  |  | SI | VA@Dt-UA-Lt |
| Q160 | varchar |  |  | SI | DRX-OD-Axis |
| Q161 | varchar |  |  | SI | DRX-OD-Add |
| Q162 | varchar |  |  | SI | DRX-OD-VADT |
| Q163 | varchar |  |  | SI | DRX-OD-VANR |
| Q164 | varchar |  |  | SI | DRX-OS-Sph |
| Q165 | varchar |  |  | SI | DRX-OS-Cyl |
| Q166 | varchar |  |  | SI | DRX-OS-Axis |
| Q167 | varchar |  |  | SI | DRX-OS-Add |
| Q168 | varchar |  |  | SI | DRX-OS-VADT |
| Q169 | varchar |  |  | SI | DRX-OS-VANR |
| Q17 | varchar |  |  | SI | VA@Nr-UA-Rt |
| Q170 | varchar |  |  | SI | DRX-OU-VADT |
| Q171 | varchar |  |  | SI | DRX-OU-VANR |
| Q172 | varchar |  |  | SI | Dynamic RX Notes |
| Q173 | varchar |  |  | SI | SRX-OD- Sph |
| Q174 | varchar |  |  | SI | SRX-OD- Cyl |
| Q175 | varchar |  |  | SI | SRX-OD- Axis |
| Q176 | varchar |  |  | SI | SRX-OD- Add |
| Q177 | varchar |  |  | SI | SRX-OD- VADT |
| Q178 | varchar |  |  | SI | SRX-OD- VANR |
| Q179 | varchar |  |  | SI | SRX-OS- Sph |
| Q18 | varchar |  |  | SI | VA@Nr-UA-Lt |
| Q180 | varchar |  |  | SI | SRX-OS- Cyl |
| Q181 | varchar |  |  | SI | SRX-OS- Axis |
| Q182 | varchar |  |  | SI | SRX-OS- Add |
| Q183 | varchar |  |  | SI | SRX-OS- VADT |
| Q184 | varchar |  |  | SI | SRX-OS- VANR |
| Q185 | varchar |  |  | SI | SRX-OU- VADT |
| Q186 | varchar |  |  | SI | SRX-OU- VANR |
| Q187 | varchar |  |  | SI | Statix Rx Notes |
| Q188 | varchar |  |  | SI | SRX- Informed Consent |
| Q189 | varchar |  |  | SI | VA - Dt |
| Q19 | varchar |  |  | SI | Add-OD-Fx |
| Q190 | varchar |  |  | SI | Shape |
| Q191 | varchar |  |  | SI | Biomicroscopy Right Eye |
| Q192 | varchar |  |  | SI | Biomicroscopy left Eye |
| Q193 | varchar |  |  | SI | PS Right Eye |
| Q194 | varchar |  |  | SI | PS Left Eye |
| Q195 | varchar |  |  | SI | Sph |
| Q196 | varchar |  |  | SI | Cyl |
| Q197 | varchar |  |  | SI | Axis |
| Q198 | varchar |  |  | SI | Add |
| Q199 | varchar |  |  | SI | VA-Nr-UA-OU |
| Q20 | varchar |  |  | SI | Add-OS-Fx |
| Q200 | varchar |  |  | SI | VA-Dt |
| Q201 | varchar |  |  | SI | VA-Nr |
| Q202 | varchar |  |  | SI | Static Rx |
| Q203 | varchar |  |  | SI | OD |
| Q204 | varchar |  |  | SI | OS |
| Q205 | varchar |  |  | SI | OU |
| Q206 | varchar |  |  | SI | Cyl |
| Q207 | varchar |  |  | SI | Axis |
| Q208 | varchar |  |  | SI | Add |
| Q209 | varchar |  |  | SI | VA-Dt |
| Q21 | varchar |  |  | SI | Add-OD-WG |
| Q210 | varchar |  |  | SI | VA-Nr |
| Q211 | varchar |  |  | SI | Prescription Rx |
| Q212 | varchar |  |  | SI | OD |
| Q213 | varchar |  |  | SI | OS |
| Q214 | varchar |  |  | SI | OU |
| Q215 | varchar |  |  | SI | Sph |
| Q216 | varchar |  |  | SI | Cyl |
| Q217 | varchar |  |  | SI | Add |
| Q218 | varchar |  |  | SI | VA-Dt |
| Q219 | varchar |  |  | SI | VA-Nr |
| Q22 | varchar |  |  | SI | Add-OS-WG |
| Q23 | varchar |  |  | SI | Add-OD-UA |
| Q24 | varchar |  |  | SI | Notes |
| Q25 | varchar |  |  | SI | Notes |
| Q250 | varchar |  |  | SI | Light & Accommodation 2 |
| Q256 | varchar |  |  | SI | Visual Activity - Uncorrected |
| Q257 | varchar |  |  | SI | VA - Dt |
| Q258 | varchar |  |  | SI | OU |
| Q259 | varchar |  |  | SI | Wearing Glasses Rx |
| Q26 | date |  |  | SI | Rx Date |
| Q260 | varchar |  |  | SI | OD |
| Q261 | varchar |  |  | SI | OS |
| Q262 | varchar |  |  | SI | OU |
| Q263 | varchar |  |  | SI | Sph |
| Q264 | varchar |  |  | SI | Cyl |
| Q265 | varchar |  |  | SI | Axis |
| Q266 | varchar |  |  | SI | Add |
| Q267 | varchar |  |  | SI | VA - Dt |
| Q268 | varchar |  |  | SI | VA - Nr |
| Q269 | varchar |  |  | SI | Dynamic Rx |
| Q27 | varchar |  |  | SI | VA@Nr-A-Rt |
| Q270 | varchar |  |  | SI | OD |
| Q271 | varchar |  |  | SI | OS |
| Q272 | varchar |  |  | SI | OU |
| Q273 | varchar |  |  | SI | Sph |
| Q274 | varchar |  |  | SI | Cyl |
| Q275 | varchar |  |  | SI | Axis |
| Q276 | varchar |  |  | SI | Add |
| Q277 | varchar |  |  | SI | VA - Dt |
| Q278 | varchar |  |  | SI | VA - Nr |
| Q279 | varchar |  |  | SI | Static Rx |
| Q28 | varchar |  |  | SI | VA@Nr-A-Lt |
| Q280 | varchar |  |  | SI | OD |
| Q281 | varchar |  |  | SI | OS |
| Q282 | varchar |  |  | SI | OU |
| Q283 | varchar |  |  | SI | Sph |
| Q284 | varchar |  |  | SI | Cyl |
| Q285 | varchar |  |  | SI | Axis |
| Q286 | varchar |  |  | SI | Add |
| Q287 | varchar |  |  | SI | VA - Nr |
| Q288 | varchar |  |  | SI | Prescription Rx |
| Q289 | varchar |  |  | SI | OD |
| Q29 | varchar |  |  | SI | VA-CC@Dt-OD |
| Q290 | varchar |  |  | SI | OS |
| Q291 | varchar |  |  | SI | OU |
| Q30 | varchar |  |  | SI | VA-CC@Dt-OS |
| Q300 | date |  |  | SI | Date |
| Q301 | time |  |  | SI | Time |
| Q302 | varchar |  |  | SI | Informed Consent? |
| Q303 | varchar |  |  | SI | Notes |
| Q304 | varchar |  |  | SI | Notes |
| Q305 | varchar |  |  | SI | VA-Nr |
| Q306 | varchar |  |  | SI | VA-Dt |
| Q307 | varchar |  |  | SI | VA-Nr |
| Q308 | varchar |  |  | SI | Stereopsis |
| Q309 | varchar |  |  | SI | Reading |
| Q310 | varchar |  |  | SI | Colour Vision |
| Q311 | varchar |  |  | SI | Light & Accommodation |
| Q312 | varchar |  |  | SI | Reflex - Direct |
| Q313 | varchar |  |  | SI | Reflex - Consensual |
| Q314 | varchar |  |  | SI | Reflex - RAPD |
| Q315 | varchar |  |  | SI | Cover Test & Gaze |
| Q316 | varchar |  |  | SI | EOM |
| Q317 | varchar |  |  | SI | OD |
| Q318 | varchar |  |  | SI | SR: |
| Q319 | varchar |  |  | SI | IO: |
| Q320 | varchar |  |  | SI | LR: |
| Q321 | varchar |  |  | SI | MR: |
| Q322 | varchar |  |  | SI | IR: |
| Q323 | varchar |  |  | SI | SO: |
| Q324 | varchar |  |  | SI | OS |
| Q325 | varchar |  |  | SI | IO: |
| Q326 | varchar |  |  | SI | SR: |
| Q327 | varchar |  |  | SI | MR: |
| Q328 | varchar |  |  | SI | LR: |
| Q329 | varchar |  |  | SI | SO: |
| Q33 | varchar |  |  | SI | VA@Dt-A-Rt |
| Q330 | varchar |  |  | SI | IR: |
| Q331 | varchar |  |  | SI | Dry Eye Test |
| Q332 | varchar |  |  | SI | Schimer's test 1 |
| Q333 | varchar |  |  | SI | Schimer's test 2 |
| Q334 | varchar |  |  | SI | IOP-OD (mmHg) |
| Q335 | varchar |  |  | SI | IOP-OS (mmHg) |
| Q336 | varchar |  |  | SI | Topical Anesthesia Used |
| Q337 | varchar |  |  | SI | This chart contains the information from the Refra... |
| Q338 | varchar |  |  | SI | Completed charts are found at the bottom of the sc... |
| Q339 | varchar |  |  | SI | Amsler Grid |
| Q34 | varchar |  |  | SI | VA@Dt-A-Lt |
| Q340 | varchar |  |  | SI | OD |
| Q341 | varchar |  |  | SI | OD |
| Q342 | varchar |  |  | SI | OD |
| Q343 | varchar |  |  | SI | OS |
| Q344 | varchar |  |  | SI | OS |
| Q345 | varchar |  |  | SI | OS |
| Q346 | numeric |  |  | SI | Prism |
| Q347 | numeric |  |  | SI | Prism |
| Q348 | numeric |  |  | SI | Prism |
| Q349 | numeric |  |  | SI | Prism |
| Q35 | varchar |  |  | SI | VA-CC@Nr-OU |
| Q350 | numeric |  |  | SI | Prism |
| Q351 | numeric |  |  | SI | Prism |
| Q352 | numeric |  |  | SI | Prism |
| Q353 | numeric |  |  | SI | Prism |
| Q354 | numeric |  |  | SI | Prism |
| Q355 | numeric |  |  | SI | Prism |
| Q356 | numeric |  |  | SI | Prism |
| Q357 | numeric |  |  | SI | Prism |
| Q358 | varchar |  |  | SI | Prism |
| Q359 | varchar |  |  | SI | Prism |
| Q36 | varchar |  |  | SI | VA-CC@Dt-OU |
| Q360 | varchar |  |  | SI | Prism |
| Q361 | varchar |  |  | SI | Prism |
| Q362 | numeric |  |  | SI | Base |
| Q363 | numeric |  |  | SI | Base |
| Q364 | numeric |  |  | SI | Base |
| Q365 | numeric |  |  | SI | Base |
| Q366 | numeric |  |  | SI | Base |
| Q367 | numeric |  |  | SI | Base |
| Q368 | numeric |  |  | SI | Base |
| Q369 | numeric |  |  | SI | Base |
| Q37 | varchar |  |  | SI | VA-CC@Nr-OD |
| Q370 | numeric |  |  | SI | Base |
| Q371 | numeric |  |  | SI | Base |
| Q372 | numeric |  |  | SI | Base |
| Q373 | numeric |  |  | SI | Base |
| Q374 | varchar |  |  | SI | Base |
| Q375 | varchar |  |  | SI | Base |
| Q376 | varchar |  |  | SI | Base |
| Q377 | varchar |  |  | SI | Base |
| Q38 | varchar |  |  | SI | VA-OU-Dt |
| Q39 | varchar |  |  | SI | VA-OU-Nr |
| Q40 | varchar |  |  | SI | VA-CC@Nr-OS |
| Q44 | varchar |  |  | SI | VA-Nr-ODr |
| Q45 | varchar |  |  | SI | VA-Dt-A-OU |
| Q46 | varchar |  |  | SI | VA-Dt-UA-OU |
| Q47 | varchar |  |  | SI | VA-Nr-A-OU |
| Q48 | varchar |  |  | SI | VA-Dt-OSr |
| Q49 | varchar |  |  | SI | VA-Dt-ODr |
| Q50 | varchar |  |  | SI | VA-Dt-OUr |
| Q54 | varchar |  |  | SI | VA-Nr-OUr |
| Q60 | varchar |  |  | SI | Notes |
| Q61 | varchar |  |  | SI | Notes |
| Q63 | varchar |  |  | SI | Size@OD |
| Q64 | varchar |  |  | SI | Direct & Consensual |
| Q66 | varchar |  |  | SI | Shape@OS |
| Q67 | varchar |  |  | SI | Size@OS |
| Q68 | varchar |  |  | SI | Direct & Consensual |
| Q69 | varchar |  |  | SI | Shape@OD |
| Q71 | varchar |  |  | SI | Method |
| Q74 | date |  |  | SI | Date |
| Q75 | time |  |  | SI | Time |
| Q76 | varchar |  |  | SI | Topical Anesthesia used |
| Q77 | varchar |  |  | SI | Method |
| Q78 | date |  |  | SI | Date |
| Q79 | time |  |  | SI | Time |
| Q82 | varchar |  |  | SI | OD Lateral Rectus |
| Q83 | varchar |  |  | SI | OS Lateral Rectus |
| Q84 | varchar |  |  | SI | OD Medial Rectus |
| Q85 | varchar |  |  | SI | OD Superior Rectus |
| Q86 | varchar |  |  | SI | OS Superior Rectus |
| Q87 | varchar |  |  | SI | OS Medial Rectus |
| Q88 | varchar |  |  | SI | OD Inferior Rectus |
| Q89 | varchar |  |  | SI | OS Inferior Rectus |
| Q90 | varchar |  |  | SI | OD Superior Oblique |
| Q91 | varchar |  |  | SI | OS Superior Oblique |
| Q92 | varchar |  |  | SI | OS Inferior Oblique |
| Q97 | varchar |  |  | SI | Cover test |
| Q98 | varchar |  |  | SI | Notes |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*