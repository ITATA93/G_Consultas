# questionnaire.QTCEVIHPED

> Formulario de Envío de Muestra para Confirmación de VIH Pediátrico

**Schema:** questionnaire
**Columnas:** 98
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Formulario de Envío de Muestra para Confirmación de VIH Pediátrico

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Clave Definitiva |
| Q02 | varchar |  |  | SI | RUT |
| Q03 | varchar |  |  | SI | Clave Recién Nacido |
| Q04 | varchar |  |  | SI | Sexo |
| Q05 | varchar |  |  | SI | Edad |
| Q06 | varchar |  |  | SI | Años |
| Q07 | varchar |  |  | SI | Días |
| Q08 | varchar |  |  | SI | Clave Materna |
| Q09 | varchar |  |  | SI | N° ISP Materno |
| Q10 | varchar |  |  | SI | Cod. Establecimiento |
| Q11 | varchar |  |  | SI | Profesional Responsable |
| Q12 | varchar |  |  | SI | Hospital / Laboratorio |
| Q13 | varchar |  |  | SI | Unidad |
| Q14 | varchar |  |  | SI | RUT Profesional |
| Q15 | varchar |  |  | SI | Dirección |
| Q16 | varchar |  |  | SI | Región |
| Q17 | varchar |  |  | SI | Comuna |
| Q18 | varchar |  |  | SI | Fono |
| Q19 | varchar |  |  | SI | Fax |
| Q20 | varchar |  |  | SI | Mail |
| Q21 | date |  |  | SI | Fecha de Obtención |
| Q22 | time |  |  | SI | Hora |
| Q23 | varchar |  |  | SI | Tipo de Muestra |
| Q24 | varchar |  |  | SI | N° de Muestra |
| Q25 | varchar |  |  | SI | Otro |
| Q26 | varchar |  |  | SI | Cod.SurVIH |
| Q27 | varchar |  |  | SI | Datos Clínicos |
| Q28 | varchar |  |  | SI | Diagnóstico |
| Q29 | varchar |  |  | SI | Protocolo de transmisión vertical |
| Q30 | varchar |  |  | SI | Terapia |
| Q31 | bit |  |  | SI | Madre VIH (+) |
| Q32 | varchar |  |  | SI | Otro Factor |
| Q33 | varchar |  |  | SI | Clave 2 |
| Q34 | varchar |  |  | SI | Clave 3 |
| Q35 | varchar |  |  | SI | Clave 4 |
| Q36 | varchar |  |  | SI | Meses |
| Q37 | varchar |  |  | SI | Años |
| Q38 | varchar |  |  | SI | Sexo |
| Q39 | varchar |  |  | SI | RUT de la madre |
| Q40 | varchar |  |  | SI | Nacionalidad de la madre |
| Q41 | varchar |  |  | SI | 4.1 Técnica Visual |
| Q42 | varchar |  |  | SI | Otra |
| Q43 | varchar |  |  | SI | Lote |
| Q44 | date |  |  | SI | Vencimiento |
| Q45 | varchar |  |  | SI | 4.2 Técnica Instrumental |
| Q46 | varchar |  |  | SI | Otra |
| Q47 | varchar |  |  | SI | Reactividad |
| Q48 | varchar |  |  | SI | Cut-Off |
| Q49 | varchar |  |  | SI | Reactividad 2 |
| Q50 | varchar |  |  | SI | Cut-Off 2 |
| Q51 | varchar |  |  | SI | Reactividad 3 |
| Q52 | varchar |  |  | SI | Cut-Off 3 |
| Q53 | varchar |  |  | SI | Lote |
| Q54 | date |  |  | SI | Vencimiento |
| Q55 | bit |  |  | SI | Hijo de Madre en Proceso de Confirmación VIH |
| Q56 | varchar |  |  | SI | Nacionalidad |
| Q57 | varchar |  |  | SI | N° Solicitud |
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