# questionnaire.QCLXXIDEMAD

> Información Perinatal

**Schema:** questionnaire
**Columnas:** 101
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Información Perinatal

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q100 | varchar |  |  | SI | Comentarios y Observaciones |
| Q116 | varchar |  |  | SI | Nombre de la Madre |
| Q117 | numeric |  |  | SI | Edad Materna |
| Q118 | varchar |  |  | SI | Gesta |
| Q119 | numeric |  |  | SI | Número de Partos |
| Q120 | numeric |  |  | SI | Hijos Vivos |
| Q121 | varchar |  |  | SI | Grupo Sanguíneo Materno |
| Q122 | varchar |  |  | SI | Factor RH Materno |
| Q126 | varchar |  |  | SI | Patología del Embarazo |
| Q127 | varchar |  |  | SI | Medicamentos que tomó durante el embarazo |
| Q128 | varchar |  |  | SI | Tipo de Parto  |
| Q129 | varchar |  |  | SI | Causa de Cesárea |
| Q130 | varchar |  |  | SI | Causa de Fórceps |
| Q132 | varchar |  |  | SI | Inducción del Parto |
| Q133 | varchar |  |  | SI | Tipo de Anestesia (Parto) |
| Q134 | varchar |  |  | SI | Otra Anestesia (Parto) |
| Q135 | varchar |  |  | SI | Líqudo Amniótico |
| Q136 | varchar |  |  | SI | Placenta |
| Q137 | varchar |  |  | SI | Otros (Placenta) |
| Q138 | varchar |  |  | SI | Circular de Cordón |
| Q140 | varchar |  |  | SI | Complicaciones durante el Parto |
| Q141 | varchar |  |  | SI | Complicaciones Maternas |
| Q143 | varchar |  |  | SI | Complicaciones Fetales |
| Q144 | varchar |  |  | SI | Otras Complicaciones del Parto |
| Q145 | varchar |  |  | SI | 6. Babinsky |
| Q145ObsDR | varchar |  | FK | SI | 6. Babinsky DR |
| Q146 | date |  |  | SI | Fecha Nacimiento |
| Q147 | time |  |  | SI | Hora de Nacimiento |
| Q148 | varchar |  |  | SI | Sexo |
| Q149 | varchar |  |  | SI | Peso al Nacer |
| Q149ObsDR | varchar |  | FK | SI | Peso al Nacer DR |
| Q150 | varchar |  |  | SI | Talla al Nacer |
| Q150ObsDR | varchar |  | FK | SI | Talla al Nacer DR |
| Q151 | varchar |  |  | SI | Circunferencia Craneana |
| Q151ObsDR | varchar |  | FK | SI | Circunferencia Craneana DR |
| Q152 | varchar |  |  | SI | Apego |
| Q153 | varchar |  |  | SI | Duración del Apego |
| Q154 | varchar |  |  | SI | Diuresis |
| Q155 | varchar |  |  | SI | Deposiciones |
| Q156 | varchar |  |  | SI | Lactancia Materna |
| Q157 | varchar |  |  | SI | Alimentación Complementaria |
| Q158 | varchar |  |  | SI | Administración Vitamina  K |
| Q159 | varchar |  |  | SI | Reanimación |
| Q160 | varchar |  |  | SI | Anomalía Congénita |
| Q161 | varchar |  |  | SI | Muestra de Sangre de Cordón Grupo RH Coomb |
| Q162 | numeric |  |  | SI | Semanas de Gestación 1 |
| Q163 | numeric |  |  | SI | Semanas de Gestación 2 |
| Q164 | varchar |  |  | SI | Morbilidad RN |
| Q165 | varchar |  |  | SI | Apgar 1 Minuto |
| Q166 | varchar |  |  | SI | Apgar 5 Minutos |
| Q167 | varchar |  |  | SI | Apgar 10 Minutos |
| Q168 | varchar |  |  | SI | Profilaxis Ocular |
| Q170 | varchar |  |  | SI | HGT |
| Q170ObsDR | varchar |  | FK | SI | HGT DR |
| Q171 | varchar |  |  | SI | Lugar del Parto |
| Q172 | varchar |  |  | SI | Otro Lugar de Parto |
| Q173 | varchar |  |  | SI | Especifique Otra Razón |
| Q220 | varchar |  |  | SI | Profesional de Salud |
| Q221 | varchar |  |  | SI | Administración Vacuna BCG:  |
| Q222 | varchar |  |  | SI | Toma de PKU:  |
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