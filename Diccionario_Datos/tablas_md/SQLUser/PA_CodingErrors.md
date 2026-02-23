# SQLUser.PA_CodingErrors

**Schema:** SQLUser
**Columnas:** 130
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CODERR_RowId | bigint | PK |  | NO | - |
| CODERR_AdmCoding_DR | varchar |  | FK | SI | Des Ref AdmCoding |
| CODERR_Code | varchar |  |  | SI | Code |
| CODERR_ID | varchar |  |  | SI | ID |
| CODERR_NationalCode | varchar |  |  | SI | National Code |
| CODERR_Parameters | varchar |  |  | SI | Parameters |
| CODERR_SMRError_DR | bigint |  | FK | SI | Des Ref SMRError |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Visual Acuity (VA) |
| Q04 | - |  |  | SI | Right eye |
| Q05 | - |  |  | SI | Left eye |
| Q06 | - |  |  | SI | Visual Acuity |
| Q07 | - |  |  | SI | Visual acuity notes |
| Q08 | - |  |  | SI | Visual acuity correction |
| Q09 | - |  |  | SI | Visual acuity, right eye (imperial) |
| Q09ObsDR | - |  |  | SI | Visual acuity, right eye (imperial) DR |
| Q10 | - |  |  | SI | Visual acuity, right eye (metric) |
| Q10ObsDR | - |  |  | SI | Visual acuity, right eye (metric) DR |
| Q11 | - |  |  | SI | Visual acuity, right eye (decimal) |
| Q11ObsDR | - |  |  | SI | Visual acuity, right eye (decimal) DR |
| Q12 | - |  |  | SI | Visual acuity, right eye (logMAR) |
| Q12ObsDR | - |  |  | SI | Visual acuity, right eye (logMAR) DR |
| Q13 | - |  |  | SI | Visual acuity notes, right eye |
| Q14 | - |  |  | SI | Correction, right eye |
| Q15 | - |  |  | SI | Visual acuity, left eye (imperial) |
| Q15ObsDR | - |  |  | SI | Visual acuity, left eye (imperial) DR |
| Q16 | - |  |  | SI | Visual acuity, left eye (metric) |
| Q16ObsDR | - |  |  | SI | Visual acuity, left eye (metric) DR |
| Q17 | - |  |  | SI | Visual acuity, left eye (decimal) |
| Q17ObsDR | - |  |  | SI | Visual acuity, left eye (decimal) DR |
| Q18 | - |  |  | SI | Visual acuity, left eye (logMAR) |
| Q18ObsDR | - |  |  | SI | Visual acuity, left eye (logMAR) DR |
| Q19 | - |  |  | SI | Visual acuity notes, left eye |
| Q20 | - |  |  | SI | Correction, left eye |
| Q21 | - |  |  | SI | Visual acuity notes |
| Q22 | - |  |  | SI | Visual acuity, both eyes (imperial) |
| Q22ObsDR | - |  |  | SI | Visual acuity, both eyes (imperial) DR |
| Q23 | - |  |  | SI | Visual acuity, both eyes (metric) |
| Q23ObsDR | - |  |  | SI | Visual acuity, both eyes (metric) DR |
| Q24 | - |  |  | SI | Visual acuity, both eyes (decimal) |
| Q24ObsDR | - |  |  | SI | Visual acuity, both eyes (decimal) DR |
| Q25 | - |  |  | SI | Visual acuity, both eyes (logMAR) |
| Q25ObsDR | - |  |  | SI | Visual acuity, both eyes (logMAR) DR |
| Q26 | - |  |  | SI | Visual acuity notes, both eyes |
| Q27 | - |  |  | SI | Visual acuity correction, both eyes |
| Q28 | - |  |  | SI | Distance between the subject and vision chart |
| Q29 | - |  |  | SI | Unit |
| Q30 | - |  |  | SI | Method |
| Q31 | - |  |  | SI | Other method notes |
| Q32 | - |  |  | SI | Subjective change (subject's perception of visual ... |
| Q33 | - |  |  | SI | Visual acuity both eyes |
| Q34 | - |  |  | SI | Right eye |
| Q35 | - |  |  | SI | Left eye |
| Q36 | - |  |  | SI | Measurement |
| Q37 | - |  |  | SI | Add dioptres |
| Q38 | - |  |  | SI | Working distance (cm) |
| Q39 | - |  |  | SI | Measurement, right eye |
| Q40 | - |  |  | SI | Add dioptres, right eye |
| Q41 | - |  |  | SI | Working distance (cm), right eye |
| Q42 | - |  |  | SI | Measurement, left eye |
| Q43 | - |  |  | SI | Add dioptres, left eye |
| Q44 | - |  |  | SI | Working distance (cm), left eye |
| Q45 | - |  |  | SI | Near vision notes |
| Q46 | - |  |  | SI | Measurement, both eyes |
| Q47 | - |  |  | SI | Add dioptres, both eyes |
| Q48 | - |  |  | SI | Working distance (cm), both eyes |
| Q49 | - |  |  | SI | Near vision notes, both eyes |
| Q50 | - |  |  | SI | Right eye |
| Q51 | - |  |  | SI | Right eye |
| Q52 | - |  |  | SI | Right eye |
| Q53 | - |  |  | SI | Right eye |
| Q54 | - |  |  | SI | Right eye |
| Q55 | - |  |  | SI | Right eye |
| Q56 | - |  |  | SI | Right eye |
| Q57 | - |  |  | SI | Right eye |
| Q58 | - |  |  | SI | Right eye |
| Q59 | - |  |  | SI | Left eye |
| Q60 | - |  |  | SI | Left eye |
| Q61 | - |  |  | SI | Left eye |
| Q62 | - |  |  | SI | Left eye |
| Q63 | - |  |  | SI | Left eye |
| Q64 | - |  |  | SI | Left eye |
| Q65 | - |  |  | SI | Left eye |
| Q66 | - |  |  | SI | Left eye |
| Q67 | - |  |  | SI | Left eye |
| Q68 | - |  |  | SI | Visual acuity (imperial) |
| Q69 | - |  |  | SI | Visual acuity (metric) |
| Q70 | - |  |  | SI | Visual acuity (decimal) |
| Q71 | - |  |  | SI | Visual acuity (logMAR) |
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