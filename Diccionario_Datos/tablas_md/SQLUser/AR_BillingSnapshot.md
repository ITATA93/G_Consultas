# SQLUser.AR_BillingSnapshot

**Schema:** SQLUser
**Columnas:** 107
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BILLSNP_RowId | bigint | PK |  | NO | - |
| BILLSNP_CreateDate | date |  |  | SI | Create Date |
| BILLSNP_CreateTime | time |  |  | SI | Create Time |
| BILLSNP_CreateUser | varchar |  |  | SI | Create User |
| BILLSNP_SnapshotType | varchar |  |  | SI | Snapshot Type |
| BILLSNP_Text1 | varchar |  |  | SI | Text 1 |
| BILLSNP_Text2 | varchar |  |  | SI | Text 2 |
| Q100 | - |  |  | SI | Comentarios y Observaciones |
| Q116 | - |  |  | SI | Nombre de la Madre |
| Q117 | - |  |  | SI | Edad Materna |
| Q118 | - |  |  | SI | Gesta |
| Q119 | - |  |  | SI | Número de Partos |
| Q120 | - |  |  | SI | Hijos Vivos |
| Q121 | - |  |  | SI | Grupo Sanguíneo Materno |
| Q122 | - |  |  | SI | Factor RH Materno |
| Q126 | - |  |  | SI | Patología del Embarazo |
| Q127 | - |  |  | SI | Medicamentos que tomó durante el embarazo |
| Q128 | - |  |  | SI | Tipo de Parto |
| Q129 | - |  |  | SI | Causa de Cesárea |
| Q130 | - |  |  | SI | Causa de Fórceps |
| Q132 | - |  |  | SI | Inducción del Parto |
| Q133 | - |  |  | SI | Tipo de Anestesia (Parto) |
| Q134 | - |  |  | SI | Otra Anestesia (Parto) |
| Q135 | - |  |  | SI | Líqudo Amniótico |
| Q136 | - |  |  | SI | Placenta |
| Q137 | - |  |  | SI | Otros (Placenta) |
| Q138 | - |  |  | SI | Circular de Cordón |
| Q140 | - |  |  | SI | Complicaciones durante el Parto |
| Q141 | - |  |  | SI | Complicaciones Maternas |
| Q143 | - |  |  | SI | Complicaciones Fetales |
| Q144 | - |  |  | SI | Otras Complicaciones del Parto |
| Q145 | - |  |  | SI | 6. Babinsky |
| Q145ObsDR | - |  |  | SI | 6. Babinsky DR |
| Q146 | - |  |  | SI | Fecha Nacimiento |
| Q147 | - |  |  | SI | Hora de Nacimiento |
| Q148 | - |  |  | SI | Sexo |
| Q149 | - |  |  | SI | Peso al Nacer |
| Q149ObsDR | - |  |  | SI | Peso al Nacer DR |
| Q150 | - |  |  | SI | Talla al Nacer |
| Q150ObsDR | - |  |  | SI | Talla al Nacer DR |
| Q151 | - |  |  | SI | Circunferencia Craneana |
| Q151ObsDR | - |  |  | SI | Circunferencia Craneana DR |
| Q152 | - |  |  | SI | Apego |
| Q153 | - |  |  | SI | Duración del Apego |
| Q154 | - |  |  | SI | Diuresis |
| Q155 | - |  |  | SI | Deposiciones |
| Q156 | - |  |  | SI | Lactancia Materna |
| Q157 | - |  |  | SI | Alimentación Complementaria |
| Q158 | - |  |  | SI | Administración Vitamina  K |
| Q159 | - |  |  | SI | Reanimación |
| Q160 | - |  |  | SI | Anomalía Congénita |
| Q161 | - |  |  | SI | Muestra de Sangre de Cordón Grupo RH Coomb |
| Q162 | - |  |  | SI | Semanas de Gestación 1 |
| Q163 | - |  |  | SI | Semanas de Gestación 2 |
| Q164 | - |  |  | SI | Morbilidad RN |
| Q165 | - |  |  | SI | Apgar 1 Minuto |
| Q166 | - |  |  | SI | Apgar 5 Minutos |
| Q167 | - |  |  | SI | Apgar 10 Minutos |
| Q168 | - |  |  | SI | Profilaxis Ocular |
| Q170 | - |  |  | SI | HGT |
| Q170ObsDR | - |  |  | SI | HGT DR |
| Q171 | - |  |  | SI | Lugar del Parto |
| Q172 | - |  |  | SI | Otro Lugar de Parto |
| Q173 | - |  |  | SI | Especifique Otra Razón |
| Q220 | - |  |  | SI | Profesional de Salud |
| Q221 | - |  |  | SI | Administración Vacuna BCG: |
| Q222 | - |  |  | SI | Toma de PKU: |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*