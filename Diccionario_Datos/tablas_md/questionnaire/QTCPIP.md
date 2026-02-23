# questionnaire.QTCPIP

> Pressure Injury Prevention

**Schema:** questionnaire
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pressure Injury Prevention

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Skin inspection including looking under tubes, pro... |
| Q02 | varchar |  |  | SI | Pressure injury present?	 |
| Q03 | varchar |  |  | SI | Ensure a separate Wound Management form is complet... |
| Q04 | varchar |  |  | SI | Moisture management	 |
| Q05 | varchar |  |  | SI | Moisture management comments	 |
| Q06 | varchar |  |  | SI | Bed surface	 |
| Q07 | varchar |  |  | SI | Bed surface comments	 |
| Q08 | varchar |  |  | SI | Chair |
| Q09 | varchar |  |  | SI | Chair comments	 |
| Q10 | varchar |  |  | SI | Heels |
| Q11 | varchar |  |  | SI | Re-positioning plan	 |
| Q12 | varchar |  |  | SI | High density foam mattress	 |
| Q13 | varchar |  |  | SI | Static air filled mattress overlay	 |
| Q14 | varchar |  |  | SI | Alternating pressure overlay (2 cycle)	 |
| Q15 | varchar |  |  | SI | Alternating pressure mattress (2 cell cycle)	 |
| Q16 | varchar |  |  | SI | Alternatine pressure mattress(3 cell cycle)	 |
| Q17 | varchar |  |  | SI | Heels comments |
| Q18 | varchar |  |  | SI | Body Map |
| Q19 | varchar |  |  | SI | Pressure Injury Present |
| Q20 | varchar |  |  | SI | Have patients, carers and families been provided w... |
| Q21 | varchar |  |  | SI | Was pressure injury present on admission? |
| Q22 | varchar |  |  | SI | Moisture management problems |
| Q23 | varchar |  |  | SI | Referral considerations |
| Q24 | varchar |  |  | SI | Consider referral to: |
| Q25 | varchar |  |  | SI | • Continence advisor if moisture management proble... |
| Q26 | varchar |  |  | SI | • Dietician if nutrition concerns |
| Q27 | varchar |  |  | SI | • Physiotherapist if mobility concerns |
| Q28 | varchar |  |  | SI | • Occupational therapy for assessment of need or t... |
| Q29 | varchar |  |  | SI | • Wound consultant if patient has a pressure injur... |
| Q30 | varchar |  |  | SI | • Podiatry if patient has a lower limb pressure in... |
| Q31 | varchar |  |  | SI | Communicate pressure injury risk level, presence o... |
| Q32 | varchar |  |  | SI | Skin Inspection must be performed on all patients ... |
| Q33 | varchar |  |  | SI | Bed surface |
| Q34 | varchar |  |  | SI | Skin inspection comments |
| Q35 | date |  |  | SI | Date |
| Q36 | time |  |  | SI | Time |
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