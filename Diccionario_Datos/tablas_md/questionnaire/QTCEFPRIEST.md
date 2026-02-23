# questionnaire.QTCEFPRIEST

> Ficha Ingreso Personas Con Dependencia Severa

**Schema:** questionnaire
**Columnas:** 95
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ficha Ingreso Personas Con Dependencia Severa

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Asignación del Estipendio |
| Q02 | varchar |  |  | SI | Resultado Indice Barthel |
| Q02ObsDR | varchar |  | FK | SI | Resultado Indice Barthel DR |
| Q03 | varchar |  |  | SI | Previsión |
| Q04 | varchar |  |  | SI | PRAIS |
| Q05 | varchar |  |  | SI | Chile Solidario |
| Q06 | varchar |  |  | SI | PASIS |
| Q07 | varchar |  |  | SI | Ficha Protección Social Menor a 8.500 pts. |
| Q08 | varchar |  |  | SI | Corresponde Estipendio |
| Q09 | varchar |  |  | SI | Asigna Estipendio |
| Q10 | varchar |  |  | SI | Antecedentes del cuidador |
| Q11 | varchar |  |  | SI | Rut Cuidador |
| Q12 | varchar |  |  | SI | Apellidos del Cuidador |
| Q13 | varchar |  |  | SI | Nombre del Cuidador |
| Q14 | date |  |  | SI | Fecha de Nacimiento del Cuidador |
| Q15 | varchar |  |  | SI | Género´del Cuidador |
| Q16 | varchar |  |  | SI | Estado Civil del Cuidador |
| Q17 | varchar |  |  | SI | Domicilio del Cuidador |
| Q18 | varchar |  |  | SI | Población/Villa |
| Q19 | varchar |  |  | SI | E-Mail |
| Q20 | varchar |  |  | SI | Escolaridad |
| Q21 | varchar |  |  | SI | Relación/Parentesco |
| Q22 | varchar |  |  | SI | Otro (Especifique) |
| Q23 | varchar |  |  | SI | Previsión del Cuidador |
| Q24 | numeric |  |  | SI | Teléfono Fijo |
| Q25 | numeric |  |  | SI | Celular |
| Q26 | varchar |  |  | SI | Postrado Oncológico |
| Q27 | varchar |  |  | SI | Programa alivio dolor |
| Q28 | varchar |  |  | SI | Uso oxigenoterapia |
| Q29 | varchar |  |  | SI | Oxigenoterapia Observaciones |
| Q30 | varchar |  |  | SI | Diáisis |
| Q31 | varchar |  |  | SI | Diálisis Observaciones |
| Q33 | varchar |  |  | SI | Condición sensorial |
| Q34 | varchar |  |  | SI | Estado de conciencia |
| Q35 | varchar |  |  | SI | Vías de comunicación |
| Q36 | varchar |  |  | SI | Alimentación |
| Q37 | varchar |  |  | SI | Cavidad bucal |
| Q38 | varchar |  |  | SI | Continencia |
| Q39 | varchar |  |  | SI | Formas de apoyo a incontinencia |
| Q40 | varchar |  |  | SI | Tendencia a fecalomas |
| Q41 | varchar |  |  | SI | Amputaciónes u ortesis |
| Q42 | varchar |  |  | SI | Estado nutricional |
| Q44 | varchar |  |  | SI | Prevención de UPP |
| Q45 | numeric |  |  | SI | Cantidad |
| Q46 | varchar |  |  | SI | Localización |
| Q47 | varchar |  |  | SI | Grado o tipo |
| Q48 | varchar |  |  | SI | Breve descripción |
| Q49 | varchar |  |  | SI | Factores de Riesgo Más Importantes |
| Q50 | varchar |  |  | SI | Aseo (Uñas) |
| Q51 | varchar |  |  | SI | Cortes (Uñas) |
| Q52 | varchar |  |  | SI | Alteraciones (Uñas) |
| Q60 | varchar |  |  | SI | Tipo de Pensión |
| Q61 | varchar |  |  | SI | Estado de Uñas |
| Q62 | varchar |  |  | SI | Presencia de Heridas |
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