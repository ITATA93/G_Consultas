# SQLUser.PA_DeceasedPatient

**Schema:** SQLUser
**Columnas:** 113
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DEC_RowId | bigint | PK |  | NO | - |
| ChildQ73DR | - |  |  | SI | Child Reference: Wound Edge and Periwound |
| DEC_Date | date |  |  | SI | Date |
| DEC_PAPMI_DR | bigint |  | FK | SI | Des Ref PAPMI |
| DEC_Time | time |  |  | SI | Time |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Date wound identified |
| Q04 | - |  |  | SI | Incident report number |
| Q05 | - |  |  | SI | Wound number |
| Q06 | - |  |  | SI | Please complete a separate form for each wound ide... |
| Q07 | - |  |  | SI | Expected date to heal |
| Q08 | - |  |  | SI | Achieved healing date |
| Q09 | - |  |  | SI | Wound location |
| Q10 | - |  |  | SI | Other location |
| Q11 | - |  |  | SI | Foot detail |
| Q12 | - |  |  | SI | Laterality |
| Q13 | - |  |  | SI | Orientation |
| Q14 | - |  |  | SI | Type of wound |
| Q15 | - |  |  | SI | Burn level |
| Q16 | - |  |  | SI | Burn type |
| Q17 | - |  |  | SI | Other wound type |
| Q18 | - |  |  | SI | Bodymap |
| Q19 | - |  |  | SI | Head |
| Q20 | - |  |  | SI | Feet |
| Q21 | - |  |  | SI | Acquired location |
| Q22 | - |  |  | SI | Consent for photography obtained? |
| Q23 | - |  |  | SI | Wound normally managed by |
| Q24 | - |  |  | SI | Type of healing |
| Q25 | - |  |  | SI | Wound closure material used |
| Q26 | - |  |  | SI | Overall goal |
| Q28 | - |  |  | SI | Treatment plan |
| Q29 | - |  |  | SI | Dressing frequency |
| Q30 | - |  |  | SI | Change earlier if leaking |
| Q31 | - |  |  | SI | Analgesia required / recommended prior to wound tr... |
| Q32 | - |  |  | SI | Refer to medication chart |
| Q33 | - |  |  | SI | Cleansing / Care of surrounding region |
| Q34 | - |  |  | SI | Cleaning - wound bed |
| Q35 | - |  |  | SI | Primary dressing |
| Q36 | - |  |  | SI | Secondary dressing |
| Q37 | - |  |  | SI | Additional dressing detail |
| Q38 | - |  |  | SI | Short term goal |
| Q39 | - |  |  | SI | Established aetiology within 14 days |
| Q40 | - |  |  | SI | Established aetiology within 14 days |
| Q41 | - |  |  | SI | Established aetiology within 14 days |
| Q42 | - |  |  | SI | Control underlying factors within 14 days |
| Q43 | - |  |  | SI | Control underlying factors within 14 days |
| Q44 | - |  |  | SI | Control underlying factors within 14 days |
| Q45 | - |  |  | SI | Control pain within 7 days |
| Q46 | - |  |  | SI | Control pain within 7 days |
| Q47 | - |  |  | SI | Control pain within 7 days |
| Q48 | - |  |  | SI | Absence of necrotic tissue within 14 days |
| Q49 | - |  |  | SI | Absence of necrotic tissue within 14 days |
| Q50 | - |  |  | SI | Absence of necrotic tissue within 14 days |
| Q51 | - |  |  | SI | Absence of clinical infections within 14 days |
| Q52 | - |  |  | SI | Absence of clinical infections within 14 days |
| Q53 | - |  |  | SI | Absence of clinical infections within 14 days |
| Q54 | - |  |  | SI | Healthy surrounding tissue and reduction of oedema... |
| Q55 | - |  |  | SI | Healthy surrounding tissue and reduction of oedema... |
| Q56 | - |  |  | SI | Healthy surrounding tissue and reduction of oedema... |
| Q57 | - |  |  | SI | Decreased wound surface area by 25% within 42 days... |
| Q58 | - |  |  | SI | Decreased wound surface area by 25% within 42 days... |
| Q59 | - |  |  | SI | Decreased wound surface area by 25% within 42 days... |
| Q60 | - |  |  | SI | Decreased wound surface area by 50% within 60 days... |
| Q61 | - |  |  | SI | Decreased wound surface area by 50% within 60 days... |
| Q62 | - |  |  | SI | Decreased wound surface area by 50% within 60 days... |
| Q63 | - |  |  | SI | Demonstration of adherence to treatment / preventi... |
| Q64 | - |  |  | SI | Demonstration of adherence to treatment / preventi... |
| Q65 | - |  |  | SI | Demonstration of adherence to treatment / preventi... |
| Q66 | - |  |  | SI | Expected date |
| Q67 | - |  |  | SI | Review date |
| Q68 | - |  |  | SI | Achieved date |
| Q76 | - |  |  | SI | Laterality |
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