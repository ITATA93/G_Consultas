# SQLUser.LBC_SpecimenComment

**Schema:** SQLUser
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCSCOM_RowID | bigint | PK |  | NO | - |
| LBCSCOM_Code | varchar |  |  | SI | Code |
| LBCSCOM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCSCOM_CreatedDate | date |  |  | SI | Created Date |
| LBCSCOM_CreatedTime | time |  |  | SI | Created Time |
| LBCSCOM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCSCOM_DateFrom | date |  |  | SI | Effective date for the record |
| LBCSCOM_DateTo | date |  |  | SI | Last day the record is active  |
| LBCSCOM_Desc | varchar |  |  | SI | Description |
| LBCSCOM_Owner | varchar |  |  | SI | Owner |
| LBCSCOM_Reportable | varchar |  |  | SI | Reportable |
| LBCSCOM_SpecimenCommentGroup_DR | bigint |  | FK | SI | Specimen Comment Group |
| LBCSCOM_UpdatedDate | date |  |  | SI | Updated Date |
| LBCSCOM_UpdatedTime | time |  |  | SI | Updated Time |
| LBCSCOM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| LBCSCOM_UseInCollection | varchar |  |  | SI | Available in Specimen Collection |
| LBCSCOM_UseInLabReg | varchar |  |  | SI | Available in Lab Registration |
| LBCSCOM_UseInOrderEntry | varchar |  |  | SI | Available in Order Entry |
| LBCSCOM_UseInReception | varchar |  |  | SI | Available in Specimen Reception |
| LBCSCOM_UseInResultEntry | varchar |  |  | SI | Available in Result Entry |
| Q01 | - |  |  | SI | Paciente Reintervenido |
| Q02 | - |  |  | SI | Cirugia Principal |
| Q03 | - |  |  | SI | Fecha Inicio Cirugia |
| Q04 | - |  |  | SI | Hora Inicio Cirugia |
| Q05 | - |  |  | SI | Arsenalera |
| Q06 | - |  |  | SI | Duración Cirugia |
| Q07 | - |  |  | SI | Razón de Reintervención |
| Q08 | - |  |  | SI | Anestesiólogo |
| Q09 | - |  |  | SI | Cirugia Secundaria |
| Q10 | - |  |  | SI | Pabellonera |
| Q11 | - |  |  | SI | Enfermera Pabellón |
| Q12 | - |  |  | SI | Primer Cirujano |
| Q13 | - |  |  | SI | Fecha Término Cirugia |
| Q14 | - |  |  | SI | Hora Término Cirugia |
| Q15 | - |  |  | SI | Primer Ayudante (Cirujano) |
| Q16 | - |  |  | SI | N° Episodio |
| Q17 | - |  |  | SI | ANAOP |
| Q18 | - |  |  | SI | Cirugías secundarias 2 |
| Q18hidden | - |  |  | SI | Cirugías secundarias 2 - oculto |
| Q19 | - |  |  | SI | Se reinterviene por: |
| Q20 | - |  |  | SI | Reintervención Secundaria |
| Q20hidden | - |  |  | SI | Reintervención Secundaria - oculto |
| Q23 | - |  |  | SI | Comentarios |
| Q24 | - |  |  | SI | Tipo de Reintervención |
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