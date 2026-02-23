# SQLUser.MRC_MolecularMutation

**Schema:** SQLUser
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MM_RowId | bigint | PK |  | NO | - |
| MM_Code | varchar |  |  | NO | Code |
| MM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MM_CreatedDate | date |  |  | SI | Created Date |
| MM_CreatedTime | time |  |  | SI | Created Time |
| MM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MM_DateFrom | date |  |  | SI | Date From |
| MM_DateTo | date |  |  | SI | Date To |
| MM_Desc | varchar |  |  | NO | Description |
| MM_Owner | varchar |  |  | SI | Owner |
| MM_UpdatedDate | date |  |  | SI | Updated Date |
| MM_UpdatedTime | time |  |  | SI | Updated Time |
| MM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | ¿Alguna vez has andado en un AUTO manejado por alg... |
| Q02 | - |  |  | SI | ¿Has usado alguna vez alcohol o drogas para RELAJA... |
| Q03 | - |  |  | SI | ¿Has consumido alguna vez alcohol o drogras estand... |
| Q04 | - |  |  | SI | ¿Has OLVIDADO alguna vez cosas que hiciste mientra... |
| Q05 | - |  |  | SI | ¿Te ha dicho tu familia o AMIGOS que debes disminu... |
| Q06 | - |  |  | SI | ¿Te has metido alguna vez en PROBLEMAS mientras es... |
| Q07 | - |  |  | SI | Resultado Test de CRAFFT |
| Q07ObsDR | - |  |  | SI | Resultado Test de CRAFFT DR |
| Q08 | - |  |  | SI | ¿Ha consumido bebidas alcohólicas (más de unos poc... |
| Q09 | - |  |  | SI | ¿Ha fumado marihuana o probado hachís? |
| Q10 | - |  |  | SI | ¿Ha usado algún otro tipo de sustancias que altere... |
| Q11 | - |  |  | SI | Fecha |
| Q12 | - |  |  | SI | Hora |
| Q13 | - |  |  | SI | Intervención |
| Q14 | - |  |  | SI | Motivo de Intervención |
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