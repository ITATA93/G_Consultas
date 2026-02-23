# questionnaire.QTCEVIH

> Formulario de envío de muestra para confirmación de VIH

**Schema:** questionnaire
**Columnas:** 105
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Formulario de envío de muestra para confirmación de VIH

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Clave |
| Q02 | varchar |  |  | SI | RUT |
| Q03 | varchar |  |  | SI | Edad |
| Q04 | varchar |  |  | SI | Sexo |
| Q05 | varchar |  |  | SI | Nacionalidad |
| Q06 | varchar |  |  | SI | Profesional Responsable |
| Q07 | varchar |  |  | SI | Hospital/Laboratorio |
| Q08 | varchar |  |  | SI | Unidad |
| Q09 | varchar |  |  | SI | RUT |
| Q10 | varchar |  |  | SI | Dirección |
| Q11 | varchar |  |  | SI | Región |
| Q12 | varchar |  |  | SI | Comuna |
| Q13 | varchar |  |  | SI | Fono |
| Q14 | varchar |  |  | SI | Fax |
| Q15 | varchar |  |  | SI | Mail |
| Q16 | date |  |  | SI | Fecha de Obtención |
| Q17 | time |  |  | SI | Hora Obtención |
| Q18 | varchar |  |  | SI | Tipo de Muestra |
| Q19 | varchar |  |  | SI | N° de Muestra |
| Q20 | varchar |  |  | SI | Cod. Sur VIH |
| Q21 | varchar |  |  | SI | Datos Clinicos |
| Q22 | varchar |  |  | SI | Diagnóstico |
| Q23 | varchar |  |  | SI | Protocolo de Transmisión Vertical |
| Q24 | varchar |  |  | SI | Terapia |
| Q25 | varchar |  |  | SI | Factor de Riesgo |
| Q26 | varchar |  |  | SI | Técnico Visual |
| Q27 | varchar |  |  | SI | Técnica Instrumental |
| Q28 | varchar |  |  | SI | Lote |
| Q29 | varchar |  |  | SI | Vencimiento |
| Q30 | varchar |  |  | SI | Clasificación |
| Q31 | varchar |  |  | SI | Otro |
| Q32 | varchar |  |  | SI | Reactividad 1 |
| Q33 | varchar |  |  | SI | Reactividad 2 |
| Q34 | varchar |  |  | SI | Reactividad 3 |
| Q35 | varchar |  |  | SI | Cut-Off 1 |
| Q36 | varchar |  |  | SI | Cut-Off 2 |
| Q37 | varchar |  |  | SI | Cut-Off 3 |
| Q38 | varchar |  |  | SI | Cod. Establecimiento |
| Q39 | varchar |  |  | SI | Otra |
| Q40 | varchar |  |  | SI | Otra |
| Q41 | varchar |  |  | SI | Otro Factor |
| Q42 | varchar |  |  | SI | Otra Clasificación |
| Q43 | varchar |  |  | SI | Clave 2 |
| Q44 | varchar |  |  | SI | Clave 3 |
| Q45 | varchar |  |  | SI | Clave 4 |
| Q46 | varchar |  |  | SI | RUT |
| Q47 | varchar |  |  | SI | RUT |
| Q48 | varchar |  |  | SI | Mail |
| Q49 | varchar |  |  | SI | Instrucciones: Inicial del 1° nombre, iniciales 1°... |
| Q50 | varchar |  |  | SI | Sexo |
| Q51 | varchar |  |  | SI | Nacionalidad |
| Q52 | varchar |  |  | SI | 4.1 Técnica Visual |
| Q53 | varchar |  |  | SI | Lote |
| Q54 | date |  |  | SI | Vencimiento |
| Q55 | varchar |  |  | SI | 4.2 Técnica Instrumental |
| Q56 | varchar |  |  | SI | Antecedentes Clínicos VIH anterior (indicar país) |
| Q57 | varchar |  |  | SI | Uso de TARV previo |
| Q58 | varchar |  |  | SI | Profilaxis Preexposición (PrEp) |
| Q59 | varchar |  |  | SI | Edad |
| Q60 | varchar |  |  | SI | Clasificación |
| Q61 | date |  |  | SI | Vencimiento |
| Q62 | varchar |  |  | SI | Profesional Responsable |
| Q63 | varchar |  |  | SI | Hospital / Laboratorio |
| Q64 | varchar |  |  | SI | Unidad |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*