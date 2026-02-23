# SQLUser.ARC_ItemEncEntryType

**Schema:** SQLUser
**Columnas:** 133
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ETYPE_ParRef | varchar | PK |  | NO | ARC_ItmMast Parent Reference |
| ETYPE_Childsub | double |  |  | NO | Childsub |
| ETYPE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ETYPE_CreatedDate | date |  |  | SI | Created Date |
| ETYPE_CreatedTime | time |  |  | SI | Created Time |
| ETYPE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ETYPE_EncEntryType_DR | bigint |  | FK | SI | Des Ref EncEntryType |
| ETYPE_RowId | varchar |  |  | NO | - |
| ETYPE_UpdatedDate | date |  |  | SI | Updated Date |
| ETYPE_UpdatedTime | time |  |  | SI | Updated Time |
| ETYPE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Surgical scars |
| Q01N | - |  |  | SI | Note |
| Q01ObsDR | - |  |  | SI | Surgical scars DR |
| Q03 | - |  |  | SI | Ostomy |
| Q03N | - |  |  | SI | Note |
| Q03ObsDR | - |  |  | SI | Ostomy DR |
| Q05 | - |  |  | SI | Globular |
| Q05N | - |  |  | SI | Note |
| Q05ObsDR | - |  |  | SI | Globular DR |
| Q07 | - |  |  | SI | Ascites |
| Q07N | - |  |  | SI | Note |
| Q07ObsDR | - |  |  | SI | Ascites DR |
| Q09 | - |  |  | SI | Lattices venous |
| Q09N | - |  |  | SI | Note |
| Q09ObsDR | - |  |  | SI | Lattices venous DR |
| Q11 | - |  |  | SI | Abdominal tenderness |
| Q11L | - |  |  | SI | Location |
| Q11N | - |  |  | SI | Note |
| Q11ObsDR | - |  |  | SI | Abdominal tenderness DR |
| Q11R | - |  |  | SI | Radiation |
| Q15 | - |  |  | SI | Blumberg sign |
| Q15N | - |  |  | SI | Note |
| Q15ObsDR | - |  |  | SI | Blumberg sign DR |
| Q17 | - |  |  | SI | Murphys sign |
| Q17N | - |  |  | SI | Note |
| Q17ObsDR | - |  |  | SI | Murphys sign DR |
| Q19 | - |  |  | SI | Sign of jordan |
| Q19N | - |  |  | SI | Note |
| Q19ObsDR | - |  |  | SI | Sign of jordan DR |
| Q21 | - |  |  | SI | Peritonism |
| Q21N | - |  |  | SI | Note |
| Q21ObsDR | - |  |  | SI | Peritonism DR |
| Q23 | - |  |  | SI | Peristalsis |
| Q23N | - |  |  | SI | Note |
| Q23ObsDR | - |  |  | SI | Peristalsis DR |
| Q25 | - |  |  | SI | Palpable liver |
| Q25N | - |  |  | SI | Note |
| Q25ObsDR | - |  |  | SI | Palpable liver DR |
| Q27 | - |  |  | SI | Palpable spleen |
| Q27N | - |  |  | SI | Note |
| Q27ObsDR | - |  |  | SI | Palpable spleen DR |
| Q29 | - |  |  | SI | Palpable abdominal masses |
| Q29N | - |  |  | SI | Note |
| Q29ObsDR | - |  |  | SI | Palpable abdominal masses DR |
| Q31 | - |  |  | SI | Bladder distention |
| Q31N | - |  |  | SI | Note |
| Q31ObsDR | - |  |  | SI | Bladder distention DR |
| Q33 | - |  |  | SI | Hernia |
| Q33N | - |  |  | SI | Note |
| Q33ObsDR | - |  |  | SI | Hernia DR |
| Q35 | - |  |  | SI | Inguinal lymphadenopathy |
| Q35N | - |  |  | SI | Note |
| Q35ObsDR | - |  |  | SI | Inguinal lymphadenopathy DR |
| Q37 | - |  |  | SI | Other |
| Q39 | - |  |  | SI | Caput medusae |
| Q39ObsDR | - |  |  | SI | Caput medusae DR |
| Q50 | - |  |  | SI | Rebound tenderness |
| Q50L | - |  |  | SI | Location |
| Q50N | - |  |  | SI | Note |
| Q50ObsDR | - |  |  | SI | Rebound tenderness DR |
| Q50R | - |  |  | SI | Radiation |
| Q51 | - |  |  | SI | Guarding |
| Q51N | - |  |  | SI | Note |
| Q51ObsDR | - |  |  | SI | Guarding DR |
| Q52 | - |  |  | SI | Flank tenderness |
| Q52N | - |  |  | SI | Note |
| Q52ObsDR | - |  |  | SI | Flank tenderness DR |
| Q52a | - |  |  | SI | Flank tenderness |
| Q52aObsDR | - |  |  | SI | Flank tenderness DR |
| Q53 | - |  |  | SI | Rectal examination done |
| Q53N | - |  |  | SI | Note |
| Q54N | - |  |  | SI | Note |
| Q55 | - |  |  | SI | Bowel sounds |
| Q55N | - |  |  | SI | Note |
| Q55ObsDR | - |  |  | SI | Bowel sounds DR |
| Q56 | - |  |  | SI | Caput medusae |
| Q56N | - |  |  | SI | Note |
| Q56ObsDR | - |  |  | SI | Caput medusae DR |
| Q57 | - |  |  | SI | Rectal examination |
| Q60 | - |  |  | SI | Appearance of abdomen |
| Q60N | - |  |  | SI | Note |
| Q60ObsDR | - |  |  | SI | Appearance of abdomen DR |
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