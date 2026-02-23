# questionnaire.QGXXXMNDC

> Neonatal death checklist

**Schema:** questionnaire
**Columnas:** 121
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Neonatal death checklist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Mother infomed by |
| Q02 | varchar |  |  | SI | Partner informed by |
| Q03 | varchar |  |  | SI | Consultant obstetrician informed |
| Q03ObsDR | varchar |  | FK | SI | Consultant obstetrician informed DR |
| Q04 | varchar |  |  | SI | Consultant/senior doctor spoken to parents |
| Q04ObsDR | varchar |  | FK | SI | Consultant/senior doctor spoken to parents DR |
| Q05 | varchar |  |  | SI | Post-mortem procedure discussed with doctor |
| Q05ObsDR | varchar |  | FK | SI | Post-mortem procedure discussed with doctor DR |
| Q06 | varchar |  |  | SI | Informed consent obtained and signed |
| Q06ObsDR | varchar |  | FK | SI | Informed consent obtained and signed DR |
| Q07 | varchar |  |  | SI | Type of post-mortem agreed to |
| Q08 | varchar |  |  | SI | Pathology request completed by doctor |
| Q08ObsDR | varchar |  | FK | SI | Pathology request completed by doctor DR |
| Q09 | varchar |  |  | SI | Opportunity to see/hold baby |
| Q09ObsDR | varchar |  | FK | SI | Opportunity to see/hold baby DR |
| Q10 | varchar |  |  | SI | Religious advisor required |
| Q10ObsDR | varchar |  | FK | SI | Religious advisor required DR |
| Q11 | varchar |  |  | SI | Religious ceremony held |
| Q11ObsDR | varchar |  | FK | SI | Religious ceremony held DR |
| Q12 | varchar |  |  | SI | Photographs offered |
| Q12ObsDR | varchar |  | FK | SI | Photographs offered DR |
| Q13 | varchar |  |  | SI | Photographs awaited |
| Q13ObsDR | varchar |  | FK | SI | Photographs awaited DR |
| Q14 | varchar |  |  | SI | Photographs given |
| Q14ObsDR | varchar |  | FK | SI | Photographs given DR |
| Q15 | varchar |  |  | SI | Birth acknowledgement given |
| Q15ObsDR | varchar |  | FK | SI | Birth acknowledgement given DR |
| Q16 | varchar |  |  | SI | Cot card given |
| Q16ObsDR | varchar |  | FK | SI | Cot card given DR |
| Q17 | varchar |  |  | SI | Namebands given |
| Q17ObsDR | varchar |  | FK | SI | Namebands given DR |
| Q18 | varchar |  |  | SI | Lock of hair given |
| Q18ObsDR | varchar |  | FK | SI | Lock of hair given DR |
| Q19 | varchar |  |  | SI | Foot/hand print given |
| Q19ObsDR | varchar |  | FK | SI | Foot/hand print given DR |
| Q20 | varchar |  |  | SI | Certificate of blessing given |
| Q20ObsDR | varchar |  | FK | SI | Certificate of blessing given DR |
| Q21 | varchar |  |  | SI | Identification card completed |
| Q21ObsDR | varchar |  | FK | SI | Identification card completed DR |
| Q22 | varchar |  |  | SI | Request to pathology to collect baby |
| Q22ObsDR | varchar |  | FK | SI | Request to pathology to collect baby DR |
| Q23 | varchar |  |  | SI | Funeral options discussed |
| Q23ObsDR | varchar |  | FK | SI | Funeral options discussed DR |
| Q24 | varchar |  |  | SI | Future appointments cancelled |
| Q24ObsDR | varchar |  | FK | SI | Future appointments cancelled DR |
| Q25 | varchar |  |  | SI | Visit from midwife required |
| Q25ObsDR | varchar |  | FK | SI | Visit from midwife required DR |
| Q26 | varchar |  |  | SI | 6week follow-up arranged |
| Q26ObsDR | varchar |  | FK | SI | 6week follow-up arranged DR |
| Q27 | varchar |  |  | SI | General practitioner informed |
| Q27ObsDR | varchar |  | FK | SI | General practitioner informed DR |
| Q28 | varchar |  |  | SI | Paediatrician informed |
| Q28ObsDR | varchar |  | FK | SI | Paediatrician informed DR |
| Q29 | varchar |  |  | SI | Death certificate completed |
| Q29ObsDR | varchar |  | FK | SI | Death certificate completed DR |
| Q30 | varchar |  |  | SI | Other information |
| Q31 | varchar |  |  | SI | Completed form handed to secretary |
| Q31ObsDR | varchar |  | FK | SI | Completed form handed to secretary DR |
| Q32 | varchar |  |  | SI | Prescription to suppress lactation given |
| Q32ObsDR | varchar |  | FK | SI | Prescription to suppress lactation given DR |
| Q33 | varchar |  |  | SI | Information about funeral arranging given |
| Q33ObsDR | varchar |  | FK | SI | Information about funeral arranging given DR |
| Q34 | varchar |  |  | SI | Post-mortem consent obtained and signed |
| Q34ObsDR | varchar |  | FK | SI | Post-mortem consent obtained and signed DR |
| Q35 | varchar |  |  | SI | Parents decision on funeral |
| Q36 | varchar |  |  | SI | Religious advisor called |
| Q36ObsDR | varchar |  | FK | SI | Religious advisor called DR |
| Q37 | varchar |  |  | SI | Have parents read the Still Birth & Neonatal Death... |
| Q38 | varchar |  |  | SI | Post mortem requested |
| Q39 | varchar |  |  | SI | Birth registration appointment needed |
| Q40 | varchar |  |  | SI | Note - Birth registration appointment needed |
| Q41 | varchar |  |  | SI | Is a coroner required |
| Q42 | varchar |  |  | SI | Has coroner been contacted |
| Q43 | varchar |  |  | SI | Notes |
| Q44 | varchar |  |  | SI | Support leaflets given |
| Q45 | varchar |  |  | SI | Support for siblings required |
| Q46 | varchar |  |  | SI | Council cremation papers completed |
| Q47 | varchar |  |  | SI | Cremation form |
| Q48 | date |  |  | SI | Date of registrar appointment |
| Q49 | date |  |  | SI | Date of birth registration appointment |
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