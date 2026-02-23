# questionnaire.QGXXXBRADEN

> Escala Braden

**Schema:** questionnaire
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Escala Braden

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | SENSORY PERCEPTION - Ability to respond meaningful... |
| Q02 | varchar |  |  | SI | MOISTURE - Degree to which skin is exposed to mois... |
| Q03 | varchar |  |  | SI | ACTIVITY - Degree of physical activity |
| Q04 | varchar |  |  | SI | MOBILITY - Ability to change and control body posi... |
| Q05 | varchar |  |  | SI | NUTRITION - Usual food intake pattern |
| Q06 | varchar |  |  | SI | FRICTION AND SHEAR |
| Q07 | varchar |  |  | SI | 6 - 12: High risk |
| Q08 | varchar |  |  | SI | 13 - 14: Moderate risk |
| Q09 | varchar |  |  | SI | 15 - 16: Low risk |
| Q10 | varchar |  |  | SI | The Braden scale assesses a patients risk of devel... |
| Q11 | varchar |  |  | SI | 15 - 23: Low risk |
| Q12 | varchar |  |  | SI | 6 - 9: Very High risk |
| Q13 | varchar |  |  | SI | 10 - 12: High risk |
| Q14 | varchar |  |  | SI | 15 - 18: Low risk |
| Q15 | varchar |  |  | SI | 19 - 23: No risk |
| Q16 | numeric |  |  | SI | Number of pressure injuries at the time of evaluat... |
| Q17 | varchar |  |  | SI | Score |
| Q18 | varchar |  |  | SI | Classification |
| Q19 | varchar |  |  | SI | 6 - 9 |
| Q20 | varchar |  |  | SI | Very high risk |
| Q21 | varchar |  |  | SI | 10 - 12 |
| Q22 | varchar |  |  | SI | High risk |
| Q23 | varchar |  |  | SI | 15 - 18 |
| Q24 | varchar |  |  | SI | Low risk |
| Q25 | varchar |  |  | SI | 19 - 23 |
| Q26 | varchar |  |  | SI | No risk |
| Q27 | varchar |  |  | SI | 13 - 14 |
| Q28 | varchar |  |  | SI | Moderate risk |
| Q29 | time |  |  | SI | Time |
| Q30 | date |  |  | SI | Date |
| Q31 | varchar |  |  | SI | • Bergstrom N, Braden B, Kemp M, Champagne M, Ruby... |
| Q32 | varchar |  |  | SI | • Nurs Res. 1998 Sep-Oct;47(5):261-9. doi: 10.1097... |
| Q33 | varchar |  |  | SI | • Torra i Bou, Joan-Enric & García-Fernández, Fran... |
| Q34 | varchar |  |  | SI | • https://pubmed.ncbi.nlm.nih.gov/9766454/ |
| Q35 | varchar |  |  | SI | • https://www.researchgate.net/publication/2263936... |
| Q36 | varchar |  |  | SI | • https://www.bradenscale.com/ |
| Q37 | varchar |  |  | SI | •Bergstom N, Braden BJ, Laguzza A, Holman V. The B... |
| Q38 | varchar |  |  | SI | •Bergstrom N, Braden B, Kemp M, Champagne M, Ruby ... |
| Q39 | varchar |  |  | SI | •The Braden Scale is a summated rating scale made ... |
| Q40 | varchar |  |  | SI | •A lower Braden Scale Score indicates a lower leve... |
| Q41 | varchar |  |  | SI | •A score of 19 or higher, for instance, would indi... |
| Q42 | varchar |  |  | SI | •The assessment can also be used to evaluate the c... |
| Q43 | varchar |  |  | SI | •Copyright Barbara Braden and Nancy Bergstrom, 198... |
| Q44 | varchar |  |  | SI | •Braden B. Bergstrom N. Braden Scale For Predictin... |
| Q45 | varchar |  |  | SI | https://www.researchgate.net/publication/19608074_... |
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