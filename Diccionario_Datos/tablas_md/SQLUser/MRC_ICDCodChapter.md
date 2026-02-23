# SQLUser.MRC_ICDCodChapter

**Schema:** SQLUser
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CHAP_RowId | bigint | PK |  | NO | - |
| CHAP_Code | varchar |  |  | NO | Code |
| CHAP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CHAP_CreatedDate | date |  |  | SI | Created Date |
| CHAP_CreatedTime | time |  |  | SI | Created Time |
| CHAP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CHAP_DateFrom | date |  |  | SI | Date From |
| CHAP_DateTo | date |  |  | SI | Date To |
| CHAP_Desc | varchar |  |  | NO | Description |
| CHAP_Owner | varchar |  |  | SI | Owner |
| CHAP_UpdatedDate | date |  |  | SI | Updated Date |
| CHAP_UpdatedTime | time |  |  | SI | Updated Time |
| CHAP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | ¿Has tenido problemas con otras personas por causa... |
| Q02 | - |  |  | SI | ¿Has perdido amistades a causa del alcohol? |
| Q03 | - |  |  | SI | ¿Has tenido problemas con otras personas por causa... |
| Q04 | - |  |  | SI | ¿Te molesta que te critiquen por la forma como tom... |
| Q05 | - |  |  | SI | ¿Has tenido ganas de disminuir lo que tomas? |
| Q06 | - |  |  | SI | ¿Te ha pasado que tomas más de lo que querías? |
| Q07 | - |  |  | SI | ¿Has tenido que tomar alcohol en las mañanas? |
| Q08 | - |  |  | SI | ¿Después de haber bebido no recuerdas parte de lo ... |
| Q09 | - |  |  | SI | 1. ¿Has tenido problemas con otras personas por ca... |
| Q10 | - |  |  | SI | 2. ¿Has perdido amistades a causa del alcohol? |
| Q11 | - |  |  | SI | 3. ¿Has tenido problemas con otras personas por ca... |
| Q12 | - |  |  | SI | 4. ¿Te molesta que te critiquen por la forma como ... |
| Q13 | - |  |  | SI | 5. ¿Has tenido ganas de disminuir lo que tomas? |
| Q14 | - |  |  | SI | 6. ¿Te ha pasado que tomas más de lo que querías? |
| Q15 | - |  |  | SI | 7. ¿Has tenido que tomar alcohol en las mañanas? |
| Q16 | - |  |  | SI | 8. ¿Después de haber bebido no recuerdas parte de ... |
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