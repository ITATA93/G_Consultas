# SQLUser.MRC_ICDLocation

**Schema:** SQLUser
**Columnas:** 100
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LOC_ParREf | bigint | PK |  | NO | MRC_ICDDx Parent Reference |
| LOC_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| LOC_Childsub | double |  |  | NO | Childsub |
| LOC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LOC_CreatedDate | date |  |  | SI | Created Date |
| LOC_CreatedTime | time |  |  | SI | Created Time |
| LOC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LOC_RowId | varchar |  |  | NO | - |
| LOC_UpdatedDate | date |  |  | SI | Updated Date |
| LOC_UpdatedTime | time |  |  | SI | Updated Time |
| LOC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Autonomo |
| Q02 | - |  |  | SI | Total |
| Q03 | - |  |  | SI | Parcial |
| Q04 | - |  |  | SI | Adecuada |
| Q05 | - |  |  | SI | Inadecuada |
| Q06 | - |  |  | SI | Habito de Higene |
| Q07 | - |  |  | SI | Arreglado |
| Q08 | - |  |  | SI | Descuidado |
| Q09 | - |  |  | SI | Piel Integra |
| Q10 | - |  |  | SI | Fria |
| Q11 | - |  |  | SI | Sudorosa |
| Q12 | - |  |  | SI | Normal |
| Q13 | - |  |  | SI | Palida |
| Q14 | - |  |  | SI | Icterica |
| Q15 | - |  |  | SI | Cianotica |
| Q16 | - |  |  | SI | Detalle |
| Q17 | - |  |  | SI | Edemas |
| Q18 | - |  |  | SI | Detalle |
| Q19 | - |  |  | SI | Signo de pliegue positivo |
| Q20 | - |  |  | SI | Linfedema |
| Q21 | - |  |  | SI | Heridas |
| Q22 | - |  |  | SI | Localizacion |
| Q23 | - |  |  | SI | Tipo |
| Q24 | - |  |  | SI | Flebitis |
| Q25 | - |  |  | SI | Localizacion |
| Q26 | - |  |  | SI | Estadio |
| Q27 | - |  |  | SI | Varices |
| Q28 | - |  |  | SI | Ulceras por presion |
| Q29 | - |  |  | SI | Localizacion |
| Q30 | - |  |  | SI | Estadio |
| Q31 | - |  |  | SI | Tamaño |
| Q32 | - |  |  | SI | Otras alteraciones de la piel |
| Q33 | - |  |  | SI | Detalle |
| Q34 | - |  |  | SI | Cateteres |
| Q35 | - |  |  | SI | Localizacion |
| Q36 | - |  |  | SI | Tipo |
| Q37 | - |  |  | SI | Fecha |
| Q38 | - |  |  | SI | Diagnostico 1 |
| Q39 | - |  |  | SI | Diagnostico 2 |
| Q40 | - |  |  | SI | Conclusión |
| Q41 | - |  |  | SI | Objetivo Registro |
| Q42 | - |  |  | SI | Higiene |
| Q43 | - |  |  | SI | Higiene Corporal Integridad de la Piel |
| Q44 | - |  |  | SI | Higiene Adecuada |
| Q45 | - |  |  | SI | Arreglo Personal |
| Q46 | - |  |  | SI | Color de la Piel |
| Q47 | - |  |  | SI | Detalle Ictérica |
| Q48 | - |  |  | SI | Detalle Cianótica |
| Q49 | - |  |  | SI | Localización de Varices |
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