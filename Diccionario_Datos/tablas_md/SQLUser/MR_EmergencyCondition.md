# SQLUser.MR_EmergencyCondition

**Schema:** SQLUser
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EMC_ParRef | bigint | PK |  | NO | MR_Adm Parent Reference |
| EMC_Childsub | double |  |  | NO | Childsub |
| EMC_EmergCond_DR | bigint |  | FK | SI | Des Ref to EmergCond |
| EMC_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | SENSORY PERCEPTION - Ability to respond meaningful... |
| Q02 | - |  |  | SI | MOISTURE - Degree to which skin is exposed to mois... |
| Q03 | - |  |  | SI | ACTIVITY - Degree of physical activity |
| Q04 | - |  |  | SI | MOBILITY - Ability to change and control body posi... |
| Q05 | - |  |  | SI | NUTRITION - Usual food intake pattern |
| Q06 | - |  |  | SI | FRICTION AND SHEAR |
| Q07 | - |  |  | SI | 6 - 12: High risk |
| Q08 | - |  |  | SI | 13 - 14: Moderate risk |
| Q09 | - |  |  | SI | 15 - 16: Low risk |
| Q10 | - |  |  | SI | The Braden scale assesses a patients risk of devel... |
| Q11 | - |  |  | SI | 15 - 23: Low risk |
| Q12 | - |  |  | SI | 6 - 9: Very High risk |
| Q13 | - |  |  | SI | 10 - 12: High risk |
| Q14 | - |  |  | SI | 15 - 18: Low risk |
| Q15 | - |  |  | SI | 19 - 23: No risk |
| Q16 | - |  |  | SI | Number of pressure injuries at the time of evaluat... |
| Q17 | - |  |  | SI | Score |
| Q18 | - |  |  | SI | Classification |
| Q19 | - |  |  | SI | 6 - 9 |
| Q20 | - |  |  | SI | Very high risk |
| Q21 | - |  |  | SI | 10 - 12 |
| Q22 | - |  |  | SI | High risk |
| Q23 | - |  |  | SI | 15 - 18 |
| Q24 | - |  |  | SI | Low risk |
| Q25 | - |  |  | SI | 19 - 23 |
| Q26 | - |  |  | SI | No risk |
| Q27 | - |  |  | SI | 13 - 14 |
| Q28 | - |  |  | SI | Moderate risk |
| Q29 | - |  |  | SI | Time |
| Q30 | - |  |  | SI | Date |
| Q31 | - |  |  | SI | • Bergstrom N, Braden B, Kemp M, Champagne M, Ruby... |
| Q32 | - |  |  | SI | • Nurs Res. 1998 Sep-Oct |
| Q33 | - |  |  | SI | • Torra i Bou, Joan-Enric & García-Fernández, Fran... |
| Q34 | - |  |  | SI | • https://pubmed.ncbi.nlm.nih.gov/9766454/ |
| Q35 | - |  |  | SI | • https://www.researchgate.net/publication/2263936... |
| Q36 | - |  |  | SI | • https://www.bradenscale.com/ |
| Q37 | - |  |  | SI | •Bergstom N, Braden BJ, Laguzza A, Holman V. The B... |
| Q38 | - |  |  | SI | •Bergstrom N, Braden B, Kemp M, Champagne M, Ruby ... |
| Q39 | - |  |  | SI | •The Braden Scale is a summated rating scale made ... |
| Q40 | - |  |  | SI | •A lower Braden Scale Score indicates a lower leve... |
| Q41 | - |  |  | SI | •A score of 19 or higher, for instance, would indi... |
| Q42 | - |  |  | SI | •The assessment can also be used to evaluate the c... |
| Q43 | - |  |  | SI | •Copyright Barbara Braden and Nancy Bergstrom, 198... |
| Q44 | - |  |  | SI | •Braden B. Bergstrom N. Braden Scale For Predictin... |
| Q45 | - |  |  | SI | https://www.researchgate.net/publication/19608074_... |
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