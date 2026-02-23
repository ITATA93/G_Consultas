# SQLUser.CT_TimelineEvent

**Schema:** SQLUser
**Columnas:** 101
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TLEV_RowID | bigint | PK |  | NO | - |
| CQ33 | - |  |  | SI | (null) |
| CQ39 | - |  |  | SI | (null) |
| CQ6 | - |  |  | SI | (null) |
| Q1 | - |  |  | SI | Número o identificación de tubo |
| Q10 | - |  |  | SI | Otro |
| Q11 | - |  |  | SI | Sobrio |
| Q12 | - |  |  | SI | Aliento Etílico |
| Q13 | - |  |  | SI | Ebriedad Manifiesta |
| Q14 | - |  |  | SI | Estado de Coma |
| Q16 | - |  |  | SI | Prescencia de Drogas old |
| Q17 | - |  |  | SI | Otras |
| Q19 | - |  |  | SI | RUT o RUN |
| Q2 | - |  |  | SI | Fecha toma de muestra |
| Q20 | - |  |  | SI | Persona que tomó la muestra |
| Q21 | - |  |  | SI | N° de parte policial |
| Q22 | - |  |  | SI | Fiscalía o tribunal receptor del parte |
| Q3 | - |  |  | SI | Hora de la toma de muestra |
| Q30 | - |  |  | SI | Rechaza toma de muestra old |
| Q31 | - |  |  | SI | Hora del suceso que motiva el Exámen |
| Q33 | - |  |  | SI | Apreciación Clínica |
| Q34 | - |  |  | SI | Comisaria |
| Q35 | - |  |  | SI | Comuna |
| Q36 | - |  |  | SI | Número de Boleta |
| Q37 | - |  |  | SI | Provincia |
| Q38 | - |  |  | SI | Condición en el tránsito de la persona a quien se ... |
| Q39 | - |  |  | SI | Grado de Ebriedad old |
| Q4 | - |  |  | SI | Nombre Completo |
| Q40 | - |  |  | SI | Año |
| Q41 | - |  |  | SI | Fecha y hora del suceso que motiva el examen |
| Q42 | - |  |  | SI | Nombre |
| Q43 | - |  |  | SI | Comisaría o unidad policial emisora del parte |
| Q44 | - |  |  | SI | Respecto del grado de ebriedad |
| Q45 | - |  |  | SI | Presencia de TEC |
| Q46 | - |  |  | SI | Presencia de Drogas |
| Q47 | - |  |  | SI | Rechaza Toma de Muestra |
| Q5 | - |  |  | SI | Cédula de Identidad N° |
| Q6 | - |  |  | SI | Sexo |
| Q7 | - |  |  | SI | Edad |
| Q8 | - |  |  | SI | Peatón |
| Q9 | - |  |  | SI | Conductor |
| QCPN | - |  |  | SI | N° placa func. policial |
| QHospitalDR | - |  |  | SI | Hospital ID |
| QNOMED | - |  |  | SI | Nombre del Médico |
| QOB | - |  |  | SI | Presenta TEC old |
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
| TLEV_Code | varchar |  |  | NO | Code |
| TLEV_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| TLEV_Color | varchar |  |  | NO | Color of the Event/Interval |
| TLEV_CreatedDate | date |  |  | SI | Created Date |
| TLEV_CreatedTime | time |  |  | SI | Created Time |
| TLEV_CreatedUser_DR | bigint |  | FK | SI | Created User |
| TLEV_DateFrom | date |  |  | NO | Date From |
| TLEV_DateTo | date |  |  | SI | Date To |
| TLEV_Desc | varchar |  |  | NO | Description |
| TLEV_Event | varchar |  |  | NO | The specific event type |
| TLEV_Owner | varchar |  |  | SI | Owner |
| TLEV_Purpose | varchar |  |  | SI | Purpose of the Event/Interval |
| TLEV_TimelineEventGroup_DR | bigint |  | FK | NO | Timeline Event Group |
| TLEV_UpdatedDate | date |  |  | SI | Updated Date |
| TLEV_UpdatedTime | time |  |  | SI | Updated Time |
| TLEV_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*