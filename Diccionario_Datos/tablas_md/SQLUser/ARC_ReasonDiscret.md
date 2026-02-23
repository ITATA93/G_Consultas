# SQLUser.ARC_ReasonDiscret

**Schema:** SQLUser
**Columnas:** 93
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| READIS_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Instrumento de Evaluación de Salud Oral (OHAT) par... |
| Q02 | - |  |  | SI | Cuidados Primarios |
| Q03 | - |  |  | SI | Tipo de Evaluación |
| Q04 | - |  |  | SI | NOTA: Una estrella * indica que se requiere la der... |
| Q05 | - |  |  | SI | Categoría |
| Q06 | - |  |  | SI | 0 = Saludable |
| Q07 | - |  |  | SI | 1 = Cambios |
| Q08 | - |  |  | SI | 2 = Enfermo |
| Q09 | - |  |  | SI | Labios |
| Q10 | - |  |  | SI | Intervención |
| Q11 | - |  |  | SI | Derivar a |
| Q12 | - |  |  | SI | Lengua |
| Q13 | - |  |  | SI | Intervención |
| Q14 | - |  |  | SI | Derivar a |
| Q15 | - |  |  | SI | Encías y tejidos |
| Q16 | - |  |  | SI | Intervención |
| Q17 | - |  |  | SI | Derivar a |
| Q18 | - |  |  | SI | Saliva |
| Q19 | - |  |  | SI | Intervención |
| Q20 | - |  |  | SI | Derivar a |
| Q21 | - |  |  | SI | Otro |
| Q22 | - |  |  | SI | Dientes Naturales |
| Q23 | - |  |  | SI | Dientes naturales |
| Q24 | - |  |  | SI | Derivar a |
| Q25 | - |  |  | SI | Prótesis dental |
| Q26 | - |  |  | SI | Prótesis dental |
| Q27 | - |  |  | SI | Intervención |
| Q28 | - |  |  | SI | Identificar la prótesis |
| Q29 | - |  |  | SI | Derivar a |
| Q30 | - |  |  | SI | Otro |
| Q31 | - |  |  | SI | Higiene oral |
| Q32 | - |  |  | SI | Intervención |
| Q33 | - |  |  | SI | Derivar a |
| Q34 | - |  |  | SI | Otro |
| Q35 | - |  |  | SI | Dolor dental |
| Q36 | - |  |  | SI | Derivar a |
| Q37 | - |  |  | SI | Otro |
| Q38 | - |  |  | SI | Otro |
| Q39 | - |  |  | SI | otro |
| Q40 | - |  |  | SI | otro |
| Q41 | - |  |  | SI | Otro |
| Q42 | - |  |  | SI | Notas |
| Q43 | - |  |  | SI | Completado por |
| Q44 | - |  |  | SI | Fecha |
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
| READIS_Code | varchar |  |  | NO | Code |
| READIS_CreatedDate | date |  |  | SI | Created Date |
| READIS_CreatedTime | time |  |  | SI | Created Time |
| READIS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| READIS_Desc | varchar |  |  | NO | Description |
| READIS_UpdatedDate | date |  |  | SI | Updated Date |
| READIS_UpdatedTime | time |  |  | SI | Updated Time |
| READIS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*