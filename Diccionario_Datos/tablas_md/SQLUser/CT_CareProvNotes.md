# SQLUser.CT_CareProvNotes

**Schema:** SQLUser
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Profesionales**. Médicos y personal de salud.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NOTES_ParRef | varchar | PK |  | NO | CT_CareProv Parent Reference |
| NOTES_Childsub | double |  |  | NO | Childsub |
| NOTES_CreatedDate | date |  |  | SI | Created Date |
| NOTES_CreatedTime | time |  |  | SI | Created Time |
| NOTES_CreatedUser_DR | bigint |  | FK | SI | Created User |
| NOTES_Date | date |  |  | SI | Date |
| NOTES_HTMLPlainText | longvarbinary |  |  | SI | Care Provider Notes (HTMLPlainText) for Priority W... |
| NOTES_HTMLRichText | longvarbinary |  |  | SI | Care Provider Notes (HTMLRichText) for Priority Wo... |
| NOTES_RowId | varchar |  |  | NO | - |
| NOTES_UpdatedDate | date |  |  | SI | Updated Date |
| NOTES_UpdatedTime | time |  |  | SI | Updated Time |
| NOTES_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Vivió ó trabajó Ud. en algún pais latinoamericano ... |
| Q02 | - |  |  | SI | Vivió ó trabajó su madre o abuela en pais latinoam... |
| Q03 | - |  |  | SI | Habitó Ud. alguna vez en algún lugar donde vió vin... |
| Q04 | - |  |  | SI | Fué Ud. alguna vez picada por vinchuca? |
| Q05 | - |  |  | SI | Ha recibido tranfusiones de sangre en Chile antes ... |
| Q06 | - |  |  | SI | Ha sido alguna vez diagnosticada de problemas card... |
| Q07 | - |  |  | SI | Ha sido alguna vez diagnosticada de problemas inte... |
| Q08 | - |  |  | SI | Ha tenido abortos, pérdidas, hijos prematuros?(***... |
| Q09 | - |  |  | SI | Sabe Ud. si es hija, hermana ó nieta de mujer con ... |
| Q10 | - |  |  | SI | Sabe Ud. si tiene algún otro familiar (padre, tíos... |
| Q11 | - |  |  | SI | Observación 01 |
| Q12 | - |  |  | SI | Observación 02 |
| Q13 | - |  |  | SI | Observación 03 |
| Q14 | - |  |  | SI | Observación 04 |
| Q15 | - |  |  | SI | Observación 05 |
| Q16 | - |  |  | SI | Observación 06 |
| Q17 | - |  |  | SI | Observación 07 |
| Q18 | - |  |  | SI | Observación 08 |
| Q19 | - |  |  | SI | Observación 09 |
| Q20 | - |  |  | SI | Observación 10 |
| Q21 | - |  |  | SI | Profesional |
| Q22 | - |  |  | SI | (*): Bloqueos, arritmias, angina de esfuerzo que s... |
| Q23 | - |  |  | SI | (**): Megacolon, constipación, megaesófago u otra ... |
| Q24 | - |  |  | SI | (***): Este criterio por si solo no debe considera... |
| Q25 | - |  |  | SI | que ha vivido en zona endémica. |
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