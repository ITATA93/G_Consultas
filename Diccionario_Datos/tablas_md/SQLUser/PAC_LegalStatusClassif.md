# SQLUser.PAC_LegalStatusClassif

**Schema:** SQLUser
**Columnas:** 90
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LEGST_RowId | bigint | PK |  | NO | - |
| LEGST_Code | varchar |  |  | NO | Code |
| LEGST_Consent | varchar |  |  | SI | Consent |
| LEGST_CreatedDate | date |  |  | SI | Created Date |
| LEGST_CreatedTime | time |  |  | SI | Created Time |
| LEGST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LEGST_DateFrom | date |  |  | SI | DateFrom |
| LEGST_DateTo | date |  |  | SI | DateTo |
| LEGST_Days | double |  |  | SI | Days |
| LEGST_Desc | varchar |  |  | NO | Description |
| LEGST_MHACT_DR | bigint |  | FK | SI | Des Ref MHACT |
| LEGST_NationalCode | varchar |  |  | SI | National Code |
| LEGST_UpdatedDate | date |  |  | SI | Updated Date |
| LEGST_UpdatedTime | time |  |  | SI | Updated Time |
| LEGST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Llanto |
| Q02 | - |  |  | SI | Sueño |
| Q03 | - |  |  | SI | Reflejo Moro |
| Q04 | - |  |  | SI | Temblor |
| Q05 | - |  |  | SI | Hipertonía |
| Q06 | - |  |  | SI | Excoriaciones (área) |
| Q07 | - |  |  | SI | Sacudidas mioclónicas |
| Q08 | - |  |  | SI | Convulsiones generalizadas |
| Q09 | - |  |  | SI | Sudoración |
| Q10 | - |  |  | SI | Fiebre |
| Q11 | - |  |  | SI | Bostezos frecuentes &gt |
| Q12 | - |  |  | SI | Piel marmorata |
| Q13 | - |  |  | SI | Congestion nasal |
| Q14 | - |  |  | SI | Estornudos &gt |
| Q15 | - |  |  | SI | Aleteo nasal |
| Q16 | - |  |  | SI | Frecuencia respiratoria |
| Q17 | - |  |  | SI | Succión excesiva |
| Q18 | - |  |  | SI | Mal apetito |
| Q19 | - |  |  | SI | Regurgitación |
| Q20 | - |  |  | SI | Deposiciones |
| Q21 | - |  |  | SI | Comments |
| Q22 | - |  |  | SI | Comments |
| Q23 | - |  |  | SI | Comments |
| Q24 | - |  |  | SI | Comments |
| Q25 | - |  |  | SI | Comments |
| Q26 | - |  |  | SI | Comments |
| Q27 | - |  |  | SI | Fecha |
| Q28 | - |  |  | SI | Hora |
| Q29 | - |  |  | SI | Summary statement |
| Q30 | - |  |  | SI | Puntaje |
| Q31 | - |  |  | SI | Classification |
| Q32 | - |  |  | SI | 0 - 37 |
| Q33 | - |  |  | SI | Un puntaje más alto podría indicar un riesgo aumen... |
| Q34 | - |  |  | SI | 0 - 37: Un puntaje más alto podría indicar un ries... |
| Q35 | - |  |  | SI | The Neonatal Abstinence Scoring System (NASS) is u... |
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