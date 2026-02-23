# questionnaire.QTCEBRADEN

> Escala de Braden para la Predicción de úlceras por Presión

**Schema:** questionnaire
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Escala de Braden para la Predicción de úlceras por Presión

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Servicio |
| Q02 | varchar |  |  | SI | Percepción Sensorial |
| Q03 | varchar |  |  | SI | Movilidad |
| Q04 | varchar |  |  | SI | Actividad |
| Q05 | varchar |  |  | SI | Humedad |
| Q06 | varchar |  |  | SI | Nutrición |
| Q07 | varchar |  |  | SI | Fuerzas de fricción y cizalla |
| Q08 | varchar |  |  | SI | Reevaluación |
| Q09 | varchar |  |  | SI | Información a familiar (Primer Contacto) |
| Q10 | date |  |  | SI | Fecha de información a familia |
| Q11 | varchar |  |  | SI | Aceptación de Medidas |
| Q12 | varchar |  |  | SI | Nombre del Familiar |
| Q13 | varchar |  |  | SI | Nombre Responsable |
| Q14 | varchar |  |  | SI | Grado |
| Q14ObsDR | varchar |  | FK | SI | Grado DR |
| Q15 | varchar |  |  | SI | Etiqueta Riesgo Bajo |
| Q16 | varchar |  |  | SI | Etiqueta Riesgo Moderado |
| Q17 | varchar |  |  | SI | Etiqueta Riesgo Alto |
| Q18 | varchar |  |  | SI | Se realizan medidas según riesgo evaluado |
| Q19 | varchar |  |  | SI | Razón de No Realización |
| Q20 | varchar |  |  | SI | Servicio |
| Q21 | date |  |  | SI | Fecha de la Actividad |
| Q22 | time |  |  | SI | Hora de la Actividad |
| Q30 | varchar |  |  | SI | Examen de Piel: Valoración Diaria |
| Q31 | varchar |  |  | SI | Higiene de la Piel: Diario 3 veces/día |
| Q32 | varchar |  |  | SI | Cambios Posturales: Cada 2 horas |
| Q33 | varchar |  |  | SI | Superficies de Apoyo: Dinámicas  |
| Q35 | varchar |  |  | SI | Examen de Piel: Valoración Diaria |
| Q36 | varchar |  |  | SI | Higiene de la Piel: Diario 2 veces/día |
| Q37 | varchar |  |  | SI | Cambios Posturales: Cada 2-3 horas |
| Q38 | varchar |  |  | SI | Superficie de Apoyo: Dinámicas |
| Q40 | varchar |  |  | SI | Examen de Piel: Valoración Diaria |
| Q41 | varchar |  |  | SI | Higiene de la Piel: Diario 2 veces/día |
| Q42 | varchar |  |  | SI | Cambios Posturales: Cada 4 horas |
| Q43 | varchar |  |  | SI | Superficies de Apoyo: Estáticas |
| Q44 | varchar |  |  | SI | Cada 7 días |
| Q45 | varchar |  |  | SI | Cada 3 días |
| Q46 | varchar |  |  | SI | Cada 7 días |
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