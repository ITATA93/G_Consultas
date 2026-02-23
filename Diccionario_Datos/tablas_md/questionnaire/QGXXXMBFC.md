# questionnaire.QGXXXMBFC

> Baby First Check-Midwife

**Schema:** questionnaire
**Columnas:** 154
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Baby First Check-Midwife

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | bit |  |  | SI | Name bands checked by parents |
| Q02 | varchar |  |  | SI | Temperature (°C) |
| Q02ObsDR | varchar |  | FK | SI | Temperature (°C) DR |
| Q03 | varchar |  |  | SI | Heart rate&nbsp;(bpm) |
| Q03ObsDR | varchar |  | FK | SI | Heart rate&nbsp;(bpm) DR |
| Q04 | varchar |  |  | SI | Respiratory rate&nbsp;(br/min) |
| Q04ObsDR | varchar |  | FK | SI | Respiratory rate&nbsp;(br/min) DR |
| Q05 | varchar |  |  | SI | Weight |
| Q05ObsDR | varchar |  | FK | SI | Weight DR |
| Q06 | varchar |  |  | SI | Length |
| Q06ObsDR | varchar |  | FK | SI | Length DR |
| Q07 | varchar |  |  | SI | Head circumference |
| Q07ObsDR | varchar |  | FK | SI | Head circumference DR |
| Q07a | varchar |  |  | SI | Neonatal head circumference&nbsp;(cm) |
| Q07aObsDR | varchar |  | FK | SI | Neonatal head circumference&nbsp;(cm) DR |
| Q08 | varchar |  |  | SI | Consent to administer vitamin K&nbsp;checked with ... |
| Q08ObsDR | varchar |  | FK | SI | Consent to administer vitamin K&nbsp;checked with ... |
| Q09 | varchar |  |  | SI | Has the paediatrician been contacted? |
| Q09ObsDR | varchar |  | FK | SI | Has the paediatrician been contacted? DR |
| Q10 | varchar |  |  | SI | Vitamin K given by |
| Q11 | varchar |  |  | SI | Vitamin K checked by |
| Q12 | varchar |  |  | SI | Vitamin K batch no |
| Q12ObsDR | varchar |  | FK | SI | Vitamin K batch no DR |
| Q13 | varchar |  |  | SI | Administration route |
| Q13ObsDR | varchar |  | FK | SI | Administration route DR |
| Q14 | varchar |  |  | SI | Are the sagittal sutures &amp; fontanelles normal? |
| Q14ObsDR | varchar |  | FK | SI | Are the sagittal sutures &amp; fontanelles normal?... |
| Q15 | varchar |  |  | SI | Do the eyes appear normal? |
| Q15ObsDR | varchar |  | FK | SI | Do the eyes appear normal? DR |
| Q16 | varchar |  |  | SI | Do the ears appear normal? |
| Q16ObsDR | varchar |  | FK | SI | Do the ears appear normal? DR |
| Q17 | varchar |  |  | SI | Mouth & palate normal |
| Q17ObsDR | varchar |  | FK | SI | Mouth & palate normal DR |
| Q18 | varchar |  |  | SI | Does the neck appear normal? |
| Q18ObsDR | varchar |  | FK | SI | Does the neck appear normal? DR |
| Q19 | varchar |  |  | SI | Skin colour normal |
| Q19ObsDR | varchar |  | FK | SI | Skin colour normal DR |
| Q20 | varchar |  |  | SI | Does the chest appear normal? |
| Q20ObsDR | varchar |  | FK | SI | Does the chest appear normal? DR |
| Q21 | varchar |  |  | SI | Does the umbilical cord appear normal? |
| Q21ObsDR | varchar |  | FK | SI | Does the umbilical cord appear normal? DR |
| Q22 | varchar |  |  | SI | Genitalia normal |
| Q22ObsDR | varchar |  | FK | SI | Genitalia normal DR |
| Q23 | varchar |  |  | SI | Anus normal |
| Q23ObsDR | varchar |  | FK | SI | Anus normal DR |
| Q24 | varchar |  |  | SI | Spine normal |
| Q24ObsDR | varchar |  | FK | SI | Spine normal DR |
| Q25 | varchar |  |  | SI | Limb skin colour normal |
| Q25ObsDR | varchar |  | FK | SI | Limb skin colour normal DR |
| Q26 | varchar |  |  | SI | Palmar / Plantar creases normal |
| Q26ObsDR | varchar |  | FK | SI | Palmar / Plantar creases normal DR |
| Q27 | varchar |  |  | SI | Muscle tone normal |
| Q27ObsDR | varchar |  | FK | SI | Muscle tone normal DR |
| Q28 | varchar |  |  | SI | Digits normal |
| Q28ObsDR | varchar |  | FK | SI | Digits normal DR |
| Q29 | varchar |  |  | SI | Axillae normal |
| Q29ObsDR | varchar |  | FK | SI | Axillae normal DR |
| Q30 | varchar |  |  | SI | Examination notes |
| Q31 | varchar |  |  | SI | Cord bloods sent for rhesus programme |
| Q31ObsDR | varchar |  | FK | SI | Cord bloods sent for rhesus programme DR |
| Q32 | date |  |  | SI | Rhesus bloods sent - date |
| Q33 | time |  |  | SI | Rhesus bloods sent - time |
| Q34 | varchar |  |  | SI | Has the first feed&nbsp;been&nbsp;offered |
| Q34ObsDR | varchar |  | FK | SI | Has the first feed&nbsp;been&nbsp;offered DR |
| Q35 | date |  |  | SI | First breastfeeding offered date |
| Q36 | date |  |  | SI | First artificial feeding offered date |
| Q37 | time |  |  | SI | First breastfeeding offered time |
| Q38 | time |  |  | SI | First artificial feeding offered time |
| Q39 | varchar |  |  | SI | Vitamin K oral dose |
| Q39ObsDR | varchar |  | FK | SI | Vitamin K oral dose DR |
| Q40 | varchar |  |  | SI | Blood group +Rhesus |
| Q40ObsDR | varchar |  | FK | SI | Blood group +Rhesus DR |
| Q41 | varchar |  |  | SI | Midwife countersigning |
| Q43 | varchar |  |  | SI | Blood group type and rhesus status |
| Q44 | date |  |  | SI | Date |
| Q45 | time |  |  | SI | Time |
| Q46 | varchar |  |  | SI | Have the baby's name bands been checked by parents... |
| Q47 | varchar |  |  | SI | Weight (kg) |
| Q47ObsDR | varchar |  | FK | SI | Weight (kg) DR |
| Q48 | varchar |  |  | SI | Length (cm) |
| Q48ObsDR | varchar |  | FK | SI | Length (cm) DR |
| Q49 | varchar |  |  | SI | Neonatal thoracic circumference (cm) |
| Q49ObsDR | varchar |  | FK | SI | Neonatal thoracic circumference (cm) DR |
| Q50 | varchar |  |  | SI | Neonatal abdominal girth (cm) |
| Q50ObsDR | varchar |  | FK | SI | Neonatal abdominal girth (cm) DR |
| Q51 | varchar |  |  | SI | Sutures &amp; fontanelle comment |
| Q52 | varchar |  |  | SI | Eyes comment |
| Q53 | varchar |  |  | SI | Mouth &amp; palate comments |
| Q54 | varchar |  |  | SI | Neck comments |
| Q55 | varchar |  |  | SI | Skin colour comments |
| Q56 | varchar |  |  | SI | Limb skin colour comments |
| Q57 | varchar |  |  | SI | Digits comments |
| Q58 | varchar |  |  | SI | Chest comments |
| Q59 | varchar |  |  | SI | Umbilical cord comments |
| Q60 | varchar |  |  | SI | Genitalia comments |
| Q61 | varchar |  |  | SI | Anus comments |
| Q62 | varchar |  |  | SI | Spine&nbsp;comments |
| Q63 | varchar |  |  | SI | Palmar / Plantar creases comments |
| Q64 | varchar |  |  | SI | Muscle tone comments |
| Q65 | varchar |  |  | SI | Reflexes comments |
| Q66 | varchar |  |  | SI | Axillae comments |
| Q67 | varchar |  |  | SI | Hips normal |
| Q68 | varchar |  |  | SI | Hips comments |
| Q69 | varchar |  |  | SI | Notes |
| Q70 | varchar |  |  | SI | Administering prophylactic eye treatment |
| Q71 | varchar |  |  | SI | Prophylactic eye treatment given by |
| Q72 | varchar |  |  | SI | Prophylactic eye treatment checked by |
| Q73 | varchar |  |  | SI | Type of prophylactic eye treatment |
| Q74 | varchar |  |  | SI | Administration route |
| Q75 | varchar |  |  | SI | Notes |
| Q76 | varchar |  |  | SI | Ears comment |
| Q77 | varchar |  |  | SI | Reflexes normal |
| Q77ObsDR | varchar |  | FK | SI | Reflexes normal DR |
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