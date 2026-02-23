# questionnaire.QTCEFMEN

> Formulario de Notificación Inmediata de caso de Meningitis Bacteriana Enfermedad Meningocóccica y Enfermedad Invasiva por Haemophilus Influenzae

**Schema:** questionnaire
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Formulario de Notificación Inmediata de caso de Meningitis Bacteriana Enfermedad Meningocóccica y Enfermedad Invasiva por Haemophilus Influenzae

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Seremi Región |
| Q02 | varchar |  |  | SI | Servicio Salud |
| Q03 | varchar |  |  | SI | Oficina Provincial |
| Q04 | varchar |  |  | SI | Establecimiento |
| Q05 | date |  |  | SI | Fecha Notificación |
| Q06 | varchar |  |  | SI | Fecha Validación SEREMI |
| Q07 | varchar |  |  | SI | Médico Tratante |
| Q08 | varchar |  |  | SI | Persona que Notifica |
| Q09 | numeric |  |  | SI | Teléfono |
| QCF49 | varchar |  |  | SI | CLASIFICACIÓN FINAL |
| QCF50 | varchar |  |  | SI | Confirmado o Descartado por |
| QCF51 | varchar |  |  | SI | Por Laboratorio |
| QIC10 | varchar |  |  | SI | Embarazo |
| QIC11 | varchar |  |  | SI | Semana de Gestación |
| QIC12 | varchar |  |  | SI | Ocupación |
| QIC14 | varchar |  |  | SI | Pertenencia declarada a algún prueblo originario |
| QIC15 | varchar |  |  | SI | Nacionalidad |
| QIEP39 | date |  |  | SI | Fecha Tratamiento de Contactos |
| QIEP45 | varchar |  |  | SI | Corresponde |
| QIEP46 | varchar |  |  | SI | Si corresponde, Institución donde se realizó el Bl... |
| QINFC16 | numeric |  |  | SI | N° de Historia Clínica |
| QINFC17 | date |  |  | SI | Fecha Primeros Síntomas |
| QINFC18 | date |  |  | SI | Fecha Primera Consulta |
| QINFC19 | date |  |  | SI | Fecha Hospitalización |
| QINFC20 | varchar |  |  | SI | Est. Hospitalización |
| QINFC21 | varchar |  |  | SI | Establecimiento Derivación |
| QINFC22 | varchar |  |  | SI | Diagnóstico de Ingreso |
| QINFC23 | varchar |  |  | SI | Caso |
| QINFC24 | varchar |  |  | SI | Nombre Caso Primario |
| QINFC27 | varchar |  |  | SI | Fallecido |
| QINFC28 | date |  |  | SI | Fecha Fallecimiento |
| QINFC29 | varchar |  |  | SI | Cuál |
| QINFL30 | date |  |  | SI | Fecha Toma de Muestra |
| QINFL31 | varchar |  |  | SI | LATEX Resultado |
| QINFL32 | varchar |  |  | SI | GRAM Resultado |
| QINFL33 | varchar |  |  | SI | CULTIVO LCR Resultado |
| QINFL34 | varchar |  |  | SI | HEMOCULTIVO Resultado |
| QINFL35 | varchar |  |  | SI | Otro Resultado |
| QINFL36 | date |  |  | SI | Fecha de Envío al ISP |
| QINFL37 | varchar |  |  | SI | Resultado ISP |
| QINFL38 | varchar |  |  | SI | Resultado Exámenes |
| QLOC51 | varchar |  |  | SI | Localización (Aplica en Enf. Meningocóccica o Enf.... |
| QLOC52 | varchar |  |  | SI | Otra (Especifique) |
| QLOC54 | varchar |  |  | SI | País |
| QOBS55 | varchar |  |  | SI | Observaciones |
| QPC53 | varchar |  |  | SI | País de Contagio |
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