# questionnaire.QTCBQD

> Braden QD Scale

**Schema:** questionnaire
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Braden QD Scale

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | The ability to independently change and control bo... |
| Q04 | varchar |  |  | SI | The ability to respond meaningfully, in a developm... |
| Q05 | varchar |  |  | SI | Tolerance of the Skin and Supporting Structure |
| Q06 | varchar |  |  | SI | Friction: occurs when skin moves against support s... |
| Q07 | varchar |  |  | SI | Usual diet for age – assess pattern over the most ... |
| Q08 | varchar |  |  | SI | TISSUE PERFUSION AND OXYGENATION |
| Q09 | varchar |  |  | SI | Medical Devices |
| Q10 | varchar |  |  | SI | Any diagnostic or therapeutic device that is curre... |
| Q11 | varchar |  |  | SI | REPOSITIONABILITY / SKIN PROTECTION |
| Q12 | varchar |  |  | SI | The Braden QD is a refinement of the Braden Q whic... |
| Q13 | varchar |  |  | SI | 1. Curley MAQ, Hasbani NR, Quigley SM, et al. Pred... |
| Q14 | varchar |  |  | SI | 2. Quigley SM, Curley MAQ. Skin Integrity in the P... |
| Q15 | varchar |  |  | SI | The new Braden QD scale identifies risk for both i... |
| Q16 | varchar |  |  | SI | MOBILITY |
| Q17 | varchar |  |  | SI | SENSORY PERCEPTION |
| Q18 | varchar |  |  | SI | FRICTION & SHEAR |
| Q19 | varchar |  |  | SI | NUTRITION |
| Q20 | varchar |  |  | SI | NUMBER of MEDICAL DEVICES |
| Q21 | varchar |  |  | SI | 3. Bergstom N, Braden BJ, Laguzza A, Holman V. The... |
| Q22 | varchar |  |  | SI | REPOSITIONABILITY / SKIN PROTECTION |
| Q23 | varchar |  |  | SI | Any diagnostic or therapeutic device that is curre... |
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