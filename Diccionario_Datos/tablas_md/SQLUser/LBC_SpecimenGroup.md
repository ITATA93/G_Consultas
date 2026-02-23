# SQLUser.LBC_SpecimenGroup

**Schema:** SQLUser
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCSPG_RowID | bigint | PK |  | NO | - |
| LBCSPG_Code | varchar |  |  | NO | Code |
| LBCSPG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCSPG_CreatedDate | date |  |  | SI | Created Date |
| LBCSPG_CreatedTime | time |  |  | SI | Created Time |
| LBCSPG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCSPG_DateFrom | date |  |  | SI | Effective date for the record |
| LBCSPG_DateTo | date |  |  | SI | Last day the record is active  |
| LBCSPG_Desc | varchar |  |  | NO | Description |
| LBCSPG_Owner | varchar |  |  | SI | Owner |
| LBCSPG_UpdatedDate | date |  |  | SI | Updated Date |
| LBCSPG_UpdatedTime | time |  |  | SI | Updated Time |
| LBCSPG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | 1. ¿ Se ha sentido muy excitado, nervioso o en ten... |
| Q02 | - |  |  | SI | 2. ¿Ha estado muy preocupado por algo? |
| Q03 | - |  |  | SI | 3. ¿Se ha sentido muy irritable? |
| Q04 | - |  |  | SI | 4. ¿Ha tenido dificultad para relajarse? |
| Q05 | - |  |  | SI | 5. ¿Ha dormido mal, ha tenido dificultades para do... |
| Q06 | - |  |  | SI | 6. ¿Ha tenido dolores de cabeza o nuca? |
| Q07 | - |  |  | SI | 7. ¿Ha tenido alguno de los siguientes síntomas: t... |
| Q08 | - |  |  | SI | 8. ¿Ha estado preocupado por su salud? |
| Q09 | - |  |  | SI | 9. ¿Ha tenido alguna dificultad para conciliar el ... |
| Q10 | - |  |  | SI | 1. ¿Se ha sentido con poca energía? |
| Q11 | - |  |  | SI | 2. ¿Ha perdido usted su interés por las cosas? |
| Q12 | - |  |  | SI | 3. ¿Ha perdido la confianza en sí mismo? |
| Q13 | - |  |  | SI | 4. ¿Se ha sentido usted desesperanzado, sin espera... |
| Q14 | - |  |  | SI | 5 ¿Ha tenido dificultades para concentrarse? |
| Q15 | - |  |  | SI | 6 ¿Ha perdido peso? (a causa de su falta de apetit... |
| Q16 | - |  |  | SI | 7 ¿Se ha estado despertando demasiado temprano? |
| Q17 | - |  |  | SI | 8 ¿Se ha sentido usted enlentecido? |
| Q18 | - |  |  | SI | 9 ¿Cree usted que ha tenido tendencia a encontrars... |
| Q19 | - |  |  | SI | Puntaje Subescala de Ansiedad |
| Q20 | - |  |  | SI | Puntaje Subescala de Depresión |
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