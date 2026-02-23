# questionnaire.QTCEESPIRO

> Espirometría

**Schema:** questionnaire
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Espirometría

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | numeric |  |  | SI | VEF1 (lt) Basal Real |
| Q02 | numeric |  |  | SI | VEF1 (lt) Basal Predicho |
| Q03 | varchar |  |  | SI | VEF1 (lt) Basal % Predicho |
| Q04 | numeric |  |  | SI | VEF1 (lt) Basal P95 |
| Q05 | numeric |  |  | SI | VEF1 (lt) Posbroncodilatador REAL |
| Q06 | varchar |  |  | SI | VEF1 (lt) Posbroncodilatador % Predicho |
| Q07 | varchar |  |  | SI | VEF1 (lt) Postboncodilatador % Cambio |
| Q08 | numeric |  |  | SI | CVF (lt) Basal Real |
| Q09 | numeric |  |  | SI | CVF (lt) Basal Predicho |
| Q10 | varchar |  |  | SI | CVF (lt) Basal % Predicho |
| Q11 | numeric |  |  | SI | CVF (lt) Basal P95 |
| Q12 | numeric |  |  | SI | CVF (lt) Postbroncodilatador |
| Q13 | varchar |  |  | SI | CVF (lt) postbroncodilatador % Predicho |
| Q14 | varchar |  |  | SI | CVF (lt) postbroncodilatador % Cambio |
| Q15 | varchar |  |  | SI | VEF1/CVF (%) Basal Real |
| Q16 | varchar |  |  | SI | VEF1/CVF (%) Basal Predicho |
| Q17 | varchar |  |  | SI | VEF/CVF (%) Basal % Predicho |
| Q18 | numeric |  |  | SI | VEF/CVF (%) Basal P95 |
| Q19 | varchar |  |  | SI | VEF/CVF (%) posbroncodilatador REAL |
| Q20 | varchar |  |  | SI | VEF/CVF (%) Postbroncodilator % Predicho |
| Q21 | varchar |  |  | SI | VEF/CVF (%) postbroncodilatador % Cambio |
| Q22 | numeric |  |  | SI | FEF 25-75 (lt/seg) Basal REAL |
| Q23 | numeric |  |  | SI | FEF 25-75 (lt/seg) Basal Predicho |
| Q24 | varchar |  |  | SI | FEF 25-75 (lt/seg) Basal % Predicho |
| Q25 | numeric |  |  | SI | FEF 25-75 (lt/seg) Basal P95 |
| Q26 | numeric |  |  | SI | FEF 25-75 (lt/seg) postbroncodilatador Real |
| Q27 | varchar |  |  | SI | FEF 25-75 (lt/seg) postbroncodilatador % Predicho |
| Q28 | varchar |  |  | SI | FEF 25-75 (lt/seg) postbroncodilatador % Cambio |
| Q29 | varchar |  |  | SI | Conclusión |
| Q30 | varchar |  |  | SI | Espirometría |
| Q31 | varchar |  |  | SI | Peso |
| Q31ObsDR | varchar |  | FK | SI | Peso DR |
| Q32 | varchar |  |  | SI | Talla |
| Q32ObsDR | varchar |  | FK | SI | Talla DR |
| Q33 | varchar |  |  | SI | IMC |
| Q34 | varchar |  |  | SI | Edad |
| Q35 | varchar |  |  | SI | Meses |
| Q36 | varchar |  |  | SI | Días |
| Q37 | varchar |  |  | SI | Diferencia en Litros del VEF1 |
| Q38 | varchar |  |  | SI | Diferencia en Litros de la CVF |
| Q39 | varchar |  |  | SI | Diferencia en Litros de la FEF 25-75 |
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