# SQLUser.LBC_InstrumentEventTrans

**Schema:** SQLUser
**Columnas:** 102
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCINET_ParRef | bigint | PK |  | NO | Parent instrument DR |
| LBCINET_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCINET_DateFrom | date |  |  | SI | Date From |
| LBCINET_DateTo | date |  |  | SI | Date To |
| LBCINET_EventType_DR | bigint |  | FK | SI | Internal event type |
| LBCINET_InstrumentEventType | varchar |  |  | SI | Instrument event type |
| LBCINET_RowID | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Are you aware of the facts of death? |
| Q02 | - |  |  | SI | Sign |
| Q02UDt | - |  |  | SI | Sign Last Updated Date |
| Q02UTm | - |  |  | SI | Sign Last Updated Time |
| Q03 | - |  |  | SI | Is the death a reportable or reviewable death? |
| Q04 | - |  |  | SI | Sign |
| Q04UDt | - |  |  | SI | Sign Last Updated Date |
| Q04UTm | - |  |  | SI | Sign Last Updated Time |
| Q05 | - |  |  | SI | No palpable pulse |
| Q06 | - |  |  | SI | No palpable pulse |
| Q06UDt | - |  |  | SI | No palpable pulse Last Updated Date |
| Q06UTm | - |  |  | SI | No palpable pulse Last Updated Time |
| Q07 | - |  |  | SI | No heart sounds heard for 2 minutes |
| Q08 | - |  |  | SI | No heart sounds heard for two minutes |
| Q08UDt | - |  |  | SI | No heart sounds heard for two minutes Last Updated... |
| Q08UTm | - |  |  | SI | No heart sounds heard for two minutes Last Updated... |
| Q09 | - |  |  | SI | Pupils dilated and not responsive to light |
| Q10 | - |  |  | SI | Pupils dilated and not responsive to light |
| Q10UDt | - |  |  | SI | Pupils dilated and not responsive to light Last Up... |
| Q10UTm | - |  |  | SI | Pupils dilated and not responsive to light Last Up... |
| Q11 | - |  |  | SI | No response to central stimulus |
| Q12 | - |  |  | SI | No response to central stimulus |
| Q12UDt | - |  |  | SI | No response to central stimulus Last Updated Date |
| Q12UTm | - |  |  | SI | No response to central stimulus Last Updated Time |
| Q13 | - |  |  | SI | No motor (withdrawal) response or facial grimace i... |
| Q14 | - |  |  | SI | No motor (withdrawal) response or facial grimace i... |
| Q14UDt | - |  |  | SI | No motor (withdrawal) response or facial grimace i... |
| Q14UTm | - |  |  | SI | No motor (withdrawal) response or facial grimace i... |
| Q15 | - |  |  | SI | ECG strip shows no rhythm - optional |
| Q16 | - |  |  | SI | Electrocardiogram strip shows no electrical activi... |
| Q16UDt | - |  |  | SI | Electrocardiogram strip shows no electrical activi... |
| Q16UTm | - |  |  | SI | Electrocardiogram strip shows no electrical activi... |
| Q17 | - |  |  | SI | Medical officer who confirms they will certify dea... |
| Q18 | - |  |  | SI | Next of kin / family |
| Q19 | - |  |  | SI | Location of patient when verification was undertak... |
| Q20 | - |  |  | SI | Comments |
| Q20TxtOnly | - |  |  | SI | Comments Plain Text Only |
| Q21 | - |  |  | SI | Funeral director name |
| Q22 | - |  |  | SI | Date |
| Q23 | - |  |  | SI | Time |
| Q24 | - |  |  | SI | No palpable carotid pulse |
| Q25 | - |  |  | SI | No heart sounds heard for two minutes |
| Q26 | - |  |  | SI | No breath sounds heard for two minutes |
| Q27 | - |  |  | SI | No breath sounds heard for two minutes |
| Q27UDt | - |  |  | SI | No breath sounds heard for two minutes Last Update... |
| Q27UTm | - |  |  | SI | No breath sounds heard for two minutes Last Update... |
| Q28 | - |  |  | SI | Pupils dilated and not responsive to light |
| Q29 | - |  |  | SI | No response to central stimulus |
| Q30 | - |  |  | SI | No motor (withdrawal) response or facial grimace i... |
| Q31 | - |  |  | SI | Electrocardiogram strip shows no electrical activi... |
| Q32 | - |  |  | SI | This is an obvious death - the person has injuries... |
| Q33 | - |  |  | SI | Death verification completed by |
| Q34 | - |  |  | SI | It is not appropriate to complete a death verifica... |
| Q35 | - |  |  | SI | It is not appropriate to complete a death verifica... |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*