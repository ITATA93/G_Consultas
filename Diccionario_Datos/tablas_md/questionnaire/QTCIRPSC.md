# questionnaire.QTCIRPSC

> Interventional Radiology Patient Safety Checklist

**Schema:** questionnaire
**Columnas:** 94
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Interventional Radiology Patient Safety Checklist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Procedure |
| Q02 | varchar |  |  | SI | Discussed with referring physician / MDT	 |
| Q03 | varchar |  |  | SI | Imaging reviewed	 |
| Q04 | varchar |  |  | SI | Relevant medical history	 |
| Q05 | varchar |  |  | SI | Informed consent	 |
| Q06 | varchar |  |  | SI | Contrast-Induced Nephropathy (CIN) prophylaxis	 |
| Q07 | varchar |  |  | SI | Specific tools present / ordered	 |
| Q08 | varchar |  |  | SI | Fasting order given	 |
| Q09 | varchar |  |  | SI | Relevant lab tests ordered	 |
| Q10 | varchar |  |  | SI | Anesthesiology necessary	 |
| Q11 | varchar |  |  | SI | Anticoagulant medication stopped	 |
| Q12 | varchar |  |  | SI | Contrast allergy prophylaxis necessary	 |
| Q13 | varchar |  |  | SI | Name	 |
| Q14 | varchar |  |  | SI | Role |
| Q15 | longvarbinary |  |  | SI | Signature |
| Q15UDt | date |  |  | SI | Signature Last Updated Date |
| Q15UTm | time |  |  | SI | Signature Last Updated Time |
| Q16 | varchar |  |  | SI | All team members introduced	 |
| Q17 | varchar |  |  | SI | All records with patient	 |
| Q18 | varchar |  |  | SI | Correct patient / Site	 |
| Q19 | varchar |  |  | SI | Patient fasting	 |
| Q20 | varchar |  |  | SI | IV access	 |
| Q21 | varchar |  |  | SI | Monitoring equipment attached	 |
| Q22 | varchar |  |  | SI | Coagulation screen / Lab tests checked	 |
| Q23 | varchar |  |  | SI | Allergies and/or prophylaxis checked	 |
| Q24 | varchar |  |  | SI | Antibiotics / other drugs administered	 |
| Q25 | varchar |  |  | SI | Consent / complications discussed	 |
| Q26 | varchar |  |  | SI | Name |
| Q27 | varchar |  |  | SI | Role |
| Q28 | longvarbinary |  |  | SI | Signature |
| Q28UDt | date |  |  | SI | Signature Last Updated Date |
| Q28UTm | time |  |  | SI | Signature Last Updated Time |
| Q29 | varchar |  |  | SI | Post-op note written	 |
| Q30 | varchar |  |  | SI | Vital signs normal during the procedure	 |
| Q31 | varchar |  |  | SI | Medication and CM recorded	 |
| Q32 | varchar |  |  | SI | Lab tests ordered	 |
| Q33 | varchar |  |  | SI | All samples labeled and sent to the lab	 |
| Q34 | varchar |  |  | SI | Procedure results discussed with the patient	 |
| Q35 | varchar |  |  | SI | Post-discharge instructions given	 |
| Q36 | varchar |  |  | SI | Follow up tests / imaging orders	 |
| Q37 | varchar |  |  | SI | Follow up OPD appointment made	 |
| Q38 | varchar |  |  | SI | Procedure results communicated to the referrer	 |
| Q39 | varchar |  |  | SI | Name |
| Q40 | varchar |  |  | SI | Role |
| Q41 | longvarbinary |  |  | SI | Signature	 |
| Q41UDt | date |  |  | SI | Signature	 Last Updated Date |
| Q41UTm | time |  |  | SI | Signature	 Last Updated Time |
| Q42 | varchar |  |  | SI | Post-interventional (ICU) bed required	 |
| Q43 | varchar |  |  | SI | Correct laterality |
| Q44 | varchar |  |  | SI | Relevant medications ordered / in stock |
| Q45 | varchar |  |  | SI | Comment |
| Q46 | varchar |  |  | SI | Comment |
| Q47 | varchar |  |  | SI | Comment |
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