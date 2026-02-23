# SQLUser.OR_AnaestComplicationCard

**Schema:** SQLUser
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANACC_ParRef | varchar | PK |  | NO | MR_Adm Parent Reference |
| ANACC_Childsub | double |  |  | NO | Childsub |
| ANACC_RowId | varchar |  |  | NO | - |
| ANACC_Type_DR | bigint |  | FK | SI | Des Ref ORCAnaestComplications |
| Q1 | - |  |  | SI | Feeding |
| Q10 | - |  |  | SI | Sedation |
| Q11 | - |  |  | SI | Is sedation being minimised as much as possible? |
| Q12 | - |  |  | SI | Is a non-benzodiazepine strategy being used, if po... |
| Q13 | - |  |  | SI | Thromboembolic Prophylaxis |
| Q14 | - |  |  | SI | Is the patient receiving venous thromboembolism (V... |
| Q15 | - |  |  | SI | Does the venous thromboembolism (VTE) prophylaxis ... |
| Q16 | - |  |  | SI | For patients at high bleeding risk, are thromboemb... |
| Q17 | - |  |  | SI | Head of bed elevated |
| Q18 | - |  |  | SI | Is head of bed elevated to at least 30 degrees? |
| Q19 | - |  |  | SI | Ulcer Prophylaxis |
| Q2 | - |  |  | SI | What feeds or diet is the patient receiving? |
| Q20 | - |  |  | SI | Does this patient require stress ulcer prophylaxis... |
| Q21 | - |  |  | SI | Can stress ulcer prophylaxis be discontinued? |
| Q22 | - |  |  | SI | Glycaemic Control |
| Q23 | - |  |  | SI | Is glycaemic control adequate (blood glucose targe... |
| Q24 | - |  |  | SI | Spontaneous Breathing Trial |
| Q25 | - |  |  | SI | Does this patient qualify for a spontaneous breath... |
| Q26 | - |  |  | SI | Bowel Regimen |
| Q27 | - |  |  | SI | Is a bowel routine ordered? |
| Q28 | - |  |  | SI | Does the bowel routine need to be adjusted or esca... |
| Q29 | - |  |  | SI | Indwelling Catheters and Lines |
| Q3 | - |  |  | SI | Can this be optimised? |
| Q30 | - |  |  | SI | Can the central line or the arterial line be remov... |
| Q31 | - |  |  | SI | Does the patient still require a foley catheter? |
| Q32 | - |  |  | SI | De-escalate Antibiotics |
| Q33 | - |  |  | SI | Can the patient's antibiotics be narrowed or disco... |
| Q34 | - |  |  | SI | Do all antibiotics have stop dates? |
| Q35 | - |  |  | SI | Provenance details |
| Q36 | - |  |  | SI | Vincent W, Hatton K. Critically ill patients need ... |
| Q37 | - |  |  | SI | Date |
| Q38 | - |  |  | SI | Time |
| Q4 | - |  |  | SI | If 'nil per os' (NPO), do they still need to be? |
| Q5 | - |  |  | SI | If projected to be 'nil per os' (NPO) for a long t... |
| Q6 | - |  |  | SI | Analgesia |
| Q7 | - |  |  | SI | Is pain control adequate? |
| Q8 | - |  |  | SI | Are non-opioid adjuncts  being used? |
| Q9 | - |  |  | SI | Can oral analgesics be added instead of intravenou... |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*