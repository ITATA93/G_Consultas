# questionnaire.QCLXXNISUIC

> Informe Ficha Personal de Intento de Suicidio

**Schema:** questionnaire
**Columnas:** 95
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Informe Ficha Personal de Intento de Suicidio

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | 1. Identificacion Individual |
| Q02 | varchar |  |  | SI | Nombre |
| Q03 | varchar |  |  | SI | Sexo |
| Q04 | varchar |  |  | SI | Fecha de Nacimiento |
| Q05 | varchar |  |  | SI | Edad |
| Q06 | varchar |  |  | SI | RUN |
| Q07 | numeric |  |  | SI | N° de Hijos |
| Q08 | varchar |  |  | SI | Educacion |
| Q09 | varchar |  |  | SI | Actividad |
| Q10 | varchar |  |  | SI | Otra Actividad |
| Q11 | varchar |  |  | SI | Domicilio |
| Q12 | varchar |  |  | SI | Comuna |
| Q13 | varchar |  |  | SI | N° Ficha Clínica |
| Q14 | varchar |  |  | SI | Centro de Salud de su Domicilio |
| Q15 | varchar |  |  | SI | 2. Relativos a Intento de Suicidio |
| Q16 | date |  |  | SI | Fecha de Intento de Suicidio |
| Q17 | varchar |  |  | SI | Causa |
| Q18 | varchar |  |  | SI | Método utilizado en el intento |
| Q19 | varchar |  |  | SI | Fue derivada/o a Psiquiatra después del intento |
| Q20 | varchar |  |  | SI | Fue derivado a Equipo de Salud Mental del Centro d... |
| Q21 | varchar |  |  | SI | ¿Cuál? |
| Q22 | varchar |  |  | SI | Establecimiento de Salud donde se realiza la atenc... |
| Q23 | varchar |  |  | SI | En caso que no recibio atencion en un Establecimie... |
| Q24 | varchar |  |  | SI | Profesor |
| Q25 | varchar |  |  | SI | Carabinero |
| Q26 | varchar |  |  | SI | Otro |
| Q27 | varchar |  |  | SI | 3. Antecedentes de Salud de la Persona con Intento... |
| Q28 | varchar |  |  | SI | Padece de enfermedad física |
| Q29 | varchar |  |  | SI | Padece de enfermedad mental |
| Q30 | varchar |  |  | SI | Esta en tratamiento por la enfermedad mental |
| Q31 | varchar |  |  | SI | En que Establecimiento está en tratamiento por la ... |
| Q32 | varchar |  |  | SI | Consume drogas |
| Q33 | varchar |  |  | SI | Maltrato infantil |
| Q34 | varchar |  |  | SI | VIF |
| Q35 | varchar |  |  | SI | 4.  Relativos a la Persona con Intento de Suicidio... |
| Q36 | varchar |  |  | SI | La persona individualizada ha realizado con anteri... |
| Q37 | varchar |  |  | SI | Intentos de Suicidios |
| Q38 | numeric |  |  | SI | ¿Cuántos? |
| Q39 | varchar |  |  | SI | Hay intentos de suicidio en la familia |
| Q40 | varchar |  |  | SI | Hay suicidios en la familia |
| Q42 | varchar |  |  | SI | 5. Familiar que estaría dispuesta/o a entregar may... |
| Q43 | varchar |  |  | SI | Nombre |
| Q44 | numeric |  |  | SI | Telefono |
| Q45 | varchar |  |  | SI | Direccion |
| Q46 | varchar |  |  | SI | 6. Funcionario responsable de la Informacion |
| Q47 | varchar |  |  | SI | Nombre Completo |
| Q48 | varchar |  |  | SI | RUN |
| Q49 | varchar |  |  | SI | Cargo |
| Q50 | varchar |  |  | SI | Establecimiento |
| Q51 | varchar |  |  | SI | Comuna |
| Q52 | date |  |  | SI | Fecha |
| Q53 | varchar |  |  | SI | Apellido Paterno |
| Q54 | varchar |  |  | SI | Apellido Materno |
| Q55 | varchar |  |  | SI | ¿Qué funcionario/s realiza la atencion de urgencia... |
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