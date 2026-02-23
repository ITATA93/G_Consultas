# questionnaire.QTCENTCVT

> Clinical Vestibular Tests

**Schema:** questionnaire
**Columnas:** 96
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Clinical Vestibular Tests

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Gait |
| Q01N | varchar |  |  | SI | Gait_Note |
| Q02 | varchar |  |  | SI | Nystagmus |
| Q02N | varchar |  |  | SI | Nystagmus_Note |
| Q03 | varchar |  |  | SI | Cerebellar Function Test |
| Q04 | varchar |  |  | SI | Past-pointing : Eyes open |
| Q04N | varchar |  |  | SI | PPEO_Note |
| Q04ObsDR | varchar |  | FK | SI | Past-pointing : Eyes open DR |
| Q05 | varchar |  |  | SI | Past-pointing : Eyes closed |
| Q05N | varchar |  |  | SI | PPEC_Note |
| Q05ObsDR | varchar |  | FK | SI | Past-pointing : Eyes closed DR |
| Q06 | varchar |  |  | SI | Dysdidokinesia |
| Q06N | varchar |  |  | SI | Dysdidokinesia_Note |
| Q07 | varchar |  |  | SI | Romberg's Test |
| Q08 | varchar |  |  | SI | Eyes open |
| Q08N | varchar |  |  | SI | Romberg eye open_Note |
| Q08ObsDR | varchar |  | FK | SI | Eyes open DR |
| Q09 | varchar |  |  | SI | Eyes closed |
| Q09N | varchar |  |  | SI | Romberg eye closed_Note |
| Q09ObsDR | varchar |  | FK | SI | Eyes closed DR |
| Q10 | varchar |  |  | SI | Unterberger's Test |
| Q11 | varchar |  |  | SI | Eyes closed |
| Q11N | varchar |  |  | SI | Eyes closed_Note |
| Q11ObsDR | varchar |  | FK | SI | Eyes closed DR |
| Q12 | varchar |  |  | SI | Walking in a straight line |
| Q13 | varchar |  |  | SI | Eyes open |
| Q13N | varchar |  |  | SI | Eyes open_Note |
| Q13ObsDR | varchar |  | FK | SI | Eyes open DR |
| Q14 | varchar |  |  | SI | Eyes closed |
| Q14N | varchar |  |  | SI | Eyes closed_Note |
| Q14ObsDR | varchar |  | FK | SI | Eyes closed DR |
| Q15 | varchar |  |  | SI | Cranial Nerves |
| Q16 | varchar |  |  | SI | Cranial Nerves : II to XII |
| Q16N | varchar |  |  | SI | Cranial Nerves II to XII_Note |
| Q17 | varchar |  |  | SI | For detailed examination of Cranial Nerves use Neu... |
| Q17A | varchar |  |  | SI | Use Neurological Examination Form for details |
| Q18 | varchar |  |  | SI | Corneal Reflex (Cranial Nerve V) - Right |
| Q18N | varchar |  |  | SI | CR Right_Note |
| Q19 | varchar |  |  | SI | Corneal Reflex (Cranial Nerve V) - Left |
| Q19N | varchar |  |  | SI | CR Left_Note |
| Q20 | varchar |  |  | SI | Positional Test |
| Q21 | varchar |  |  | SI | Dix-Hallpike : Right |
| Q21N | varchar |  |  | SI | Dix-Hallpike Right_Note |
| Q22 | varchar |  |  | SI | Dix-Hallpike : Left |
| Q22N | varchar |  |  | SI | Dix-Hallpike Left_Note |
| Q23 | varchar |  |  | SI | Halmagyi Maneuver |
| Q24 | varchar |  |  | SI | Right |
| Q24N | varchar |  |  | SI | Right_Note |
| Q25 | varchar |  |  | SI | Left |
| Q25N | varchar |  |  | SI | Left_Note |
| Q26 | varchar |  |  | SI | Hyperventilation |
| Q26N | varchar |  |  | SI | Hyperventilation_Note |
| Q27 | bigint |  |  | SI | Inference |
| Q27TxtOnly | bigint |  |  | SI | Inference Plain Text Only |
| Q47 | varchar |  |  | SI | Unterberger's Test outcome |
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