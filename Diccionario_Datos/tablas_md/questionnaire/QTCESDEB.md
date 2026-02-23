# questionnaire.QTCESDEB

> Solicitud de Examen bacteriologico

**Schema:** questionnaire
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Solicitud de Examen bacteriologico

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Nombre del Paciente |
| Q02 | varchar |  |  | SI | Apellido Paterno |
| Q03 | varchar |  |  | SI | Apellido Materno |
| Q04 | varchar |  |  | SI | Fecha de Nacimiento |
| Q05 | varchar |  |  | SI | Edad  |
| Q06 | varchar |  |  | SI | Unidad |
| Q07 | varchar |  |  | SI | Sexo |
| Q08 | varchar |  |  | SI | Rut |
| Q09 | varchar |  |  | SI | Diagnostico |
| Q10 | bit |  |  | SI | Con Antibiotico |
| Q11 | bit |  |  | SI | Profilaxis |
| Q12 | bit |  |  | SI | Cetirizina |
| Q13 | bit |  |  | SI | Amikacina |
| Q14 | bit |  |  | SI | Nitrofurantoina |
| Q15 | bit |  |  | SI | cefortin (ex-cloxacilina) |
| Q16 | bit |  |  | SI | Rifampicina |
| Q17 | bit |  |  | SI | Ampicilina |
| Q18 | bit |  |  | SI | Cefadroxilo |
| Q19 | bit |  |  | SI | Gemtamicina |
| Q20 | bit |  |  | SI | Penicilina |
| Q21 | bit |  |  | SI | Ceftazidima |
| Q22 | bit |  |  | SI | Ciprofloxacino |
| Q23 | bit |  |  | SI | Sulfametropin |
| Q24 | bit |  |  | SI | Tetraciclina |
| Q25 | bit |  |  | SI | Cefazolina |
| Q26 | varchar |  |  | SI | Otros |
| Q27 | varchar |  |  | SI | Fecha de inicio ATB |
| Q28 | varchar |  |  | SI | N° dias de tratamoiento |
| Q29 | bit |  |  | SI | Urocultivo |
| Q30 | bit |  |  | SI | Ceprocultivo |
| Q31 | bit |  |  | SI | Hemocultio(*) |
| Q32 | varchar |  |  | SI | Secreciones |
| Q33 | varchar |  |  | SI | Otras Heridas |
| Q34 | bit |  |  | SI | Tejidos |
| Q35 | varchar |  |  | SI | Especificar |
| Q36 | varchar |  |  | SI | Cateter |
| Q37 | bit |  |  | SI | Tincion de GRAM |
| Q38 | varchar |  |  | SI | Responsable de recolección |
| Q39 | varchar |  |  | SI | Fecha y hora toma muestra |
| Q40 | varchar |  |  | SI | Responsable recepción |
| Q41 | varchar |  |  | SI | Fecha y hora recepción |
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