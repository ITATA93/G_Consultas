# questionnaire.QCLXXETPE

> Encuesta Telefónica Procedimientos Endoscópicos

**Schema:** questionnaire
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Encuesta Telefónica Procedimientos Endoscópicos

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | numeric |  |  | SI | Talla (aproximada) |
| Q02 | varchar |  |  | SI | kg |
| Q03 | numeric |  |  | SI | Peso (aproximado) |
| Q04 | varchar |  |  | SI | cm |
| Q05 | varchar |  |  | SI | IMC |
| Q06 | varchar |  |  | SI | Tamizaje Telefónico |
| Q07 | varchar |  |  | SI | Colonoscopías: Contactar 4 días previos al procedi... |
| Q08 | varchar |  |  | SI | Endoscopías altas: Contactar 2 días previos al pro... |
| Q09 | varchar |  |  | SI | 1. Alergias |
| Q10 | varchar |  |  | SI | Observaciones |
| Q11 | varchar |  |  | SI | 2. Uso de anticoagulantes orales |
| Q12 | varchar |  |  | SI | Observaciones |
| Q13 | varchar |  |  | SI | 3. Uso de antiagregantes plaquetarios |
| Q14 | varchar |  |  | SI | Observaciones |
| Q15 | varchar |  |  | SI | 4. Diabetes Mellitus |
| Q16 | varchar |  |  | SI | Observaciones |
| Q17 | varchar |  |  | SI | a) Uso de hipoglicemiantes orales |
| Q18 | varchar |  |  | SI | Observaciones |
| Q19 | varchar |  |  | SI | b) Uso de insulina |
| Q20 | varchar |  |  | SI | Observaciones |
| Q21 | varchar |  |  | SI | 5. Cardiopatías congénitas, valvulares y/o marcapa... |
| Q22 | varchar |  |  | SI | Observaciones |
| Q23 | varchar |  |  | SI | 6. Posibilidad de embarazo |
| Q24 | varchar |  |  | SI | Observaciones |
| Q25 | varchar |  |  | SI | 7.Insuficiencia respiratoria, renal o hepática |
| Q26 | varchar |  |  | SI | Observaciones |
| Q27 | varchar |  |  | SI | 8. Obesidad mórbida (según IMC calculado) |
| Q28 | varchar |  |  | SI | Observaciones |
| Q29 | varchar |  |  | SI | Se confirman indicaciones para día del procedimien... |
| Q30 | varchar |  |  | SI | *Régimen |
| Q31 | varchar |  |  | SI | *Hora de presentación |
| Q32 | varchar |  |  | SI | *Acompañante |
| Q33 | varchar |  |  | SI | *Teléfono de contacto ante dudas |
| Q34 | varchar |  |  | SI | Criterios de exclusión absoluta que serán derivado... |
| Q35 | varchar |  |  | SI | Colonoscopía: Paciente ≥ 75 años |
| Q36 | varchar |  |  | SI | Paciente ASA ≥ III |
| Q37 | varchar |  |  | SI | Paciente alérgico al latex |
| Q38 | varchar |  |  | SI | Embarazadas |
| Q39 | varchar |  |  | SI | Endoscopía: Paciente ≥ 80 años |
| Q40 | varchar |  |  | SI | Paciente IMC > 40 |
| Q41 | varchar |  |  | SI | Paciente alérgico a BZD |
| Q42 | varchar |  |  | SI | Paciente en TACO |
| Q43 | date |  |  | SI | Fecha de contacto telefónico |
| Q44 | varchar |  |  | SI | TENS/Enfermera responsable |
| Q45 | varchar |  |  | SI | *Paciente que presenta uno o más de los ítems seña... |
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