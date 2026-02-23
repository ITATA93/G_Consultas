# questionnaire.QCLXXDETRN

> Detalles RN Externo

**Schema:** questionnaire
**Columnas:** 108
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Detalles RN Externo

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q06 | varchar |  |  | SI | Comentarios y Observaciones |
| Q111 | date |  |  | SI | Fecha de Ingreso |
| Q112 | time |  |  | SI | Hora de Ingreso |
| Q114 | varchar |  |  | SI | Información entregada por |
| Q115 | varchar |  |  | SI | Contacto |
| Q116 | varchar |  |  | SI | Procedencia del paciente |
| Q117 | varchar |  |  | SI | Procedencia, descripción |
| Q123 | varchar |  |  | SI | Profesional de Salud |
| Q124 | varchar |  |  | SI | Fono Contacto |
| Q125 | date |  |  | SI | Fecha Nacimiento |
| Q126 | time |  |  | SI | Hora de Nacimiento |
| Q129 | varchar |  |  | SI | Sexo |
| Q130 | varchar |  |  | SI | Peso al Nacer |
| Q130ObsDR | varchar |  | FK | SI | Peso al Nacer DR |
| Q131 | varchar |  |  | SI | Talla al Nacer |
| Q131ObsDR | varchar |  | FK | SI | Talla al Nacer DR |
| Q132 | varchar |  |  | SI | Circunferencia Craneana |
| Q132ObsDR | varchar |  | FK | SI | Circunferencia Craneana DR |
| Q134 | varchar |  |  | SI | Apego |
| Q135 | varchar |  |  | SI | Apego Duración |
| Q141 | varchar |  |  | SI | Diuresis |
| Q143 | varchar |  |  | SI | Deposiciones |
| Q144 | varchar |  |  | SI | Lactancia Materna |
| Q145 | varchar |  |  | SI | Alimentación Complementaria |
| Q146 | varchar |  |  | SI | Administración Vitamina  K |
| Q147 | varchar |  |  | SI | Alimentación Complementaria |
| Q148 | varchar |  |  | SI | Reanimación |
| Q149 | varchar |  |  | SI | Profilaxis Ocular |
| Q150 | varchar |  |  | SI | Anomalía Congénita |
| Q152 | varchar |  |  | SI | Muestra de Sangre de Cordón Grupo RH Coomb |
| Q153 | numeric |  |  | SI | Semanas de Gestación 1 |
| Q154 | numeric |  |  | SI | Semanas de Gestación 2 |
| Q155 | varchar |  |  | SI | Morbilidad RN |
| Q156 | varchar |  |  | SI | Apgar 1 Minuto |
| Q157 | varchar |  |  | SI | Apgar 5 Minutos |
| Q158 | varchar |  |  | SI | Apgar 10 Minutos |
| Q159 | varchar |  |  | SI | Nombre de la Madre |
| Q160 | numeric |  |  | SI | Edad Materna |
| Q161 | varchar |  |  | SI | Gesta |
| Q162 | numeric |  |  | SI | Número de Partos |
| Q163 | numeric |  |  | SI | Hijos Vivos |
| Q164 | varchar |  |  | SI | Grupo Sanguíneo Materno |
| Q165 | varchar |  |  | SI | Factor RH Materno |
| Q170 | varchar |  |  | SI | Patología del Embarazo |
| Q171 | varchar |  |  | SI | Medicamentos que tomó durante el embarazo |
| Q172 | varchar |  |  | SI | Tipo de Parto  |
| Q173 | varchar |  |  | SI | Causa de Cesárea |
| Q174 | varchar |  |  | SI | Causa de Fórceps |
| Q175 | varchar |  |  | SI | Método de Inducción |
| Q176 | varchar |  |  | SI | Tipo de Anestesia (Parto) |
| Q177 | varchar |  |  | SI | Otra Anestesia (Parto) |
| Q178 | varchar |  |  | SI | Líqudo Amniótico |
| Q179 | varchar |  |  | SI | Placenta |
| Q180 | varchar |  |  | SI | Otros (Placenta) |
| Q181 | varchar |  |  | SI | Circular de Cordón |
| Q182 | varchar |  |  | SI | Complicaciones durante el Parto |
| Q183 | varchar |  |  | SI | Complicaciones Maternas |
| Q184 | varchar |  |  | SI | Complicaciones Fetales |
| Q185 | varchar |  |  | SI | Otras Complicaciones del Parto |
| Q186 | varchar |  |  | SI | Lugar del Parto |
| Q187 | varchar |  |  | SI | Otro Lugar de Parto |
| Q220 | varchar |  |  | SI | Administración Vacuna BCG:  |
| Q221 | varchar |  |  | SI | Toma de PKU:  |
| Q61 | varchar |  |  | SI | Fórmula Obstétrica |
| Q62 | varchar |  |  | SI | Obstetricia |
| Q63 | varchar |  |  | SI | Neonatología |
| Q64 | varchar |  |  | SI | Apgar |
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