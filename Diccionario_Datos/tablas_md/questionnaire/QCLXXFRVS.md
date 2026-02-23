# questionnaire.QCLXXFRVS

> Formulario de Registro de Violencia Sexual

**Schema:** questionnaire
**Columnas:** 111
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Formulario de Registro de Violencia Sexual

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | EXPLORACIÓN |
| Q02 | varchar |  |  | SI | 1. Anamnesis |
| Q03 | varchar |  |  | SI | Nombre |
| Q04 | varchar |  |  | SI | Apellido Paterno |
| Q05 | varchar |  |  | SI | Apellido Materno |
| Q06 | varchar |  |  | SI | RUN |
| Q07 | varchar |  |  | SI | Edad |
| Q08 | varchar |  |  | SI | Fecha de Nacimiento |
| Q09 | varchar |  |  | SI | Domicilio |
| Q10 | varchar |  |  | SI | Comuna |
| Q11 | varchar |  |  | SI | Estado Civil |
| Q12 | varchar |  |  | SI | Nivel Educacional |
| Q13 | varchar |  |  | SI | Actividad |
| Q14 | varchar |  |  | SI | Relación con el Agresor |
| Q15 | varchar |  |  | SI | Especifique: |
| Q16 | varchar |  |  | SI | Datos del Denunciante (completar en el caso de que... |
| Q17 | varchar |  |  | SI | Nombre |
| Q18 | varchar |  |  | SI | RUN |
| Q19 | varchar |  |  | SI | Edad |
| Q20 | date |  |  | SI | Fecha de Nacimiento |
| Q21 | varchar |  |  | SI | Domicilio |
| Q22 | varchar |  |  | SI | Comuna |
| Q23 | varchar |  |  | SI | Datos del Agresor (si se conoce la información) |
| Q24 | numeric |  |  | SI | Número de agresores:  |
| Q26 | bit |  |  | SI | No se cuenta con esta información |
| Q27 | varchar |  |  | SI | Descripción del suceso |
| Q28 | date |  |  | SI | Fecha / Hora del Suceso |
| Q29 | time |  |  | SI | Hora del Suceso |
| Q30 | varchar |  |  | SI | (Observaciones) |
| Q31 | varchar |  |  | SI | Sospecha de penetración  |
| Q32 | varchar |  |  | SI | Si se trata de Violencia Física, precisar |
| Q33 | varchar |  |  | SI | Relato del suceso |
| Q34 | varchar |  |  | SI | 2. Antecedentes Relevantes |
| Q35 | numeric |  |  | SI | Edad de Menarquia |
| Q36 | date |  |  | SI | Fecha de Última Regla |
| Q37 | varchar |  |  | SI | ¿Cursando Embarazo actual? |
| Q38 | varchar |  |  | SI | Método Anticonceptivo |
| Q39 | varchar |  |  | SI | Historia previa de Abuso Sexual |
| Q40 | varchar |  |  | SI | Observaciones |
| Q41 | varchar |  |  | SI | 3. Examen Fïsico |
| Q42 | varchar |  |  | SI | Examen Físico General |
| Q43 | varchar |  |  | SI | Examinación Genitales |
| Q44 | varchar |  |  | SI | Examinación Región Anal |
| Q45 | varchar |  |  | SI | Ecotomografía / Colposcopía |
| Q46 | varchar |  |  | SI | 4. Exámenes para el peritaje de Agresión Sexual |
| Q47 | varchar |  |  | SI | Muestras solicitadas para análisis: |
| Q48 | varchar |  |  | SI | Otros |
| Q49 | varchar |  |  | SI | CONCLUSIONES |
| Q50 | varchar |  |  | SI | Conclusiones |
| Q51 | varchar |  |  | SI | Pronóstico Médico-Legal |
| Q52 | varchar |  |  | SI | TRATAMIENTO |
| Q53 | varchar |  |  | SI | Con entrega de anticoncepción de emergencia  |
| Q54 | varchar |  |  | SI | Con profilaxis ITS  |
| Q55 | varchar |  |  | SI | Con profilaxis VIH  |
| Q56 | varchar |  |  | SI | Otros tratamientos |
| Q57 | varchar |  |  | SI | DATOS DEL PROFESIONAL |
| Q58 | varchar |  |  | SI | Nombre del Profesional: |
| Q59 | varchar |  |  | SI | RUN del Profesional |
| Q60 | varchar |  |  | SI | Tipo de Profesional |
| Q61 | date |  |  | SI | Fecha de Registro del Documento |
| Q62 | time |  |  | SI | Hora de Registro del documento |
| Q63 | varchar |  |  | SI | ¿Usuario recibió capacitación en Peritaje Forense? |
| Q64 | varchar |  |  | SI | Violencia Física |
| Q65 | varchar |  |  | SI | Comentario Prevención Embarazo |
| Q66 | varchar |  |  | SI | Comentario Prevención Infecciones |
| Q67 | varchar |  |  | SI | Comentario Prevención VIH |
| Q68 | varchar |  |  | SI | Sexo del Agresor |
| Q69 | varchar |  |  | SI | ¿Usuario pertenece al Registro Nacional de Peritos... |
| Q70 | varchar |  |  | SI | Con profilaxis Hepatitis B |
| Q71 | varchar |  |  | SI | Comentario profilaxis Hepatitis B |
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