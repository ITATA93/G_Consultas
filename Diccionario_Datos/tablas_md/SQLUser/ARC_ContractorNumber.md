# SQLUser.ARC_ContractorNumber

**Schema:** SQLUser
**Columnas:** 102
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONTRN_RowId | bigint | PK |  | NO | - |
| CONTRN_Active | varchar |  |  | SI | Active |
| CONTRN_AuxInstype_DR | bigint |  | FK | SI | Des Ref AuxInstype |
| CONTRN_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CONTRN_CreatedDate | date |  |  | SI | Created Date |
| CONTRN_CreatedTime | time |  |  | SI | Created Time |
| CONTRN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CONTRN_DateFrom | date |  |  | SI | DateFrom |
| CONTRN_DateTo | date |  |  | SI | DateTo |
| CONTRN_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| CONTRN_Owner | varchar |  |  | SI | Owner |
| CONTRN_Prefix | varchar |  |  | SI | Prefix |
| CONTRN_RangeEnd | varchar |  |  | SI | Range End |
| CONTRN_RangeStart | varchar |  |  | SI | Range Start |
| CONTRN_UpdatedDate | date |  |  | SI | Updated Date |
| CONTRN_UpdatedTime | time |  |  | SI | Updated Time |
| CONTRN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| CQ01 | - |  |  | SI | (null) |
| CQ39 | - |  |  | SI | (null) |
| Q01 | - |  |  | SI | Establecimiento de Procedencia |
| Q02 | - |  |  | SI | Exclusiva EFM |
| Q03 | - |  |  | SI | Control Ginecologico |
| Q04 | - |  |  | SI | Morbilidad Ginecologica |
| Q05 | - |  |  | SI | Control Prenatal |
| Q06 | - |  |  | SI | Control Paternidad responsable |
| Q07 | - |  |  | SI | Examen de Salud del Adulto |
| Q08 | - |  |  | SI | Control Cronicos |
| Q09 | - |  |  | SI | Morbilidad adultos |
| Q10 | - |  |  | SI | Anterior EFM |
| Q11 | - |  |  | SI | Resultado |
| Q12 | - |  |  | SI | Motivos del EFM |
| Q13 | - |  |  | SI | Especifique |
| Q14 | - |  |  | SI | Nodulo Palpable Der. |
| Q15 | - |  |  | SI | Nódulo Palpable Izq. |
| Q16 | - |  |  | SI | Nodulo Axilar Der. |
| Q17 | - |  |  | SI | Nodulo Axilar Izq. |
| Q18 | - |  |  | SI | Nodo Supraclavicular Der. |
| Q19 | - |  |  | SI | Nodo Supraclavicular Izq. |
| Q20 | - |  |  | SI | Derrame Hepatico Pezon Der. |
| Q21 | - |  |  | SI | Derrame Hepatico Pezon Izq. |
| Q22 | - |  |  | SI | Retraccion del Pezon Der. |
| Q23 | - |  |  | SI | Retraccion del Pezon Izq. |
| Q24 | - |  |  | SI | Eczema del Pezon Der. |
| Q25 | - |  |  | SI | Eczema del Pezon Izq. |
| Q26 | - |  |  | SI | Retraccion Piel Mama Der. |
| Q27 | - |  |  | SI | Retraccion Piel Mama Izq. |
| Q28 | - |  |  | SI | Ulceracion Piel Mama Der. |
| Q29 | - |  |  | SI | Ulceracion Piel Mama Izq. |
| Q30 | - |  |  | SI | Eritema Piel Mama Der. |
| Q31 | - |  |  | SI | Eritema Piel Mama Izq. |
| Q32 | - |  |  | SI | Edema Piel Mama Der. |
| Q33 | - |  |  | SI | Edema Piel Mama Izq. |
| Q34 | - |  |  | SI | Autoexamen Mamario (AEM) |
| Q35 | - |  |  | SI | Obs Imagen |
| Q38 | - |  |  | SI | Observaciones |
| Q39 | - |  |  | SI | Derivado a |
| Q40 | - |  |  | SI | Especifique |
| Q41 | - |  |  | SI | PROXIMO EFM |
| Q42 | - |  |  | SI | Actividad Realizada |
| Q43 | - |  |  | SI | Examen Mamario |
| QRQuest | - |  |  | SI | Resultado Examen Físico Mamario |
| QRQuestObsDR | - |  |  | SI | Resultado Examen Físico Mamario DR |
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