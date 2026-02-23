# SQLUser.ARC_PackagePrefPayment

**Schema:** SQLUser
**Columnas:** 100
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PREFPM_ParRef | bigint | PK |  | NO | ARC_Package Parent Reference |
| PREFPM_Childsub | double |  |  | NO | Childsub |
| PREFPM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PREFPM_CreatedDate | date |  |  | SI | Created Date |
| PREFPM_CreatedTime | time |  |  | SI | Created Time |
| PREFPM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PREFPM_DateFrom | date |  |  | SI | DateFrom |
| PREFPM_DateTo | date |  |  | SI | DateTo |
| PREFPM_DiscAmount | double |  |  | SI | DiscountAmount |
| PREFPM_DiscPerc | double |  |  | SI | DiscountPerc |
| PREFPM_PayMode_DR | bigint |  | FK | SI | Des Ref CTPayMode |
| PREFPM_RowId | varchar |  |  | NO | - |
| PREFPM_UpdatedDate | date |  |  | SI | Updated Date |
| PREFPM_UpdatedTime | time |  |  | SI | Updated Time |
| PREFPM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Talla (aproximada) |
| Q02 | - |  |  | SI | kg |
| Q03 | - |  |  | SI | Peso (aproximado) |
| Q04 | - |  |  | SI | cm |
| Q05 | - |  |  | SI | IMC |
| Q06 | - |  |  | SI | Tamizaje Telefónico |
| Q07 | - |  |  | SI | Colonoscopías: Contactar 4 días previos al procedi... |
| Q08 | - |  |  | SI | Endoscopías altas: Contactar 2 días previos al pro... |
| Q09 | - |  |  | SI | 1. Alergias |
| Q10 | - |  |  | SI | Observaciones |
| Q11 | - |  |  | SI | 2. Uso de anticoagulantes orales |
| Q12 | - |  |  | SI | Observaciones |
| Q13 | - |  |  | SI | 3. Uso de antiagregantes plaquetarios |
| Q14 | - |  |  | SI | Observaciones |
| Q15 | - |  |  | SI | 4. Diabetes Mellitus |
| Q16 | - |  |  | SI | Observaciones |
| Q17 | - |  |  | SI | a) Uso de hipoglicemiantes orales |
| Q18 | - |  |  | SI | Observaciones |
| Q19 | - |  |  | SI | b) Uso de insulina |
| Q20 | - |  |  | SI | Observaciones |
| Q21 | - |  |  | SI | 5. Cardiopatías congénitas, valvulares y/o marcapa... |
| Q22 | - |  |  | SI | Observaciones |
| Q23 | - |  |  | SI | 6. Posibilidad de embarazo |
| Q24 | - |  |  | SI | Observaciones |
| Q25 | - |  |  | SI | 7.Insuficiencia respiratoria, renal o hepática |
| Q26 | - |  |  | SI | Observaciones |
| Q27 | - |  |  | SI | 8. Obesidad mórbida (según IMC calculado) |
| Q28 | - |  |  | SI | Observaciones |
| Q29 | - |  |  | SI | Se confirman indicaciones para día del procedimien... |
| Q30 | - |  |  | SI | *Régimen |
| Q31 | - |  |  | SI | *Hora de presentación |
| Q32 | - |  |  | SI | *Acompañante |
| Q33 | - |  |  | SI | *Teléfono de contacto ante dudas |
| Q34 | - |  |  | SI | Criterios de exclusión absoluta que serán derivado... |
| Q35 | - |  |  | SI | Colonoscopía: Paciente ≥ 75 años |
| Q36 | - |  |  | SI | Paciente ASA ≥ III |
| Q37 | - |  |  | SI | Paciente alérgico al latex |
| Q38 | - |  |  | SI | Embarazadas |
| Q39 | - |  |  | SI | Endoscopía: Paciente ≥ 80 años |
| Q40 | - |  |  | SI | Paciente IMC > 40 |
| Q41 | - |  |  | SI | Paciente alérgico a BZD |
| Q42 | - |  |  | SI | Paciente en TACO |
| Q43 | - |  |  | SI | Fecha de contacto telefónico |
| Q44 | - |  |  | SI | TENS/Enfermera responsable |
| Q45 | - |  |  | SI | *Paciente que presenta uno o más de los ítems seña... |
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