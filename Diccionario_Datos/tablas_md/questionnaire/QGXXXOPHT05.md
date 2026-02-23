# questionnaire.QGXXXOPHT05

> Refractions Only

**Schema:** questionnaire
**Columnas:** 248
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Refractions Only

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
| Q156 | varchar |  |  | SI | Axis-OD-WG |
| Q157 | varchar |  |  | SI | Axis-OS-WG |
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
| Q19 | varchar |  |  | SI | Add-OD-Fx |
| Q190 | date |  |  | SI | Date |
| Q191 | time |  |  | SI | Time |
| Q192 | varchar |  |  | SI | This chart shows the last data entered for this pa... |
| Q193 | varchar |  |  | SI | VA-Dt |
| Q194 | varchar |  |  | SI | OD |
| Q195 | varchar |  |  | SI | OS |
| Q196 | varchar |  |  | SI | OU |
| Q197 | varchar |  |  | SI | OU |
| Q198 | varchar |  |  | SI | VA-Nr |
| Q199 | varchar |  |  | SI | Visual Acuity - Uncorrected |
| Q20 | varchar |  |  | SI | Add-OS-Fx |
| Q200 | varchar |  |  | SI | Wearing Glasses Rx |
| Q201 | varchar |  |  | SI | OD |
| Q202 | varchar |  |  | SI | OS |
| Q203 | varchar |  |  | SI | OU |
| Q204 | varchar |  |  | SI | Notes |
| Q205 | varchar |  |  | SI | Sph |
| Q206 | varchar |  |  | SI | Cyl |
| Q207 | varchar |  |  | SI | Axis |
| Q208 | varchar |  |  | SI | Add |
| Q209 | varchar |  |  | SI | VA-Dt |
| Q21 | varchar |  |  | SI | Add-OD-WG |
| Q210 | varchar |  |  | SI | VA-Nr |
| Q211 | varchar |  |  | SI | Dynamic Rx |
| Q212 | varchar |  |  | SI | OD |
| Q213 | varchar |  |  | SI | OS |
| Q214 | varchar |  |  | SI | OU |
| Q215 | varchar |  |  | SI | Notes |
| Q216 | varchar |  |  | SI | Sph |
| Q217 | varchar |  |  | SI | Cyl |
| Q218 | varchar |  |  | SI | Axis |
| Q219 | varchar |  |  | SI | Add |
| Q22 | varchar |  |  | SI | Add-OS-WG |
| Q220 | varchar |  |  | SI | VA-Dt |
| Q221 | varchar |  |  | SI | VA-Nr |
| Q222 | varchar |  |  | SI | Static Rx |
| Q223 | varchar |  |  | SI | Informed Consent? |
| Q224 | varchar |  |  | SI | OD |
| Q225 | varchar |  |  | SI | OS |
| Q226 | varchar |  |  | SI | OU |
| Q227 | varchar |  |  | SI | Notes |
| Q228 | varchar |  |  | SI | Sph |
| Q229 | varchar |  |  | SI | Cyl |
| Q23 | varchar |  |  | SI | Add-OD-UA |
| Q230 | varchar |  |  | SI | Axis |
| Q231 | varchar |  |  | SI | Add |
| Q232 | varchar |  |  | SI | VA-Dt |
| Q233 | varchar |  |  | SI | VA-Nr |
| Q234 | varchar |  |  | SI | Prescription Rx |
| Q235 | varchar |  |  | SI | OD |
| Q236 | varchar |  |  | SI | OS |
| Q237 | varchar |  |  | SI | OU |
| Q238 | varchar |  |  | SI | Notes |
| Q239 | varchar |  |  | SI | Sph |
| Q24 | varchar |  |  | SI | Notes |
| Q240 | varchar |  |  | SI | Cyl |
| Q241 | varchar |  |  | SI | Axis |
| Q242 | varchar |  |  | SI | Add |
| Q243 | varchar |  |  | SI | VA-Dt |
| Q244 | varchar |  |  | SI | VA-Nr |
| Q245 | varchar |  |  | SI | Informed consent? |
| Q25 | varchar |  |  | SI | Notes |
| Q26 | date |  |  | SI | Rx Date |
| Q27 | varchar |  |  | SI | VA@Nr-A-Rt |
| Q28 | varchar |  |  | SI | VA@Nr-A-Lt |
| Q29 | varchar |  |  | SI | VA-CC@Dt-OD |
| Q30 | varchar |  |  | SI | VA-CC@Dt-OS |
| Q33 | varchar |  |  | SI | VA@Dt-A-Rt |
| Q34 | varchar |  |  | SI | VA@Dt-A-Lt |
| Q35 | varchar |  |  | SI | VA-CC@Nr-OU |
| Q36 | varchar |  |  | SI | VA-CC@Dt-OU |
| Q37 | varchar |  |  | SI | VA-CC@Nr-OD |
| Q38 | varchar |  |  | SI | VA-OU-Dt |
| Q39 | varchar |  |  | SI | VA-OU-Nr |
| Q40 | varchar |  |  | SI | VA-CC@Nr-OS |
| Q41 | varchar |  |  | SI | VA-Nr-UA-OU |
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
| Q63 | varchar |  |  | SI | Size |
| Q64 | varchar |  |  | SI | Direct & Consensual |
| Q66 | varchar |  |  | SI | Shape |
| Q67 | varchar |  |  | SI | Size |
| Q68 | varchar |  |  | SI | Direct & Consensual |
| Q69 | varchar |  |  | SI | Shape |
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