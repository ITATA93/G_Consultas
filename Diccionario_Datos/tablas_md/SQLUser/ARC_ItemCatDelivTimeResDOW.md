# SQLUser.ARC_ItemCatDelivTimeResDOW

**Schema:** SQLUser
**Columnas:** 104
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DOW_ParRef | varchar | PK |  | NO | ARC_ItemCatDelivTimeRes Parent Reference |
| DOW_Childsub | double |  |  | NO | Childsub |
| DOW_CreatedDate | date |  |  | SI | Created Date |
| DOW_CreatedTime | time |  |  | SI | Created Time |
| DOW_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DOW_DateFrom | date |  |  | SI | Date From |
| DOW_DateTo | date |  |  | SI | Date To |
| DOW_DayOfWeek_DR | double |  | FK | SI | Des Ref DayOfWeek |
| DOW_RowId | varchar |  |  | NO | - |
| DOW_UpdatedDate | date |  |  | SI | Updated Date |
| DOW_UpdatedTime | time |  |  | SI | Updated Time |
| DOW_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Tipo Examen Físico |
| Q02 | - |  |  | SI | Estado General |
| Q03 | - |  |  | SI | Estado Psíquico |
| Q04 | - |  |  | SI | Otro Estado Psíquico |
| Q05 | - |  |  | SI | Conciencia |
| Q05ObsDR | - |  |  | SI | Conciencia DR |
| Q06 | - |  |  | SI | Piel |
| Q06ObsDR | - |  |  | SI | Piel DR |
| Q07 | - |  |  | SI | Mucosas |
| Q07ObsDR | - |  |  | SI | Mucosas DR |
| Q08 | - |  |  | SI | Cabeza - Cara |
| Q08ObsDR | - |  |  | SI | Cabeza - Cara DR |
| Q09 | - |  |  | SI | Pupilas |
| Q09ObsDR | - |  |  | SI | Pupilas DR |
| Q10 | - |  |  | SI | Conjuntivas |
| Q10ObsDR | - |  |  | SI | Conjuntivas DR |
| Q11 | - |  |  | SI | Dentadura |
| Q11ObsDR | - |  |  | SI | Dentadura DR |
| Q12 | - |  |  | SI | Lenguaje |
| Q13 | - |  |  | SI | Cuello |
| Q13ObsDR | - |  |  | SI | Cuello DR |
| Q14 | - |  |  | SI | Vía Aérea |
| Q14ObsDR | - |  |  | SI | Vía Aérea DR |
| Q15 | - |  |  | SI | Respiración |
| Q16 | - |  |  | SI | Tórax |
| Q16ObsDR | - |  |  | SI | Tórax DR |
| Q17 | - |  |  | SI | Extremidades Superiores |
| Q17ObsDR | - |  |  | SI | Extremidades Superiores DR |
| Q18 | - |  |  | SI | Abdomen |
| Q18ObsDR | - |  |  | SI | Abdomen DR |
| Q19 | - |  |  | SI | Genito-Urinario |
| Q19ObsDR | - |  |  | SI | Genito-Urinario DR |
| Q20 | - |  |  | SI | Extremidades Inferiores |
| Q20ObsDR | - |  |  | SI | Extremidades Inferiores DR |
| Q21 | - |  |  | SI | Edema |
| Q21ObsDR | - |  |  | SI | Edema DR |
| Q22 | - |  |  | SI | Comentario 1 |
| Q23 | - |  |  | SI | Comentario 2 |
| Q24 | - |  |  | SI | Comentario 3 |
| Q25 | - |  |  | SI | Comentario 4 |
| Q26 | - |  |  | SI | Comentario 5 |
| Q27 | - |  |  | SI | Comentario 6 |
| Q28 | - |  |  | SI | Comentario 7 |
| Q29 | - |  |  | SI | Comentario 8 |
| Q30 | - |  |  | SI | Comentario 9 |
| Q31 | - |  |  | SI | Comentario 10 |
| Q32 | - |  |  | SI | Comentario 11 |
| Q33 | - |  |  | SI | Comentario 12 |
| Q34 | - |  |  | SI | Comentario 13 |
| Q35 | - |  |  | SI | Comentario 14 |
| Q36 | - |  |  | SI | Comentario 15 |
| Q37 | - |  |  | SI | Comentario 16 |
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