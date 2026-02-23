# SQLUser.LB_QCReview

**Schema:** SQLUser
**Columnas:** 113
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBQCRE_RowID | bigint | PK |  | NO | - |
| LBQCRE_Comments | varchar |  |  | SI | Review comments |
| LBQCRE_CorrectiveAction_DR | bigint |  | FK | SI | Review Corrective Action |
| LBQCRE_Date | date |  |  | SI | Review Date |
| LBQCRE_RootCause_DR | bigint |  | FK | SI | Review Root Cause |
| LBQCRE_RunData | varchar |  |  | SI | List of run data included in review  |
| LBQCRE_Time | time |  |  | SI | Review Time |
| LBQCRE_Type_DR | bigint |  | FK | SI | Review Type |
| LBQCRE_User_DR | bigint |  | FK | SI | Review User |
| Q01 | - |  |  | SI | Clave |
| Q02 | - |  |  | SI | RUT |
| Q03 | - |  |  | SI | Edad |
| Q04 | - |  |  | SI | Sexo |
| Q05 | - |  |  | SI | Nacionalidad |
| Q06 | - |  |  | SI | Profesional Responsable |
| Q07 | - |  |  | SI | Hospital/Laboratorio |
| Q08 | - |  |  | SI | Unidad |
| Q09 | - |  |  | SI | RUT |
| Q10 | - |  |  | SI | Dirección |
| Q11 | - |  |  | SI | Región |
| Q12 | - |  |  | SI | Comuna |
| Q13 | - |  |  | SI | Fono |
| Q14 | - |  |  | SI | Fax |
| Q15 | - |  |  | SI | Mail |
| Q16 | - |  |  | SI | Fecha de Obtención |
| Q17 | - |  |  | SI | Hora Obtención |
| Q18 | - |  |  | SI | Tipo de Muestra |
| Q19 | - |  |  | SI | N° de Muestra |
| Q20 | - |  |  | SI | Cod. Sur VIH |
| Q21 | - |  |  | SI | Datos Clinicos |
| Q22 | - |  |  | SI | Diagnóstico |
| Q23 | - |  |  | SI | Protocolo de Transmisión Vertical |
| Q24 | - |  |  | SI | Terapia |
| Q25 | - |  |  | SI | Factor de Riesgo |
| Q26 | - |  |  | SI | Técnico Visual |
| Q27 | - |  |  | SI | Técnica Instrumental |
| Q28 | - |  |  | SI | Lote |
| Q29 | - |  |  | SI | Vencimiento |
| Q30 | - |  |  | SI | Clasificación |
| Q31 | - |  |  | SI | Otro |
| Q32 | - |  |  | SI | Reactividad 1 |
| Q33 | - |  |  | SI | Reactividad 2 |
| Q34 | - |  |  | SI | Reactividad 3 |
| Q35 | - |  |  | SI | Cut-Off 1 |
| Q36 | - |  |  | SI | Cut-Off 2 |
| Q37 | - |  |  | SI | Cut-Off 3 |
| Q38 | - |  |  | SI | Cod. Establecimiento |
| Q39 | - |  |  | SI | Otra |
| Q40 | - |  |  | SI | Otra |
| Q41 | - |  |  | SI | Otro Factor |
| Q42 | - |  |  | SI | Otra Clasificación |
| Q43 | - |  |  | SI | Clave 2 |
| Q44 | - |  |  | SI | Clave 3 |
| Q45 | - |  |  | SI | Clave 4 |
| Q46 | - |  |  | SI | RUT |
| Q47 | - |  |  | SI | RUT |
| Q48 | - |  |  | SI | Mail |
| Q49 | - |  |  | SI | Instrucciones: Inicial del 1° nombre, iniciales 1°... |
| Q50 | - |  |  | SI | Sexo |
| Q51 | - |  |  | SI | Nacionalidad |
| Q52 | - |  |  | SI | 4.1 Técnica Visual |
| Q53 | - |  |  | SI | Lote |
| Q54 | - |  |  | SI | Vencimiento |
| Q55 | - |  |  | SI | 4.2 Técnica Instrumental |
| Q56 | - |  |  | SI | Antecedentes Clínicos VIH anterior (indicar país) |
| Q57 | - |  |  | SI | Uso de TARV previo |
| Q58 | - |  |  | SI | Profilaxis Preexposición (PrEp) |
| Q59 | - |  |  | SI | Edad |
| Q60 | - |  |  | SI | Clasificación |
| Q61 | - |  |  | SI | Vencimiento |
| Q62 | - |  |  | SI | Profesional Responsable |
| Q63 | - |  |  | SI | Hospital / Laboratorio |
| Q64 | - |  |  | SI | Unidad |
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