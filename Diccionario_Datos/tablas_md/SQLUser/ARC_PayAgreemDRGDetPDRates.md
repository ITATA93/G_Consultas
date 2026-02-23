# SQLUser.ARC_PayAgreemDRGDetPDRates

**Schema:** SQLUser
**Columnas:** 108
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PDR_ParRef | varchar | PK |  | NO | ARC_PayAgreemDRGDetails Parent Reference |
| PDR_Childsub | double |  |  | NO | Childsub |
| PDR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PDR_CreatedDate | date |  |  | SI | Created Date |
| PDR_CreatedTime | time |  |  | SI | Created Time |
| PDR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PDR_DayFrom | double |  |  | SI | Day From |
| PDR_DayTo | double |  |  | SI | Day To |
| PDR_Rate | double |  |  | SI | Rate |
| PDR_RowId | varchar |  |  | NO | - |
| PDR_UpdatedDate | date |  |  | SI | Updated Date |
| PDR_UpdatedTime | time |  |  | SI | Updated Time |
| PDR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| PD_OverrideBillGrp_DR | bigint |  | FK | SI | Des Ref ARCBillGrp |
| PD_OverrideBillSub_DR | varchar |  | FK | SI | Des Ref ARCBillSub |
| PD_OverrideDesc | varchar |  |  | SI | Description |
| PD_PayorCode | varchar |  |  | SI | Payor Code  |
| Q01 | - |  |  | SI | Nivel |
| Q02 | - |  |  | SI | 10 |
| Q03 | - |  |  | SI | 9 |
| Q04 | - |  |  | SI | 8 |
| Q05 | - |  |  | SI | 7 |
| Q06 | - |  |  | SI | 6 |
| Q07 | - |  |  | SI | 5 |
| Q08 | - |  |  | SI | 4 |
| Q09 | - |  |  | SI | 3 |
| Q10 | - |  |  | SI | 2 |
| Q11 | - |  |  | SI | 1 |
| Q12 | - |  |  | SI | Eficiencia (***) |
| Q13 | - |  |  | SI | Ambiente (*) |
| Q14 | - |  |  | SI | Contenido (**) |
| Q15 | - |  |  | SI | Eficiencia |
| Q16 | - |  |  | SI | Ambiente |
| Q17 | - |  |  | SI | Contenido |
| Q18 | - |  |  | SI | Eficiencia |
| Q19 | - |  |  | SI | Ambiente |
| Q20 | - |  |  | SI | Contenido |
| Q21 | - |  |  | SI | Eficiencia |
| Q22 | - |  |  | SI | Ambiente |
| Q23 | - |  |  | SI | Contenido |
| Q24 | - |  |  | SI | Eficiencia |
| Q25 | - |  |  | SI | Ambiente |
| Q26 | - |  |  | SI | Contenido |
| Q27 | - |  |  | SI | Eficiencia |
| Q28 | - |  |  | SI | Ambiente |
| Q29 | - |  |  | SI | Contenido |
| Q30 | - |  |  | SI | Eficiencia |
| Q31 | - |  |  | SI | Ambiente |
| Q32 | - |  |  | SI | Contenido |
| Q33 | - |  |  | SI | Eficiencia |
| Q34 | - |  |  | SI | Ambiente |
| Q35 | - |  |  | SI | Contenido |
| Q36 | - |  |  | SI | Eficiencia |
| Q37 | - |  |  | SI | Ambiente |
| Q38 | - |  |  | SI | Contenido |
| Q39 | - |  |  | SI | Normal en todos los ambientes sin restricciones de... |
| Q40 | - |  |  | SI | A veces (#) reducida frente a condiciones adversas... |
| Q41 | - |  |  | SI | A veces reducida frente a condiciones ideales cuan... |
| Q42 | - |  |  | SI | A veces reducida frente a condiciones adversas aún... |
| Q43 | - |  |  | SI | A veces reducida en condiciones ideales cuando no ... |
| Q44 | - |  |  | SI | Usualmente (##) reducida bajo condiciones adversas... |
| Q45 | - |  |  | SI | Usualmente reducida bajo condiciones ideales, aún ... |
| Q46 | - |  |  | SI | Usualmente reducida bajo condiciones adversas aún ... |
| Q47 | - |  |  | SI | Usualmente reducida en condiciones ideales aún cua... |
| Q48 | - |  |  | SI | El habla no es un medio viable de comunicación en ... |
| Q49 | - |  |  | SI | Eficiencia |
| Q50 | - |  |  | SI | Estado de la Inteligibilidad |
| Q51 | - |  |  | SI | Nivel |
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