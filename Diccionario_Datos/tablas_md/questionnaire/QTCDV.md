# questionnaire.QTCDV

> Death Verification

**Schema:** questionnaire
**Columnas:** 95
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Death Verification

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Are you aware of the facts of death? |
| Q02 | longvarbinary |  |  | SI | Sign |
| Q02UDt | date |  |  | SI | Sign Last Updated Date |
| Q02UTm | time |  |  | SI | Sign Last Updated Time |
| Q03 | varchar |  |  | SI | Is the death a reportable or reviewable death? |
| Q04 | longvarbinary |  |  | SI | Sign |
| Q04UDt | date |  |  | SI | Sign Last Updated Date |
| Q04UTm | time |  |  | SI | Sign Last Updated Time |
| Q05 | bit |  |  | SI | No palpable pulse |
| Q06 | longvarbinary |  |  | SI | No palpable pulse |
| Q06UDt | date |  |  | SI | No palpable pulse Last Updated Date |
| Q06UTm | time |  |  | SI | No palpable pulse Last Updated Time |
| Q07 | bit |  |  | SI | No heart sounds heard for 2 minutes |
| Q08 | longvarbinary |  |  | SI | No heart sounds heard for two minutes |
| Q08UDt | date |  |  | SI | No heart sounds heard for two minutes Last Updated... |
| Q08UTm | time |  |  | SI | No heart sounds heard for two minutes Last Updated... |
| Q09 | bit |  |  | SI | Pupils dilated and not responsive to light |
| Q10 | longvarbinary |  |  | SI | Pupils dilated and not responsive to light |
| Q10UDt | date |  |  | SI | Pupils dilated and not responsive to light Last Up... |
| Q10UTm | time |  |  | SI | Pupils dilated and not responsive to light Last Up... |
| Q11 | bit |  |  | SI | No response to central stimulus |
| Q12 | longvarbinary |  |  | SI | No response to central stimulus |
| Q12UDt | date |  |  | SI | No response to central stimulus Last Updated Date |
| Q12UTm | time |  |  | SI | No response to central stimulus Last Updated Time |
| Q13 | bit |  |  | SI | No motor (withdrawal) response or facial grimace i... |
| Q14 | longvarbinary |  |  | SI | No motor (withdrawal) response or facial grimace i... |
| Q14UDt | date |  |  | SI | No motor (withdrawal) response or facial grimace i... |
| Q14UTm | time |  |  | SI | No motor (withdrawal) response or facial grimace i... |
| Q15 | bit |  |  | SI | ECG strip shows no rhythm - optional |
| Q16 | longvarbinary |  |  | SI | Electrocardiogram strip shows no electrical activi... |
| Q16UDt | date |  |  | SI | Electrocardiogram strip shows no electrical activi... |
| Q16UTm | time |  |  | SI | Electrocardiogram strip shows no electrical activi... |
| Q17 | varchar |  |  | SI | Medical officer who confirms they will certify dea... |
| Q18 | varchar |  |  | SI | Next of kin / family |
| Q19 | varchar |  |  | SI | Location of patient when verification was undertak... |
| Q20 | bigint |  |  | SI | Comments |
| Q20TxtOnly | bigint |  |  | SI | Comments Plain Text Only |
| Q21 | varchar |  |  | SI | Funeral director name |
| Q22 | date |  |  | SI | Date |
| Q23 | time |  |  | SI | Time |
| Q24 | varchar |  |  | SI | No palpable carotid pulse |
| Q25 | varchar |  |  | SI | No heart sounds heard for two minutes |
| Q26 | varchar |  |  | SI | No breath sounds heard for two minutes |
| Q27 | longvarbinary |  |  | SI | No breath sounds heard for two minutes |
| Q27UDt | date |  |  | SI | No breath sounds heard for two minutes Last Update... |
| Q27UTm | time |  |  | SI | No breath sounds heard for two minutes Last Update... |
| Q28 | varchar |  |  | SI | Pupils dilated and not responsive to light |
| Q29 | varchar |  |  | SI | No response to central stimulus |
| Q30 | varchar |  |  | SI | No motor (withdrawal) response or facial grimace i... |
| Q31 | varchar |  |  | SI | Electrocardiogram strip shows no electrical activi... |
| Q32 | varchar |  |  | SI | This is an obvious death - the person has injuries... |
| Q33 | varchar |  |  | SI | Death verification completed by |
| Q34 | varchar |  |  | SI | It is not appropriate to complete a death verifica... |
| Q35 | varchar |  |  | SI | It is not appropriate to complete a death verifica... |
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