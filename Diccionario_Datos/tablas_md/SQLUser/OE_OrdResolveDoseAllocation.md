# SQLUser.OE_OrdResolveDoseAllocation

**Schema:** SQLUser
**Columnas:** 134
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RDA_ParRef | varchar | PK |  | NO | OEOrd_ResolveDose Parent Reference |
| Q01 | - |  |  | SI | Current support / services (& frequency) |
| Q02 | - |  |  | SI | Lives |
| Q04 | - |  |  | SI | Personal care assistance |
| Q06 | - |  |  | SI | Home help |
| Q08 | - |  |  | SI | Meals on wheels |
| Q10 | - |  |  | SI | Personal alarm |
| Q11 | - |  |  | SI | Other |
| Q13 | - |  |  | SI | Details |
| Q14 | - |  |  | SI | Current functional level |
| Q15 | - |  |  | SI | Mobility |
| Q16 | - |  |  | SI | Gait aid |
| Q17 | - |  |  | SI | Exercise tolerance |
| Q18 | - |  |  | SI | Falls history |
| Q19 | - |  |  | SI | Follow up required |
| Q20 | - |  |  | SI | Occupational performance |
| Q21 | - |  |  | SI | Personal care |
| Q22 | - |  |  | SI | Current |
| Q23 | - |  |  | SI | Management plan for discharge |
| Q24 | - |  |  | SI | Domestic |
| Q25 | - |  |  | SI | Current |
| Q26 | - |  |  | SI | Management plan for discharge |
| Q27 | - |  |  | SI | Community |
| Q28 | - |  |  | SI | Current |
| Q29 | - |  |  | SI | Management plan for discharge |
| Q30 | - |  |  | SI | Driving |
| Q31 | - |  |  | SI | Current |
| Q32 | - |  |  | SI | Management plan for discharge |
| Q33 | - |  |  | SI | Post-operative driving restrictions discussed |
| Q34 | - |  |  | SI | Discharge transport |
| Q35 | - |  |  | SI | Home environment |
| Q36 | - |  |  | SI | Home |
| Q37 | - |  |  | SI | Main access |
| Q38 | - |  |  | SI | No of steps |
| Q39 | - |  |  | SI | Rail(s) |
| Q40 | - |  |  | SI | Distance from carpark |
| Q41 | - |  |  | SI | Alternative access |
| Q42 | - |  |  | SI | No of steps |
| Q43 | - |  |  | SI | Rail(s) |
| Q44 | - |  |  | SI | Distance from carpark |
| Q45 | - |  |  | SI | Internal |
| Q46 | - |  |  | SI | Clear from obstructions |
| Q47 | - |  |  | SI | Bathroom |
| Q48 | - |  |  | SI | Current equipment |
| Q49 | - |  |  | SI | Rail(s) |
| Q50 | - |  |  | SI | Toilet |
| Q51 | - |  |  | SI | Distance from bedroom |
| Q52 | - |  |  | SI | Current equipment |
| Q53 | - |  |  | SI | Rail(s) |
| Q54 | - |  |  | SI | Bed |
| Q55 | - |  |  | SI | Knee height or above |
| Q56 | - |  |  | SI | Seating |
| Q57 | - |  |  | SI | Knee height or above |
| Q58 | - |  |  | SI | Physical assessment |
| Q59 | - |  |  | SI | Range of Motion (ROM) |
| Q60 | - |  |  | SI | 10m Walk |
| Q61 | - |  |  | SI | Slow |
| Q62 | - |  |  | SI | Fast |
| Q63 | - |  |  | SI | Power |
| Q64 | - |  |  | SI | Comments |
| Q65 | - |  |  | SI | Patient goals |
| Q67 | - |  |  | SI | Risk Assessment and Prediction Tool (RAPT) Score |
| Q68 | - |  |  | SI | Physiotherapy follow up |
| Q69 | - |  |  | SI | Discharge directly home |
| Q70 | - |  |  | SI | Inpatient physiotherapy |
| Q71 | - |  |  | SI | Appointment details |
| Q72 | - |  |  | SI | Occupational Therapy Intervention / Follow up |
| Q73 | - |  |  | SI | Likely equipment needs |
| Q74 | - |  |  | SI | Likely support service needs |
| Q75 | - |  |  | SI | Referral to community-based Occupational Therapy s... |
| Q76 | - |  |  | SI | Pre-admission home assessment |
| Q77 | - |  |  | SI | Referral sent |
| Q78 | - |  |  | SI | Reason for referral |
| Q79 | - |  |  | SI | Equipment loan request |
| Q80 | - |  |  | SI | Referral sent |
| Q81 | - |  |  | SI | Details |
| Q82 | - |  |  | SI | Occupational therapist signature |
| Q82UDt | - |  |  | SI | Occupational therapist signature Last Updated Date |
| Q82UTm | - |  |  | SI | Occupational therapist signature Last Updated Time |
| Q83 | - |  |  | SI | Occupational therapist signature date |
| Q84 | - |  |  | SI | Physiotherapist signature |
| Q84UDt | - |  |  | SI | Physiotherapist signature Last Updated Date |
| Q84UTm | - |  |  | SI | Physiotherapist signature Last Updated Time |
| Q85 | - |  |  | SI | Physiotherapist signature date |
| Q86 | - |  |  | SI | Clinician |
| Q87 | - |  |  | SI | Clinician |
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
| RDA_AdmixItemID | varchar |  |  | SI | Admixture Item ID |
| RDA_Childsub | double |  |  | NO | Childsub |
| RDA_Form_DR | bigint |  | FK | SI | Des Ref to PHCForm |
| RDA_ItmMast_DR | varchar |  | FK | SI | Des Ref to ARCIM |
| RDA_Quantity | double |  |  | SI | Quantity |
| RDA_RowId | varchar |  |  | NO | - |
| RDA_Strength_DR | bigint |  | FK | SI | Des Ref to PHCStrength |
| RDA_UnitVolume | double |  |  | SI | Unit Volume |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*