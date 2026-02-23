# SQLUser.NR_Nurse_Rostering

**Schema:** SQLUser
**Columnas:** 125
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NUR_RowId | bigint | PK |  | NO | - |
| NUR_Date | date |  |  | NO | Date |
| NUR_Nurse_DR | varchar |  | FK | NO | Nurse Des Ref to CTCP |
| NUR_SchedType_DR | bigint |  | FK | SI | Schedule Type Des Ref to PACSched |
| NUR_Ward_DR | bigint |  | FK | SI | Ward Des Ref to Ward |
| Q01 | - |  |  | SI | Mother infomed by |
| Q02 | - |  |  | SI | Partner informed by |
| Q03 | - |  |  | SI | Consultant obstetrician informed |
| Q03ObsDR | - |  |  | SI | Consultant obstetrician informed DR |
| Q04 | - |  |  | SI | Consultant/senior doctor spoken to parents |
| Q04ObsDR | - |  |  | SI | Consultant/senior doctor spoken to parents DR |
| Q05 | - |  |  | SI | Post-mortem procedure discussed with doctor |
| Q05ObsDR | - |  |  | SI | Post-mortem procedure discussed with doctor DR |
| Q06 | - |  |  | SI | Informed consent obtained and signed |
| Q06ObsDR | - |  |  | SI | Informed consent obtained and signed DR |
| Q07 | - |  |  | SI | Type of post-mortem agreed to |
| Q08 | - |  |  | SI | Pathology request completed by doctor |
| Q08ObsDR | - |  |  | SI | Pathology request completed by doctor DR |
| Q09 | - |  |  | SI | Opportunity to see/hold baby |
| Q09ObsDR | - |  |  | SI | Opportunity to see/hold baby DR |
| Q10 | - |  |  | SI | Religious advisor required |
| Q10ObsDR | - |  |  | SI | Religious advisor required DR |
| Q11 | - |  |  | SI | Religious ceremony held |
| Q11ObsDR | - |  |  | SI | Religious ceremony held DR |
| Q12 | - |  |  | SI | Photographs offered |
| Q12ObsDR | - |  |  | SI | Photographs offered DR |
| Q13 | - |  |  | SI | Photographs awaited |
| Q13ObsDR | - |  |  | SI | Photographs awaited DR |
| Q14 | - |  |  | SI | Photographs given |
| Q14ObsDR | - |  |  | SI | Photographs given DR |
| Q15 | - |  |  | SI | Birth acknowledgement given |
| Q15ObsDR | - |  |  | SI | Birth acknowledgement given DR |
| Q16 | - |  |  | SI | Cot card given |
| Q16ObsDR | - |  |  | SI | Cot card given DR |
| Q17 | - |  |  | SI | Namebands given |
| Q17ObsDR | - |  |  | SI | Namebands given DR |
| Q18 | - |  |  | SI | Lock of hair given |
| Q18ObsDR | - |  |  | SI | Lock of hair given DR |
| Q19 | - |  |  | SI | Foot/hand print given |
| Q19ObsDR | - |  |  | SI | Foot/hand print given DR |
| Q20 | - |  |  | SI | Certificate of blessing given |
| Q20ObsDR | - |  |  | SI | Certificate of blessing given DR |
| Q21 | - |  |  | SI | Identification card completed |
| Q21ObsDR | - |  |  | SI | Identification card completed DR |
| Q22 | - |  |  | SI | Request to pathology to collect baby |
| Q22ObsDR | - |  |  | SI | Request to pathology to collect baby DR |
| Q23 | - |  |  | SI | Funeral options discussed |
| Q23ObsDR | - |  |  | SI | Funeral options discussed DR |
| Q24 | - |  |  | SI | Future appointments cancelled |
| Q24ObsDR | - |  |  | SI | Future appointments cancelled DR |
| Q25 | - |  |  | SI | Visit from midwife required |
| Q25ObsDR | - |  |  | SI | Visit from midwife required DR |
| Q26 | - |  |  | SI | 6week follow-up arranged |
| Q26ObsDR | - |  |  | SI | 6week follow-up arranged DR |
| Q27 | - |  |  | SI | General practitioner informed |
| Q27ObsDR | - |  |  | SI | General practitioner informed DR |
| Q28 | - |  |  | SI | Paediatrician informed |
| Q28ObsDR | - |  |  | SI | Paediatrician informed DR |
| Q29 | - |  |  | SI | Death certificate completed |
| Q29ObsDR | - |  |  | SI | Death certificate completed DR |
| Q30 | - |  |  | SI | Other information |
| Q31 | - |  |  | SI | Completed form handed to secretary |
| Q31ObsDR | - |  |  | SI | Completed form handed to secretary DR |
| Q32 | - |  |  | SI | Prescription to suppress lactation given |
| Q32ObsDR | - |  |  | SI | Prescription to suppress lactation given DR |
| Q33 | - |  |  | SI | Information about funeral arranging given |
| Q33ObsDR | - |  |  | SI | Information about funeral arranging given DR |
| Q34 | - |  |  | SI | Post-mortem consent obtained and signed |
| Q34ObsDR | - |  |  | SI | Post-mortem consent obtained and signed DR |
| Q35 | - |  |  | SI | Parents decision on funeral |
| Q36 | - |  |  | SI | Religious advisor called |
| Q36ObsDR | - |  |  | SI | Religious advisor called DR |
| Q37 | - |  |  | SI | Have parents read the Still Birth & Neonatal Death... |
| Q38 | - |  |  | SI | Post mortem requested |
| Q39 | - |  |  | SI | Birth registration appointment needed |
| Q40 | - |  |  | SI | Note - Birth registration appointment needed |
| Q41 | - |  |  | SI | Is a coroner required |
| Q42 | - |  |  | SI | Has coroner been contacted |
| Q43 | - |  |  | SI | Notes |
| Q44 | - |  |  | SI | Support leaflets given |
| Q45 | - |  |  | SI | Support for siblings required |
| Q46 | - |  |  | SI | Council cremation papers completed |
| Q47 | - |  |  | SI | Cremation form |
| Q48 | - |  |  | SI | Date of registrar appointment |
| Q49 | - |  |  | SI | Date of birth registration appointment |
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