# questionnaire.QTCAHPRHORT

> Orthopaedic Pre-Admission Clinic Assessment

**Schema:** questionnaire
**Columnas:** 126
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Orthopaedic Pre-Admission Clinic Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Current support / services (& frequency) |
| Q02 | varchar |  |  | SI | Lives |
| Q04 | bit |  |  | SI | Personal care assistance |
| Q06 | bit |  |  | SI | Home help |
| Q08 | bit |  |  | SI | Meals on wheels |
| Q10 | bit |  |  | SI | Personal alarm |
| Q11 | bit |  |  | SI | Other |
| Q13 | varchar |  |  | SI | Details |
| Q14 | varchar |  |  | SI | Current functional level |
| Q15 | varchar |  |  | SI | Mobility |
| Q16 | varchar |  |  | SI | Gait aid |
| Q17 | varchar |  |  | SI | Exercise tolerance |
| Q18 | varchar |  |  | SI | Falls history |
| Q19 | varchar |  |  | SI | Follow up required |
| Q20 | varchar |  |  | SI | Occupational performance |
| Q21 | varchar |  |  | SI | Personal care |
| Q22 | varchar |  |  | SI | Current |
| Q23 | varchar |  |  | SI | Management plan for discharge |
| Q24 | varchar |  |  | SI | Domestic |
| Q25 | varchar |  |  | SI | Current |
| Q26 | varchar |  |  | SI | Management plan for discharge |
| Q27 | varchar |  |  | SI | Community |
| Q28 | varchar |  |  | SI | Current |
| Q29 | varchar |  |  | SI | Management plan for discharge |
| Q30 | varchar |  |  | SI | Driving |
| Q31 | varchar |  |  | SI | Current |
| Q32 | varchar |  |  | SI | Management plan for discharge |
| Q33 | bit |  |  | SI | Post-operative driving restrictions discussed |
| Q34 | bit |  |  | SI | Discharge transport |
| Q35 | varchar |  |  | SI | Home environment |
| Q36 | varchar |  |  | SI | Home |
| Q37 | varchar |  |  | SI | Main access |
| Q38 | varchar |  |  | SI | No of steps |
| Q39 | varchar |  |  | SI | Rail(s) |
| Q40 | varchar |  |  | SI | Distance from carpark |
| Q41 | varchar |  |  | SI | Alternative access |
| Q42 | varchar |  |  | SI | No of steps |
| Q43 | varchar |  |  | SI | Rail(s) |
| Q44 | varchar |  |  | SI | Distance from carpark |
| Q45 | varchar |  |  | SI | Internal |
| Q46 | bit |  |  | SI | Clear from obstructions |
| Q47 | varchar |  |  | SI | Bathroom |
| Q48 | varchar |  |  | SI | Current equipment |
| Q49 | varchar |  |  | SI | Rail(s) |
| Q50 | varchar |  |  | SI | Toilet |
| Q51 | varchar |  |  | SI | Distance from bedroom |
| Q52 | varchar |  |  | SI | Current equipment |
| Q53 | varchar |  |  | SI | Rail(s) |
| Q54 | varchar |  |  | SI | Bed |
| Q55 | bit |  |  | SI | Knee height or above |
| Q56 | varchar |  |  | SI | Seating |
| Q57 | bit |  |  | SI | Knee height or above |
| Q58 | varchar |  |  | SI | Physical assessment |
| Q59 | varchar |  |  | SI | Range of Motion (ROM) |
| Q60 | varchar |  |  | SI | 10m Walk |
| Q61 | varchar |  |  | SI | Slow |
| Q62 | varchar |  |  | SI | Fast |
| Q63 | varchar |  |  | SI | Power |
| Q64 | varchar |  |  | SI | Comments |
| Q65 | varchar |  |  | SI | Patient goals |
| Q67 | numeric |  |  | SI | Risk Assessment and Prediction Tool (RAPT) Score |
| Q68 | varchar |  |  | SI | Physiotherapy follow up |
| Q69 | varchar |  |  | SI | Discharge directly home |
| Q70 | varchar |  |  | SI | Inpatient physiotherapy |
| Q71 | varchar |  |  | SI | Appointment details |
| Q72 | varchar |  |  | SI | Occupational Therapy Intervention / Follow up |
| Q73 | varchar |  |  | SI | Likely equipment needs |
| Q74 | varchar |  |  | SI | Likely support service needs |
| Q75 | varchar |  |  | SI | Referral to community-based Occupational Therapy s... |
| Q76 | bit |  |  | SI | Pre-admission home assessment |
| Q77 | date |  |  | SI | Referral sent |
| Q78 | varchar |  |  | SI | Reason for referral |
| Q79 | bit |  |  | SI | Equipment loan request |
| Q80 | date |  |  | SI | Referral sent |
| Q81 | varchar |  |  | SI | Details |
| Q82 | longvarbinary |  |  | SI | Occupational therapist signature |
| Q82UDt | date |  |  | SI | Occupational therapist signature Last Updated Date |
| Q82UTm | time |  |  | SI | Occupational therapist signature Last Updated Time |
| Q83 | date |  |  | SI | Occupational therapist signature date |
| Q84 | longvarbinary |  |  | SI | Physiotherapist signature |
| Q84UDt | date |  |  | SI | Physiotherapist signature Last Updated Date |
| Q84UTm | time |  |  | SI | Physiotherapist signature Last Updated Time |
| Q85 | date |  |  | SI | Physiotherapist signature date |
| Q86 | varchar |  |  | SI | Clinician |
| Q87 | varchar |  |  | SI | Clinician |
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