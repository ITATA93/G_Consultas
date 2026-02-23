# SQLUser.ARC_OrdSetDateOSPrice

**Schema:** SQLUser
**Columnas:** 123
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PRICE_ParRef | varchar | PK |  | NO | ARC_OrdSetDateOS Parent Reference |
| PRICE_Childsub | double |  |  | NO | Childsub |
| PRICE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PRICE_CreatedDate | date |  |  | SI | Created Date |
| PRICE_CreatedTime | time |  |  | SI | Created Time |
| PRICE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PRICE_DateFrom | date |  |  | SI | Date From |
| PRICE_DateTo | date |  |  | SI | Date To |
| PRICE_EpisodeType | varchar |  |  | SI | Episode Type |
| PRICE_Hospital_DR | bigint |  | FK | SI | Hospital DR |
| PRICE_Price | double |  |  | SI | Price |
| PRICE_RowId | varchar |  |  | NO | - |
| PRICE_Tariff_DR | bigint |  | FK | SI | Des Ref Tariff |
| PRICE_UpdatedDate | date |  |  | SI | Updated Date |
| PRICE_UpdatedTime | time |  |  | SI | Updated Time |
| PRICE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q06 | - |  |  | SI | Comentarios y Observaciones |
| Q111 | - |  |  | SI | Fecha de Ingreso |
| Q112 | - |  |  | SI | Hora de Ingreso |
| Q114 | - |  |  | SI | Información entregada por |
| Q115 | - |  |  | SI | Contacto |
| Q116 | - |  |  | SI | Procedencia del paciente |
| Q117 | - |  |  | SI | Procedencia, descripción |
| Q123 | - |  |  | SI | Profesional de Salud |
| Q124 | - |  |  | SI | Fono Contacto |
| Q125 | - |  |  | SI | Fecha Nacimiento |
| Q126 | - |  |  | SI | Hora de Nacimiento |
| Q129 | - |  |  | SI | Sexo |
| Q130 | - |  |  | SI | Peso al Nacer |
| Q130ObsDR | - |  |  | SI | Peso al Nacer DR |
| Q131 | - |  |  | SI | Talla al Nacer |
| Q131ObsDR | - |  |  | SI | Talla al Nacer DR |
| Q132 | - |  |  | SI | Circunferencia Craneana |
| Q132ObsDR | - |  |  | SI | Circunferencia Craneana DR |
| Q134 | - |  |  | SI | Apego |
| Q135 | - |  |  | SI | Apego Duración |
| Q141 | - |  |  | SI | Diuresis |
| Q143 | - |  |  | SI | Deposiciones |
| Q144 | - |  |  | SI | Lactancia Materna |
| Q145 | - |  |  | SI | Alimentación Complementaria |
| Q146 | - |  |  | SI | Administración Vitamina  K |
| Q147 | - |  |  | SI | Alimentación Complementaria |
| Q148 | - |  |  | SI | Reanimación |
| Q149 | - |  |  | SI | Profilaxis Ocular |
| Q150 | - |  |  | SI | Anomalía Congénita |
| Q152 | - |  |  | SI | Muestra de Sangre de Cordón Grupo RH Coomb |
| Q153 | - |  |  | SI | Semanas de Gestación 1 |
| Q154 | - |  |  | SI | Semanas de Gestación 2 |
| Q155 | - |  |  | SI | Morbilidad RN |
| Q156 | - |  |  | SI | Apgar 1 Minuto |
| Q157 | - |  |  | SI | Apgar 5 Minutos |
| Q158 | - |  |  | SI | Apgar 10 Minutos |
| Q159 | - |  |  | SI | Nombre de la Madre |
| Q160 | - |  |  | SI | Edad Materna |
| Q161 | - |  |  | SI | Gesta |
| Q162 | - |  |  | SI | Número de Partos |
| Q163 | - |  |  | SI | Hijos Vivos |
| Q164 | - |  |  | SI | Grupo Sanguíneo Materno |
| Q165 | - |  |  | SI | Factor RH Materno |
| Q170 | - |  |  | SI | Patología del Embarazo |
| Q171 | - |  |  | SI | Medicamentos que tomó durante el embarazo |
| Q172 | - |  |  | SI | Tipo de Parto |
| Q173 | - |  |  | SI | Causa de Cesárea |
| Q174 | - |  |  | SI | Causa de Fórceps |
| Q175 | - |  |  | SI | Método de Inducción |
| Q176 | - |  |  | SI | Tipo de Anestesia (Parto) |
| Q177 | - |  |  | SI | Otra Anestesia (Parto) |
| Q178 | - |  |  | SI | Líqudo Amniótico |
| Q179 | - |  |  | SI | Placenta |
| Q180 | - |  |  | SI | Otros (Placenta) |
| Q181 | - |  |  | SI | Circular de Cordón |
| Q182 | - |  |  | SI | Complicaciones durante el Parto |
| Q183 | - |  |  | SI | Complicaciones Maternas |
| Q184 | - |  |  | SI | Complicaciones Fetales |
| Q185 | - |  |  | SI | Otras Complicaciones del Parto |
| Q186 | - |  |  | SI | Lugar del Parto |
| Q187 | - |  |  | SI | Otro Lugar de Parto |
| Q220 | - |  |  | SI | Administración Vacuna BCG: |
| Q221 | - |  |  | SI | Toma de PKU: |
| Q61 | - |  |  | SI | Fórmula Obstétrica |
| Q62 | - |  |  | SI | Obstetricia |
| Q63 | - |  |  | SI | Neonatología |
| Q64 | - |  |  | SI | Apgar |
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