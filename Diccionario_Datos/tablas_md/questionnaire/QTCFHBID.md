# questionnaire.QTCFHBID

> Fast Hugs BID

**Schema:** questionnaire
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Fast Hugs BID

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q1 | varchar |  |  | SI | Feeding |
| Q10 | varchar |  |  | SI | Sedation |
| Q11 | varchar |  |  | SI | Is sedation being minimised as much as possible? |
| Q12 | varchar |  |  | SI | Is a non-benzodiazepine strategy being used, if po... |
| Q13 | varchar |  |  | SI | Thromboembolic Prophylaxis |
| Q14 | varchar |  |  | SI | Is the patient receiving venous thromboembolism (V... |
| Q15 | varchar |  |  | SI | Does the venous thromboembolism (VTE) prophylaxis ... |
| Q16 | varchar |  |  | SI | For patients at high bleeding risk, are thromboemb... |
| Q17 | varchar |  |  | SI | Head of bed elevated |
| Q18 | varchar |  |  | SI | Is head of bed elevated to at least 30 degrees? |
| Q19 | varchar |  |  | SI | Ulcer Prophylaxis |
| Q2 | varchar |  |  | SI | What feeds or diet is the patient receiving? |
| Q20 | varchar |  |  | SI | Does this patient require stress ulcer prophylaxis... |
| Q21 | varchar |  |  | SI | Can stress ulcer prophylaxis be discontinued? |
| Q22 | varchar |  |  | SI | Glycaemic Control |
| Q23 | varchar |  |  | SI | Is glycaemic control adequate (blood glucose targe... |
| Q24 | varchar |  |  | SI | Spontaneous Breathing Trial |
| Q25 | varchar |  |  | SI | Does this patient qualify for a spontaneous breath... |
| Q26 | varchar |  |  | SI | Bowel Regimen |
| Q27 | varchar |  |  | SI | Is a bowel routine ordered? |
| Q28 | varchar |  |  | SI | Does the bowel routine need to be adjusted or esca... |
| Q29 | varchar |  |  | SI | Indwelling Catheters and Lines |
| Q3 | varchar |  |  | SI | Can this be optimised? |
| Q30 | varchar |  |  | SI | Can the central line or the arterial line be remov... |
| Q31 | varchar |  |  | SI | Does the patient still require a foley catheter? |
| Q32 | varchar |  |  | SI | De-escalate Antibiotics |
| Q33 | varchar |  |  | SI | Can the patient's antibiotics be narrowed or disco... |
| Q34 | varchar |  |  | SI | Do all antibiotics have stop dates? |
| Q35 | varchar |  |  | SI | Provenance details |
| Q36 | varchar |  |  | SI | Vincent W, Hatton K. Critically ill patients need ... |
| Q37 | date |  |  | SI | Date |
| Q38 | time |  |  | SI | Time |
| Q4 | varchar |  |  | SI | If 'nil per os' (NPO), do they still need to be? |
| Q5 | varchar |  |  | SI | If projected to be 'nil per os' (NPO) for a long t... |
| Q6 | varchar |  |  | SI | Analgesia |
| Q7 | varchar |  |  | SI | Is pain control adequate? |
| Q8 | varchar |  |  | SI | Are non-opioid adjuncts  being used? |
| Q9 | varchar |  |  | SI | Can oral analgesics be added instead of intravenou... |
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